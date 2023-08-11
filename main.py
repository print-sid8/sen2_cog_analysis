## Imports and setting up GDAL environment variables
import datetime
import requests as rq
import logging
import numpy as np
import json

from scripts.ndvi_and_kmeans_gen import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

from argparse import ArgumentParser
import time

def main(payload, start_date, end_date):

    images_to_run, multishape = get_sen2a_images(payload,start_date,end_date)

    results = []

    for image in images_to_run:
        for geom_index, _ in enumerate(multishape.geoms):
            image_result = process_image(payload, multishape, image, geom_index)
            results.append(image_result)

    logger.info('NDVI analysis complete')

    for result in results:
        logger.info(result)


if __name__ == "__main__":

    start = time.time()

    # Read arguments from command line
    parser = ArgumentParser()

    # Adding optional argument
    parser.add_argument("--start-date", help = "Provide a start date as string in YYYY-MM-DD format")
    parser.add_argument("--end-date" ,help = "Provide an end date as string in YYYY-MM-DD format")

    clargs = parser.parse_args()

    if any(elem is None for elem in [clargs.start_date,clargs.end_date]):
            logger.debug("Some arguments not provided by user")
            print("\nKindly provide all the required inputs for the main.py script. Please check arguments using 'python3 main.py --help'\n")
            exit(0)
    else:
        logger.debug(f"Arguments are provided by user - start={clargs.start_date}, end={clargs.end_date}")
        logger.info(f"NDVI and KMeans Analysis beginning for date range = {clargs.end_date} to {clargs.start_date}\n")
        start_date = clargs.start_date
        end_date = clargs.end_date


    logger.info("Querying given Github GIST to get raw GeoJSON")

    ### Using GET request to download raw Geojson from github gist link
    gist = rq.get('https://gist.githubusercontent.com/thaisbendixen/e126c37a3fa021495414658eeaf86d8d/raw/5d1926dcb3a4b9d631521ba12ea79fdc1ecd2df7/doberitz_multipolygon.geojson')
    geoj = gist.json()
    #### Naming polygons within Multipolygon for use later
    ## Adding "poly_ID" to the two polygons in the multipolygon geojson for later use
    for i in range(len(geoj['features'])):
        geoj['features'][i]['properties']['id'] = f"poly_{i+1}"
    
    main(geoj,start_date,end_date)
    
    print('\nNDVI analysis complete :\n')
    
    end = time.time()

    print("\n\n TOTAL TIME TAKEN : ", round(end-start,2), "seconds")