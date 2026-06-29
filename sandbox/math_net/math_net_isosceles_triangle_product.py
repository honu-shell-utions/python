# -----------------------------------------------------------------------------
# Jim McCleery
# June 29, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2021_5c37b9
# -----------------------------------------------------------------------------

# Import math functions needed for geometric calculations
from math import sqrt, atan, degrees
# Import numpy to generate arrays of evenly spaced numbers
import numpy as np
# Import matplotlib plotting tools
from matplotlib.pyplot import plot, axis, title, show


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Draws a straight line segment between two points: (x1, y1) and (x2, y2).
    """
    # matplotlib's plot takes a list of X-coordinates and a list of Y-coordinates
    plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# MAIN SCRIPT
# -----------------------------------------------------------------------------

# Instead of random guessing, we generate a grid of 1000 potential values 
# to scan through systematically.
side_choices = np.linspace(5, 10, 1000)
base_choices = np.linspace(5, 20, 1000)

# Variables to store our correct dimensions once found
side = None
base = None
height = None

# Nested loops: check every combination of side and base values
for s in side_choices:
    for b in base_choices:
        # Check if the math is valid for a real triangle 
        # (the hypotenuse 's' must be longer than the half-base)
        if s > (b / 2):
            h = sqrt(s**2 - (b / 2)**2)
            
            # Check if this combination matches our specific geometric condition
            if abs(s**2 - 2 * b * h) < 0.001:
                side = s
                base = b
                height = h
                break # Exit the inner loop
    if side is not None:
        break # Exit the outer loop if we found a match

# Calculate the vertex angle (theta) of the isosceles triangle using trigonometry
theta = 2 * atan(base / (2 * height))

# Define the (x, y) coordinates for the 3 vertices of the triangle
x0, y0 = 0, 0
x1, y1 = base, 0
x2, y2 = base / 2, height

# Draw the 3 sides of the triangle using our helper function
plot_line(x0, y0, x1, y1)  # Base side
plot_line(x2, y2, x1, y1)  # Right side
plot_line(x0, y0, x2, y2)  # Left side

# Clean up the visual presentation of the window
axis('off')    # Hide the graph grid lines and outer bounding border box
axis('equal')  # Force the X and Y axes to use the same scale so the geometry isn't distorted

# Add a title at the top, converting the angle from radians to easy-to-read degrees
# ':0.3f' limits the display to exactly 3 decimal places
title(f'Angle theta = {degrees(theta):0.3f} degrees.')

# Pop up the final window showing the rendered triangle plot
show()
