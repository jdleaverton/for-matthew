
import unittest
import numpy as np
import cv2
from load_images import load_images
from convert_to_greyscale import convert_to_greyscale
from set_greyscale_threshold import set_greyscale_threshold, get_threshold_value
from convert_to_bitmap_and_array import convert_to_bitmap, convert_to_array
from compute_statistics import compute_statistics
from calibrate_bitmap import identify_fibers
from plot_3d import plot_3d
from matplotlib import pyplot as plt

class TestImageProcessing(unittest.TestCase):

    def setUp(self):
        self.directory = 'test_images'  # directory with test images
        self.images = load_images(self.directory)
        self.threshold_value = 127  # arbitrary threshold value for testing

    def test_load_images(self):
        self.assertIsInstance(self.images, list)
        self.assertTrue(all(isinstance(i, np.ndarray) for i in self.images))

    def test_convert_to_greyscale(self):
        greyscale_images = convert_to_greyscale(self.images)
        self.assertTrue(all(len(i.shape) == 2 for i in greyscale_images))  # check if images are indeed greyscale

    def test_set_greyscale_threshold(self):
        greyscale_images = convert_to_greyscale(self.images)
        thresholded_images = set_greyscale_threshold(greyscale_images, self.threshold_value)
        self.assertTrue(all(i.dtype == np.uint8 for i in thresholded_images))  # check if images are binary

    def test_convert_to_bitmap_and_array(self):
        greyscale_images = convert_to_greyscale(self.images)
        thresholded_images = set_greyscale_threshold(greyscale_images, self.threshold_value)
        bitmap_images = convert_to_bitmap(thresholded_images)
        self.assertTrue(all(i.dtype == np.uint8 for i in bitmap_images))  # check if images are binary
        arrays = convert_to_array(bitmap_images)
        self.assertTrue(all(isinstance(i, np.ndarray) for i in arrays))  # check if images are converted to arrays

    def test_compute_statistics(self):
        greyscale_images = convert_to_greyscale(self.images)
        thresholded_images = set_greyscale_threshold(greyscale_images, self.threshold_value)
        bitmap_images = convert_to_bitmap(thresholded_images)
        arrays = convert_to_array(bitmap_images)
        stats = compute_statistics(arrays)
        self.assertIsInstance(stats, dict)
        self.assertTrue('mean' in stats and 'std_dev' in stats)

    def test_identify_and_label_fibers(self):
        greyscale_images = convert_to_greyscale(self.images)
        thresholded_images = set_greyscale_threshold(greyscale_images, self.threshold_value)
        bitmap_images = convert_to_bitmap(thresholded_images)
        arrays = convert_to_array(bitmap_images)
        labeled_arrays = identify_fibers(arrays)
        self.assertTrue(all(isinstance(i, np.ndarray) for i in labeled_arrays))  # check if output is list of arrays

    def test_plot_3d(self):
        greyscale_images = convert_to_greyscale(self.images)
        thresholded_images = set_greyscale_threshold(greyscale_images, self.threshold_value)
        bitmap_images = convert_to_bitmap(thresholded_images)
        arrays = convert_to_array(bitmap_images)
        labeled_arrays = identify_fibers(arrays)
        fig = plot_3d(labeled_arrays)
        self.assertIsInstance(fig, plt.Figure)

if __name__ == '__main__':
    unittest.main()

