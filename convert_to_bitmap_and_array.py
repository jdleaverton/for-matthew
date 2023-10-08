
import cv2
import numpy as np

def convert_to_bitmap(images):
    """
    Convert a list of images to binary format (bitmap).

    Parameters:
    images (list): A list of thresholded images.

    Returns:
    list: A list of bitmap images.
    """
    # Initialize an empty list to store the bitmap images
    bitmap_images = []

    # For each image in the list of images
    for image in images:
        # Convert the image to binary format using OpenCV's threshold function
        _, bitmap_image = cv2.threshold(image, 127, 255, cv2.THRESH_BINARY)

        # Append the bitmap image to the list of bitmap images
        bitmap_images.append(bitmap_image)

    # Return the list of bitmap images
    return bitmap_images

def convert_to_array(images):
    """
    Convert a list of images to NumPy arrays.

    Parameters:
    images (list): A list of bitmap images.

    Returns:
    list: A list of NumPy arrays.
    """
    # Initialize an empty list to store the NumPy arrays
    arrays = []

    # For each image in the list of images
    for image in images:
        # Convert the image to a NumPy array
        array = np.array(image)

        # Append the array to the list of arrays
        arrays.append(array)

    # Return the list of arrays
    return arrays
