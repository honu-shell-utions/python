# -----------------------------------------------------------------------------
# Jim McCleery
# October 12, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=mem_2024_b25895
# -----------------------------------------------------------------------------

"""
Visualization and verification for the geometry problem:
"Let ABC be a triangle with ∠BAC = 60°. Let D be a point on the line AC such that
AB = AD and A lies between C and D. Suppose that there are two points E != F on
the circumcircle of triangle DBC such that AE = AF = BC. Prove that the line EF
passes through the circumcenter of ABC."
"""

from math import pi, sqrt, cos, sin
from random import uniform
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Geometry Helper Functions
# -----------------------------------------------------------------------------

def distance(A, B):
    """
    Calculate the straight-line distance between two points A and B.
    Each point is represented as a tuple: (x, y).
    """
    x1, y1 = A
    x2, y2 = B
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def define_circle_from_points(A, B, C):
    """
    Find the unique circle (circumcircle) passing through 3 non-collinear points.
    Returns:
        (center, radius) where center is an (x, y) tuple.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    temp = x2**2 + y2**2
    bc = (x1**2 + y1**2 - temp) / 2
    cd = (temp - x3**2 - y3**2) / 2

    determinant = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    center_x = (bc * (y2 - y3) - cd * (y1 - y2)) / determinant
    center_y = ((x1 - x2) * cd - (x2 - x3) * bc) / determinant
    center = (center_x, center_y)

    radius = distance(center, A)
    return center, radius


def circle_circle_intersections(C0, r0, C1, r1):
    """
    Find the intersection points of two circles.
    Parameters:
        C0, r0: center and radius of the first circle
        C1, r1: center and radius of the second circle
    Returns:
        (P1, P2, True) if two intersections exist, otherwise ((0, 0), (0, 0), False).
    """
    x0, y0 = C0
    x1, y1 = C1

    try:
        # Distance between the two centers
        d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

        # Distance along the center-line to the chord midpoint
        a = (r0**2 - r1**2 + d**2) / (2 * d)

        # Half-length of the intersection chord
        h = sqrt(r0**2 - a**2)

        # Coordinates of the chord midpoint
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d

        # The two intersection points
        P1 = (x2 + h * (y1 - y0) / d, y2 - h * (x1 - x0) / d)
        P2 = (x2 - h * (y1 - y0) / d, y2 + h * (x1 - x0) / d)
        return P1, P2, True

    except (ValueError, ZeroDivisionError):
        return (0, 0), (0, 0), False


def line_intersection_from_points(A, B, C, D):
    """
    Find the intersection point of two lines:
    Line 1 passing through points A and B.
    Line 2 passing through points C and D.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D

    try:
        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y4 - y3) / (x4 - x3)

        x = (y1 - slope1 * x1 - y3 + slope2 * x3) / (slope2 - slope1)
        y = y1 + slope1 * (x - x1)
        return (x, y), True
    except ZeroDivisionError:
        return (0, 0), False


def point_line_distance(P, line):
    """
    Calculate the perpendicular distance from point P to a line.
    The line is defined by coefficients: (a, b, c) for a*x + b*y + c = 0.
    """
    x, y = P
    a, b, c = line
    return abs(a * x + b * y + c) / sqrt(a**2 + b**2)


# -----------------------------------------------------------------------------
# Plotting Helper Functions
# -----------------------------------------------------------------------------

def plot_circle(C, radius, color="gray", linestyle="--"):
    """Plot a full circle given its center and radius."""
    center_x, center_y = C
    angles = np.linspace(0, 2 * pi, 500)
    x_vals = radius * np.cos(angles) + center_x
    y_vals = radius * np.sin(angles) + center_y
    plt.plot(x_vals, y_vals, color=color, linestyle=linestyle, linewidth=1)


def plot_line(A, B, color="black", linestyle="-", linewidth=1.5):
    """Plot a straight line segment between two points A and B."""
    plt.plot([A[0], B[0]], [A[1], B[1]], color=color, linestyle=linestyle, linewidth=linewidth)


def plot_labeled_point(point, label, offset=(0.3, 0.3), color="black"):
    """
    Plot a single point as a dot and add a text label with its coordinates.
    Offset shifts the label text slightly so it does not overlap the dot.
    """
    x, y = point
    plt.plot(x, y, "o", color=color, markersize=5)
    text = f"{label} ({x:.2f}, {y:.2f})"
    plt.text(x + offset[0], y + offset[1], text, fontsize=8, color=color, weight="bold")


