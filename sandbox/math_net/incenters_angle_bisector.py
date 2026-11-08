# -----------------------------------------------------------------------------
# Jim McCleery
# November 8, 2026
# Kailua-Kona, HI
#
# MIT Math_Net Geometry Explorer:
# https://mathnet.mit.edu/explorer.html?p=zhk_2018_3be4cf
#
# Problem:
# Points N, K, L lie on the sides AB, BC, CA of a triangle ABC respectively
# so that AL = BK and CN is the bisector of the angle C. The segments AK and
# BL meet at the point P. Let I and J be the incentres of the triangles APL
# and BPK respectively. The lines CN and IJ meet at point Q. Prove IP = JQ.
# -----------------------------------------------------------------------------

from math import pi, sqrt, sin, cos, acos
from random import uniform
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# Helper Geometry Functions
# Points are stored as 2D tuples: (x, y)
# =============================================================================

def distance(A, B):
    """
    Calculate the straight-line (Euclidean) distance between two points A and B.
    Formula: sqrt((x1 - x2)^2 + (y1 - y2)^2)
    """
    x1, y1 = A
    x2, y2 = B
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def law_of_cosines(side_a, side_b, side_c):
    """
    Find the interior angle opposite to 'side_c' using the Law of Cosines:
        cos(C) = (a^2 + b^2 - c^2) / (2 * a * b)
    Returns the angle in radians and a boolean status flag.
    """
    try:
        cos_val = (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)
        # Clamp to [-1, 1] to avoid minor floating-point precision domain errors
        cos_val = max(-1.0, min(1.0, cos_val))
        return acos(cos_val), True
    except (ValueError, ZeroDivisionError):
        return 0.0, False


def line_intersection_from_points(A, B, C, D):
    """
    Find the intersection point of two infinite lines:
    Line 1 passing through points A and B, and Line 2 passing through C and D.
    Returns ((x, y), True) if they intersect, or ((0, 0), False) if parallel.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D

    try:
        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y4 - y3) / (x4 - x3)

        if slope1 == slope2:
            return (0.0, 0.0), False

        x = (y1 - slope1 * x1 - y3 + slope2 * x3) / (slope2 - slope1)
        y = y1 + slope1 * (x - x1)
        return (x, y), True
    except ZeroDivisionError:
        # Handles lines that are strictly vertical
        return (0.0, 0.0), False


def incircle_of_triangle(A, B, C):
    """
    Find the incenter (center) and inradius (radius) of the circle inscribed
    inside triangle ABC.
    - The incenter is a weighted average of vertices based on opposite side lengths.
    - Inradius r = Area / semiperimeter.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    a = distance(B, C)
    b = distance(A, C)
    c = distance(A, B)

    # Semiperimeter
    s = (a + b + c) / 2.0

    # Area via Heron's formula
    area = sqrt(max(0.0, s * (s - a) * (s - b) * (s - c)))
    radius = area / s

    # Weighted coordinates of the incenter
    center_x = (a * x1 + b * x2 + c * x3) / (a + b + c)
    center_y = (a * y1 + b * y2 + c * y3) / (a + b + c)

    return (center_x, center_y), radius


def plot_circle(C, radius, color="black", linestyle="-"):
    """Draw a circle around center C with a given radius."""
    center_x, center_y = C
    angles = np.linspace(0, 2 * pi, 300)
    x_vals = radius * np.cos(angles) + center_x
    y_vals = radius * np.sin(angles) + center_y
    plt.plot(x_vals, y_vals, color=color, linestyle=linestyle, linewidth=1)


def plot_line(A, B, color="black", linestyle="-", linewidth=1.2):
    """Draw a straight segment between points A and B."""
    plt.plot([A[0], B[0]], [A[1], B[1]], color=color, linestyle=linestyle, linewidth=linewidth)


def label_point(P, name, offset=(0.2, 0.2)):
    """Draw a marker and text label for a geometric point."""
    plt.plot(P[0], P[1], "o", color="navy", markersize=4)
    plt.text(P[0] + offset[0], P[1] + offset[1], name, fontsize=10, fontweight="bold")


