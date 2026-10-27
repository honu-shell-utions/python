# Jim McCleery
# October 27, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=mem_2021_d02682

"""
Geometric verification for the problem:
Let ABC be a triangle and M be the midpoint of BC.
Let X be a point on ray AB such that 2 * angle(CXA) = angle(CMA).
Let Y be a point on ray AC such that 2 * angle(AYB) = angle(AMB).
The line BC intersects the circumcircle of triangle AXY at P and Q,
such that P, B, C, Q lie in order on line BC.
Prove that PB = QC.
"""

from math import pi, sqrt, sin, cos, tan, acos
from random import uniform
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Core Geometry Helper Functions
# -----------------------------------------------------------------------------

def distance(A, B):
    """
    Calculate the Euclidean (straight-line) distance between two points.
    Each point is represented as a tuple of coordinates: (x, y).
    """
    x1, y1 = A
    x2, y2 = B
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def mid_point(A, B):
    """
    Find the midpoint of the line segment connecting points A and B.
    """
    x1, y1 = A
    x2, y2 = B
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def law_of_cosines(side_a, side_b, side_c):
    """
    Calculate the angle (in radians) opposite to side_c using the Law of Cosines:
        c^2 = a^2 + b^2 - 2ab * cos(C)
    Returns:
        (angle, True) if a valid triangle can be formed, otherwise (0, False).
    """
    try:
        cos_val = (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)
        # Clamp value to [-1, 1] to avoid math domain errors from float rounding
        cos_val = max(-1.0, min(1.0, cos_val))
        return acos(cos_val), True
    except (ValueError, ZeroDivisionError):
        return 0, False


