"""
Jim McCleery
April 27, 2026
Kailua-Kona, HI

Problem source:
https://mathnet.mit.edu/explorer.html?view=detail&problem=ba1138e632ba6feb36c23770206a5a0a39c45d9057d873cd936320e012af0ac3&mode=country&country=United+States
"""

from math import acos, cos, pi, sin, sqrt

import matplotlib.pyplot as plt
import numpy as np


def law_of_cosines(side_a, side_b, opposite_side):
    """
    Return the angle opposite opposite_side in a triangle with side lengths
    side_a, side_b, and opposite_side.

    The returned angle is measured in radians.
    """
    cosine_value = (
        side_a**2 + side_b**2 - opposite_side**2
    ) / (2 * side_a * side_b)

    return acos(cosine_value)


def circle_through_three_points(point_1, point_2, point_3):
    """
    Return the center and radius of the circle through three non-collinear points.

    Args:
        point_1, point_2, point_3: ordered pairs of the form (x, y)

    Returns:
        center_x, center_y, radius
    """
    x1, y1 = point_1
    x2, y2 = point_2
    x3, y3 = point_3

    s1 = x1**2 + y1**2
    s2 = x2**2 + y2**2
    s3 = x3**2 + y3**2

    determinant = (
        x1 * y2 + x2 * y3 + x3 * y1
        - x2 * y1 - x3 * y2 - x1 * y3
    )

    if abs(determinant) < 1e-12:
        raise ValueError("The three points are collinear, so no circle is defined.")

    center_x = 0.5 * (
        s1 * y2 + s2 * y3 + s3 * y1
        - s2 * y1 - s3 * y2 - s1 * y3
    ) / determinant

    center_y = -0.5 * (
        s1 * x2 + s2 * x3 + s3 * x1
        - s2 * x1 - s3 * x2 - s1 * x3
    ) / determinant

    radius = sqrt((x1 - center_x) ** 2 + (y1 - center_y) ** 2)

    return center_x, center_y, radius


def plot_segment(point_1, point_2, **kwargs):
    """
    Plot the line segment from point_1 to point_2.
    """
    x1, y1 = point_1
    x2, y2 = point_2
    plt.plot([x1, x2], [y1, y2], **kwargs)


def plot_circle(center_x, center_y, radius, **kwargs):
    """
    Plot a circle with the given center and radius.
    """
    theta = np.linspace(0, 2 * pi, 1000)
    x_values = center_x + radius * np.cos(theta)
    y_values = center_y + radius * np.sin(theta)

    plt.plot(x_values, y_values, **kwargs)


def label_point(label, point, dx=0.12, dy=0.12):
    """
    Label a point on the graph with a small offset.
    """
    x, y = point
    plt.scatter(x, y, zorder=3)
    plt.text(x + dx, y + dy, label, fontsize=12, weight="bold")


# -----------------------------------------------------------------------------
# Construct the points.
#
# The figure is built from triangles with side lengths 5, 6, 7 and related
# segments.  Point A is placed at the origin and point B on the x-axis.
# -----------------------------------------------------------------------------

A = (0, 0)
B = (5, 0)

# Angle at A in the triangle with sides 5, 6, and 7.
alpha = law_of_cosines(5, 7, 6)

# Point C is located 7 units from A at angle alpha.
C = (7 * cos(alpha), 7 * sin(alpha))

# Point D lies on the x-axis.
D = (12, 0)

# Angle used to place point E relative to B.
beta = law_of_cosines(5, 6, 7)

E = (
    5 + 11 * cos(pi - beta),
    11 * sin(pi - beta),
)

# Point F is placed 6 units from A in the opposite direction from angle alpha.
F = (
    6 * cos(alpha - pi),
    6 * sin(alpha - pi),
)

# -----------------------------------------------------------------------------
# Find the circumcircle determined by D, E, and F.
# -----------------------------------------------------------------------------

center_x, center_y, radius = circle_through_three_points(D, E, F)
circle_area = pi * radius**2

# -----------------------------------------------------------------------------
# Draw the figure.
# -----------------------------------------------------------------------------

segments = [
    (A, D),
    (E, B),
    (F, C),
    (F, D),
    (E, D),
    (F, E),
]

for point_1, point_2 in segments:
    plot_segment(point_1, point_2, color="black", linewidth=2)

plot_circle(center_x, center_y, radius, color="blue", linewidth=2)

# Label the vertices.
for label, point in {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
}.items():
    label_point(label, point)

# Give F a custom offset so the label is easier to read.
label_point("F", F, dx=-0.45, dy=0.18)

plt.title(f"Area of Circumcircle = {circle_area:.6f}")
plt.axis("equal")
plt.grid(True, alpha=0.3)
plt.show()
