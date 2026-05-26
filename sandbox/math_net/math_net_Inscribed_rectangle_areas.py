# -----------------------------------------------------------------------------
# Jim McCleery
# May 26, 2026
# Kailua-Kona, HI
#
# Problem link:
# https://mathnet.mit.edu/explorer.html?p=usa_2025_1bed77
# -----------------------------------------------------------------------------

from math import pi, sqrt
from random import uniform

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Return the area of a polygon using the shoelace formula.

    The polygon should be given as an ordered list of points:

        [(x1, y1), (x2, y2), (x3, y3), ...]

    The formula works by walking around the outside of the polygon and
    combining the coordinates of neighboring points.
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
    Return the x-coordinates and y-coordinates needed to fill a polygon.

    Matplotlib's fill() command wants the x-values and y-values in two
    separate lists. This function separates them.

    The first point is repeated at the end so the polygon is closed.
    """
    x_coordinates, y_coordinates = zip(*vertices)

    x_coordinates = list(x_coordinates)
    y_coordinates = list(y_coordinates)

    x_coordinates.append(x_coordinates[0])
    y_coordinates.append(y_coordinates[0])

    return x_coordinates, y_coordinates


# -----------------------------------------------------------------------------
def plot_circle(center_x, center_y, radius, start_angle=0, stop_angle=2 * pi):
    """
    Plot a circle, or part of a circle.

    Angles are measured in radians.
    A full circle goes from 0 to 2*pi.
    """
    angles = np.linspace(start_angle, stop_angle, 1500)

    x_values = center_x + radius * np.cos(angles)
    y_values = center_y + radius * np.sin(angles)

    plt.plot(x_values, y_values)


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Plot a line segment from point (x1, y1) to point (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------

# Radius of the small circle
small_radius = 6

# Radius of the large circle
large_radius = 15

# Centers and important points
large_center_x, large_center_y = 0, 0
small_center_x, small_center_y = 9, 0

left_point_x, left_point_y = -large_radius, 0
right_point_x, right_point_y = large_radius, 0

top_small_circle_x = 9
top_small_circle_y = sqrt(large_radius**2 - 9**2)

# Search for a point on the small circle that makes the two red triangle
# areas nearly equal.
#
# The point (x, y) is chosen on the upper-left part of the small circle.
# Since the small circle has center (9, 0) and radius 6, its equation is:
#
#     (x - 9)^2 + y^2 = 6^2
#
# Solving for y gives:
#
#     y = sqrt(6^2 - (x - 9)^2)
#
while True:
    x = uniform(3, 9)
    y = sqrt(small_radius**2 - (x - small_center_x) ** 2)

    # Reflected and related points used in the drawing
    lower_left_x, lower_left_y = x, -y
    lower_right_x, lower_right_y = 18 - x, -y
    upper_right_x, upper_right_y = 18 - x, y

    # The two red triangles
    triangle_1 = [
        (x, y),
        (lower_left_x, lower_left_y),
        (left_point_x, left_point_y),
    ]

    triangle_2 = [
        (x, y),
        (top_small_circle_x, top_small_circle_y),
        (upper_right_x, upper_right_y),
    ]

    area_1 = polygon_area(triangle_1)
    area_2 = polygon_area(triangle_2)

    # Stop searching when the two areas are close enough.
    if abs(area_1 - area_2) < 0.0001:
        break


# Draw the large and small circles
plot_circle(large_center_x, large_center_y, large_radius)
plot_circle(small_center_x, small_center_y, small_radius)

# Draw the horizontal diameter of the large circle
plot_line(left_point_x, left_point_y, right_point_x, right_point_y)

# Draw lines connected to the left point
plot_line(left_point_x, left_point_y, x, y)
plot_line(left_point_x, left_point_y, lower_left_x, lower_left_y)

# Draw the remaining line segments in the figure
plot_line(x, y, top_small_circle_x, top_small_circle_y)
plot_line(top_small_circle_x, top_small_circle_y, upper_right_x, upper_right_y)
plot_line(lower_left_x, lower_left_y, x, y)
plot_line(lower_right_x, lower_right_y, upper_right_x, upper_right_y)
plot_line(x, y, upper_right_x, upper_right_y)
plot_line(lower_left_x, lower_left_y, lower_right_x, lower_right_y)
plot_line(top_small_circle_x, top_small_circle_y, small_center_x, small_center_y)
plot_line(top_small_circle_x, top_small_circle_y, upper_right_x, upper_right_y)
plot_line(left_point_x, left_point_y, lower_left_x, lower_left_y)

# Fill the two equal-area triangles in red
plt.fill(
    *polygon_fill_coordinates(triangle_1),
    color="red",
    edgecolor="red",
    linewidth=2,
)

plt.fill(
    *polygon_fill_coordinates(triangle_2),
    color="red",
    edgecolor="red",
    linewidth=2,
)

# Make the x- and y-scales equal so circles look like circles
plt.axis("equal")

# Add a title showing the common triangle area
plt.title(f"The area of each red triangle is approximately {area_1:0.2f}")

plt.show()
