import unittest
from unittest.mock import patch

from mock_data import STAC_data

from context import get_sen2a_images


class Tests(unittest.TestCase):

    def setUp(self):

        # setting cloud cover to 45 due to Mock Data
        self.cloud_cover = 45
        self.filter_images = get_sen2a_images(STAC_data,'2021-10-01','2021-11-01')
    
    def test_STAC_filtering(self):
        filtered_items = self.filter_images

        self.assertIsNotNone(filtered_items)

if __name__ == '__main__':
    unittest.main(verbosity=5)