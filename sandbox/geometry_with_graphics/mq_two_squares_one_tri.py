# -----------------------------------------------------------------------------
# Jim McCleery
# May 21, 2026
# Kailua-Kona, HI
#
# https://youtu.be/ymJvyTKT0s4?si=yqlPWLVSFeNCciOx
# -----------------------------------------------------------------------------

from random import uniform
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Draw a line segment from point (x1, y1) to point (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Find the area of a polygon using the shoelace formula.

    The vertices should be listed in order around the polygon.
    Example:
        [(0, 0), (4, 0), (4, 3)]
    """
    area = 0
    number_of_vertices = len(vertices)

    for i in range(number_of_vertices):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % number_of_vertices]

        area += x1 * y2 - y1 * x2

    return abs(area) / 2


# -----------------------------------------------------------------------------
def polygon_fill_coordinates(vertices):
    """
    Convert a list of polygon vertices into two lists:
        one list of x-coordinates
        one list of y-coordinates

    The first point is repeated at the end so the polygon closes.
    """
    x_values = []
    y_values = []

    for x, y in vertices:
        x_values.append(x)
        y_values.append(y)

    # Repeat the first point to close the polygon.
    x_values.append(vertices[0][0])
    y_values.append(vertices[0][1])

    return x_values, y_values


# -----------------------------------------------------------------------------
def draw_diagram(extra_length):
    """
    Draw one version of the geometric diagram.

    The variable extra_length changes the horizontal length of part of the figure.
    Even though the shape changes, the red triangle's area remains constant.
    """

    # Main points along the top horizontal line.
    x0, y0 = 0, 0
    x1, y1 = 3, 0
    x2, y2 = 3 + extra_length, 0
    x3, y3 = 7 + extra_length, 0

    # Points below the top line.
    x4, y4 = x3, -4
    x5, y5 = x2, -4
    x6, y6 = 3, -3
    x7, y7 = 0, -3

    # Find the y-intercept of the slanted line through (x1, y1) and (x5, y5).
    slope = (y5 - y1) / (x5 - x1)
    x8 = 0
    y8 = y5 - slope * x5

    # Draw the outer and inner line segments.
    plot_line(x0, y0, x3, y3)
    plot_line(x3, y3, x4, y4)
    plot_line(x5, y5, x4, y4)
    plot_line(x5, y5, x2, y2)

    plot_line(x1, y1, x6, y6)
    plot_line(x6, y6, x7, y7)
    plot_line(x8, y8, x7, y7)
    plot_line(x8, y8, x5, y5)

    # The red triangle has vertices at these three points.
    red_triangle = [(x1, y1), (x2, y2), (x8, y8)]

    # Fill the red triangle.
    x_fill, y_fill = polygon_fill_coordinates(red_triangle)
    plt.fill(x_fill, y_fill, color="red", edgecolor="red", linewidth=2)

    # Compute and display the area of the red triangle.
    area = polygon_area(red_triangle)
    plt.title(f"Area of the red triangle = {area:0.3f}")

    # Make equal units on the x-axis and y-axis so the geometry is not distorted.
    plt.axis("equal")

    # Display the finished picture.
    plt.show()


# -----------------------------------------------------------------------------
# Draw 10 random versions of the diagram.
# The red triangle changes shape, but its area stays the same.
for _ in range(10):
    extra_length = uniform(2, 10)
    draw_diagram(extra_length)
