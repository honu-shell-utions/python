# Jim McCleery
# October 8, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=btw_2019_dec150

"""
Problem Statement from Image:
Let ABC be a triangle with AB = AC. Let M be the midpoint of BC.
Let circles with diameters AC, BM intersect at points M, P.
Let MP intersect AB at Q. Let R be a point on AP such that QR || BP.
Prove that CP bisects angle RCB.
"""

from math import pi, sqrt, cos, sin, acos, degrees
from random import uniform
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Essential Geometry Functions
# -----------------------------------------------------------------------------

def distance(point_a, point_b):
    """
    Calculate the straight-line (Euclidean) distance between two points.
    Points are represented as (x, y) tuples.
    """
    x1, y1 = point_a
    x2, y2 = point_b
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def mid_point(point_a, point_b):
    """
    Calculate the midpoint between two points.
    """
    x1, y1 = point_a
    x2, y2 = point_b
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def circle_circle_intersections(c0, r0, c1, r1):
    """
    Find the two intersection points between two circles.
    c0, c1: (x, y) centers of the circles.
    r0, r1: radii of the circles.
    """
    x0, y0 = c0
    x1, y1 = c1

    try:
        # Distance between circle centers
        d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

        # Distance from c0 to the chord baseline
        a = (r0**2 - r1**2 + d**2) / (2 * d)
        h = sqrt(r0**2 - a**2)

        # Base point on the line connecting centers
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d

        # Two intersection coordinates
        p1 = (x2 + h * (y1 - y0) / d, y2 - h * (x1 - x0) / d)
        p2 = (x2 - h * (y1 - y0) / d, y2 + h * (x1 - x0) / d)

        return p1, p2, True
    except (ValueError, ZeroDivisionError):
        return (0, 0), (0, 0), False


def line_intersection_from_points(a, b, c, d):
    """
    Find the intersection point of line AB and line CD.
    """
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c
    x4, y4 = d

    try:
        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y4 - y3) / (x4 - x3)

        # Solve for x where both line equations match
        x = (y1 - slope1 * x1 - y3 + slope2 * x3) / (slope2 - slope1)
        y = y1 + slope1 * (x - x1)
        return (x, y), True
    except ZeroDivisionError:
        return (0, 0), False


def intersection_of_lines(line1, line2):
    """
    Find the intersection of two lines given in slope-intercept form (m, b).
    """
    m1, b1 = line1
    m2, b2 = line2

    if m1 == m2:
        return (0, 0), False

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return (x, y), True


def law_of_cosines(d1, d2, opposite_side):
    """
    Find the angle (in radians) between sides d1 and d2 opposite 'opposite_side'.
    """
    try:
        cosine_val = (d1**2 + d2**2 - opposite_side**2) / (2 * d1 * d2)
        # Clamp value within [-1, 1] to prevent domain errors from floating point imprecision
        cosine_val = max(-1.0, min(1.0, cosine_val))
        return acos(cosine_val), True
    except (ValueError, ZeroDivisionError):
        return 0, False


# -----------------------------------------------------------------------------
# Plotting Helper Functions
# -----------------------------------------------------------------------------

def plot_circle(center, radius, color="gray", linestyle="--"):
    """
    Draw a circular outline on the current Matplotlib plot.
    """
    angles = np.linspace(0, 2 * pi, 500)
    x_vals = center[0] + radius * np.cos(angles)
    y_vals = center[1] + radius * np.sin(angles)
    plt.plot(x_vals, y_vals, color=color, linestyle=linestyle, linewidth=1)


def plot_line(point_a, point_b, color="black", linestyle="-", linewidth=1.5):
    """
    Draw a line segment between point_a and point_b.
    """
    plt.plot([point_a[0], point_b[0]], [point_a[1], point_b[1]],
             color=color, linestyle=linestyle, linewidth=linewidth)


