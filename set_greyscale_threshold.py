
import cv2

def set_greyscale_threshold(images, threshold_value):
    """
    Apply a threshold to a list of greyscale images.

    Parameters:
    images (list): A list of greyscale images.
    threshold_value (int): The threshold value to apply.

    Returns:
    list: A list of thresholded images.
    """
    # Initialize an empty list to store the thresholded images
    thresholded_images = []

    # For each image in the list of images
    for image in images:
        # Apply the threshold using OpenCV's threshold function
        _, thresholded_image = cv2.threshold(image, threshold_value, 255, cv2.THRESH_BINARY)

        # Append the thresholded image to the list of thresholded images
        thresholded_images.append(thresholded_image)

    # Return the list of thresholded images
    return thresholded_images

def get_threshold_value():
    """
    Prompt the user to enter a threshold value.

    Returns:
    int: The user-specified threshold value.
    """
    # Prompt the user to enter a threshold value
    threshold_value = int(input("Please enter a threshold value (0-255): "))

    # Return the threshold value
    return threshold_value

