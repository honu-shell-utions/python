"""
Jim McCleery
November 20, 2026
Kailua-Kona, HI

https://mathnet.mit.edu/explorer.html?p=usa_ca585c

Problem:
A triangle has sides of length 888, 925, and x > 0. Find the value of x that
minimizes the area of the circle circumscribed about the triangle.
"""

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------
from math import acos, cos, pi, sin, sqrt  # Standard math functions & constants
from random import uniform                 # Generates random decimal numbers
import matplotlib.pyplot as plt            # Library for drawing graphs/shapes
import numpy as np                         # Library for fast array math


# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------
def circum_circle(A, B, C):
    """
    Find the unique circle passing through three points (A, B, and C).

    Parameters:
        A, B, C: Three points written as (x, y) tuples.

    Returns:
        (center, radius, True) if a valid circle is found.
        ((0, 0), 0, False) if the points lie on a straight line.
    """
    # Unpack the (x, y) coordinates of each point into separate variables
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    try:
        # Pre-calculate x^2 + y^2 for each point to simplify the algebra
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2

        # Compute determinants to solve the system of circle equations
        M11 = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
        M12 = s1 * y2 + s2 * y3 + s3 * y1 - s2 * y1 - s3 * y2 - s1 * y3
        M13 = s1 * x2 + s2 * x3 + s3 * x1 - s2 * x1 - s3 * x2 - s1 * x3

        # Calculate the center (x, y) of the circumscribed circle
        center_x = 0.5 * M12 / M11
        center_y = -0.5 * M13 / M11
        center = (center_x, center_y)

        # Since all three vertices lie on the circle, the distance from the
        # center to vertex A gives us the radius
        radius = distance(A, center)

        return center, radius, True

    # If the three points form a flat line, M11 is 0, causing a ZeroDivisionError
    except (ValueError, ZeroDivisionError):
        return (0, 0), 0, False


def distance(A, B):
    """Return the straight-line distance between two (x, y) points."""
    x1, y1 = A
    x2, y2 = B
    # Apply the Pythagorean theorem: sqrt((dx)^2 + (dy)^2)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def law_of_cosines(d1, d2, side):
    """
    Find an angle of a triangle using the Law of Cosines:
    c^2 = a^2 + b^2 - 2ab * cos(C)

    Returns:
        (angle_in_radians, True) if valid, or (0, False) if invalid.
    """
    try:
        # Rearrange the Law of Cosines to solve for cos(angle)
        cosine_value = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)

        # Tiny computer rounding errors can produce values like 1.0000000000000002.
        # Clamp the value strictly between -1 and 1 so acos() won't crash.
        cosine_value = max(-1.0, min(1.0, cosine_value))

        # Convert the cosine ratio back into an angle in radians
        angle = acos(cosine_value)
        return angle, True

    except (ValueError, ZeroDivisionError):
        return 0, False


def plot_circle(C, radius, start=0, stop=2 * pi):
    """Plot the outline of a circle centered at C with a given radius."""
    center_x, center_y = C

    # Create 1,500 closely spaced angles so the circle looks smooth
    angles = np.linspace(start, stop, 1500)

    # Convert polar coordinates (radius, angle) to Cartesian (x, y) arrays
    x_values = radius * np.cos(angles) + center_x
    y_values = radius * np.sin(angles) + center_y

    plt.plot(x_values, y_values, color="steelblue")


def plot_line(A, B):
    """Plot a straight line segment between two (x, y) points."""
    x1, y1 = A
    x2, y2 = B
    # plt.plot expects a list of x-coordinates followed by a list of y-coordinates
    plt.plot([x1, x2], [y1, y2], color="darkred")


def polygon_fill_coordinates(*vertices):
    """
    Return closed coordinate tuples suitable for passing into plt.fill().
    Repeats the first vertex at the end so the polygon closes properly.
    """
    x_coordinates = tuple(point[0] for point in vertices) + (vertices[0][0],)
    y_coordinates = tuple(point[1] for point in vertices) + (vertices[0][1],)
    return x_coordinates, y_coordinates


