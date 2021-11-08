## Imports and setting up GDAL environment variables
import os, sys
import datetime
import requests as rq
import logging

import numpy as np

from PIL import Image

from osgeo import gdal

from shapely.geometry import shape, MultiPolygon

import rasterio as rio
from rasterio.mask import mask

from sklearn.cluster import KMeans

gdal.SetConfigOption('GDAL_HTTP_COOKIEFILE', '~/cookies.txt')
gdal.SetConfigOption('GDAL_HTTP_COOKIEJAR', '~/cookies.txt')
gdal.SetConfigOption('GDAL_DISABLE_READDIR_ON_OPEN', 'YES')
gdal.SetConfigOption('CPL_VSIL_CURL_ALLOWED_EXTENSIONS', 'TIF')
np.seterr(divide='ignore', invalid='ignore')

from utils import *

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)

class get_ndvi_and_kmeans():

    def __init__(self, geojson_data, start_date, end_date):

        self.payload = {}
        self.payload['start_date']=start_date
        self.payload['end_date']=end_date
        self.payload['aois']= geojson_data
        ### Creating Multipolygon in Shapely for geometric operations on the geojson, such as convex_hull, 
        ### incase that is the area of interest to get NDVI values/arrays.
        self.multishape = MultiPolygon([shape(pol['geometry']) for pol in self.payload['aois']['features']])
        self.kmeans_clusters = 5

        self.response = []


    def get_sen2a_images(self):

        ## Querying AWS/Element84 STAC API endpoint.
        '''
        - Element8s STAC API endpoint takes start and end date and a bounding box for area of interest.
        - The Sentinel 2A images are in the "/sentinel-s2-l2a-cogs/items/" url, which gives links of images kept in the Open Data AWS S3.
        - The response is a JSON which has to be sifted through to arrive at ideal images for our usecase
        '''

        # Getting overall bounds of the given multipolygon
        bounds = list(self.multishape.bounds)
        # removing "spaces" in bounds list/string to avoid issues in sending HTTP requests
        bbox = str(bounds).replace(' ','')

        ## searching for COGs in AWS
        url = f"https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items? \
        limit=550&bbox={bbox}& \
        datetime={self.payload['start_date']}T00:00:00Z/{self.payload['end_date']}T23:59:59Z"

        try:
            search_response = rq.get(url).json()
        except Exception as e:
            logger.error('\nSentinel-2 Element84 URL failed')
            logger.error("ELEMENT84 API ENDPOINT responed with :", e)
            

        items = search_response['features']

        ## Initializing an empty list to append only the required data from the STAC JSON response
        bandlist = []

        ## Choosing only dates that have Cloud Cover less than 10%
        for item in items:
            if item['properties']['eo:cloud_cover'] < 10:
                image = [
                    item['assets']['thumbnail']['href'], # PNG/JPG True Color
                    item['properties']['datetime'].split('T')[0],  # DATE in format - 2021-01-01T21:31:13Z 
                    item['assets']['B04']['href'],  # RED
                    item['assets']['B08']['href'],  # NIR
                    item['assets']['visual']['href'], # TIF true color
                    item['properties']['sentinel:data_coverage']]
                bandlist.append(image)

            
        ## remove duplicates/double images per day with difference of seconds between each other
        ## these images are quite common due to the way Sen2 images are stored in AWS, as tiles. 

        images_to_run = []

        ## Going through the filtered dates from STAC, looking for duplicated dates,
        ## then choosing the item that has better [sentinel:data_coverage] among duplicated dates.

        for prev, current, forward in list_iterator(bandlist):
            if prev is not None:
                if not any((prev[1] or current[1]) in sublist for sublist in images_to_run):
                    if prev[1] == current[1]:
                        if prev[5] > current[5]:
                            images_to_run.append(prev)
                        else:
                            images_to_run.append(current)
            else:
                if not any((current[1] or forward[1]) in sublist for sublist in images_to_run):
                    if current[1] == forward[1]:
                        if current[5] > forward[5]:
                            images_to_run.append(current)
                        else:
                            images_to_run.append(forward)
        
        return images_to_run
    
    def get_band_riodatasets(self,to_run_images):

        date = to_run_images[1]
        b4 = to_run_images[2]
        b8 = to_run_images[3]
        tci_image = to_run_images[4]

        logger.debug('\nOpening red band')
        try:
            red = rio.open(b4)
        except Exception as e:
            logger.error('Issue with Sentinel-2 AWS S3 Link :', e)

        logger.debug('\nOpening nir band')
        nir = rio.open(b8)

        logger.info("NIR and RED bands acquired")

        return nir, red, date, tci_image

    def compute_ndvi_arrays(self, nir, red, polygon):

        utm_shape = reproject_aoi(red.crs, polygon)

        # Using COG links to get clipped arrays from AWS

        logger.debug(f'Clipping NIR band to provided geometry - {utm_shape}')

        nir_array, _ = mask(nir, get_geojson_from_poly(utm_shape), crop=True)
        logger.debug('NIR array clipped!')

        logger.debug(f'Clipping RED band to provided geometry - {utm_shape}')

        red_array, red_transform = mask(red, get_geojson_from_poly(utm_shape), crop=True)
        logger.debug('RED array clipped!')

        # scaling is applied to Sen-2A images to reduce image size and keep arrays as Uint type
        # the scaling is multiplied applied back to get ideal NDVI values,
        # with float arrays of sen2 bands
        SCALE = 0.001

        # Getting NDVI array
        logger.info('Computing NDVI array..')
        ndvi_array = getndvi(red_array[0]*SCALE, nir_array[0]*SCALE)

        crs = nir.crs

        return ndvi_array, red_transform, crs
    
    def create_kmeans_output(self,ndvi_array,transform_info,crs,index):

        if np.count_nonzero(np.isnan(ndvi_array)) > 0:
            logger.debug('NAN values found in NDVI array, making them 99')
            ndvi = np.nan_to_num(ndvi_array,nan=99)
        
        ### Preparing for KMeans

        # Initializing empty array, to later add flattened NDVI for KMeans classfier
        flatndvi = np.empty((ndvi.shape[0]*ndvi.shape[1],1))

        logger.info('Flattening NDVI array..')
        flatndvi[:, 0] = ndvi.flatten()

        ## Applying KMeans clustering to the NDVI array

        logger.info("KMeans clustering begins..")

        km = KMeans(n_clusters= self.kmeans_clusters,random_state=0)
        logger.debug('Fitting KMeans Clusters..')
        km.fit(flatndvi)
        logger.debug('Predicting Classes/Clusters..')
        km.predict(flatndvi)
        
        logger.info('KMeans output ready and reshaped!')
        out_dat = km.labels_.reshape((ndvi.shape[0], ndvi.shape[1]))

        ## Creating Geotiff and PNG output for later viewing in Jupyter Notebook
        ras_meta = dict(driver="GTiff",
                        dtype=out_dat.dtype,
                        count=1,
                        height=out_dat.shape[0],
                        width=out_dat.shape[1],
                        crs=crs,
                        nodata=0.0,
                        transform=transform_info)
        
        logger.info('Writing KMeans output as Geotiff')

        outfolder = "./kmeans_output/"

        if not os.path.exists(outfolder):
            os.makedirs(outfolder)

        with rio.open(f"{outfolder}Unsupervised_KMeans_{self.payload['aois']['features'][index]['properties']['id']}.tif","w", **ras_meta) as dst:
            dst.write(out_dat,1)

        out_tiff_file = f"{outfolder}Unsupervised_KMeans_{self.payload['aois']['features'][index]['properties']['id']}.tif"
        out_colored_file = f"{out_tiff_file.split('.tif')[0]}_col.tif"

        logger.info('Making KMeans output a colored Geotiff')
        # use gdal-dem and color.txt file to apply colors to the reclassified raster
        os.system(f"gdaldem color-relief -alpha {out_tiff_file} ./colormap.txt {out_colored_file}")

        logger.info(f"Saving KMeans output as Colored PNG - {out_tiff_file.replace('.tif','.png')}")
        # convert Geotiff to Plain PNG file with no georeference
        im = Image.open(out_colored_file)
        im.save(out_tiff_file.replace('.tif','.png'))