import matplotlib.pyplot as plt
from PIL import Image
import numpy as np
import logging
import cv2
logging.basicConfig(level=logging.INFO)

def calibrate_bitmap():
    # Define a variable to store the average values
    avg_values = [None, None, None]
    labels = ['composite fibers', 'composite matrix', 'composite voids']

    def onclick(event):
        nonlocal avg_values
        nonlocal labels

        # Get the x and y coordinates of the click, rounded to integers
        x, y = int(event.xdata), int(event.ydata)

        # Define the size of the grid around the click
        grid_size = 15

        # Calculate the boundaries of the grid
        x_start = max(0, x - grid_size // 2)
        y_start = max(0, y - grid_size // 2)
        x_end = x_start + grid_size
        y_end = y_start + grid_size

        # Extract the grid from the image
        grid = img_array[y_start:y_end, x_start:x_end]

        # Calculate the average value in the grid and store it
        for i in range(3):
            if avg_values[i] is None:
                avg_values[i] = int(np.mean(grid))
                logging.info(f'Bitmap value for {labels[i]}: {avg_values[i]}')
                break

        # Close the plot after the click
        plt.close()

    # Load the image
    img = Image.open('images/C0006438_00000.DCM.jpg')
    img_array = np.array(img)

    for i in range(3):
        # Display the image
        plt.imshow(img_array)
        logging.info(f'Please select the bitmap value for {labels[i]}')

        # Connect the click event to the onclick function
        cid = plt.gcf().canvas.mpl_connect('button_press_event', onclick)

        # Show the plot and wait for a click
        plt.show()

    return [int(value) for value in avg_values if value is not None]