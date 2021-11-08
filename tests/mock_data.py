STAC_data = {
  "type": "FeatureCollection",
  "stac_version": "1.0.0-beta.2",
  "stac_extensions": [],
  "context": {
    "page": 1,
    "limit": 550,
    "matched": 24,
    "returned": 24
  },
  "numberMatched": 24,
  "numberReturned": 24,
  "features": [
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2A_32UQD_20211102_0_L2A",
      "bbox": [
        11.927835243788259,
        52.17549424226928,
        13.6341671437856,
        53.21198351848647
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              13.531018505310676,
              52.17549424226928
            ],
            [
              11.927835243788259,
              52.2262340066898
            ],
            [
              11.994655250134956,
              53.21198351848647
            ],
            [
              13.6341671437856,
              53.159413588610356
            ],
            [
              13.531018505310676,
              52.17549424226928
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-11-02T10:26:15Z",
        "platform": "sentinel-2a",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32632,
        "sentinel:utm_zone": 32,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "QD",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2A_MSIL2A_20211102T102201_N0301_R065_T32UQD_20211102T133155",
        "sentinel:data_coverage": 100,
        "eo:cloud_cover": 99.74,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-11-02T17:28:23.001Z",
        "updated": "2021-11-02T17:28:23.001Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/32/U/QD/2021/11/2/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            699960,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/11/2/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/11/2/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_32UQD_20211102_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/S2A_32UQD_20211102_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-11-2-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-11-2-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/32/U/QD/2021/11/S2A_32UQD_20211102_0_L2A/S2A_32UQD_20211102_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2A_32UQD_20211102_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_32UQD_20211102_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2A_33UUU_20211102_0_L2A",
      "bbox": [
        12.004776505505363,
        52.22622021187267,
        13.67852915179595,
        53.24195439072247
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              12.071609146443508,
              52.22622021187267
            ],
            [
              12.004776505505363,
              53.211969225496986
            ],
            [
              13.648326817133606,
              53.24195439072247
            ],
            [
              13.67852915179595,
              52.25515957252248
            ],
            [
              12.071609146443508,
              52.22622021187267
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-11-02T10:26:14Z",
        "platform": "sentinel-2a",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32633,
        "sentinel:utm_zone": 33,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "UU",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2A_MSIL2A_20211102T102201_N0301_R065_T33UUU_20211102T133155",
        "sentinel:data_coverage": 100,
        "eo:cloud_cover": 99.83,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-11-02T17:30:20.530Z",
        "updated": "2021-11-02T17:30:20.530Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/U/UU/2021/11/2/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            300000,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/11/2/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/11/2/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_33UUU_20211102_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/S2A_33UUU_20211102_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-11-2-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-11-2-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/33/U/UU/2021/11/S2A_33UUU_20211102_0_L2A/S2A_33UUU_20211102_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2A_33UUU_20211102_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_33UUU_20211102_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2A_32UQD_20211030_0_L2A",
      "bbox": [
        12.344738488411577,
        52.17549424226928,
        13.6341671437856,
        53.19006394517389
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              13.531018505310676,
              52.17549424226928
            ],
            [
              12.344738488411577,
              52.21514509261181
            ],
            [
              12.766414561797433,
              53.19006394517389
            ],
            [
              13.6341671437856,
              53.159413588610356
            ],
            [
              13.531018505310676,
              52.17549424226928
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-30T10:16:18Z",
        "platform": "sentinel-2a",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32632,
        "sentinel:utm_zone": 32,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "QD",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2A_MSIL2A_20211030T101141_N0301_R022_T32UQD_20211030T120510",
        "sentinel:data_coverage": 63.49,
        "eo:cloud_cover": 27.71,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-30T17:05:11.472Z",
        "updated": "2021-10-30T17:05:11.472Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/32/U/QD/2021/10/30/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            699960,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/30/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/30/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_32UQD_20211030_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/S2A_32UQD_20211030_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-30-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-30-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/32/U/QD/2021/10/S2A_32UQD_20211030_0_L2A/S2A_32UQD_20211030_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2A_32UQD_20211030_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_32UQD_20211030_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2A_33UUU_20211030_0_L2A",
      "bbox": [
        12.352170135755808,
        52.23285226233641,
        13.67852915179595,
        53.24195439072247
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              12.352170135755808,
              52.23285226233641
            ],
            [
              12.783448671711007,
              53.22900578890437
            ],
            [
              13.648326817133606,
              53.24195439072247
            ],
            [
              13.67852915179595,
              52.25515957252248
            ],
            [
              12.352170135755808,
              52.23285226233641
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-30T10:16:17Z",
        "platform": "sentinel-2a",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32633,
        "sentinel:utm_zone": 33,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "UU",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2A_MSIL2A_20211030T101141_N0301_R022_T33UUU_20211030T120510",
        "sentinel:data_coverage": 67.56,
        "eo:cloud_cover": 25.89,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-30T17:26:48.943Z",
        "updated": "2021-10-30T17:26:48.943Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/U/UU/2021/10/30/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            300000,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/30/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/30/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_33UUU_20211030_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/S2A_33UUU_20211030_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-30-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-30-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/33/U/UU/2021/10/S2A_33UUU_20211030_0_L2A/S2A_33UUU_20211030_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2A_33UUU_20211030_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_33UUU_20211030_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2B_32UQD_20211028_0_L2A",
      "bbox": [
        11.927835243788259,
        52.17549424226928,
        13.6341671437856,
        53.21198351848647
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              13.531018505310676,
              52.17549424226928
            ],
            [
              11.927835243788259,
              52.2262340066898
            ],
            [
              11.994655250134956,
              53.21198351848647
            ],
            [
              13.6341671437856,
              53.159413588610356
            ],
            [
              13.531018505310676,
              52.17549424226928
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-28T10:26:12Z",
        "platform": "sentinel-2b",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32632,
        "sentinel:utm_zone": 32,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "QD",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2B_MSIL2A_20211028T102039_N0301_R065_T32UQD_20211028T121942",
        "sentinel:data_coverage": 100,
        "eo:cloud_cover": 0.61,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-28T17:30:57.308Z",
        "updated": "2021-10-28T17:30:57.308Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/32/U/QD/2021/10/28/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            699960,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/28/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/28/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_32UQD_20211028_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/S2B_32UQD_20211028_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-28-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-28-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/32/U/QD/2021/10/S2B_32UQD_20211028_0_L2A/S2B_32UQD_20211028_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2B_32UQD_20211028_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2B_32UQD_20211028_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2B_33UUU_20211028_0_L2A",
      "bbox": [
        12.004776505505363,
        52.22622021187267,
        13.67852915179595,
        53.24195439072247
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              12.071609146443508,
              52.22622021187267
            ],
            [
              12.004776505505363,
              53.211969225496986
            ],
            [
              13.648326817133606,
              53.24195439072247
            ],
            [
              13.67852915179595,
              52.25515957252248
            ],
            [
              12.071609146443508,
              52.22622021187267
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-28T10:26:11Z",
        "platform": "sentinel-2b",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32633,
        "sentinel:utm_zone": 33,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "UU",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2B_MSIL2A_20211028T102039_N0301_R065_T33UUU_20211028T121942",
        "sentinel:data_coverage": 100,
        "eo:cloud_cover": 0.66,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-28T17:25:21.153Z",
        "updated": "2021-10-28T17:25:21.153Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/U/UU/2021/10/28/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            300000,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/28/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/28/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_33UUU_20211028_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/S2B_33UUU_20211028_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-28-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-28-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/33/U/UU/2021/10/S2B_33UUU_20211028_0_L2A/S2B_33UUU_20211028_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2B_33UUU_20211028_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2B_33UUU_20211028_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2B_32UQD_20211025_0_L2A",
      "bbox": [
        12.338017178017953,
        52.17549424226928,
        13.6341671437856,
        53.190252895173025
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              13.531018505310676,
              52.17549424226928
            ],
            [
              12.338017178017953,
              52.21533559303878
            ],
            [
              12.7604409779005,
              53.190252895173025
            ],
            [
              13.6341671437856,
              53.159413588610356
            ],
            [
              13.531018505310676,
              52.17549424226928
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-25T10:16:15Z",
        "platform": "sentinel-2b",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32632,
        "sentinel:utm_zone": 32,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "QD",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2B_MSIL2A_20211025T101029_N0301_R022_T32UQD_20211025T130834",
        "sentinel:data_coverage": 63.88,
        "eo:cloud_cover": 88.05,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-25T16:24:54.071Z",
        "updated": "2021-10-25T16:24:54.071Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/32/U/QD/2021/10/25/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            699960,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/25/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/25/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_32UQD_20211025_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/S2B_32UQD_20211025_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-25-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-25-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/32/U/QD/2021/10/S2B_32UQD_20211025_0_L2A/S2B_32UQD_20211025_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2B_32UQD_20211025_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2B_32UQD_20211025_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2B_33UUU_20211025_0_L2A",
      "bbox": [
        12.34544191732079,
        52.23270104363841,
        13.67852915179595,
        53.24195439072247
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              12.34544191732079,
              52.23270104363841
            ],
            [
              12.777161869707212,
              53.228888659137716
            ],
            [
              13.648326817133606,
              53.24195439072247
            ],
            [
              13.67852915179595,
              52.25515957252248
            ],
            [
              12.34544191732079,
              52.23270104363841
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-25T10:16:14Z",
        "platform": "sentinel-2b",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32633,
        "sentinel:utm_zone": 33,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "UU",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2B_MSIL2A_20211025T101029_N0301_R022_T33UUU_20211025T130834",
        "sentinel:data_coverage": 67.96,
        "eo:cloud_cover": 89.58,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-25T16:17:46.690Z",
        "updated": "2021-10-25T16:17:46.690Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/U/UU/2021/10/25/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            300000,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/25/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/25/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_33UUU_20211025_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/S2B_33UUU_20211025_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-25-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-25-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/33/U/UU/2021/10/S2B_33UUU_20211025_0_L2A/S2B_33UUU_20211025_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2B_33UUU_20211025_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2B_33UUU_20211025_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2A_32UQD_20211023_0_L2A",
      "bbox": [
        11.927835243788259,
        52.17549424226928,
        13.6341671437856,
        53.21198351848647
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              13.531018505310676,
              52.17549424226928
            ],
            [
              11.927835243788259,
              52.2262340066898
            ],
            [
              11.994655250134956,
              53.21198351848647
            ],
            [
              13.6341671437856,
              53.159413588610356
            ],
            [
              13.531018505310676,
              52.17549424226928
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-23T10:26:16Z",
        "platform": "sentinel-2a",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32632,
        "sentinel:utm_zone": 32,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "QD",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2A_MSIL2A_20211023T102101_N0301_R065_T32UQD_20211023T115920",
        "sentinel:data_coverage": 100,
        "eo:cloud_cover": 12.52,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-23T17:23:10.624Z",
        "updated": "2021-10-23T17:23:10.624Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/32/U/QD/2021/10/23/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            699960,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/23/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/23/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_32UQD_20211023_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/S2A_32UQD_20211023_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-23-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-23-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/32/U/QD/2021/10/S2A_32UQD_20211023_0_L2A/S2A_32UQD_20211023_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2A_32UQD_20211023_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_32UQD_20211023_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2A_33UUU_20211023_0_L2A",
      "bbox": [
        12.004776505505363,
        52.22622021187267,
        13.67852915179595,
        53.24195439072247
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              12.071609146443508,
              52.22622021187267
            ],
            [
              12.004776505505363,
              53.211969225496986
            ],
            [
              13.648326817133606,
              53.24195439072247
            ],
            [
              13.67852915179595,
              52.25515957252248
            ],
            [
              12.071609146443508,
              52.22622021187267
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-23T10:26:15Z",
        "platform": "sentinel-2a",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32633,
        "sentinel:utm_zone": 33,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "UU",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2A_MSIL2A_20211023T102101_N0301_R065_T33UUU_20211023T115920",
        "sentinel:data_coverage": 100,
        "eo:cloud_cover": 11.58,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-23T17:23:26.807Z",
        "updated": "2021-10-23T17:23:26.807Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/U/UU/2021/10/23/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            300000,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/23/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/23/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_33UUU_20211023_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/S2A_33UUU_20211023_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-23-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-23-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/33/U/UU/2021/10/S2A_33UUU_20211023_0_L2A/S2A_33UUU_20211023_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2A_33UUU_20211023_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_33UUU_20211023_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2A_32UQD_20211020_0_L2A",
      "bbox": [
        12.34503147130386,
        52.17549424226928,
        13.6341671437856,
        53.19003559212178
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              13.531018505310676,
              52.17549424226928
            ],
            [
              12.34503147130386,
              52.21513677992735
            ],
            [
              12.561255631868775,
              52.716448523189904
            ],
            [
              12.767310112318041,
              53.19003559212178
            ],
            [
              13.6341671437856,
              53.159413588610356
            ],
            [
              13.531018505310676,
              52.17549424226928
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-20T10:16:19Z",
        "platform": "sentinel-2a",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32632,
        "sentinel:utm_zone": 32,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "QD",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2A_MSIL2A_20211020T101041_N0301_R022_T32UQD_20211020T120420",
        "sentinel:data_coverage": 63.41,
        "eo:cloud_cover": 99.99,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-20T18:52:32.736Z",
        "updated": "2021-10-20T18:52:32.736Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/32/U/QD/2021/10/20/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            699960,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/20/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/20/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_32UQD_20211020_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/S2A_32UQD_20211020_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-20-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-20-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/32/U/QD/2021/10/S2A_32UQD_20211020_0_L2A/S2A_32UQD_20211020_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2A_32UQD_20211020_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_32UQD_20211020_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2A_33UUU_20211020_0_L2A",
      "bbox": [
        12.35275529476361,
        52.23286539578274,
        13.67852915179595,
        53.24195439072247
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              12.35275529476361,
              52.23286539578274
            ],
            [
              12.784346887908805,
              53.22902249649813
            ],
            [
              13.648326817133606,
              53.24195439072247
            ],
            [
              13.67852915179595,
              52.25515957252248
            ],
            [
              12.35275529476361,
              52.23286539578274
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-20T10:16:18Z",
        "platform": "sentinel-2a",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32633,
        "sentinel:utm_zone": 33,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "UU",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2A_MSIL2A_20211020T101041_N0301_R022_T33UUU_20211020T120420",
        "sentinel:data_coverage": 67.52,
        "eo:cloud_cover": 99.99,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-20T18:54:51.169Z",
        "updated": "2021-10-20T18:54:51.169Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/U/UU/2021/10/20/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            300000,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/20/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/20/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_33UUU_20211020_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/S2A_33UUU_20211020_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-20-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-20-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/33/U/UU/2021/10/S2A_33UUU_20211020_0_L2A/S2A_33UUU_20211020_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2A_33UUU_20211020_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_33UUU_20211020_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2B_32UQD_20211018_0_L2A",
      "bbox": [
        11.927835243788259,
        52.17549424226928,
        13.6341671437856,
        53.21198351848647
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              13.531018505310676,
              52.17549424226928
            ],
            [
              11.927835243788259,
              52.2262340066898
            ],
            [
              11.994655250134956,
              53.21198351848647
            ],
            [
              13.6341671437856,
              53.159413588610356
            ],
            [
              13.531018505310676,
              52.17549424226928
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-18T10:26:12Z",
        "platform": "sentinel-2b",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32632,
        "sentinel:utm_zone": 32,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "QD",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2B_MSIL2A_20211018T101939_N0301_R065_T32UQD_20211018T131832",
        "sentinel:data_coverage": 100,
        "eo:cloud_cover": 99.81,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-18T17:00:32.974Z",
        "updated": "2021-10-18T17:00:32.974Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/32/U/QD/2021/10/18/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            699960,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/18/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/18/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_32UQD_20211018_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/S2B_32UQD_20211018_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-18-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-18-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/32/U/QD/2021/10/S2B_32UQD_20211018_0_L2A/S2B_32UQD_20211018_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2B_32UQD_20211018_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2B_32UQD_20211018_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2B_33UUU_20211018_0_L2A",
      "bbox": [
        12.004776505505363,
        52.22622021187267,
        13.67852915179595,
        53.24195439072247
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              12.071609146443508,
              52.22622021187267
            ],
            [
              12.004776505505363,
              53.211969225496986
            ],
            [
              13.648326817133606,
              53.24195439072247
            ],
            [
              13.67852915179595,
              52.25515957252248
            ],
            [
              12.071609146443508,
              52.22622021187267
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-18T10:26:11Z",
        "platform": "sentinel-2b",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32633,
        "sentinel:utm_zone": 33,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "UU",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2B_MSIL2A_20211018T101939_N0301_R065_T33UUU_20211018T131832",
        "sentinel:data_coverage": 100,
        "eo:cloud_cover": 99.82,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-18T16:29:22.816Z",
        "updated": "2021-10-18T16:29:22.816Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/U/UU/2021/10/18/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            300000,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/18/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/18/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_33UUU_20211018_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/S2B_33UUU_20211018_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-18-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-18-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/33/U/UU/2021/10/S2B_33UUU_20211018_0_L2A/S2B_33UUU_20211018_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2B_33UUU_20211018_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2B_33UUU_20211018_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2B_32UQD_20211015_0_L2A",
      "bbox": [
        12.338017178017953,
        52.17549424226928,
        13.6341671437856,
        53.190252895173025
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              13.531018505310676,
              52.17549424226928
            ],
            [
              12.338017178017953,
              52.21533559303878
            ],
            [
              12.7604409779005,
              53.190252895173025
            ],
            [
              13.6341671437856,
              53.159413588610356
            ],
            [
              13.531018505310676,
              52.17549424226928
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-15T10:16:15Z",
        "platform": "sentinel-2b",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32632,
        "sentinel:utm_zone": 32,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "QD",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2B_MSIL2A_20211015T101029_N0301_R022_T32UQD_20211015T131608",
        "sentinel:data_coverage": 63.88,
        "eo:cloud_cover": 100,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-15T17:41:25.118Z",
        "updated": "2021-10-15T17:41:25.118Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/32/U/QD/2021/10/15/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            699960,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/15/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/15/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_32UQD_20211015_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/S2B_32UQD_20211015_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-15-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-15-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/32/U/QD/2021/10/S2B_32UQD_20211015_0_L2A/S2B_32UQD_20211015_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2B_32UQD_20211015_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2B_32UQD_20211015_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2B_33UUU_20211015_0_L2A",
      "bbox": [
        12.34544199724327,
        52.232701045436976,
        13.67852915179595,
        53.24195439072247
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              12.34544199724327,
              52.232701045436976
            ],
            [
              12.777461323837253,
              53.22889424582003
            ],
            [
              13.648326817133606,
              53.24195439072247
            ],
            [
              13.67852915179595,
              52.25515957252248
            ],
            [
              12.34544199724327,
              52.232701045436976
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-15T10:16:14Z",
        "platform": "sentinel-2b",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32633,
        "sentinel:utm_zone": 33,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "UU",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2B_MSIL2A_20211015T101029_N0301_R022_T33UUU_20211015T131608",
        "sentinel:data_coverage": 67.95,
        "eo:cloud_cover": 100,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-15T17:22:09.582Z",
        "updated": "2021-10-15T17:22:09.582Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/U/UU/2021/10/15/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            300000,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/15/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/15/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_33UUU_20211015_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/S2B_33UUU_20211015_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-15-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-15-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/33/U/UU/2021/10/S2B_33UUU_20211015_0_L2A/S2B_33UUU_20211015_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2B_33UUU_20211015_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2B_33UUU_20211015_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2A_32UQD_20211013_0_L2A",
      "bbox": [
        11.927835243788259,
        52.17549424226928,
        13.6341671437856,
        53.21198351848647
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              13.531018505310676,
              52.17549424226928
            ],
            [
              11.927835243788259,
              52.2262340066898
            ],
            [
              11.994655250134956,
              53.21198351848647
            ],
            [
              13.6341671437856,
              53.159413588610356
            ],
            [
              13.531018505310676,
              52.17549424226928
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-13T10:26:16Z",
        "platform": "sentinel-2a",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32632,
        "sentinel:utm_zone": 32,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "QD",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2A_MSIL2A_20211013T101951_N0301_R065_T32UQD_20211013T115233",
        "sentinel:data_coverage": 100,
        "eo:cloud_cover": 5.21,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-13T18:07:49.756Z",
        "updated": "2021-10-13T18:07:49.756Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/32/U/QD/2021/10/13/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            699960,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/13/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/13/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_32UQD_20211013_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/S2A_32UQD_20211013_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-13-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-13-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/32/U/QD/2021/10/S2A_32UQD_20211013_0_L2A/S2A_32UQD_20211013_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2A_32UQD_20211013_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_32UQD_20211013_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2A_33UUU_20211013_0_L2A",
      "bbox": [
        12.004776505505363,
        52.22622021187267,
        13.67852915179595,
        53.24195439072247
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              12.071609146443508,
              52.22622021187267
            ],
            [
              12.004776505505363,
              53.211969225496986
            ],
            [
              13.648326817133606,
              53.24195439072247
            ],
            [
              13.67852915179595,
              52.25515957252248
            ],
            [
              12.071609146443508,
              52.22622021187267
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-13T10:26:15Z",
        "platform": "sentinel-2a",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32633,
        "sentinel:utm_zone": 33,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "UU",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2A_MSIL2A_20211013T101951_N0301_R065_T33UUU_20211013T115233",
        "sentinel:data_coverage": 100,
        "eo:cloud_cover": 4.96,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-13T17:45:15.345Z",
        "updated": "2021-10-13T17:45:15.345Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/U/UU/2021/10/13/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            300000,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/13/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/13/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_33UUU_20211013_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/S2A_33UUU_20211013_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-13-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-13-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/33/U/UU/2021/10/S2A_33UUU_20211013_0_L2A/S2A_33UUU_20211013_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2A_33UUU_20211013_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_33UUU_20211013_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2A_32UQD_20211010_0_L2A",
      "bbox": [
        12.34473883753708,
        52.17549424226928,
        13.6341671437856,
        53.19000719005932
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              13.531018505310676,
              52.17549424226928
            ],
            [
              12.34473883753708,
              52.215145082706655
            ],
            [
              12.76820699659458,
              53.19000719005932
            ],
            [
              13.6341671437856,
              53.159413588610356
            ],
            [
              13.531018505310676,
              52.17549424226928
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-10T10:16:19Z",
        "platform": "sentinel-2a",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32632,
        "sentinel:utm_zone": 32,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "QD",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2A_MSIL2A_20211010T100941_N0301_R022_T32UQD_20211010T115015",
        "sentinel:data_coverage": 63.44,
        "eo:cloud_cover": 0.89,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-10T17:04:18.950Z",
        "updated": "2021-10-10T17:04:18.950Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/32/U/QD/2021/10/10/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            699960,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/10/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/10/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_32UQD_20211010_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/S2A_32UQD_20211010_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-10-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-10-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/32/U/QD/2021/10/S2A_32UQD_20211010_0_L2A/S2A_32UQD_20211010_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2A_32UQD_20211010_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_32UQD_20211010_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2A_33UUU_20211010_0_L2A",
      "bbox": [
        12.352170695519535,
        52.232852274901255,
        13.67852915179595,
        53.24195439072247
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              12.352170695519535,
              52.232852274901255
            ],
            [
              12.785544867660738,
              53.22904476939789
            ],
            [
              13.648326817133606,
              53.24195439072247
            ],
            [
              13.67852915179595,
              52.25515957252248
            ],
            [
              12.352170695519535,
              52.232852274901255
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-10T10:16:18Z",
        "platform": "sentinel-2a",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32633,
        "sentinel:utm_zone": 33,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "UU",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2A_MSIL2A_20211010T100941_N0301_R022_T33UUU_20211010T115015",
        "sentinel:data_coverage": 67.5,
        "eo:cloud_cover": 0.84,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-10T17:13:52.702Z",
        "updated": "2021-10-10T17:13:52.702Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/U/UU/2021/10/10/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            300000,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/10/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/10/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2A_33UUU_20211010_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/S2A_33UUU_20211010_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-10-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-10-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/33/U/UU/2021/10/S2A_33UUU_20211010_0_L2A/S2A_33UUU_20211010_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2A_33UUU_20211010_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2A_33UUU_20211010_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2B_33UUU_20211008_0_L2A",
      "bbox": [
        12.004776505505363,
        52.22622021187267,
        13.67852915179595,
        53.24195439072247
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              12.071609146443508,
              52.22622021187267
            ],
            [
              12.004776505505363,
              53.211969225496986
            ],
            [
              13.648326817133606,
              53.24195439072247
            ],
            [
              13.67852915179595,
              52.25515957252248
            ],
            [
              12.071609146443508,
              52.22622021187267
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-08T10:26:11Z",
        "platform": "sentinel-2b",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32633,
        "sentinel:utm_zone": 33,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "UU",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2B_MSIL2A_20211008T101829_N0301_R065_T33UUU_20211008T132426",
        "sentinel:data_coverage": 100,
        "eo:cloud_cover": 14.33,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-08T18:59:02.423Z",
        "updated": "2021-10-08T18:59:02.423Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/U/UU/2021/10/8/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            300000,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/8/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/8/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_33UUU_20211008_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/S2B_33UUU_20211008_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-8-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-8-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/33/U/UU/2021/10/S2B_33UUU_20211008_0_L2A/S2B_33UUU_20211008_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2B_33UUU_20211008_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2B_33UUU_20211008_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2B_32UQD_20211008_0_L2A",
      "bbox": [
        11.927835243788259,
        52.17549424226928,
        13.6341671437856,
        53.21198351848647
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              13.531018505310676,
              52.17549424226928
            ],
            [
              11.927835243788259,
              52.2262340066898
            ],
            [
              11.994655250134956,
              53.21198351848647
            ],
            [
              13.6341671437856,
              53.159413588610356
            ],
            [
              13.531018505310676,
              52.17549424226928
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-08T10:26:11Z",
        "platform": "sentinel-2b",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32632,
        "sentinel:utm_zone": 32,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "QD",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2B_MSIL2A_20211008T101829_N0301_R065_T32UQD_20211008T132426",
        "sentinel:data_coverage": 100,
        "eo:cloud_cover": 19.25,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-08T19:05:23.182Z",
        "updated": "2021-10-08T19:05:23.182Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/32/U/QD/2021/10/8/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            699960,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/8/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/8/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_32UQD_20211008_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/S2B_32UQD_20211008_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-8-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-8-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/32/U/QD/2021/10/S2B_32UQD_20211008_0_L2A/S2B_32UQD_20211008_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2B_32UQD_20211008_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2B_32UQD_20211008_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2B_32UQD_20211005_0_L2A",
      "bbox": [
        12.347076436672431,
        52.17549424226928,
        13.6341671437856,
        53.189978816102716
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              13.531018505310676,
              52.17549424226928
            ],
            [
              12.347076436672431,
              52.21507873861548
            ],
            [
              12.769102779355844,
              53.189978816102716
            ],
            [
              13.6341671437856,
              53.159413588610356
            ],
            [
              13.531018505310676,
              52.17549424226928
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-05T10:16:14Z",
        "platform": "sentinel-2b",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32632,
        "sentinel:utm_zone": 32,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "QD",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2B_MSIL2A_20211005T101029_N0301_R022_T32UQD_20211005T150142",
        "sentinel:data_coverage": 63.34,
        "eo:cloud_cover": 100,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-05T19:14:55.709Z",
        "updated": "2021-10-05T19:14:55.709Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/32/U/QD/2021/10/5/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            699960,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/5/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/32/U/QD/2021/10/5/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            699960,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            699960,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            699960,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_32UQD_20211005_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/S2B_32UQD_20211005_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-5-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-32-U-QD-2021-10-5-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/32/U/QD/2021/10/S2B_32UQD_20211005_0_L2A/S2B_32UQD_20211005_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2B_32UQD_20211005_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2B_32UQD_20211005_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    },
    {
      "type": "Feature",
      "stac_version": "1.0.0-beta.2",
      "stac_extensions": [
        "eo",
        "view",
        "proj"
      ],
      "id": "S2B_33UUU_20211005_0_L2A",
      "bbox": [
        12.354802995560398,
        52.23291133196369,
        13.67852915179595,
        53.24195439072247
      ],
      "geometry": {
        "type": "Polygon",
        "coordinates": [
          [
            [
              12.354802995560398,
              52.23291133196369
            ],
            [
              12.786143094236055,
              53.22905588714042
            ],
            [
              13.648326817133606,
              53.24195439072247
            ],
            [
              13.67852915179595,
              52.25515957252248
            ],
            [
              12.354802995560398,
              52.23291133196369
            ]
          ]
        ]
      },
      "properties": {
        "datetime": "2021-10-05T10:16:13Z",
        "platform": "sentinel-2b",
        "constellation": "sentinel-2",
        "instruments": [
          "msi"
        ],
        "gsd": 10,
        "view:off_nadir": 0,
        "proj:epsg": 32633,
        "sentinel:utm_zone": 33,
        "sentinel:latitude_band": "U",
        "sentinel:grid_square": "UU",
        "sentinel:sequence": "0",
        "sentinel:product_id": "S2B_MSIL2A_20211005T101029_N0301_R022_T33UUU_20211005T150142",
        "sentinel:data_coverage": 67.4,
        "eo:cloud_cover": 100,
        "sentinel:valid_cloud_cover": True,
        "created": "2021-10-05T19:11:27.795Z",
        "updated": "2021-10-05T19:11:27.795Z"
      },
      "collection": "sentinel-s2-l2a-cogs",
      "assets": {
        "thumbnail": {
          "title": "Thumbnail",
          "type": "image/png",
          "roles": [
            "thumbnail"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l1c/tiles/33/U/UU/2021/10/5/0/preview.jpg"
        },
        "overview": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/L2A_PVI.tif",
          "proj:shape": [
            343,
            343
          ],
          "proj:transform": [
            320,
            0,
            300000,
            0,
            -320,
            5900040,
            0,
            0,
            1
          ]
        },
        "info": {
          "title": "Original JSON metadata",
          "type": "application/json",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/5/0/tileInfo.json"
        },
        "metadata": {
          "title": "Original XML metadata",
          "type": "application/xml",
          "roles": [
            "metadata"
          ],
          "href": "https://roda.sentinel-hub.com/sentinel-s2-l2a/tiles/33/U/UU/2021/10/5/0/metadata.xml"
        },
        "visual": {
          "title": "True color image",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "overview"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            },
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            },
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/TCI.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B01": {
          "title": "Band 1 (coastal)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B01",
              "common_name": "coastal",
              "center_wavelength": 0.4439,
              "full_width_half_max": 0.027
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/B01.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B02": {
          "title": "Band 2 (blue)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B02",
              "common_name": "blue",
              "center_wavelength": 0.4966,
              "full_width_half_max": 0.098
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/B02.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B03": {
          "title": "Band 3 (green)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B03",
              "common_name": "green",
              "center_wavelength": 0.56,
              "full_width_half_max": 0.045
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/B03.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B04": {
          "title": "Band 4 (red)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B04",
              "common_name": "red",
              "center_wavelength": 0.6645,
              "full_width_half_max": 0.038
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/B04.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B05": {
          "title": "Band 5",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B05",
              "center_wavelength": 0.7039,
              "full_width_half_max": 0.019
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/B05.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B06": {
          "title": "Band 6",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B06",
              "center_wavelength": 0.7402,
              "full_width_half_max": 0.018
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/B06.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B07": {
          "title": "Band 7",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B07",
              "center_wavelength": 0.7825,
              "full_width_half_max": 0.028
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/B07.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B08": {
          "title": "Band 8 (nir)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 10,
          "eo:bands": [
            {
              "name": "B08",
              "common_name": "nir",
              "center_wavelength": 0.8351,
              "full_width_half_max": 0.145
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/B08.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "B8A": {
          "title": "Band 8A",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B8A",
              "center_wavelength": 0.8648,
              "full_width_half_max": 0.033
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/B8A.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B09": {
          "title": "Band 9",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 60,
          "eo:bands": [
            {
              "name": "B09",
              "center_wavelength": 0.945,
              "full_width_half_max": 0.026
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/B09.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "B11": {
          "title": "Band 11 (swir16)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B11",
              "common_name": "swir16",
              "center_wavelength": 1.6137,
              "full_width_half_max": 0.143
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/B11.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "B12": {
          "title": "Band 12 (swir22)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "gsd": 20,
          "eo:bands": [
            {
              "name": "B12",
              "common_name": "swir22",
              "center_wavelength": 2.22024,
              "full_width_half_max": 0.242
            }
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/B12.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        },
        "AOT": {
          "title": "Aerosol Optical Thickness (AOT)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/AOT.tif",
          "proj:shape": [
            1830,
            1830
          ],
          "proj:transform": [
            60,
            0,
            300000,
            0,
            -60,
            5900040,
            0,
            0,
            1
          ]
        },
        "WVP": {
          "title": "Water Vapour (WVP)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/WVP.tif",
          "proj:shape": [
            10980,
            10980
          ],
          "proj:transform": [
            10,
            0,
            300000,
            0,
            -10,
            5900040,
            0,
            0,
            1
          ]
        },
        "SCL": {
          "title": "Scene Classification Map (SCL)",
          "type": "image/tiff; application=geotiff; profile=cloud-optimized",
          "roles": [
            "data"
          ],
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/SCL.tif",
          "proj:shape": [
            5490,
            5490
          ],
          "proj:transform": [
            20,
            0,
            300000,
            0,
            -20,
            5900040,
            0,
            0,
            1
          ]
        }
      },
      "links": [
        {
          "rel": "self",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs/items/S2B_33UUU_20211005_0_L2A"
        },
        {
          "rel": "canonical",
          "href": "https://sentinel-cogs.s3.us-west-2.amazonaws.com/sentinel-s2-l2a-cogs/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/S2B_33UUU_20211005_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-5-0",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a-aws/workflow-publish-sentinel/tiles-33-U-UU-2021-10-5-0"
        },
        {
          "title": "Source STAC Item",
          "rel": "derived_from",
          "href": "https://cirrus-v0-data-1qm7gekzjucbq.s3.us-west-2.amazonaws.com/sentinel-s2-l2a/33/U/UU/2021/10/S2B_33UUU_20211005_0_L2A/S2B_33UUU_20211005_0_L2A.json",
          "type": "application/json"
        },
        {
          "title": "sentinel-s2-l2a/workflow-cog-archive/S2B_33UUU_20211005_0_L2A",
          "rel": "via-cirrus",
          "href": "https://cirrus-earth-search.aws.element84.com/v0/catid/sentinel-s2-l2a/workflow-cog-archive/S2B_33UUU_20211005_0_L2A"
        },
        {
          "rel": "parent",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "collection",
          "href": "https://earth-search.aws.element84.com/v0/collections/sentinel-s2-l2a-cogs"
        },
        {
          "rel": "root",
          "href": "https://earth-search.aws.element84.com/v0/"
        }
      ]
    }
  ],
  "links": []
}