"""
Jim McCleery
April 28, 2026
Kailua-Kona, HI

Source:
https://mathnet.mit.edu/explorer.html?view=problems&mode=country&country=United+States
"""

from math import acos, cos, pi, sin, sqrt

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Geometry helper functions
# -----------------------------------------------------------------------------

def distance(point_1, point_2):
    """Return the Euclidean distance between two points."""
    x1, y1 = point_1
    x2, y2 = point_2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def midpoint(point_1, point_2):
    """Return the midpoint of the segment joining two points."""
    x1, y1 = point_1
    x2, y2 = point_2
    return (x1 + x2) / 2, (y1 + y2) / 2


def quadratic_roots(a, b, c):
    """
    Return the real roots of a quadratic equation.

    Solves:
        a*x^2 + b*x + c = 0

    Returns:
        (root_1, root_2)
    """
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        raise ValueError("The quadratic has no real roots.")

    root_1 = (-b - sqrt(discriminant)) / (2 * a)
    root_2 = (-b + sqrt(discriminant)) / (2 * a)

    return root_1, root_2


def circle_through_points(point_1, point_2, point_3):
    """
    Return the center and radius of the circle through three non-collinear points.
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

    m12 = (
        s1 * y2 + s2 * y3 + s3 * y1
        - s2 * y1 - s3 * y2 - s1 * y3
    )

    m13 = (
        s1 * x2 + s2 * x3 + s3 * x1
        - s2 * x1 - s3 * x2 - s1 * x3
    )

    center_x = 0.5 * m12 / determinant
    center_y = -0.5 * m13 / determinant

    center = (center_x, center_y)
    radius = distance(center, point_1)

    return center, radius


def horizontal_line_circle_intersection(center, radius, y_value):
    """
    Return the two intersection points of a circle with the horizontal line y = y_value.
    """
    center_x, center_y = center

    # Circle equation:
    #     (x - center_x)^2 + (y - center_y)^2 = radius^2
    #
    # Substitute y = y_value and solve for x.
    a = 1
    b = -2 * center_x
    c = center_x**2 + (y_value - center_y) ** 2 - radius**2

    x1, x2 = quadratic_roots(a, b, c)

    return (x1, y_value), (x2, y_value)


# -----------------------------------------------------------------------------
# Plotting helper functions
# -----------------------------------------------------------------------------

def plot_segment(ax, point_1, point_2, **kwargs):
    """Plot a line segment between two points."""
    x1, y1 = point_1
    x2, y2 = point_2
    ax.plot([x1, x2], [y1, y2], **kwargs)


def plot_circle(ax, center, radius, **kwargs):
    """Plot a circle."""
    center_x, center_y = center
    theta = np.linspace(0, 2 * pi, 1000)

    x_values = center_x + radius * np.cos(theta)
    y_values = center_y + radius * np.sin(theta)

    ax.plot(x_values, y_values, **kwargs)


def label_point(ax, point, label, x_offset=0.04, y_offset=0.04):
    """Mark and label a point on the plot."""
    x, y = point
    ax.scatter(x, y, zorder=3)
    ax.text(x + x_offset, y + y_offset, label, fontsize=12)


# -----------------------------------------------------------------------------
# Main construction
# -----------------------------------------------------------------------------

def main():
    # Define an equilateral triangle ABC with side length 2.
    A = (0, 0)
    B = (2, 0)
    C = (2 * cos(pi / 3), 2 * sin(pi / 3))

    # Find the circumcircle of triangle ABC.
    O, radius = circle_through_points(A, B, C)

    # Find the midpoint of AC.
    M = midpoint(A, C)

    # Draw the horizontal chord through M.
    X, Y = horizontal_line_circle_intersection(O, radius, M[1])

    # Compute the length of chord XY.
    chord_length = distance(X, Y)

    # Create the figure.
    fig, ax = plt.subplots(figsize=(7, 7))

    # Plot triangle ABC.
    plot_segment(ax, A, B, color="black", linewidth=2)
    plot_segment(ax, B, C, color="black", linewidth=2)
    plot_segment(ax, C, A, color="black", linewidth=2)

    # Plot chord XY.
    plot_segment(ax, X, Y, color="red", linewidth=2)

    # Plot the circumcircle.
    plot_circle(ax, O, radius, color="blue", linewidth=2)

    # Label important points.
    label_point(ax, A, "A", -0.12, -0.12)
    label_point(ax, B, "B", 0.04, -0.12)
    label_point(ax, C, "C", 0.04, 0.04)
    label_point(ax, O, "O", 0.04, 0.04)
    label_point(ax, M, "M", 0.04, 0.04)
    label_point(ax, X, "X", -0.15, 0.04)
    label_point(ax, Y, "Y", 0.04, 0.04)

    # Format the plot.
    ax.set_title(f"The distance from X to Y is {chord_length:.3f}")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.3)

    plt.show()


if __name__ == "__main__":
    main()