# -----------------------------------------------------------------------------
# Main Simulation and Plotting Routine
# -----------------------------------------------------------------------------

# Fixed geometry parameters
alpha = pi / 3      # Angle BAC = 60 degrees
AB = 10.0           # Length of segment AB

# Fixed coordinates:
# A is placed at the origin (0, 0)
# B is placed along the x-axis at (10, 0)
A = (0.0, 0.0)
B = (AB, 0.0)

# D lies on line AC such that AB = AD and A is between C and D.
# Angle of line AC is +alpha (60 degrees), so ray AD points backwards at (alpha - pi).
D = (AB * cos(alpha - pi), AB * sin(alpha - pi))

# Generate configurations with valid random angles
num_trials = 3

for trial in range(num_trials):
    # Randomly pick angle B (beta) such that the triangle can close
    beta = uniform(0.1, 2 * pi / 3 - 0.1)

    # Ray AC direction from A
    T1 = (cos(alpha), sin(alpha))
    # Ray BC direction from B
    T2 = (AB + cos(pi - beta), sin(pi - beta))

    # Vertex C is where ray AC and ray BC intersect
    C, ok = line_intersection_from_points(A, T1, B, T2)
    if not ok:
        continue

    # Circumcircle of triangle DBC (center I, radius r)
    I, r = define_circle_from_points(D, B, C)

    # E and F lie on the circumcircle of DBC, at distance BC from A.
    # Therefore, they are the intersections of circle(D, B, C) and circle(center=A, radius=BC).
    BC = distance(B, C)
    E, F, ok_inter = circle_circle_intersections(A, BC, I, r)
    if not ok_inter:
        continue

    # Circumcircle of triangle ABC (center I0, radius r0)
    I0, r0 = define_circle_from_points(A, B, C)

    # Line EF equation: a*x + b*y + c = 0
    if abs(E[0] - F[0]) < 1e-9:
        # Vertical line EF: x - E[0] = 0
        a, b, c = 1.0, 0.0, -E[0]
    else:
        m = (E[1] - F[1]) / (E[0] - F[0])
        a = m
        b = -1.0
        c = E[1] - m * E[0]

    # Verify that the line EF passes through circumcenter I0 (distance should be ~0)
    dist_I0_to_EF = point_line_distance(I0, (a, b, c))

    # --- Plotting ---
    plt.figure(figsize=(10, 10))

    # Draw circles
    plot_circle(I, r, color="tab:blue", linestyle="--")      # Circumcircle of DBC
    plot_circle(I0, r0, color="tab:green", linestyle=":")   # Circumcircle of ABC

    # Draw triangle and construction segments
    plot_line(A, B, color="black", linewidth=1.5)
    plot_line(B, C, color="black", linewidth=1.5)
    plot_line(C, D, color="black", linewidth=1.5)
    plot_line(D, B, color="tab:gray", linestyle="--", linewidth=1)
    plot_line(E, F, color="tab:red", linewidth=1.8)          # Secant line EF

    # Plot points with coordinate labels
    plot_labeled_point(A, "A", offset=(-1.0, 0.4), color="black")
    plot_labeled_point(B, "B", offset=(0.4, -0.4), color="black")
    plot_labeled_point(C, "C", offset=(-1.0, 0.5), color="black")
    plot_labeled_point(D, "D", offset=(-2.5, -0.8), color="black")
    plot_labeled_point(E, "E", offset=(0.4, 0.4), color="tab:purple")
    plot_labeled_point(F, "F", offset=(0.4, -0.6), color="tab:purple")
    plot_labeled_point(I0, "I0 (Circumcenter)", offset=(0.4, 0.4), color="tab:green")

    # Add descriptive title displaying verification
    plt.title(
        f"Circumcenter Verification for Triangle ABC\n"
        f"Distance from Circumcenter I0 to Line EF = {dist_I0_to_EF:.4e}",
        fontsize=11,
        weight="bold",
        pad=15
    )

    plt.axis("equal")
    plt.grid(True, linestyle=":", alpha=0.5)
    plt.tight_layout()
    plt.show()
