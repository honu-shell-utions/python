"""
Jim McCleery
April 30, 2026
Kailua-Kona, HI

Inspired by:
https://youtu.be/blf5tSEXM8o?si=QxOo9EU-_6nvOiO5
"""

from math import pi, sqrt

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Basic geometry helpers
# -----------------------------------------------------------------------------

def distance(point_1, point_2):
    """Return the Euclidean distance between two points."""
    x1, y1 = point_1
    x2, y2 = point_2
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def polygon_area(vertices):
    """
    Return the area of a polygon using the shoelace formula.

    The vertices must be listed in order around the polygon.
    """
    area = 0

    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]
        area += x1 * y2 - y1 * x2

    return abs(area) / 2


def polygon_fill_coordinates(vertices):
    """
    Return x- and y-coordinate lists suitable for filling a closed polygon.
    """
    x_values, y_values = zip(*vertices)
    return list(x_values) + [x_values[0]], list(y_values) + [y_values[0]]


# -----------------------------------------------------------------------------
# Plotting helpers
# -----------------------------------------------------------------------------

def plot_line(point_1, point_2, **kwargs):
    """Plot a line segment between two points."""
    x1, y1 = point_1
    x2, y2 = point_2
    plt.plot([x1, x2], [y1, y2], **kwargs)


def plot_circle_arc(center, radius, start_angle=0, stop_angle=2 * pi, **kwargs):
    """
    Plot part of a circle.

    Angles are measured in radians.
    """
    center_x, center_y = center

    angles = np.linspace(start_angle, stop_angle, 1000)
    x_values = center_x + radius * np.cos(angles)
    y_values = center_y + radius * np.sin(angles)

    plt.plot(x_values, y_values, **kwargs)


def label_point(label, point, dx=1.0, dy=1.0):
    """Add a label near a point."""
    x, y = point
    plt.text(x + dx, y + dy, label, fontsize=12, weight="bold")


# -----------------------------------------------------------------------------
# Main construction
# -----------------------------------------------------------------------------

def main():
    """
    Draw the circular sector diagram and compute the area of the red triangle.

        r - sqrt(r^2 - 30^2) = 18

    Solving exactly gives:

        r = 34
        h = 16

    """

    radius = 34
    h = 16

    # Define the key points in the diagram.
    center = (0, 0)
    top = (0, radius)
    left = (-radius, 0)
    chord_start = (0, h)
    chord_end = (-sqrt(radius**2 - h**2), h)

    # The red triangle is formed by the center, top point, and left point.
    triangle_vertices = [center, top, left]
    triangle_area = polygon_area(triangle_vertices)

    # Fill the triangle.
    plt.fill(
        *polygon_fill_coordinates(triangle_vertices),
        color="red",
        edgecolor="red",
        alpha=0.7,
        linewidth=2,
    )

    # Draw the quarter-circle arc and triangle sides.
    plot_circle_arc(center, radius, pi / 2, pi, color="black", linewidth=2)
    plot_line(left, top, color="black", linewidth=2)
    plot_line(center, top, color="black", linewidth=2)
    plot_line(left, center, color="black", linewidth=2)

    # Draw the horizontal chord.
    plot_line(chord_start, chord_end, color="black", linewidth=2)

    # Label the vertices and important points.
    label_point("A", center, dx=1.0, dy=-3.0)
    label_point("B", top, dx=1.0, dy=1.0)
    label_point("C", left, dx=-4.5, dy=1.0)
    label_point("D", chord_start, dx=1.0, dy=1.0)
    label_point("E", chord_end, dx=-4.5, dy=1.0)

    # Optional: mark the points themselves.
    points = [center, top, left, chord_start, chord_end]
    x_points, y_points = zip(*points)
    plt.scatter(x_points, y_points, color="black", zorder=3)

    plt.title(f"Area of Red Triangle: {triangle_area:.2f}")
    plt.axis("equal")
    plt.grid(True, alpha=0.3)
    plt.show()


if __name__ == "__main__":
    main()