# =============================================================================
# Main Simulation Loop
# =============================================================================

A = (0.0, 0.0)

for _ in range(100):
    plt.cla()

    # 1. Randomly pick triangle side lengths
    AB_len = uniform(5, 20)
    BC_len = uniform(5, 20)
    AC_len = uniform(5, 20)

    # Ensure the Triangle Inequality holds
    if (AB_len + BC_len <= AC_len) or (AB_len + AC_len <= BC_len) or (BC_len + AC_len <= AB_len):
        continue

    # Fix A at the origin and B along the positive x-axis
    B = (AB_len, 0.0)

    # 2. Compute interior angles: alpha (at A), beta (at B), and gamma (at C)
    alpha, ok_a = law_of_cosines(AB_len, AC_len, BC_len)
    beta, ok_b = law_of_cosines(AB_len, BC_len, AC_len)
    if not (ok_a and ok_b):
        continue

    gamma = pi - alpha - beta
    # Skip degenerate/extremely sharp sliver triangles
    if alpha < pi / 12 or beta < pi / 12 or gamma < pi / 12:
        continue

    # 3. Compute coordinates of Vertex C
    C = (AC_len * cos(alpha), AC_len * sin(alpha))

    # 4. Angle bisector of C intersects side AB at point N
    # Using the Law of Sines in triangle CAN:
    half_gamma = gamma / 2.0
    angle_anc = pi - alpha - half_gamma
    AN_len = AC_len * sin(half_gamma) / sin(angle_anc)
    N = (AN_len, 0.0)

    # 5. Points L on CA and K on BC such that AL = BK
    segment_len = uniform(1, min(AC_len, BC_len) * 0.9)
    L = (segment_len * cos(alpha), segment_len * sin(alpha))
    K = (AB_len + segment_len * cos(pi - beta), segment_len * sin(pi - beta))

    # 6. Intersect segments AK and BL at point P
    P, ok_p = line_intersection_from_points(A, K, B, L)
    if not ok_p:
        continue

    # 7. Incenters I (for triangle APL) and J (for triangle BPK)
    I, r1 = incircle_of_triangle(A, P, L)
    J, r2 = incircle_of_triangle(B, P, K)

    # 8. Point Q is the intersection of the angle bisector CN and line IJ
    Q, ok_q = line_intersection_from_points(C, N, I, J)
    if not ok_q:
        continue

    # 9. Verify the theorem: IP == JQ
    IP = distance(I, P)
    JQ = distance(J, Q)

    # -------------------------------------------------------------------------
    # Plotting & Geometric Labels
    # -------------------------------------------------------------------------
    # Draw primary triangle ABC
    plot_line(A, B, color="black", linewidth=1.5)
    plot_line(B, C, color="black", linewidth=1.5)
    plot_line(C, A, color="black", linewidth=1.5)

    # Draw cevians and intersecting lines
    plot_line(A, K, color="forestgreen", linestyle="--")
    plot_line(B, L, color="forestgreen", linestyle="--")
    plot_line(C, N, color="purple", linestyle="-.")
    plot_line(I, J, color="crimson", linestyle="-.")

    # Inscribed circles
    plot_circle(I, r1, color="steelblue")
    plot_circle(J, r2, color="steelblue")

    # Add text labels to all problem vertices and intersections
    label_point(A, "A", offset=(-0.6, -0.6))
    label_point(B, "B", offset=(0.3, -0.6))
    label_point(C, "C", offset=(0.0, 0.5))
    label_point(N, "N", offset=(0.1, -0.7))
    label_point(L, "L", offset=(-0.8, 0.2))
    label_point(K, "K", offset=(0.4, 0.2))
    label_point(P, "P", offset=(0.2, 0.3))
    label_point(I, "I", offset=(0.2, 0.2))
    label_point(J, "J", offset=(0.2, 0.2))
    label_point(Q, "Q", offset=(0.2, 0.2))

    plt.title(f"Theorem Verification: IP = {IP:.4f}, JQ = {JQ:.4f}", fontsize=11)
    plt.axis("off")
    plt.axis("equal")
    plt.pause(1)

plt.show()
