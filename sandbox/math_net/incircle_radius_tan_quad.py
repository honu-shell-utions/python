# -----------------------------------------------------------------------------
# Jim McCleery
# July 27, 2026
# Kailua-Kona, HI
#
# Reference Problem:
# https://mathnet.mit.edu/explorer.html?p=usa_2007_bd6b58
# -----------------------------------------------------------------------------

import numpy as np
import matplotlib.pyplot as plt
from math import sqrt, cos, sin, acos, tan, pi


def law_of_cosines(d1, d2, side):
    """
    Calculates the angle (in radians) opposite 'side' in a triangle
    with side lengths d1, d2, and 'side' using the Law of Cosines.
    """
    try:
        # Cosine rule formula: cos(theta) = (a^2 + b^2 - c^2) / (2 * a * b)
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except ValueError:
        # Returns False if side lengths cannot form a valid triangle
        return 0, False


def plot_line(x1, y1, x2, y2):
    """
    Plots a straight line segment between two points: (x1, y1) and (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2], color="blue")


def plot_circle(x, y, radius, start=0, stop=2 * pi):
    """
    Plots a circle (or arc) centered at (x, y) with a given radius.
    """
    # Create 1,500 evenly spaced angle points from start to stop
    angle = np.linspace(start, stop, 1500)
    
    # Calculate the x and y coordinates on the circle boundary
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    
    plt.plot(x_arr, y_arr, color="red")


# --- Main Geometry Calculations ---

# Calculate angles using side lengths of the triangles formed by the diagonal AC
alpha, _ = law_of_cosines(6, sqrt(13), 7)
beta, _ = law_of_cosines(2, sqrt(13), 3)
gamma, _ = law_of_cosines(6, 7, sqrt(13))

# Calculate incircle center offset and radius
a = (6 * tan(gamma / 2) - 2) / (tan(gamma / 2) - 1)
radius = 2 - a

# --- Coordinate Definitions (Matching Quadrilateral ABCD) ---

# Point A: Located at the origin (0, 0)
x0, y0 = 0, 0  # Point A

# Point B: AB = 2 at angle (alpha + beta) from AD
x1, y1 = 2 * cos(alpha + beta), 2 * sin(alpha + beta)  # Point B

# Point C: Diagonal AC = sqrt(13) at angle alpha from AD
x2, y2 = sqrt(13) * cos(alpha), sqrt(13) * sin(alpha)  # Point C

# Point D: AD = 6 along the horizontal axis
x3, y3 = 6, 0  # Point D

# Incircle Center Point O
x4, y4 = a, 2 - a

# --- Plotting Section ---

# Draw quadrilateral edges connecting vertices
plot_line(x0, y0, x1, y1)  # Side AB
plot_line(x1, y1, x2, y2)  # Side BC
plot_line(x2, y2, x3, y3)  # Side CD
plot_line(x0, y0, x3, y3)  # Side AD

# Draw the incircle
plot_circle(x4, y4, radius)

# Add vertex labels A, B, C, D
plt.text(x0, y0, '  A', fontsize=12, verticalalignment='top', horizontalalignment='right')
plt.text(x1, y1, '  B', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
plt.text(x2, y2, '  C', fontsize=12, verticalalignment='bottom', horizontalalignment='left')
plt.text(x3, y3, '  D', fontsize=12, verticalalignment='top', horizontalalignment='left')

# Set figure formatting
plt.title(f'The radius of the incircle is {radius:0.3f}')
plt.axis('equal')  # Keep 1:1 aspect ratio so circles aren't distorted
plt.axis('off')    # Hide coordinate grid axes
plt.show()
