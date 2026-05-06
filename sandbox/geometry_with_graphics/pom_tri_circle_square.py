"""
Jim McCleery
May 6, 2026
Kailua-Kona, HI

Diagram inspired by:
https://youtu.be/nZsokJL0SUQ?si=qAT1K5Ohtjy-nC-x
"""

import numpy as np
import matplotlib.pyplot as plt


def plot_segment(point1, point2, *, color="black", linewidth=2):
    """
    Plot a line segment between two points.

    Args:
        point1: Tuple (x, y)
        point2: Tuple (x, y)
        color: Line color
        linewidth: Line thickness
    """
    x_values = [point1[0], point2[0]]
    y_values = [point1[1], point2[1]]
    plt.plot(x_values, y_values, color=color, linewidth=linewidth)


def plot_circle(center, radius, *, color="black", linewidth=2):
    """
    Plot a circle.

    Args:
        center: Tuple (x, y)
        radius: Radius of the circle
        color: Circle color
        linewidth: Line thickness
    """
    theta = np.linspace(0, 2 * np.pi, 500)
    x_values = center[0] + radius * np.cos(theta)
    y_values = center[1] + radius * np.sin(theta)

    plt.plot(x_values, y_values, color=color, linewidth=linewidth)


def polygon_fill_coordinates(vertices):
    """
    Return x and y coordinate lists for filling a polygon.

    The polygon is closed by appending the first vertex to the end.
    """
    x_coords, y_coords = zip(*vertices)
    return list(x_coords) + [x_coords[0]], list(y_coords) + [y_coords[0]]


def label_point(label, point, *, dx=0.25, dy=0.25):
    """
    Add a label near a point.

    Args:
        label: Text label
        point: Tuple (x, y)
        dx, dy: Small offsets so the label does not cover the point
    """
    plt.text(
        point[0] + dx,
        point[1] + dy,
        label,
        fontsize=12,
        fontweight="bold",
        ha="center",
        va="center",
    )


def main():
    """
    Draw the geometric figure.

    The construction uses a 14 by 14 outer square and a tilted inner square.
    With side lengths a = 6, b = 8, and c = 10, the red square has area c^2 = 100.
    """

    # Side lengths from the 6-8-10 right triangle.
    a = 6
    b = 8
    c = 10

    # Circle radius.
    r = 2

    # The outer square has side length a + b.
    side = a + b

    # Outer square vertices.
    A = (0, 0)
    B = (side, 0)
    C = (side, side)
    D = (0, side)

    # Inner red square vertices.
    E = (a, 0)
    F = (side, a)
    G = (b, side)
    H = (0, b)

    # Circle center.
    O = (B[0] - r, B[1] + r)

    outer_square = [A, B, C, D]
    inner_square = [E, F, G, H]

    # Draw the outer square.
    for start, end in zip(outer_square, outer_square[1:] + outer_square[:1]):
        plot_segment(start, end)

    # Draw the red inner square.
    for start, end in zip(inner_square, inner_square[1:] + inner_square[:1]):
        plot_segment(start, end, color="red")

    plt.fill(
        *polygon_fill_coordinates(inner_square),
        color="red",
        alpha=0.6,
        edgecolor="red",
        linewidth=2,
    )

    # Draw the circle.
    plot_circle(O, r)

    # Label the outer square vertices.
    label_point("A", A, dx=-0.4, dy=-0.4)
    label_point("B", B, dx=0.4, dy=-0.4)
    label_point("C", C, dx=0.4, dy=0.4)
    label_point("D", D, dx=-0.4, dy=0.4)

    # Label the inner red square vertices.
    label_point("E", E, dx=0, dy=-0.5)
    label_point("F", F, dx=0.5, dy=0)
    label_point("G", G, dx=0, dy=0.5)
    label_point("H", H, dx=-0.5, dy=0)

    # Label the circle center.
    label_point("O", O, dx=0, dy=0)

    # Mark the circle center with a small dot.
    plt.scatter(*O, color="black", s=25)

    # The red square has side length c, so its area is c^2.
    red_square_area = c**2

    plt.title(f"Area of Red Square: {red_square_area}", fontsize=14)
    plt.axis("equal")
    plt.grid(True, alpha=0.25)
    plt.show()


if __name__ == "__main__":
    main()
