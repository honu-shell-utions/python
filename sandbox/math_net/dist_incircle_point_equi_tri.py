# =============================================================================
# Jim McCleery
# October 17, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=ibe_1992_431c9c
# =============================================================================
"""
Problem:
ABC is an equilateral triangle with side 2. Show that any point P on the
incircle satisfies PA^2 + PB^2 + PC^2 = 5, and that the triangle formed
with side lengths PA, PB, and PC has an area of sqrt(3)/4.

This script tests the property by picking random points P on the incircle,
calculating the distances, and plotting the geometry with labeled coordinates.
"""

from math import cos, pi, sin, sqrt
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Geometry Helper Functions
# -----------------------------------------------------------------------------
def distance(point_a, point_b):
    """
    Calculate the straight-line (Euclidean) distance between two points.

    Each point is represented as a tuple: (x, y).
    Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    """
    x1, y1 = point_a
    x2, y2 = point_b
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def incircle_of_triangle(A, B, C):
    """
    Find the inscribed circle (incircle) of a triangle.

    The incircle is the circle tangent to all three sides inside the triangle.
    Returns:
        center: (x, y) coordinates of the incenter
        radius: length of the inradius
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    # Compute the length of each side opposite to vertices A, B, and C
    a = distance(B, C)
    b = distance(A, C)
    c = distance(A, B)

    # Semiperimeter (half the perimeter of the triangle)
    s = (a + b + c) / 2

    # Heron's formula gives the area of the triangle
    area = sqrt(s * (s - a) * (s - b) * (s - c))

    # For any triangle: Area = inradius * semiperimeter
    radius = area / s

    # The incenter coordinates are the weighted average of the vertices
    center_x = (a * x1 + b * x2 + c * x3) / (a + b + c)
    center_y = (a * y1 + b * y2 + c * y3) / (a + b + c)

    return (center_x, center_y), radius


def triangle_area_from_heron(a, b, c):
    """
    Calculate the area of a triangle given its three side lengths using Heron's formula.

    Returns:
        (area, True) if the side lengths form a valid triangle
        (0, False) if the triangle is degenerate or invalid
    """
    try:
        s = (a + b + c) / 2
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        return area, True
    except ValueError:
        return 0, False


# -----------------------------------------------------------------------------
# Plotting Helper Functions
# -----------------------------------------------------------------------------
def plot_circle(center, radius):
    """Plot the outline of a full circle given its center and radius."""
    cx, cy = center
    angles = np.linspace(0, 2 * pi, 500)
    x_values = cx + radius * np.cos(angles)
    y_values = cy + radius * np.sin(angles)
    plt.plot(x_values, y_values, "g--", label="Incircle")


def plot_line(point_a, point_b):
    """Plot a straight line segment connecting two points."""
    plt.plot([point_a[0], point_b[0]], [point_a[1], point_b[1]], "b-")


def plot_labeled_point(point, label, offset=(0.04, 0.04), color="black"):
    """
    Plot a single point as a marker and display its name and coordinates.

    Parameters:
        point: tuple (x, y)
        label: name of the point (e.g., 'A', 'B', 'C', 'P', 'I')
        offset: small distance shift (dx, dy) so the text does not cover the point
        color: color of the marker
    """
    x, y = point
    plt.plot(x, y, "o", color=color)

    # Format the coordinate text to 2 decimal places for neatness
    coord_text = f"{label} ({x:.2f}, {y:.2f})"
    plt.text(x + offset[0], y + offset[1], coord_text, fontsize=9, weight="bold")


# -----------------------------------------------------------------------------
# Main Simulation
# -----------------------------------------------------------------------------
# Side length of the equilateral triangle
side_length = 2.0

# Define vertices of equilateral triangle ABC:
# Point A is placed at the origin (0, 0)
# Point B is placed along the x-axis at (2, 0)
# Point C forms the top vertex at (1, sqrt(3))
A = (0.0, 0.0)
B = (side_length, 0.0)
C = (side_length / 2.0, side_length * sqrt(3) / 2.0)

# Calculate the incenter (I) and inradius (r)
I, r = incircle_of_triangle(A, B, C)

# Run 10 random trials testing points on the incircle
for trial in range(10):
    plt.cla()
    plt.figure(figsize=(7, 6))

    # Pick a random angle around the incircle to place point P
    theta = uniform(0, 2 * pi)
    P = (I[0] + r * cos(theta), I[1] + r * sin(theta))

    # 1. Draw the equilateral triangle sides
    plot_line(A, B)
    plot_line(B, C)
    plot_line(C, A)

    # 2. Draw the incircle
    plot_circle(I, r)

    # 3. Plot and label all key points with their coordinates
    plot_labeled_point(A, "A", offset=(-0.25, -0.08), color="blue")
    plot_labeled_point(B, "B", offset=(0.05, -0.08), color="blue")
    plot_labeled_point(C, "C", offset=(-0.10, 0.06), color="blue")
    plot_labeled_point(I, "I", offset=(0.04, 0.04), color="green")
    plot_labeled_point(P, "P", offset=(0.05, 0.05), color="red")

    # 4. Draw dashed helper lines from P to each vertex
    plt.plot([P[0], A[0]], [P[1], A[1]], "r:", alpha=0.6)
    plt.plot([P[0], B[0]], [P[1], B[1]], "r:", alpha=0.6)
    plt.plot([P[0], C[0]], [P[1], C[1]], "r:", alpha=0.6)

    # Compute distances from P to A, B, and C
    d1 = distance(P, A)
    d2 = distance(P, B)
    d3 = distance(P, C)

    # Verify theoretical relationships
    sum_of_squares = d1**2 + d2**2 + d3**2
    area_pa_pb_pc, _ = triangle_area_from_heron(d1, d2, d3)

    # Display results in the figure title
    plt.title(
        f"Trial {trial + 1}\n"
        f"$PA^2 + PB^2 + PC^2$ = {sum_of_squares:.5f} (Target: 5.00000)\n"
        f"Area(PA, PB, PC) = {area_pa_pb_pc:.5f} (Target: $\\sqrt{{3}}/4 \\approx$ {sqrt(3)/4:.5f})\n\n",
        fontsize=10,
    )

    # Ensure equal aspect ratio so circles and equilateral triangles appear undistorted
    plt.axis("equal")
    plt.grid(True, linestyle=":", alpha=0.5)
    plt.pause(1)
plt.show()
