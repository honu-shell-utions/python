"""
Jim McCleery
November 21, 2026
Kailua-Kona, HI

https://mathnet.mit.edu/explorer.html?p=jpn_2024_f20229
"""

# Import only the specific functions and constants used in this script
from math import pi, sqrt
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
def distance(A, B):
    """
    Return the straight-line distance between two points.

    Parameters:
        A, B: points written as (x, y) tuples

    Example:
        distance((0, 0), (3, 4)) returns 5.0
    """
    # Unpack both (x, y) point tuples into separate variables
    x1, y1 = A
    x2, y2 = B

    # Apply the Pythagorean theorem: sqrt((dx)^2 + (dy)^2)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# -----------------------------------------------------------------------------
def circum_circle(A, B, C):
    """
    Find the unique circle passing through three points.

    Parameters:
        A, B, C: three points written as (x, y) tuples

    Returns:
        (center, radius, True) where center is an (x, y) tuple.
        ((0, 0), 0, False) if the points lie in a straight line.
    """
    # Unpack the three (x, y) point tuples into individual coordinate variables
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    try:
        # Pre-calculate x^2 + y^2 for each point to simplify the formulas below
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2

        # Compute determinants (M11, M12, M13) to solve the system of circle equations
        M11 = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
        M12 = s1 * y2 + s2 * y3 + s3 * y1 - s2 * y1 - s3 * y2 - s1 * y3
        M13 = s1 * x2 + s2 * x3 + s3 * x1 - s2 * x1 - s3 * x2 - s1 * x3

        # Calculate the center coordinates (if points are collinear, M11 will be 0)
        center_x = 0.5 * M12 / M11
        center_y = -0.5 * M13 / M11

        # Group the center coordinates into a tuple
        center = (center_x, center_y)

        # Since all three points lie on the circle, the distance to point A is the radius
        radius = distance(A, center)

        return center, radius, True

    # If the three points lie on a single straight line, M11 is 0 (ZeroDivisionError)
    except (ValueError, ZeroDivisionError):
        return (0, 0), 0, False


# -----------------------------------------------------------------------------
def plot_circle(C, radius, start=0, stop=2 * pi):
    """
    Plot the outline of a circle or circular arc using Matplotlib.

    Parameters:
        C: center written as (x, y)
        radius: radius of the circle
        start: starting angle in radians (defaults to 0)
        stop: ending angle in radians (defaults to 2 * pi, a full circle)
    """
    # Unpack center coordinates
    center_x, center_y = C

    # Create 1,500 evenly spaced angles so the plotted curve looks smooth
    angles = np.linspace(start, stop, 1500)

    # Convert polar coordinates (radius, angle) to Cartesian (x, y) arrays
    x_values = radius * np.cos(angles) + center_x
    y_values = radius * np.sin(angles) + center_y

    # Draw the curve onto the current Matplotlib figure
    plt.plot(x_values, y_values, color="black")


# -----------------------------------------------------------------------------
def plot_line(A, B):
    """
    Plot a straight line segment between two points.

    Parameters:
        A, B: endpoints written as (x, y) tuples
    """
    # Unpack both endpoints
    x1, y1 = A
    x2, y2 = B

    # plt.plot takes a list of all x-values first, followed by a list of all y-values
    plt.plot([x1, x2], [y1, y2], color="black")


# -----------------------------------------------------------------------------
# Main Program: Solve and Draw the Geometry Problem
# -----------------------------------------------------------------------------

# Set up the vertices of equilateral triangle ABC with side length 10.
# Place B at the origin (0, 0) and C along the positive x-axis at (10, 0).
# Using 30-60-90 triangle ratios, the height of the triangle is 5 * sqrt(3).
B = (0, 0)
C = (10, 0)
A = (5, 5 * sqrt(3))

# Use a random search loop to find the positions of points D and E.
# Note: The problem specifies BX > CX (meaning X is to the right of midpoint x = 5),
# which happens when D is closer to A than E is (AD < 5 and AE > 8).
while True:
    # Pick a random length for segment AD between 0 and 5
    AD = uniform(0, 5)
    # Use the given constraint AD + AE = 13 to find the corresponding length of AE
    AE = 13 - AD

    # Compute the (x, y) coordinates of D along side AB and E along side AC
    # using 60-degree trigonometry (cos(60°) = 1/2, sin(60°) = sqrt(3)/2)
    D = ((10 - AD) / 2, (10 - AD) * sqrt(3) / 2)
    E = (5 + AE / 2, (10 - AE) * sqrt(3) / 2)

    # Find the circle passing through points A, D, and E
    circle_center, circle_radius, _ = circum_circle(A, D, E)

    # Because side BC lies along the x-axis (y = 0), the circle is tangent to BC
    # when its vertical distance from the x-axis (y-coordinate) equals its radius.
    if abs(circle_center[1] - circle_radius) < 0.000001:
        break

# Point X is where the circle touches side BC (directly below the circle's center)
X = (circle_center[0], 0)

# Draw the circle and the three sides of triangle ABC
plot_circle(circle_center, circle_radius)
plot_line(A, B)
plot_line(B, C)
plot_line(A, C)

# Dictionary mapping each point label to its (x, y) coordinates and a small (dx, dy)
# offset so the text labels don't overlap the lines or circle
labels = {
    "A": (A, (0.0, 0.35)),
    "B": (B, (-0.35, -0.55)),
    "C": (C, (0.25, -0.55)),
    "D": (D, (-0.55, 0.10)),
    "E": (E, (0.45, -0.20)),
    "X": (X, (0.0, -0.55)),
}

# Loop through the dictionary and place each italic label on the plot
for name, (point, offset) in labels.items():
    label_x = point[0] + offset[0]
    label_y = point[1] + offset[1]
    plt.text(
        label_x,
        label_y,
        name,
        fontsize=14,
        fontstyle="italic",
        ha="center",
        va="center",
    )

# Calculate the length of segment BX
bx_length = distance(B, X)

# Configure the chart title, keep x and y scales equal so circles aren't stretched,
# hide the axis borders, and display the final figure
plt.title(f"The length of BX is {bx_length:0.5f}.")
plt.axis("equal")
plt.axis("off")
plt.show()
