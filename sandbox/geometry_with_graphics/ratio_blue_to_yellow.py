"""
Numerical exploration of Andy's math problem.

Video:
https://youtu.be/yuHB2_G4VXA?si=T334GV3i2wZR23v7

This program searches for a point on the left side of a 3x3 square so that
a certain constructed 1x1 tilted square has one corner lying on the line
through two key points of the figure.

Once such a configuration is found, the program draws the figure and reports
the ratio:

    blue area / yellow area

Jim McCleery
March 30, 2026
Kona, HI
"""

from math import pi, sqrt, atan, tan
from random import uniform

from matplotlib.pyplot import axis, fill, plot, show, title


def plot_line(x1, y1, x2, y2):
    """Draw a line segment from (x1, y1) to (x2, y2)."""
    plot([x1, x2], [y1, y2])


def polygon_area(vertices):
    """
    Compute the area of a polygon using the shoelace formula.

    The vertices should be given in order around the polygon.
    """
    area = 0
    n = len(vertices)

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2

    return abs(area) / 2


def polygon_xy(vertices):
    """
    Convert a list of polygon vertices into x- and y-coordinate lists
    suitable for matplotlib fill().
    """
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords


# ---------------------------------------------------------------------
# Geometry setup
#
# The large square is the 3x3 square:
#   (0,0), (3,0), (3,3), (0,3)
#
# A random point x4,y4 is chosen on the left side x=0, with 0 < y < 2.
# From that point a broken line goes to (3,0) and then to a point on y=3.
#
# A 1x1 tilted square is then constructed using one of the slanted segments.
# The loop continues until the upper-right corner of that small square lies
# on the line from (3,0) to the top intersection point.
# ---------------------------------------------------------------------

while True:
    # Corners of the outer 3x3 square
    x0, y0 = 0, 0
    x1, y1 = 3, 0
    x2, y2 = 3, 3
    x3, y3 = 0, 3

    # Random point on the left side of the square
    x4, y4 = 0, uniform(0, 2)

    # Find the point (x5, y5) on the top edge y=3 so that the segment
    # from (x4, y4) to (x5, y5) has the required geometry.
    theta = atan(3 / y4)
    x5, y5 = (3 - y4) * tan(pi / 2 - theta), 3

    # Slope of the segment from (x4, y4) to (x5, y5)
    m = (y5 - y4) / (x5 - x4)

    # Point (x6, y6) is chosen on that slanted segment so that the
    # 1x1 tilted square can be built from it.
    #
    # The formula for x6 comes from the geometry of stepping one unit
    # in the slope direction and one unit in the perpendicular direction.
    x6 = (x4 * (m + 1 / m) + 1) / (m + 1 / m)
    y6 = m * (x6 - x4) + y4

    # Construct the other three vertices of the 1x1 tilted square.
    # From (x6, y6), move down 1 unit and right 1 unit in axis directions.
    x7, y7 = x6, y6 - 1
    x8, y8 = x6 + 1, y6
    x9, y9 = x8, y8 - 1

    # Slope of the line from (3,0) to the point (x5, y5) on the top edge
    m = (y5 - y1) / (x5 - x1)

    # Stop when the point (x8, y8) lies on that line, up to a tiny tolerance.
    # This is the numerical condition defining the desired configuration.
    if abs(y8 - y1 - m * (x8 - x1)) < 1e-6:
        break


# ---------------------------------------------------------------------
# Draw the figure
# ---------------------------------------------------------------------

# Small tilted square
plot_line(x8, y8, x9, y9)
plot_line(x9, y9, x7, y7)
plot_line(x6, y6, x7, y7)
plot_line(x6, y6, x8, y8)

# Outer 3x3 square
plot_line(x0, y0, x1, y1)
plot_line(x1, y1, x2, y2)
plot_line(x2, y2, x3, y3)
plot_line(x3, y3, x0, y0)

# Interior triangle and diagonals
plot_line(x1, y1, x4, y4)
plot_line(x4, y4, x5, y5)
plot_line(x1, y1, x5, y5)

# Fill the outer square yellow first
outer_square = [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]
fill(*polygon_xy(outer_square), color="yellow", edgecolor="blue", linewidth=2)

# The blue triangle cut from the square
triangle = [(x1, y1), (x4, y4), (x5, y5)]
triangle_area = polygon_area(triangle)

# Total square area is 9.
# Yellow area is what remains after removing the triangle.
yellow_area = 9 - triangle_area

# Blue area is the triangle area minus the 1x1 white square.
blue_area = triangle_area - 1

fill(*polygon_xy(triangle), color="blue", edgecolor="blue", linewidth=2)

# Fill the 1x1 tilted square white
small_square = [(x7, y7), (x6, y6), (x8, y8), (x9, y9)]
fill(*polygon_xy(small_square), color="white", edgecolor="blue", linewidth=2)

title(f"Ratio blue area to yellow area = {blue_area / yellow_area:.4f}")
axis("equal")
show()
