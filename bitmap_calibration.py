import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Define a global variable to store the average value
avg_value = None

def onclick(event):
    global avg_value

    # Get the x and y coordinates of the click, rounded to integers
    x, y = int(event.xdata), int(event.ydata)

    # Define the size of the grid around the click
    grid_size = 9

    # Calculate the boundaries of the grid
    x_start = max(0, x - grid_size // 2)
    y_start = max(0, y - grid_size // 2)
    x_end = x_start + grid_size
    y_end = y_start + grid_size

    # Extract the grid from the image
    grid = img_array[y_start:y_end, x_start:x_end]

    # Calculate the average value in the grid
    avg_value = np.mean(grid)

    # Close the plot after the click
    plt.close()

# Load the image
img = Image.open('images/C0006438_00000.DCM.jpg')
img_array = np.array(img)

# Display the image
plt.imshow(img_array)

# Connect the click event to the onclick function
cid = plt.gcf().canvas.mpl_connect('button_press_event', onclick)

# Show the plot and wait for a click
plt.show()

# After the plot is closed, print the average value
print(avg_value)