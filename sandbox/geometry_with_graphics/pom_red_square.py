"""
Jim McCleery
April 20, 2026
Kailua-Kona, HI

https://youtu.be/iPuXrtMIR2Y?si=US10zjNEzVPjHX96
"""

from math import atan, cos, pi, sin, sqrt
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Geometry helper functions
# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """Return the Euclidean distance between two points."""
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def intersection_of_lines(m1, b1, m2, b2):
    """
    Return the intersection point of two non-parallel lines in slope-intercept form.

    Each line is given by:
        y = m*x + b
    """
    if m1 == m2:
        raise ValueError("The lines are parallel and do not intersect.")

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y


def plot_line(ax, x1, y1, x2, y2, **kwargs):
    """Plot a line segment between two points."""
    ax.plot([x1, x2], [y1, y2], **kwargs)


def polygon_fill_coordinates(vertices):
    """
    Return x- and y-coordinate lists for filling a polygon.

    The first vertex is repeated at the end so the polygon is closed.
    """
    x_coords, y_coords = zip(*vertices)
    return list(x_coords) + [x_coords[0]], list(y_coords) + [y_coords[0]]


def label_point(ax, x, y, name, dx=0.08, dy=0.08):
    """Plot and label a point."""
    ax.plot(x, y, "ko", markersize=4)
    ax.text(x + dx, y + dy, f"{name} ({x:.3f}, {y:.3f})", fontsize=9)


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------
def main():
    # Basic lengths used in the construction
    s1 = sqrt(5)
    s2 = sqrt(20)
    s3 = s1 + s2

    # Define key points
    x0, y0 = 0, 0
    x1, y1 = s2, 0
    x2, y2 = s3, 0
    x3, y3 = s3, s3
    x4, y4 = s1, s3
    x5, y5 = 0, s3
    x6, y6 = s1, s2
    x7, y7 = s2, s2
    x8, y8 = 0, s2

    fig, ax = plt.subplots()

    # Draw the original figure
    plot_line(ax, x0, y0, x2, y2, color="black")
    plot_line(ax, x3, y3, x2, y2, color="black")
    plot_line(ax, x3, y3, x5, y5, color="black")
    plot_line(ax, x0, y0, x5, y5, color="black")
    plot_line(ax, x1, y1, x7, y7, color="black")
    plot_line(ax, x8, y8, x7, y7, color="black")
    plot_line(ax, x6, y6, x4, y4, color="black")

    # -------------------------------------------------------------------------
    # Construct the red square
    #
    # First, find the line through P2 and P7.
    # Then find the perpendicular line through P3.
    # Their intersection is P9.
    # The side length of the red square is |P2P9|.
    # -------------------------------------------------------------------------
    m1 = (y7 - y2) / (x7 - x2)
    b1 = y2 - m1 * x2

    m2 = -1 / m1
    b2 = y3 - m2 * x3

    x9, y9 = intersection_of_lines(m1, b1, m2, b2)
    side_length = distance(x2, y2, x9, y9)

    # Draw one side of the red square
    plot_line(ax, x9, y9, x2, y2, color="black")

    # Use the direction perpendicular to segment P2P9 to build the other vertices
    theta = atan(-m1)

    x10 = x9 + side_length * cos(pi / 2 - theta)
    y10 = y9 + side_length * sin(pi / 2 - theta)

    x11 = x2 + side_length * cos(pi / 2 - theta)
    y11 = y2 + side_length * sin(pi / 2 - theta)

    # Draw the remaining sides of the red square
    plot_line(ax, x9, y9, x10, y10, color="black")
    plot_line(ax, x10, y10, x11, y11, color="black")
    plot_line(ax, x11, y11, x2, y2, color="black")

    # Fill the red square
    square_vertices = [(x2, y2), (x9, y9), (x10, y10), (x11, y11)]
    ax.fill(
        *polygon_fill_coordinates(square_vertices),
        color="red",
        edgecolor="red",
        linewidth=2,
        alpha=0.7
    )

    # Label all coordinates
    points = {
        "P0": (x0, y0),
        "P1": (x1, y1),
        "P2": (x2, y2),
        "P3": (x3, y3),
        "P4": (x4, y4),
        "P5": (x5, y5),
        "P6": (x6, y6),
        "P7": (x7, y7),
        "P8": (x8, y8),
        "P9": (x9, y9),
        "P10": (x10, y10),
        "P11": (x11, y11),
    }

    for name, (x, y) in points.items():
        label_point(ax, x, y, name)

    # Title and formatting
    area = side_length ** 2
    ax.set_title(f"Area of red square = {area:.3f}")
    ax.set_aspect("equal")
    ax.grid(False)

    plt.show()


if __name__ == "__main__":
    main()
