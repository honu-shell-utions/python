"""
Jim McCleery
May 6, 2026
Kailua-Kona, HI

Source inspiration:
https://youtu.be/68CoMp0PVv4?si=L5fw2903LKN8r4Kj

This program constructs a geometric figure and draws the circle through
three selected points. The area of that circle is displayed in the title.
"""

from math import acos, cos, pi, sin, sqrt

import matplotlib.pyplot as plt
import numpy as np


# ---------------------------------------------------------------------------
# Geometry helper functions
# ---------------------------------------------------------------------------

def law_of_cosines(side_a, side_b, opposite_side):
    """
    Return the angle opposite 'opposite_side' in a triangle.

    The three side lengths are:
        side_a, side_b, opposite_side

    Uses:
        c^2 = a^2 + b^2 - 2ab cos(C)

    Returns:
        angle in radians
    """
    cosine_value = (
        side_a**2 + side_b**2 - opposite_side**2
    ) / (2 * side_a * side_b)

    return acos(cosine_value)


def circle_from_three_points(p1, p2, p3):
    """
    Return the center and radius of the unique circle through three points.

    Args:
        p1, p2, p3: points of the form (x, y)

    Returns:
        (center_x, center_y, radius)

    Raises:
        ValueError if the three points are collinear.
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    temp = x2**2 + y2**2
    bc = (x1**2 + y1**2 - temp) / 2
    cd = (temp - x3**2 - y3**2) / 2

    determinant = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    if abs(determinant) < 1.0e-12:
        raise ValueError("The three points are collinear; no unique circle exists.")

    center_x = (bc * (y2 - y3) - cd * (y1 - y2)) / determinant
    center_y = ((x1 - x2) * cd - (x2 - x3) * bc) / determinant

    radius = sqrt((center_x - x1) ** 2 + (center_y - y1) ** 2)

    return center_x, center_y, radius


def plot_circle(ax, center, radius, *, color="black", linewidth=2):
    """
    Plot a circle on the given axes.
    """
    center_x, center_y = center
    theta = np.linspace(0, 2 * pi, 1000)

    x_values = center_x + radius * np.cos(theta)
    y_values = center_y + radius * np.sin(theta)

    ax.plot(x_values, y_values, color=color, linewidth=linewidth)


def fill_circle(ax, center, radius, *, color="red", alpha=0.35):
    """
    Fill a circle on the given axes.
    """
    center_x, center_y = center
    theta = np.linspace(0, 2 * pi, 1000)

    x_values = center_x + radius * np.cos(theta)
    y_values = center_y + radius * np.sin(theta)

    ax.fill(x_values, y_values, color=color, alpha=alpha)


def plot_segment(ax, p1, p2, *, color="black", linewidth=2):
    """
    Plot a line segment between two points.
    """
    x1, y1 = p1
    x2, y2 = p2

    ax.plot([x1, x2], [y1, y2], color=color, linewidth=linewidth)


def label_point(ax, point, label, *, dx=0.6, dy=0.6):
    """
    Add a text label near a point.
    """
    x, y = point
    ax.scatter(x, y, color="black", s=20)
    ax.text(x + dx, y + dy, label, fontsize=12, weight="bold")


# ---------------------------------------------------------------------------
# Main construction
# ---------------------------------------------------------------------------

def main():
    """
    Construct the figure, draw the circle, and label the relevant vertices.
    """

    # These two angles come from triangles with side lengths 26, 28, and 30.
    theta = law_of_cosines(28, 30, 26)
    alpha = law_of_cosines(26, 30, 28)

    # Offset distance used to locate point E from point A.
    offset_length = 12

    # Define the main points of the construction.
    #
    # O is the origin.
    # A and C lie on the negative x-axis.
    # B and D lie on the ray determined by angle pi - theta.
    # E is constructed from A using angle alpha.
    point_o = (0, 0)
    point_a = (-30, 0)
    point_b = (
        28 * cos(pi - theta),
        28 * sin(pi - theta),
    )
    point_c = (-42, 0)
    point_d = (
        42 * cos(pi - theta),
        42 * sin(pi - theta),
    )
    point_e = (
        point_a[0] + offset_length * cos(alpha),
        offset_length * sin(alpha),
    )

    # The red circle is the circumcircle through C, D, and E.
    center_x, center_y, radius = circle_from_three_points(
        point_c,
        point_d,
        point_e,
    )
    circle_center = (center_x, center_y)
    circle_area = pi * radius**2

    # Create the plot.
    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw and shade the circle.
    fill_circle(ax, circle_center, radius, color="red", alpha=0.35)
    plot_circle(ax, circle_center, radius, color="red", linewidth=2)

    # Draw the main construction lines.
    plot_segment(ax, point_o, point_c)
    plot_segment(ax, point_o, point_d)
    plot_segment(ax, point_a, point_b)

    # Label the vertices and circle center.
    label_point(ax, point_o, "O")
    label_point(ax, point_a, "A")
    label_point(ax, point_b, "B")
    label_point(ax, point_c, "C")
    label_point(ax, point_d, "D")
    label_point(ax, point_e, "E")
    label_point(ax, circle_center, "P", dx=0.8, dy=-1.2)

    # Add a clean title and set equal scaling so the circle appears round.
    ax.set_title(f"Area of Red Circle: {circle_area:.4f}", fontsize=14)
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, linestyle="--", alpha=0.3)

    plt.show()


if __name__ == "__main__":
    main()
