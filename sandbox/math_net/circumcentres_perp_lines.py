# =============================================================================
# Jim McCleery
# October 1, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=btw_1997_e44459
#
# Problem:
# Five distinct points A, B, C, D, and E lie on a line with:
#     |AB| = |BC| = |CD| = |DE|
# The point F lies outside the line. Let G be the circumcentre of triangle ADF
# and H be the circumcentre of triangle BEF. Show that lines GH and FC are
# perpendicular (their slopes multiply to -1).
# =============================================================================

from math import pi, sqrt
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Geometry Helper Functions
# -----------------------------------------------------------------------------

def distance(point_a, point_b):
    """
    Calculate the straight-line distance between two points using the
    Pythagorean theorem: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2).
    """
    x1, y1 = point_a
    x2, y2 = point_b
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def circle_through_points(point_a, point_b, point_c):
    """
    Find the unique circle (circumcircle) passing through three points.

    Returns:
        (center, radius, True) if the points form a triangle.
        ((0, 0), 0, False) if the three points lie on the same straight line.
    """
    x1, y1 = point_a
    x2, y2 = point_b
    x3, y3 = point_c

    try:
        # Sum of squares of the coordinates for each point
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2

        # Determinants used to solve for the circumcenter coordinates
        m11 = (
            x1 * y2 + x2 * y3 + x3 * y1
            - x2 * y1 - x3 * y2 - x1 * y3
        )
        m12 = (
            s1 * y2 + s2 * y3 + s3 * y1
            - s2 * y1 - s3 * y2 - s1 * y3
        )
        m13 = (
            s1 * x2 + s2 * x3 + s3 * x1
            - s2 * x1 - s3 * x2 - s1 * x3
        )

        center_x = 0.5 * m12 / m11
        center_y = -0.5 * m13 / m11
        center = (center_x, center_y)

        # The radius is the distance from the center to any of the three vertices
        radius = distance(point_a, center)

        return center, radius, True

    except (ValueError, ZeroDivisionError):
        # Triggered if m11 is zero (i.e., all three points are collinear)
        return (0, 0), 0, False


# -----------------------------------------------------------------------------
# Plotting Helper Functions
# -----------------------------------------------------------------------------

def plot_circle(center, radius, color="gray", linestyle="--"):
    """
    Draw the outline of a full circle using center (x, y) and radius.
    """
    center_x, center_y = center
    angles = np.linspace(0, 2 * pi, 500)
    x_values = center_x + radius * np.cos(angles)
    y_values = center_y + radius * np.sin(angles)
    plt.plot(x_values, y_values, color=color, linestyle=linestyle, linewidth=1)


def plot_line(point_a, point_b, color="black", linestyle="-", linewidth=1.5):
    """
    Draw a straight line segment between two (x, y) coordinate points.
    """
    x1, y1 = point_a
    x2, y2 = point_b
    plt.plot([x1, x2], [y1, y2], color=color, linestyle=linestyle, linewidth=linewidth)


def label_point(point, label_text, offset=(0, -1.2)):
    """
    Draw a small marker dot at the point and place its text label nearby.
    """
    x, y = point
    plt.plot(x, y, "ko", markersize=4)  # Black dot
    plt.text(
        x + offset[0],
        y + offset[1],
        label_text,
        fontsize=12,
        fontweight="bold",
        ha="center",
        va="center",
    )


# -----------------------------------------------------------------------------
# Main Simulation & Demonstration
# -----------------------------------------------------------------------------

# Spacing unit between points along the baseline
s = 10

# Five collinear, equally spaced points along y = 0
A = (s, 0)
B = (2 * s, 0)
C = (3 * s, 0)
D = (4 * s, 0)
E = (5 * s, 0)

# Run simulations with random positions for F above the baseline
for iteration in range(10):
    # Pick point F outside the line (x between 0 and 50, fixed height y = 10)
    F = (uniform(0, 5 * s), s)

    # G is the circumcenter of triangle ADF; H is the circumcenter of triangle BEF
    G, Gr, ok_g = circle_through_points(A, D, F)
    H, Hr, ok_h = circle_through_points(B, E, F)

    if not ok_g or not ok_h:
        continue

    # Slope formula: (y2 - y1) / (x2 - x1)
    slope_gh = (H[1] - G[1]) / (H[0] - G[0])
    slope_fc = (C[1] - F[1]) / (C[0] - F[0])

    # Perpendicular lines have slopes whose product is -1 (m1 * m2 = -1)
    slope_product = slope_gh * slope_fc

    plt.figure(figsize=(9, 7))

    # Plot circumcircles for ADF (center G) and BEF (center H)
    plot_circle(G, Gr, color="blue", linestyle=":")
    plot_circle(H, Hr, color="red", linestyle=":")

    # Baseline segments across A through E
    plot_line(A, E, color="black", linewidth=2)

    # Rays connecting F to each baseline point
    plot_line(A, F, color="gray", linewidth=1.2)
    plot_line(B, F, color="gray", linewidth=1.2)
    plot_line(C, F, color="purple", linewidth=2)  # Highlighted line FC
    plot_line(D, F, color="gray", linewidth=1.2)
    plot_line(E, F, color="gray", linewidth=1.2)

    # Line connecting circumcenters G and H
    plot_line(G, H, color="darkgreen", linewidth=2)

    # Add labels for the points from the problem figure and construction
    label_point(A, "A", offset=(0, -1.2))
    label_point(B, "B", offset=(0, -1.2))
    label_point(C, "C", offset=(0, -1.2))
    label_point(D, "D", offset=(0, -1.2))
    label_point(E, "E", offset=(0, -1.2))
    label_point(F, "F", offset=(0, 1.2))
    label_point(G, "G", offset=(0, -1.2))
    label_point(H, "H", offset=(0, -1.2))

    plt.title(
        f"Trial {iteration + 1}: slope(GH) * slope(FC) = {slope_product:.5f}\n"
        "(A product of -1.00000 confirms lines GH and FC are perpendicular)",
        fontsize=11,
    )
    plt.axis("equal")
    plt.axis("off")
    plt.show()
