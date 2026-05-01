"""
Jim McCleery
April 30, 2026
Kailua-Kona, HI

Reference:
https://youtu.be/x2ocJ5wlNuc?si=EeILoTBDrZqlD-dR

This program draws three mutually tangent inner circles and their enclosing
circle. The centers of the circles are labeled as vertices A, B, C, and D.

A, B, C are the centers of the three smaller circles.
D is the center of the enclosing circle.
"""

from math import acos, cos, pi, sin, sqrt

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Geometry helper functions
# -----------------------------------------------------------------------------

def law_of_cosines_angle(side_a, side_b, opposite_side):
    """
    Return the angle opposite 'opposite_side' in a triangle with side lengths
    side_a, side_b, and opposite_side.

    The returned angle is measured in radians.
    """
    cosine_value = (
        side_a**2 + side_b**2 - opposite_side**2
    ) / (2 * side_a * side_b)

    return acos(cosine_value)


def plot_circle(center_x, center_y, radius, label=None):
    """
    Plot a circle with the given center and radius.

    If a label is supplied, the center point is marked and labeled.
    """
    theta = np.linspace(0, 2 * pi, 1000)

    x_values = center_x + radius * np.cos(theta)
    y_values = center_y + radius * np.sin(theta)

    plt.plot(x_values, y_values)

    if label is not None:
        plt.plot(center_x, center_y, "ko")
        plt.text(
            center_x + 0.25,
            center_y + 0.25,
            label,
            fontsize=12,
            fontweight="bold",
        )


def plot_segment(point_1, point_2, linestyle="--"):
    """
    Plot a line segment between two points.

    Each point should be given as an (x, y) pair.
    """
    x1, y1 = point_1
    x2, y2 = point_2

    plt.plot([x1, x2], [y1, y2], linestyle)


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------

def main():
    """
    Draw the circle configuration and display the area of the enclosing circle.
    """

    # Radii of the three inner circles and the enclosing circle
    radius_a = 10
    radius_b = 3
    radius_c = 2
    radius_d = 15

    # The centers A, B, and C form a triangle.
    #
    # Since the inner circles are tangent:
    #   AB = radius_a + radius_b = 13
    #   AC = radius_a + radius_c = 12
    #   BC = radius_b + radius_c = 5
    #
    # We place A at the origin and B on the positive x-axis.
    angle_a = law_of_cosines_angle(12, 13, 5)

    point_a = (0, 0)
    point_b = (radius_a + radius_b, 0)
    point_c = (
        (radius_a + radius_c) * cos(angle_a),
        (radius_a + radius_c) * sin(angle_a),
    )

    # Center of the enclosing circle.
    #
    # These coordinates come from solving the system:
    #
    #   x^2 + y^2 = (radius_d - radius_a)^2
    #   (x - 13)^2 + y^2 = (radius_d - radius_b)^2
    #   (x - 144/13)^2 + (y - 60/13)^2 = (radius_d - radius_c)^2
    #
    # The solution is:
    #   D = (25/13, -60/13)
    point_d = (25 / 13, -60 / 13)

    # Draw the four circles.
    plot_circle(*point_a, radius_a, label="A")
    plot_circle(*point_b, radius_b, label="B")
    plot_circle(*point_c, radius_c, label="C")
    plot_circle(*point_d, radius_d, label="D")

    # Draw the triangle formed by the centers of the three inner circles.
    plot_segment(point_a, point_b)
    plot_segment(point_b, point_c)
    plot_segment(point_c, point_a)

    # Draw radii from the enclosing circle center to the inner circle centers.
    plot_segment(point_d, point_a, linestyle=":")
    plot_segment(point_d, point_b, linestyle=":")
    plot_segment(point_d, point_c, linestyle=":")

    enclosing_area = pi * radius_d**2

    plt.title(f"Area of Enclosing Circle: {enclosing_area:.2f}")
    plt.axis("equal")
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
