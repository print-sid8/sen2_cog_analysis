import json

import pyproj
from pyproj import Proj

import shapely
import shapely.wkt
from shapely.ops import transform as shapely_transform

'''
## Functions

- getndvi : function to get NDVI array using NIR and RED arrays
- reproject_aoi : function takes CRS.from_espg and a WGS Shapely Polygon, to reproject WGS Shapely polygon to desired CRS
- get_geojson_from_poly : getting GeoJSON in list (as requried for rasterio mask) from any Shapely Polygon

'''

def getndvi(red, nir):
    return ((nir - red)/(nir + red))

def reproject_aoi(crs, aoishape):

    wgs84 = Proj('+proj=longlat +datum=WGS84 +no_defs', preserve_units=True)
    utm = pyproj.Proj(crs)
    trans_utm = pyproj.Transformer.from_proj(wgs84, utm)
    utm_shapely_polygon = shapely_transform(trans_utm.transform, aoishape)

    return utm_shapely_polygon

def get_geojson_from_poly(shapely_polygon):
    wktext = shapely.wkt.loads(str(shapely_polygon))
    json_str = json.dumps(shapely.geometry.mapping(wktext))
    geometry = [json.loads(json_str)]
    return geometry

## function from stackoverflow to iterate through a list
def list_iterator(iterable):
    iterator = iter(iterable)
    prev_item = None
    current_item = next(iterator)  # throws StopIteration if empty.
    for next_item in iterator:
        yield (prev_item, current_item, next_item)
        prev_item = current_item
        current_item = next_item
    yield (prev_item, current_item, None)