def define_circle_from_points(A, B, C):
    """
    Determine the circumcenter and circumradius of the circle
    passing through three non-collinear points: A, B, and C.
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


def quadratic_equation(a, b, c):
    """
    Solve a standard quadratic equation: a*x^2 + b*x + c = 0.
    Returns:
        (x1, x2, True) where x1 <= x2, or (0, 0, False) if no real roots exist.
    """
    try:
        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            return 0, 0, False

        root_d = sqrt(discriminant)
        x1 = (-b - root_d) / (2 * a)
        x2 = (-b + root_d) / (2 * a)

        if x1 > x2:
            x1, x2 = x2, x1

        return x1, x2, True
    except (ValueError, ZeroDivisionError):
        return 0, 0, False


def line_circle_intersection(center, radius, line):
    """
    Find the two intersection points between a circle and a line y = m*x + b.
    line is provided as a tuple: (m, b).
    """
    cx, cy = center
    m, b = line

    # Substitute y = m*x + b into (x - cx)^2 + (y - cy)^2 = r^2:
    # (1 + m^2)*x^2 + 2*(m*(b - cy) - cx)*x + (cx^2 + (b - cy)^2 - r^2) = 0
    quad_a = 1 + m**2
    quad_b = -2 * cx + 2 * m * b - 2 * m * cy
    quad_c = cx**2 + b**2 - 2 * b * cy + cy**2 - radius**2

    x1, x2, ok = quadratic_equation(quad_a, quad_b, quad_c)
    if not ok:
        return (0, 0), (0, 0), False

    y1 = m * x1 + b
    y2 = m * x2 + b

    return (x1, y1), (x2, y2), True


# -----------------------------------------------------------------------------
# Plotting Helper Functions
# -----------------------------------------------------------------------------

def plot_line(p1, p2, color="gray", linestyle="-", linewidth=1.5):
    """Draw a line segment connecting two points."""
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color=color, linestyle=linestyle, linewidth=linewidth)


def plot_point(p, label=None, offset=(0.3, 0.3), color="black"):
    """
    Plot a single point as a dot and optionally display its label.
    offset shifts the text label so it does not overlap the dot.
    """
    plt.plot(p[0], p[1], "o", color=color, markersize=5)
    if label:
        plt.text(p[0] + offset[0], p[1] + offset[1], label, fontsize=11, fontweight="bold", color=color)


def plot_circle(center, radius, color="steelblue", linestyle="--"):
    """Draw the boundary of a circle given its center and radius."""
    cx, cy = center
    angles = np.linspace(0, 2 * pi, 500)
    x_vals = cx + radius * np.cos(angles)
    y_vals = cy + radius * np.sin(angles)
    plt.plot(x_vals, y_vals, color=color, linestyle=linestyle, linewidth=1.2)


# -----------------------------------------------------------------------------
# Main Simulation / Verification Loop
# -----------------------------------------------------------------------------

plt.figure(figsize=(9, 7))

# Run random trials to find valid geometric configurations and verify PB = QC
for _ in range(100):
    plt.cla()

    # Generate random side lengths for triangle ABC
    AB = uniform(8, 20)
    BC = uniform(8, 20)
    AC = uniform(8, 20)

    # Check triangle inequality
    if (AB + BC <= AC) or (AB + AC <= BC) or (BC + AC <= AB):
        continue

    # Interior angles of triangle ABC
    alpha, ok1 = law_of_cosines(AB, AC, BC)  # angle at vertex A
    beta, ok2 = law_of_cosines(AB, BC, AC)   # angle at vertex B
    if not (ok1 and ok2):
        continue

    # Place A at the origin (0, 0) and B along the positive x-axis
    A = (0.0, 0.0)
    B = (AB, 0.0)
    C = (AC * cos(alpha), AC * sin(alpha))
    M = mid_point(B, C)

    # Find angle CMA (theta) using triangle ACM
    d_AM = distance(A, M)
    d_CM = distance(C, M)
    d_AC = distance(A, C)
    theta, ok3 = law_of_cosines(d_AM, d_CM, d_AC)
    if not ok3 or theta <= 0:
        continue

    # Calculate positions for points Y and X using the sine rule
    # Given conditions: 2*angle(AYB) = angle(AMB) and 2*angle(CXA) = angle(CMA)
    denom_y = sin(pi / 2 - theta / 2)
    denom_x = sin(theta / 2)
    if abs(denom_y) < 1e-5 or abs(denom_x) < 1e-5:
        continue

    BY = AB * sin(alpha) / denom_y
    Y = (AB + BY * cos(pi / 2 - theta / 2 + alpha), BY * sin(pi / 2 - theta / 2 + alpha))

    AX = AC * sin(pi - theta / 2 - alpha) / denom_x
    X = (AX, 0.0)

    # Find the circumcircle passing through A, X, and Y
    try:
        circumcenter, r = define_circle_from_points(A, Y, X)
    except ZeroDivisionError:
        continue

    # Line BC equation: y = m*x + b
    m = -tan(beta)
    b = B[1] - m * B[0]
    line_bc = (m, b)

    # Intersections P and Q of the circumcircle with line BC
    pt1, pt2, intersects = line_circle_intersection(circumcenter, r, line_bc)
    if not intersects:
        continue

    # Order points P and Q along line BC so that P, B, C, Q lie sequentially
    # (ordered by their x-coordinates)
    if pt1[0] < pt2[0]:
        P, Q = pt1, pt2
    else:
        P, Q = pt2, pt1

    # Ensure P, B, C, Q order
    if not (P[0] <= B[0] <= C[0] <= Q[0] or P[0] >= B[0] >= C[0] >= Q[0]):
        # Swap if needed based on slope orientation
        if distance(P, B) > distance(P, C):
            P, Q = Q, P

    # Measure verified lengths
    d_PB = distance(P, B)
    d_QC = distance(Q, C)

    # --- Draw Geometry ---
    # Triangle and construction segments
    plot_line(A, B, color="black", linewidth=1.5)
    plot_line(B, C, color="black", linewidth=1.5)
    plot_line(A, C, color="black", linewidth=1.5)
    plot_line(A, M, color="gray", linestyle=":")
    plot_line(C, X, color="darkorange", linestyle="--")
    plot_line(B, Y, color="darkorange", linestyle="--")
    plot_line(P, Q, color="tab:blue", linestyle="-", linewidth=1.5)

    # Circumcircle of triangle AXY
    plot_circle(circumcenter, r, color="tab:blue", linestyle="--")

    # Coordinate labels for all key geometric points
    plot_point(A, label="A (0, 0)", offset=(-0.8, -0.8))
    plot_point(B, label="B", offset=(0.3, -0.6))
    plot_point(C, label="C", offset=(0.3, 0.3))
    plot_point(M, label="M", offset=(0.3, 0.3))
    plot_point(X, label="X", offset=(0.3, -0.7), color="darkgreen")
    plot_point(Y, label="Y", offset=(0.3, 0.3), color="darkgreen")
    plot_point(P, label="P", offset=(-0.8, -0.7), color="crimson")
    plot_point(Q, label="Q", offset=(0.3, 0.3), color="crimson")

    # Figure settings and dynamic title displaying numerical check
    plt.title(f"Theorem Verification: PB = {d_PB:.5f}, QC = {d_QC:.5f} (Diff = {abs(d_PB - d_QC):.2e})", fontsize=11)
    plt.axis("off")
    plt.axis("equal")
    plt.pause(1)

plt.show()
