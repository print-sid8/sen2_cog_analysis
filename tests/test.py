import unittest
from unittest.mock import patch

from mock_data import STAC_data

from context import CreateNDVI_and_KMeans


class Tests(unittest.TestCase):

    def setUp(self):

        # setting cloud cover to 45 due to Mock Data
        self.cloud_cover = 45
        self.filter_images = CreateNDVI_and_KMeans(STAC_data,'2021-10-01','2021-11-01')
    
    def test_STAC_filtering(self):
        # Testing if STAC JSON is filtered properly
        filtered = self.filter_images.query_STAC_endpoint()
        filtered_items = self.filter_images.get_sen2a_images(filtered,self.cloud_cover)

        self.assertIsNotNone(filtered_items)

if __name__ == '__main__':
    unittest.main(verbosity=5)