
import numpy as np
import pyvista as pv

def plot_3d(arrays):
    """
    Create a 3D plot of the arrays.

    Parameters:
    arrays (list): A list of 2D numpy arrays.

    Returns:
    None
    """
    # Create a new plotter object
    plotter = pv.Plotter()

    # For each array in the list
    for i, array in enumerate(arrays):
        # Get the x, y, and z coordinates of the pixels with value 1
        y, x = (array == 1).nonzero()
        z = np.full_like(x, i)

        # Create a point cloud from the coordinates
        cloud = pv.PolyData(np.column_stack((x, y, z)))

        # Add the point cloud to the plotter
        plotter.add_mesh(cloud, color='r', opacity=0.75)

    # Set the labels for the x, y, and z axes
    plotter.add_axes(xlabel='X', ylabel='Y', zlabel='Z')

    # Set the title of the plot
    plotter.add_title('3D Plot of Arrays')

    # Display the plot
    plotter.show()
