import numpy as np
import matplotlib.pyplot as plt

def compute_statistics(arrays):
    """
    Compute descriptive statistics for each pixel position in the array.

    Parameters:
    arrays (list): A list of NumPy arrays.

    Returns:
    dict: A dictionary containing the mean, standard deviation, and other statistics for each pixel position.
    """
    # Convert the list of arrays to a 3D NumPy array
    arrays_3d = np.array(arrays)

    # Compute the mean for each pixel position
    mean = np.mean(arrays_3d, axis=0)
    print(f'Mean: {mean}')

    # Plot a 2D heatmap of the mean pixel value
    plt.imshow(mean, cmap='hot', interpolation='nearest')
    plt.colorbar(label='Mean Pixel Value')
    plt.title('2D Heatmap of Mean Pixel Value')
    plt.show()

    # Compute the standard deviation for each pixel position
    std_dev = np.std(arrays_3d, axis=0)
    print(f'Standard Deviation: {std_dev}')

    # Plot a 2D heatmap of the standard deviation
    plt.imshow(std_dev, cmap='hot', interpolation='nearest')
    plt.colorbar(label='Standard Deviation')
    plt.title('2D Heatmap of Standard Deviation')
    plt.show()

    # Compute the minimum value for each pixel position
    min_val = np.min(arrays_3d, axis=0)
    print(f'Minimum Value: {min_val}')

    # Compute the maximum value for each pixel position
    max_val = np.max(arrays_3d, axis=0)
    print(f'Maximum Value: {max_val}')

    # Compute the median for each pixel position
    median = np.median(arrays_3d, axis=0)
    print(f'Median: {median}')

    # Return the computed statistics as a dictionary
    return {
        'mean': mean,
        'std_dev': std_dev,
        'min_val': min_val,
        'max_val': max_val,
        'median': median
    }

