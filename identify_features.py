import numpy as np
import cv2

def identify_features(avg_values, arrays):
    fiber_arrays = []
    matrix_arrays = []
    void_arrays = []

    for array in arrays:
        # Initialize arrays for this image
        fiber_array = np.zeros_like(array)
        matrix_array = np.zeros_like(array)
        void_array = np.zeros_like(array)

        # Use OpenCV to find features based on the bitmap value
        _, threshold_fiber = cv2.threshold(array, avg_values[0] - 10, avg_values[0] + 10, cv2.THRESH_BINARY)
        _, threshold_matrix = cv2.threshold(array, avg_values[1] - 10, avg_values[1] + 10, cv2.THRESH_BINARY)
        _, threshold_void = cv2.threshold(array, avg_values[2] - 10, avg_values[2] + 10, cv2.THRESH_BINARY)

        # Set the pixel values in the features to be 1, and the pixels not in the features to be 0
        fiber_array = np.where(threshold_fiber > 0, 1, fiber_array)
        matrix_array = np.where(threshold_matrix > 0, 1, matrix_array)
        void_array = np.where(threshold_void > 0, 1, void_array)

        # Append the arrays for this image to the lists
        fiber_arrays.append(fiber_array)
        matrix_arrays.append(matrix_array)
        void_arrays.append(void_array)

    return fiber_arrays, matrix_arrays, void_arrays