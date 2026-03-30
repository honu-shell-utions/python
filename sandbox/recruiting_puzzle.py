"""
Python solution to the Recruiting Puzzle
Video: https://youtu.be/cxfYSPR_eUU?si=HL3AOz6MLt0Qfyuf

This script investigates one geometric interpretation of the puzzle
numerically and draws the resulting figure.

Jim McCleery
March 29, 2026
Kona, HI
"""

from math import pi, sqrt
import numpy as np
import matplotlib.pyplot as plt


def plot_line(x1, y1, x2, y2):
    """Plot a line segment between two points."""
    plt.plot([x1, x2], [y1, y2], color="black")


def polygon_area(vertices):
    """
    Compute the area of a polygon using the shoelace formula.

    Parameters
    ----------
    vertices : list[tuple[float, float]]
        Ordered list of polygon vertices.

    Returns
    -------
    float
        The polygon's area.
    """
    area = 0.0
    n = len(vertices)

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2

    return abs(area) / 2


def polygon_fill_coordinates(vertices):
    """
    Return x- and y-coordinate lists suitable for matplotlib fill().

    The polygon is closed by repeating the first vertex at the end.
    """
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords


# -----------------------------------------------------------------------------
# Geometry from the diagram
#
# The three given areas imply the following square side lengths:
#   small square area   = 5      -> side = sqrt(5)
#   medium square area  = 20     -> side = 2*sqrt(5)
#   large square area   = 36*pi  -> side = 6*sqrt(pi)
# -----------------------------------------------------------------------------
s1 = sqrt(5)         # side of the small square
s2 = 2 * s1          # side of the medium square
s3 = 6 * sqrt(pi)    # side of the large square

# -----------------------------------------------------------------------------
# Key points in the figure
#
# These points are placed directly from the diagram, working around the shape.
# -----------------------------------------------------------------------------
x0, y0 = 0, 0
x1, y1 = s1, 0
x2, y2 = s1 + s2, 0
x3, y3 = s1 + s2 + s3, 0
x4, y4 = x3, s3
x5, y5 = x2, s3
x6, y6 = x2, s2
x7, y7 = x1, 2 * s1
x8, y8 = 0, 2 * s1
x9, y9 = 0, s1
x10, y10 = s1, s1

# -----------------------------------------------------------------------------
# Labels shown on the figure
# -----------------------------------------------------------------------------
plt.text(1, 1.2, "5")
plt.text(12, 6, "36π")

# -----------------------------------------------------------------------------
# Draw the line structure of the diagram
# -----------------------------------------------------------------------------
plot_line(x0, y0, x3, y3)
plot_line(x4, y4, x3, y3)
plot_line(x4, y4, x5, y5)
plot_line(x2, y2, x5, y5)
plot_line(x6, y6, x8, y8)
plot_line(x0, y0, x8, y8)
plot_line(x7, y7, x1, y1)
plot_line(x9, y9, x10, y10)
plot_line(x4, y4, x9, y9)
plot_line(x4, y4, x7, y7)
plot_line(x9, y9, x7, y7)

# -----------------------------------------------------------------------------
# Fill the large yellow region
# -----------------------------------------------------------------------------
yellow_region = [(x0, y0), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x8, y8)]
plt.fill(
    *polygon_fill_coordinates(yellow_region),
    color="yellow",
    edgecolor="yellow",
    linewidth=2,
)

# -----------------------------------------------------------------------------
# Fill the red triangle and compute its area
# -----------------------------------------------------------------------------
red_triangle = [(x4, y4), (x7, y7), (x9, y9)]
red_area = polygon_area(red_triangle)

plt.fill(
    *polygon_fill_coordinates(red_triangle),
    color="red",
    edgecolor="red",
    linewidth=2,
)

plt.title(f"Area of red triangle: {red_area}")

# -----------------------------------------------------------------------------
# Final plot settings
# -----------------------------------------------------------------------------
plt.axis("equal")  # preserve geometric proportions
plt.show()