def add_labels(A, B, C, center, side_ab, side_ac, side_bc):
    """Add coordinate, vertex, and side-length labels to the plot."""
    # Label the three vertices with their names and (x, y) coordinates
    plt.text(A[0], A[1] - 60, f"A ({A[0]:.0f}, {A[1]:.0f})", ha="right", va="top", fontsize=9)
    plt.text(B[0], B[1] - 60, f"B ({B[0]:.0f}, {B[1]:.0f})", ha="left", va="top", fontsize=9)
    plt.text(C[0], C[1] + 50, f"C ({C[0]:.1f}, {C[1]:.1f})", ha="center", va="bottom", fontsize=9)

    # Plot and label the circumcenter
    plt.plot(center[0], center[1], "ko", markersize=4)
    plt.text(center[0] + 30, center[1], f"Center ({center[0]:.1f}, {center[1]:.1f})", fontsize=8)

    # Label the midpoints of the three sides with their lengths (888, 925, and x)
    plt.text((A[0] + B[0]) / 2, (A[1] + B[1]) / 2 - 40, f"{side_ab}", ha="center", fontsize=9, fontweight="bold")
    plt.text((A[0] + C[0]) / 2 - 40, (A[1] + C[1]) / 2, f"{side_ac}", ha="right", fontsize=9, fontweight="bold")
    plt.text((B[0] + C[0]) / 2 + 40, (B[1] + C[1]) / 2, f"x = {side_bc:.1f}", ha="left", fontsize=9, fontweight="bold")


# -----------------------------------------------------------------------------
# Main Simulation Loop
# -----------------------------------------------------------------------------
# Initialize tracking variables with large starting values
min_area = float("inf")
best_x = 0

# Known side lengths from the problem
AB = 888
AC = 925

# Fix vertex A at the origin and vertex B along the positive x-axis
A = (0, 0)
B = (AB, 0)

# By the triangle inequality, the third side x must be strictly between |AC - AB| and AC + AB
min_valid_x = abs(AC - AB) + 1
max_valid_x = AC + AB - 1

# Test random values of x and animate the search for the smallest circumcircle
for _ in range(10**6):
    # Clear the previous frame so drawings don't pile up on top of each other
    plt.cla()

    # Pick a random length for side BC (labeled 'x' in the problem)[cite: 1]
    x = uniform(min_valid_x, max_valid_x)

    # Find angle A (alpha) opposite side x, then calculate coordinates of vertex C
    alpha, ok_angle = law_of_cosines(AB, AC, x)
    if not ok_angle:
        continue
    C = (AC * cos(alpha), AC * sin(alpha))

    # Compute the circumcenter and circumradius for triangle ABC
    center, r, ok_circle = circum_circle(A, B, C)
    if not ok_circle:
        continue

    # Calculate the area of the circumscribed circle (Area = pi * r^2)
    area = pi * r**2

    # If this circle is smaller than our previous record, save the new best values
    if area < min_area:
        min_area = area
        best_x = x

    # Draw the circumscribed circle, the triangle edges, and fill the triangle
    plot_circle(center, r)
    plot_line(A, B)
    plot_line(C, B)
    plot_line(A, C)
    plt.fill(*polygon_fill_coordinates(A, B, C), color="red", alpha=0.3)

    # Add vertex coordinates and side-length labels to the plot
    add_labels(A, B, C, center, AB, AC, x)

    # Format the chart title and display settings
    plt.title(f"Minimum circle area {min_area:,.1f} occurs near x = {best_x:.1f}")
    plt.axis("equal")  # Keep x and y scales equal so circles don't look like ovals
    plt.axis("off")    # Hide the outer axes box and tick marks
    plt.pause(0.05)    # Pause briefly so the animation is visible

plt.show()
