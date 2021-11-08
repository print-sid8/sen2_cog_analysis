## Imports and setting up GDAL environment variables
import datetime
import requests as rq
import logging
import numpy as np
import json

from scripts.ndvi_and_kmeans_gen import CreateNDVI_and_KMeans

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from argparse import ArgumentParser


if __name__ == "__main__":

    # Read arguments from command line
    parser = ArgumentParser()

    # Adding optional argument
    parser.add_argument("--start_date", help = "Provide a start date as string in YYYY-MM-DD format")
    parser.add_argument("--end_date" ,help = "Provide an end date as string in YYYY-MM-DD format")
    parser.add_argument("--cloud_cover" ,help = "Provide a cloud_cover percetange in Integer/Float format")

    clargs = parser.parse_args()

    if clargs.start_date is None and clargs.end_date is None and clargs.cloud_cover is None:
        logger.debug("No arguments provided by user")
        print("\nNo arguments provided in CLI, going ahead with Defaults")
        print(f'Default start_date - {datetime.datetime.today().strftime("%Y-%m-%d")}')
        print(f'Default end_date - {(datetime.datetime.today() - datetime.timedelta(days=20)).strftime("%Y-%m-%d")}\n\n')
        print('Default Cloud Cover percentage - 10')
        clargs.start_date = datetime.datetime.today().strftime("%Y-%m-%d")
        clargs.end_date = (datetime.datetime.today() - datetime.timedelta(days=20)).strftime("%Y-%m-%d")
        clargs.cloud_cover = 10
    else:
        logger.debug(f"Arguments are provided by user - start={clargs.start_date}, end={clargs.end_date}")
        print(f"NDVI and KMeans Analysis beginning for date range = {clargs.end_date} to {clargs.start_date} and cloud cover percentage less than = {clargs.cloud_cover}\n")
    
    logger.info("Querying given Github GIST to get raw GeoJSON")

    ### Using GET request to download raw Geojson from github gist link
    gist = rq.get('https://gist.githubusercontent.com/thaisbendixen/e126c37a3fa021495414658eeaf86d8d/raw/5d1926dcb3a4b9d631521ba12ea79fdc1ecd2df7/doberitz_multipolygon.geojson')
    geoj = gist.json()
    #### Naming polygons within Multipolygon for use later
    ## Adding "poly_ID" to the two polygons in the multipolygon geojson for later use
    for i in range(len(geoj['features'])):
        geoj['features'][i]['properties']['id'] = f"poly_{i+1}"


    logger.info("Initiating Main Class with provided start and end date, and GeoJSON")
    main_class = CreateNDVI_and_KMeans(geoj,start_date=clargs.start_date,end_date=clargs.end_date)

    # Getting STAC endpoint response
    stac_output = main_class.query_STAC_endpoint()

    # Filtering images with given cloud cover perc and removing duplicates
    images_to_run = main_class.get_sen2a_images(stac_output,float(clargs.cloud_cover))
    logger.info("Got images that match your requirements from Element84 STAC endpoint")

    for image in images_to_run:

        logger.info("Getting required bands for NDVI")
        nir, red, date, tci_link = main_class.get_band_riodatasets(image)

        for index, geom in enumerate(main_class.multishape.geoms):

            ndvi, transform_info, crs = main_class.compute_ndvi_arrays(nir,red,geom)

            main_class.create_kmeans_output(ndvi,transform_info,crs,date,index)

            main_class.response.append({
                "polygon_id":main_class.payload['aois']['features'][index]['properties']['id'],
                "image_date":date,
                "true_color_image":tci_link,
                "average_ndvi":round(np.nanmean(ndvi),4),
                "median_ndvi":round(np.nanmedian(ndvi),4),
                "min_ndvi":round(np.nanmin(ndvi),4),
                "max_ndvi":round(np.nanmax(ndvi),4)
                })
    
    print('\nNDVI analysis complete :\n')
    print("Response :",main_class.response)
    print("\nKMean classification outputs stored in ./kmean_output/ folder\n","Analysis JSON response is stored in './analysis_response.json' for later use in jupyter notebooks")

    with open("./analysis_response.json","w+") as out:
        json.dump(main_class.response,out)