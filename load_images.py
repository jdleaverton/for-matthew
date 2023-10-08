
import cv2
import os
import tkinter as tk
from tkinter import filedialog

def load_images():
    """
    Prompt the user to select a directory and load all images from that directory.

    Returns:
    list: A list of loaded images.
    """
    # Initialize a Tkinter root window
    root = tk.Tk()
    # Hide the root window
    root.withdraw()

    # Prompt the user to select a directory
    directory = filedialog.askdirectory(title="Select directory with images")

    # Get a list of filenames in the directory
    filenames = os.listdir(directory)

    # Sort the filenames
    filenames.sort()

    # Initialize an empty list to store the images
    images = []

    # For each filename
    for filename in filenames:
        # Construct the full file path
        file_path = os.path.join(directory, filename)

        # Load the image using OpenCV's imread function
        image = cv2.imread(file_path)

        # Append the image to the list of images
        images.append(image)

    # Return the list of images
    return images

