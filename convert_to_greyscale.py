
import cv2

def convert_to_greyscale(images):
    """
    Convert a list of images to greyscale.

    Parameters:
    images (list): A list of images to convert to greyscale.

    Returns:
    list: A list of greyscale images.
    """
    # Initialize an empty list to store the greyscale images
    greyscale_images = []

    # For each image in the list of images
    for image in images:
        # Convert the image to greyscale using OpenCV's cvtColor function
        greyscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        # Append the greyscale image to the list of greyscale images
        greyscale_images.append(greyscale_image)

    # Return the list of greyscale images
    return greyscale_images
