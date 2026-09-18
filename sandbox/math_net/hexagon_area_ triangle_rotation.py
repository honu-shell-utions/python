# -----------------------------------------------------------------------------
# Jim McCleery
# May 20, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2024_e18b0d
# -----------------------------------------------------------------------------

from math import pi, sqrt, sin, cos, tan, radians
from random import uniform

import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Return the area of a polygon using the shoelace formula.

    The polygon is given as an ordered list of (x, y) points.
    For example:
        [(0, 0), (4, 0), (4, 3), (0, 3)]
    """
    area = 0

    # Loop through each edge of the polygon.
    # The expression (i + 1) % len(vertices) wraps around to the first point.
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        area += x1 * y2 - y1 * x2

    return abs(area) / 2


# -----------------------------------------------------------------------------
def polygon_fill_coordinates(vertices):
    """
    Return separate x-coordinate and y-coordinate lists for filling a polygon.

    Matplotlib wants the x-values in one list and the y-values in another list.
    We also repeat the first point at the end so the polygon closes.
    """
    x_coords, y_coords = zip(*vertices)

    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]

    return x_coords, y_coords


# -----------------------------------------------------------------------------
def rotate_polygon(points, angle_degrees, center=(0, 0)):
    """
    Rotate a list of points around a center point.

    Args:
        points: a list of (x, y) points
        angle_degrees: the rotation angle, measured in degrees
        center: the point around which the polygon rotates

    Returns:
        A new list of rotated (x, y) points.
    """
    points = np.array(points, dtype=float)
    center = np.array(center, dtype=float)

    # Convert degrees to radians because sine and cosine use radians.
    theta = np.radians(angle_degrees)

    # This is the standard 2D rotation matrix.
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    # Move the points so the center is at the origin,
    # rotate them, then move them back.
    rotated_points = (points - center) @ rotation_matrix.T + center

    return rotated_points.tolist()


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Draw a line segment from (x1, y1) to (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------

# Side length-related value for the triangles.
a = 14 / sqrt(3)

# The first triangle is rotated 15 degrees from the x-axis.
gamma = radians(15)

# Target area from the problem.
target_area = 91 * sqrt(3)

# Keep trying random angles until the polygon area is close to the target.
while True:
    theta = uniform(0, 60)

    # Center point.
    x0, y0 = 0, 0

    # Vertices of the first equilateral triangle.
    x1, y1 = a * cos(gamma),              a * sin(gamma)
    x2, y2 = a * cos(gamma + 2 * pi / 3), a * sin(gamma + 2 * pi / 3)
    x3, y3 = a * cos(gamma + 4 * pi / 3), a * sin(gamma + 4 * pi / 3)

    first_triangle = [(x1, y1), (x2, y2), (x3, y3)]

    # Rotate the triangle by a random angle theta.
    second_triangle = rotate_polygon(first_triangle, theta)

    x4, y4 = second_triangle[0]
    x5, y5 = second_triangle[1]
    x6, y6 = second_triangle[2]

    # These six points form the red polygon.
    vertices = [
        (x1, y1),
        (x4, y4),
        (x2, y2),
        (x5, y5),
        (x3, y3),
        (x6, y6)
    ]

    area = polygon_area(vertices)

    # Stop when the computed area is close enough to the target area.
    if abs(area - target_area) < 0.0001:
        break


# -----------------------------------------------------------------------------
# Draw the final picture
# -----------------------------------------------------------------------------

# Draw the center point.
plt.plot(x0, y0, "o")

# Fill the six-sided polygon.
plt.fill(
    *polygon_fill_coordinates(vertices),
    color="red",
    edgecolor="red",
    linewidth=2
)

# Draw the sides of the first triangle.
plot_line(x1, y1, x2, y2)
plot_line(x2, y2, x3, y3)
plot_line(x1, y1, x3, y3)

# Draw the sides of the rotated triangle.
plot_line(x4, y4, x5, y5)
plot_line(x5, y5, x6, y6)
plot_line(x4, y4, x6, y6)

# Display tan(theta) in the title.
plt.title(f"tan(theta) ≈ {round(tan(radians(theta)), 5)}")

# Make sure the scale is the same on both axes.
plt.axis("equal")

plt.show()
