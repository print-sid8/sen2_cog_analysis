## Imports and setting up GDAL environment variables
import os, sys
import datetime
import requests as rq
import logging

import numpy as np

from PIL import Image

from collections import defaultdict

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

from .utils import *

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.INFO)


def get_sen2a_images(payload,start_date,end_date):

    ## Querying AWS/Element84 STAC API endpoint.
    '''
    - Element8s STAC API endpoint takes start and end date and a bounding box for area of interest.
    - The Sentinel 2A images are in the "/sentinel-s2-l2a-cogs/items/" url, which gives links of images kept in the Open Data AWS S3.
    - The response is a JSON which has to be sifted through to arrive at ideal images for our usecase
    '''

    # Getting overall bounds of the given multipolygon
    multishape = MultiPolygon([shape(pol['geometry']) for pol in payload['features']])
    bounds = list(multishape.bounds)
    # removing "spaces" in bounds list/string to avoid issues in sending HTTP requests
    bbox = str(bounds).replace(' ','')

    ## searching for COGs in AWS
    url = f"https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items?limit=100&bbox={bbox}&datetime={start_date}T00:00:00Z/{end_date}T23:59:59Z"

    print(url)

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

    if len(bandlist) == 0:
        logger.info("No images found in the given date range with Cloud Cover below 10")
        exit(0)

    images_by_date = defaultdict(list)

    # Populate the dictionary with images grouped by date
    for image in bandlist:
        images_by_date[image[1]].append(image)

    images_to_run = []

    # Select the best image for each date group
    for date_images in images_by_date.values():
        best_image = max(date_images, key=lambda image: image[5])
        images_to_run.append(best_image)
    
    return images_to_run, multishape



def get_band_riodatasets(to_run_images):

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

def compute_ndvi_arrays(nir, red, polygon):

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


def process_image(payload, multishape, image, geom_index):
    nir, red, date, tci_link = get_band_riodatasets(image)
    ndvi, transform_info, crs = compute_ndvi_arrays(nir, red, multishape.geoms[geom_index])

    return {
        "polygon_id": payload['features'][geom_index]['properties']['id'],
        "image_date": date,
        "true_color_image": tci_link,
        "average_ndvi": round(np.nanmean(ndvi), 4),
        "median_ndvi": round(np.nanmedian(ndvi), 4),
        "min_ndvi": round(np.nanmin(ndvi), 4),
        "max_ndvi": round(np.nanmax(ndvi), 4)
    }