def label_point(point, label_text, offset=(0.2, 0.2)):
    """
    Plot a point marker and label its letter and (x, y) coordinates.
    """
    x, y = point
    plt.plot(x, y, "ro", markersize=4)
    coord_text = f"{label_text} ({x:.2f}, {y:.2f})"
    plt.text(x + offset[0], y + offset[1], coord_text, fontsize=9, weight="bold")


# -----------------------------------------------------------------------------
# Simulation & Demonstration Loop
# -----------------------------------------------------------------------------

ab_length = ac_length = 10

for _ in range(100):
    plt.cla()

    # 1. Randomly generate an isosceles triangle ABC where AB = AC
    theta = uniform(pi / 6, pi / 2)
    A = (0, 0)
    B = (ab_length, 0)
    C = (ac_length * cos(theta), ac_length * sin(theta))

    # 2. Midpoint M of BC
    M = mid_point(B, C)

    # 3. Circle 1 has diameter AC; Circle 2 has diameter BM
    center_ac = mid_point(A, C)
    radius_ac = distance(A, center_ac)

    center_bm = mid_point(B, M)
    radius_bm = distance(B, center_bm)

    # 4. Intersections of the two circles give points M and P
    int1, int2, _ = circle_circle_intersections(center_ac, radius_ac, center_bm, radius_bm)
    # Identify which intersection is P (the one that is not M)
    P = int2 if distance(int1, M) < 1e-4 else int1

    # 5. Line MP intersects AB at Q
    Q, _ = line_intersection_from_points(M, P, A, B)

    # 6. Find R on line AP such that line QR is parallel to line BP
    # Slope of BP
    slope_bp = (P[1] - B[1]) / (P[0] - B[0])
    line_qr = (slope_bp, Q[1] - slope_bp * Q[0])

    # Line AP
    slope_ap = (P[1] - A[1]) / (P[0] - A[0])
    line_ap = (slope_ap, A[1] - slope_ap * A[0])

    # R is the intersection of line AP and line QR
    R, _ = intersection_of_lines(line_qr, line_ap)

    # 7. Calculate angles to verify that CP bisects angle RCB:
    # angle_rcp = angle RCP; angle_pcb = angle PCB
    d_rc = distance(R, C)
    d_pc = distance(P, C)
    d_rp = distance(R, P)
    angle_rcp, _ = law_of_cosines(d_rc, d_pc, d_rp)
    angle_rcp = degrees(angle_rcp)

    d_bc = distance(B, C)
    d_bp = distance(B, P)
    angle_pcb, _ = law_of_cosines(d_pc, d_bc, d_bp)
    angle_pcb = degrees(angle_pcb)

    # 8. Render geometry
    plot_circle(center_ac, radius_ac, color="lightblue")
    plot_circle(center_bm, radius_bm, color="orange")

    # Draw key segments
    plot_line(A, B, color="black")
    plot_line(B, C, color="black")
    plot_line(A, C, color="black")
    plot_line(Q, M, color="gray", linestyle=":")
    plot_line(B, P, color="blue")
    plot_line(Q, R, color="blue", linestyle="--")  # parallel to BP
    plot_line(A, R, color="gray", linestyle=":")
    plot_line(C, R, color="green")
    plot_line(C, P, color="purple", linewidth=2)   # bisector CP

    # 9. Add point labels with explicit coordinate readouts
    label_point(A, "A", offset=(-0.8, -0.6))
    label_point(B, "B", offset=(0.2, -0.6))
    label_point(C, "C", offset=(0.2, 0.3))
    label_point(M, "M", offset=(0.2, 0.2))
    label_point(P, "P", offset=(0.2, -0.5))
    label_point(Q, "Q", offset=(0.1, -0.6))
    label_point(R, "R", offset=(0.2, 0.2))

    plt.title(
        f"Angle RCP = {angle_rcp:.3f}° | Angle PCB = {angle_pcb:.3f}°\n"
        f"CP bisects ∠RCB (Difference: {abs(angle_rcp - angle_pcb):.4e}°)",
        fontsize=10
    )
    plt.axis("equal")
    plt.axis("off")
    plt.pause(1)

plt.show()
