# How to run

1. Make sure Python is installed with tkinter add on
 - Otherwise you might have to install the tinker add on with `brew install tcl-tk` and `brew reinstall python@3.11 --with-tcl-tk`
 - Python should be version 3.11, not native macOS 2.7
2. Download the zipped files from this repo and put them in a folder

3. In VSCode, or some other IDE, create a python virtual environment with the terminal command: `python -m venv .venv`

4. Activate the virtual environment with `source .venv/bin/activate`

5. Install all required packages wth `pip install < requirements.txt` (or something similar, look it up)

6. Run it with `python3 main.py`

# Next Steps
- Code is incomplete and requires some remaining debugging
## Identifying features
- feature identifying takes the 9x9 pixel square average around where the user clicks, so you click first on fibers, then matrix, then voids.
- By default, I set it to identify features with bitmap values +/- 10 from the square average (lets call it aggregation threshold). You might need to bring that down some, otherwise matrix and voids might be inseparable
- Ex: for a given slice of fibers in a 2D image, it should set the fibers' pixels to 1 and everything else to 0. It repeats for all images. 
- I think a great way to make sure you are getting good feature recognition is to add up all the 1s in all three categories (fibers, matrix, voids) and see how close it is to the total number of pixels (~= 634 x 634 x 50).
- Minimizing `J(aggregation_threshold) = | (all_1s_in_features(aggregation_threshold) - total_pixels) |` would be a way to find the optimal aggregation_threshold
- Also, you can sanity check the identified feature ratios of fibers/matrix/voids with volume fraction from the composite manufacturing specs
## Plotting
- went with pyvista for 3d plotting point clouds, matplotlib used to be annoying to plot 3D, but they may have fixed it
- Minimizing `J(aggregation_threshold)` should also make the plotting work, but you might still have to finesse it a bit


Good luck
