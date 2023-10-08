
import logging
import load_images
import convert_to_greyscale
import set_greyscale_threshold
import convert_to_bitmap_and_array
import compute_statistics
import calibrate_bitmap
import identify_features
import plot_3d

def main():
    logging.basicConfig(level=logging.INFO)

    # Step 1: Load and Sort the Images
    images = load_images.load_images()

    # Step 2: Convert to Greyscale
    logging.info('Converting images to greyscale')
    greyscale_images = convert_to_greyscale.convert_to_greyscale(images)

    # Step 3: Set a Greyscale Threshold
    logging.info('Setting greyscale threshold')
    threshold_value = set_greyscale_threshold.get_threshold_value()
    thresholded_images = set_greyscale_threshold.set_greyscale_threshold(greyscale_images, threshold_value)

    # Step 4: Convert to Bitmap and Array
    logging.info('Converting images to bitmap and array')
    bitmap_images = convert_to_bitmap_and_array.convert_to_bitmap(thresholded_images)
    arrays = convert_to_bitmap_and_array.convert_to_array(bitmap_images)

    # Step 5: Descriptive Statistics
    logging.info('Computing statistics')
    statistics = compute_statistics.compute_statistics(arrays)

    # Step 6: Identify, Label, and Visualize Fibers
    avg_values = calibrate_bitmap.calibrate_bitmap()
    fiber_arrays, matrix_arrays, void_arrays = identify_features.identify_features(avg_values, arrays)
    print(avg_values)
    print(len(fiber_arrays))
    
    # Step 7: 3D Plotting
    logging.info('Plotting 3D')
    plot_3d.plot_3d(fiber_arrays)

if __name__ == "__main__":
    logging.info('Starting script')
    main()
