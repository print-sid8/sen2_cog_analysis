## Sentinel-2 COG analysis - NDVI and KMeans Clustering

This repo will help you install a Python based CLI program, that uses [Element84 API](https://www.element84.com/earth-search/) to acquire Sentinel-2 L2A images from AWS Open Data S3 buckets, in your area of interest and time range, to calculate the NDVI values and perform an Unsupervised K-Means classfication on the NDVI values in the area of interest.

The output JSON response contains average, median, min and max NDVI to allow better understanding of the Areas of Interest.

The provided Jupyter Notebook `sen2_ndvi.ipynb` allows the user to visualize the outputs of the Python scripts, on a Folium basemap.

**Note** : Currently the Area of Interest is hard-coded to be the GeoJSON acquired from this [link](https://gist.githubusercontent.com/thaisbendixen/e126c37a3fa021495414658eeaf86d8d/raw/5d1926dcb3a4b9d631521ba12ea79fdc1ecd2df7/doberitz_multipolygon.geojson). The link right now provides a Multipolygon GeoJSON and the script performs NDVI calculation and KMeans classification on all the Polygons in a Multipolygon.

### Setting up the Environment

This script was developed using Python > = 3.6, in Ubuntu 20.04.

Note : osgeo gdal must be setup, and the script `gdalinstall.sh` helps installing gdal in a Debian OS such as Ubuntu.
It is run as below -

```bash
bash gdalinstall.sh
```

The following packages must be available in the Python installation -

- requests
- numpy
- GDAL
- rasterio
- PIL
- pyproj
- shapely
- folium
- sklearn
- jupyter-notebook

The above packages can be installed using the `requirements.txt` file using :

```bash
pip install requirements.txt
```

### How to run the Script, and what to expect

The `main.py` script runs the code to extract NDVI and run the KMeans algorithm on the NDVI array.

The KMeans classification outputs are saved in `/kmeans_outputs/` as PNGs and Geotiffs.

A JSON response containing NDVI statistics, links to color image, and the name of the Polygon that is processed is saved as `analysis_response.json`.

The `main.py` script requires `--start_date`, `--end_date` and `--cloud_cover`, as arguments. If they are not provided, the script defaults the "start_date" to (CURRENT DATE), "end_date" to (CURRENT DATE - 20 days), and "cloud_cover" to 10.

To run the script, use the terminal to navigate to the cloned repo, and checkout the `--help` option -

```bash
python3 main.py --help
```
Output -

```bash
usage: main.py [-h] [--start_date START_DATE] [--end_date END_DATE] [--cloud_cover CLOUD_COVER]

optional arguments:
  -h, --help            show this help message and exit
  --start_date START_DATE
                        Provide a start date as string in YYYY-MM-DD format
  --end_date END_DATE   Provide an end date as string in YYYY-MM-DD format
  --cloud_cover CLOUD_COVER
                        Provide a cloud_cover percetange in Integer/Float format

```

##### Example:

```bash
python main.py --start_date 2021-11-07 --end_date 2021-10-05 --cloud_cover 10
```

The above command runs the scripts and gives logs in the terminal as the script proceeds,
and finishes with the below output.

```bash
NDVI analysis complete :

Response : [{'polygon_id': 'poly_1', 'image_date': '2021-10-28', 'true_color_image': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/TCI.tif', 'average_ndvi': 0.6183, 'median_ndvi': 0.6898, 'min_ndvi': -1.0, 'max_ndvi': 0.9972}, {'polygon_id': 'poly_2', 'image_date': '2021-10-28', 'true_color_image': 'https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/TCI.tif', 'average_ndvi': 0.6656, 'median_ndvi': 0.6692, 'min_ndvi': -0.0679, 'max_ndvi': 0.9967}]

KMean classification outputs stored in ./kmean_output/ folder
 Analysis JSON response is stored in './analysis_response.json' for later use in jupyter notebooks

``` 

------------------------

After running the CLI script, the user can use the Jupyter Notebook `sen2_ndvi.ipynb` to visualize the outputs on a Map and interact with the layers.

A set of prepared Matplotlib outputs are present in the Jupyter Notebook, they are kept in `./png_outputs/` folder.

Shown here below -

![](https://raw.githubusercontent.com/print-sid8/sen2_cog_analysis/main/png_outputs/Unsupervised_poly_1.png)
![](https://raw.githubusercontent.com/print-sid8/sen2_cog_analysis/main/png_outputs/Unsupervised_poly_2.png)

-------------------------

### Testing

Codes have been added to test the STAC response filtering with the help of Mock Data.

The tests can be run with -

```
python3 tests/test.py
```