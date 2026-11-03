"""
Jim McCleery
November 2, 2026
Kailua-Kona, HI

https://mathnet.mit.edu/explorer.html?p=nmo_2016_615ff2

Problem:
Let ABCD be a cyclic quadrilateral satisfying AB = AD and AB + BC = CD.
Determine angle CDA.
"""

from math import acos, atan, cos, degrees, pi, sin, sqrt
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Helper Geometry Functions
# Points are represented as 2D tuples: (x, y)
# =============================================================================

def distance(A, B):
    """
    Calculate the straight-line (Euclidean) distance between two points:
    distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    """
    x1, y1 = A
    x2, y2 = B
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def circle_through_points(A, B, C):
    """
    Find the unique circumcircle passing through three non-collinear points.

    Returns:
        (center, radius, True) on success, or ((0, 0), 0, False) on failure.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    try:
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2

        # Determinants derived from the standard circle equation
        M11 = (
            x1 * y2 + x2 * y3 + x3 * y1
            - x2 * y1 - x3 * y2 - x1 * y3
        )
        M12 = (
            s1 * y2 + s2 * y3 + s3 * y1
            - s2 * y1 - s3 * y2 - s1 * y3
        )
        M13 = (
            s1 * x2 + s2 * x3 + s3 * x1
            - s2 * x1 - s3 * x2 - s1 * x3
        )

        center_x = 0.5 * M12 / M11
        center_y = -0.5 * M13 / M11
        center = (center_x, center_y)

        radius = distance(A, center)
        return center, radius, True

    except (ValueError, ZeroDivisionError):
        return (0, 0), 0, False


def law_of_cosines(side_a, side_b, side_c):
    """
    Find the angle (in radians) opposite side_c using the Law of Cosines:
        c^2 = a^2 + b^2 - 2*a*b*cos(C)
        cos(C) = (a^2 + b^2 - c^2) / (2*a*b)

    Returns:
        (angle_in_radians, True) on success, or (0, False) on failure.
    """
    try:
        cosine_val = (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)
        
        # Clamp between -1 and 1 to guard against slight floating-point rounding errors
        cosine_val = max(-1.0, min(1.0, cosine_val))
        return acos(cosine_val), True

    except (ValueError, ZeroDivisionError):
        return 0, False


# =============================================================================
# Plotting Helpers
# =============================================================================

def plot_point_with_label(point, label, offset=(0.04, 0.04)):
    """
    Draw a single point and display its label (e.g., 'A', 'B', etc.).
    """
    x, y = point
    plt.plot(x, y, "ro")  # 'ro' plots a red dot
    plt.text(x + offset[0], y + offset[1], label, fontsize=12, fontweight="bold")


def plot_line(A, B):
    """
    Draw a straight line segment connecting point A to point B.
    """
    plt.plot([A[0], B[0]], [A[1], B[1]], "b-")  # 'b-' draws a solid blue line


def plot_circle(center, radius):
    """
    Draw a full circle given its center (x, y) and radius.
    """
    angles = np.linspace(0, 2 * pi, 500)
    x_vals = center[0] + radius * np.cos(angles)
    y_vals = center[1] + radius * np.sin(angles)
    plt.plot(x_vals, y_vals, "g--", alpha=0.6)  # 'g--' draws a dashed green circle


# =============================================================================
# Simulation / Visualization Loop
# =============================================================================

plt.figure(figsize=(7, 7))

for frame in range(100):
    plt.cla()  # Clear previous frame

    # Randomly search for a valid geometric configuration
    while True:
        AB = AD = 1.0

        # Choose angle theta for vertex D in the upper half-plane (pi/2 to pi)
        theta = uniform(pi / 2, pi)

        # Fix vertex A at the origin, B along the positive x-axis
        A = (0.0, 0.0)
        B = (AB, 0.0)
        D = (AD * cos(theta), AD * sin(theta))

        # Circumscribe the circle through triangle ABD
        circumcenter, r, ok = circle_through_points(A, B, D)
        if not ok:
            continue

        # Sample point C along the lower arc of the circumcircle
        min_angle = -atan(2 * circumcenter[1] / AB)
        gamma = uniform(min_angle, 0)
        C = (circumcenter[0] + r * cos(gamma), circumcenter[1] + r * sin(gamma))

        # Check problem condition: AB + BC = CD  =>  CD - BC = AB
        d1 = distance(C, D)  # length of CD
        d2 = distance(B, C)  # length of BC

        # Accept if CD - BC is within 0.01% tolerance of AB
        if AB * 0.9999 < (d1 - d2) < AB * 1.0001:
            break

    # Calculate angle CDA using triangle ACD side lengths
    CDA_rad, _ = law_of_cosines(AD, d1, distance(A, C))
    CDA_deg = degrees(CDA_rad)

    # Plot the circumcircle and quadrilateral edges
    plot_circle(circumcenter, r)
    plot_line(A, B)
    plot_line(B, C)
    plot_line(C, D)
    plot_line(D, A)

    # Plot points and their corresponding letter labels
    plot_point_with_label(A, "A", offset=(-0.06, -0.06))
    plot_point_with_label(B, "B", offset=(0.04, -0.06))
    plot_point_with_label(C, "C", offset=(0.04, -0.06))
    plot_point_with_label(D, "D", offset=(-0.06, 0.04))

    # Configure plot appearance
    plt.title(f"Simulation {frame + 1}/100: ∠CDA = {CDA_deg:.2f}°", fontsize=13)
    plt.axis("equal")
    plt.axis("off")
    plt.pause(0.8)

plt.show()
