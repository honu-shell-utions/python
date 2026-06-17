# -----------------------------------------------------------------------------
# Jim McCleery
# June 17, 2026
# Kailua-Kona, HI
#
# Reference Problem: https://mathnet.mit.edu/explorer.html?p=usa_2023_e8e549
# -----------------------------------------------------------------------------

from math import pi, radians, sqrt, sin, cos
from matplotlib.pyplot import plot, text, title, axis, show
import numpy as np

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def distance(x1, y1, x2, y2):
    """
    Calculate the straight-line (Euclidean) distance between two points:
    Point 1 (x1, y1) and Point 2 (x2, y2).
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def plot_circle(x, y, radius, start=0, stop=2*pi):
    """
    Draw a circular arc from a start angle to a stop angle (in radians)
    around a specified center point (x, y).
    """
    angle = np.linspace(start, stop, 1500)
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    plot(x_arr, y_arr, color='black')


def plot_line(x1, y1, x2, y2, style='-', lw=1.0):
    """
    Draw a straight line segment connecting Point 1 (x1, y1) to Point 2 (x2, y2).
    """
    plot([x1, x2], [y1, y2], linestyle=style, linewidth=lw, color='black')


def label_point(label, x, y, dx=0.0, dy=0.0, ha='center', va='center', fs=16):
    """
    Place a text label near the coordinate (x, y).
    """
    text(x + dx, y + dy, label, fontsize=fs, ha=ha, va=va)


# -----------------------------------------------------------------------------
# GEOMETRY CREATION AND PLOTTING
# -----------------------------------------------------------------------------

# Define dimensions for our shapes
radius = 2 / sqrt(3)
side = 2

# Set the center point of our main circle
x0, y0 = 0, 0                      # O

# Calculate the 3 vertices of an equilateral triangle inscribed inside the circle
# B = (x1, y1), C = (x2, y2), A = (x3, y3)
x1, y1 = radius * cos(radians(-150)), radius * sin(radians(-150))   # B
x2, y2 = radius * cos(radians(-30)),  radius * sin(radians(-30))    # C
x3, y3 = radius * cos(radians(90)),   radius * sin(radians(90))     # A

# Find the midpoints of the triangle's two upper legs
x4, y4 = (x1 + x3) / 2, (y1 + y3) / 2   # M
x5, y5 = (x2 + x3) / 2, (y2 + y3) / 2   # N

# Calculate the endpoints of the horizontal chord through y = y4
x6, y6 = sqrt(radius**2 - y4**2), y4    # Y
x7, y7 = -sqrt(radius**2 - y4**2), y4   # X

# Midpoint of chord XY
x8, y8 = (x6 + x7) / 2, y4              # T

# --- Generate the Matplotlib Display ---

# Plot the center point O as a small marker
plot(x0, y0, 'o', color='black', markersize=3)

# Plot the outer bounding circle
plot_circle(x0, y0, radius)

# Plot the three sides of the inscribed triangle
plot_line(x1, y1, x2, y2)   # BC
plot_line(x3, y3, x2, y2)   # AC
plot_line(x1, y1, x3, y3)   # AB

# Plot the horizontal chord XY
plot_line(x7, y7, x6, y6)

# Plot dotted interior segments to match the reference figure
plot_line(x4, y4, x0, y0, style=(0, (1, 4)))   # M to O
plot_line(x5, y5, x0, y0, style=(0, (1, 4)))   # N to O
plot_line(x8, y8, x0, y0, style=(0, (1, 4)))   # T to O

# -----------------------------------------------------------------------------
# LABELS
# -----------------------------------------------------------------------------

label_point('A', x3, y3, dy= 0.00, va='bottom', fs=18)

label_point('B', x1, y1, dx=-0.08, dy=-0.06, ha='right', va='top', fs=18)
label_point('C', x2, y2, dx=0.08, dy=-0.06, ha='left',  va='top', fs=18)

label_point('M', x4, y4, dx=-0.06, dy=0.04, ha='right', va='bottom', fs=18)
label_point('N', x5, y5, dx=0.06,  dy=0.04, ha='left',  va='bottom', fs=18)

label_point('T', x8, y8, dy=0.04, va='bottom', fs=18)
label_point('O', x0, y0, dy=-0.10, va='top', fs=18)

label_point('X', x7, y7, dx=-0.08, ha='right', fs=18)
label_point('Y', x6, y6, dx=0.08,  ha='left',  fs=18)

# Calculate the length of chord XY
length = distance(x6, y6, x7, y7)

# Set the graph title
title(f'The length of chord XY is {length:.4f}, which is sqrt(5).')

# Format the window
axis('equal')
axis('off')

# Display the finished visual plot
show()

# -----------------------------------------------------------------------------
