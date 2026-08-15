# -----------------------------------------------------------------------------
# Jim McCleery
# August 15, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_074dad
# -----------------------------------------------------------------------------
"""
Visualization of USA TSTST 2017 Problem 2:
Let ABC be an acute triangle, and P a point on the interior of side BC.
Let I be the incenter of triangle ABC, and denote by D the foot of the 
altitude from I to BC (the point of tangency of the incircle on BC).
Line BI meets the internal angle bisector of angle APC at X, while line CI 
meets the internal angle bisector of angle APB at Y.
Show that the points D, P, X, Y lie on a circle.
"""

from math import pi, sqrt, sin, cos, tan, acos
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Helper Geometric Functions
# -----------------------------------------------------------------------------
def law_of_cosines(side_a, side_b, side_c):
    """
    Find the angle opposite to side_c using the Law of Cosines:
        c^2 = a^2 + b^2 - 2*a*b*cos(C)  =>  cos(C) = (a^2 + b^2 - c^2) / (2*a*b)

    Returns:
        (angle_in_radians, True) if a valid triangle exists, otherwise (0, False).
    """
    try:
        cos_val = (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)
        return acos(cos_val), True
    except (ValueError, ZeroDivisionError):
        return 0.0, False


def distance(x1, y1, x2, y2):
    """Calculate the straight-line (Euclidean) distance between two points."""
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def incircle_of_triangle(x_a, y_a, x_b, y_b, x_c, y_c):
    """
    Compute the incenter coordinates (ix, iy) and inradius (r) of a triangle.
    Uses barycentric coordinates weighted by opposite side lengths.
    """
    a = distance(x_b, y_b, x_c, y_c)  # Length of side BC
    b = distance(x_a, y_a, x_c, y_c)  # Length of side AC
    c = distance(x_a, y_a, x_b, y_b)  # Length of side AB

    perimeter = a + b + c
    s = perimeter / 2.0  # Semi-perimeter

    # Heron's formula for area
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    inradius = area / s

    # Weighted average of vertex coordinates
    incenter_x = (a * x_a + b * x_b + c * x_c) / perimeter
    incenter_y = (a * y_a + b * y_b + c * y_c) / perimeter

    return incenter_x, incenter_y, inradius


def line_intersection_from_points(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Find the intersection point (x, y) of Line 1 (through points 1 & 2)
    and Line 2 (through points 3 & 4).
    """
    try:
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)
        ix = (y1 - m1 * x1 - y3 + m2 * x3) / (m2 - m1)
        iy = y1 + m1 * (ix - x1)
        return ix, iy, True
    except ZeroDivisionError:
        return 0.0, 0.0, False


def circle_through_points(x1, y1, x2, y2, x3, y3):
    """
    Calculate the center (cx, cy) and radius (r) of the unique circle
    passing through 3 non-collinear points.
    """
    try:
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2

        # Determinants to find standard equation of circumcircle
        m11 = x1 * y2 + x2 * y3 + x3 * y1 - (x2 * y1 + x3 * y2 + x1 * y3)
        m12 = s1 * y2 + s2 * y3 + s3 * y1 - (s2 * y1 + s3 * y2 + s1 * y3)
        m13 = s1 * x2 + s2 * x3 + s3 * x1 - (s2 * x1 + s3 * x2 + s1 * x3)

        cx = 0.5 * m12 / m11
        cy = -0.5 * m13 / m11
        r = sqrt((x1 - cx) ** 2 + (y1 - cy) ** 2)
        return cx, cy, r, True
    except ZeroDivisionError:
        return 0.0, 0.0, 0.0, False


def plot_line(x1, y1, x2, y2, **kwargs):
    """Draw a line segment between (x1, y1) and (x2, y2)."""
    plt.plot([x1, x2], [y1, y2], **kwargs)


def plot_circle(cx, cy, radius, **kwargs):
    """Draw a circle centered at (cx, cy) with the given radius."""
    angles = np.linspace(0, 2 * pi, 500)
    x_coords = cx + radius * np.cos(angles)
    y_coords = cy + radius * np.sin(angles)
    plt.plot(x_coords, y_coords, **kwargs)


# -----------------------------------------------------------------------------
# Main Simulation Loop
# -----------------------------------------------------------------------------
plt.figure(figsize=(9, 8))

for _ in range(10**3):
    plt.clf()  # Clear current figure for new frame

    # 1. Generate random side lengths
    AB = uniform(5, 20)
    BC = uniform(5, 20)
    AC = uniform(5, 20)

    # 2. Compute internal angles (alpha at A, beta at B, gamma at C)
    alpha, ok1 = law_of_cosines(AB, AC, BC)
    beta, ok2 = law_of_cosines(AB, BC, AC)
    if not (ok1 and ok2):
        continue

    gamma = pi - alpha - beta

    # Ensure the triangle is acute (all angles < 90 degrees / pi/2 radians)
    if alpha >= pi / 2 or beta >= pi / 2 or gamma >= pi / 2:
        continue

    # 3. Position triangle vertices
    # Place vertex A at origin, B along positive x-axis, and C in upper half-plane
    xA, yA = 0.0, 0.0
    xB, yB = AB, 0.0
    xC, yC = AB + BC * cos(pi - beta), BC * sin(pi - beta)

    # 4. Incenter (I) and Inradius (r1)
    xI, yI, r_incircle = incircle_of_triangle(xB, yB, xC, yC, xA, yA)

    # 5. Point D: Tangency point (altitude foot from I) on side BC
    dist_C_to_D = r_incircle / tan(gamma / 2)
    dist_B_to_D = BC - dist_C_to_D
    xD = xB + dist_B_to_D * cos(pi - beta)
    yD = yB + dist_B_to_D * sin(pi - beta)

    # 6. Point P: Random point chosen on the interior of segment BC
    dist_B_to_P = uniform(0.1 * BC, 0.9 * BC)
    xP = xB + dist_B_to_P * cos(pi - beta)
    yP = yB + dist_B_to_P * sin(pi - beta)

    # 7. Angle Bisector of angle APC and Intersection X with line BI
    d_PA = distance(xA, yA, xP, yP)
    d_PC = distance(xC, yC, xP, yP)
    angle_APC, _ = law_of_cosines(d_PA, d_PC, AC)

    # Point along the bisector ray of angle APC
    x_ray_X = xP + cos(pi - beta + angle_APC / 2)
    y_ray_X = yP + sin(pi - beta + angle_APC / 2)

    # X = intersection of angle bisector ray of angle APC with line BI
    xX, yX, ok_x = line_intersection_from_points(x_ray_X, y_ray_X, xP, yP, xI, yI, xB, yB)
    if not ok_x:
        continue

    # 8. Angle Bisector of angle APB and Intersection Y with line CI
    d_PB = distance(xB, yB, xP, yP)
    angle_APB, _ = law_of_cosines(d_PA, d_PB, AB)

    # Point along the bisector ray of angle APB
    x_ray_Y = xP + cos(pi - beta + angle_APC + angle_APB / 2)
    y_ray_Y = yP + sin(pi - beta + angle_APC + angle_APB / 2)

    # Y = intersection of angle bisector ray of angle APB with line CI
    xY, yY, ok_y = line_intersection_from_points(x_ray_Y, y_ray_Y, xP, yP, xI, yI, xC, yC)
    if not ok_y:
        continue

    # 9. Concyclic Circle passing through D, P, X (and theoretically Y)
    cx_DPX, cy_DPX, r_concyclic, ok_circle = circle_through_points(xD, yD, xP, yP, xX, yX)
    if not ok_circle:
        continue

    # -------------------------------------------------------------------------
    # Plotting & Labeling
    # -------------------------------------------------------------------------
    # Draw Triangle ABC
    plot_line(xA, yA, xB, yB, color='black', lw=1.5)
    plot_line(xB, yB, xC, yC, color='black', lw=1.5)
    plot_line(xC, yC, xA, yA, color='black', lw=1.5)

    # Draw cevian AP and angle bisector lines
    plot_line(xA, yA, xP, yP, color='gray', linestyle=':', lw=1.0)
    plot_line(xB, yB, xX, yX, color='teal', linestyle='--', lw=1.0)
    plot_line(xC, yC, xY, yY, color='teal', linestyle='--', lw=1.0)
    plot_line(xP, yP, xX, yX, color='orange', linestyle='--', lw=1.0)
    plot_line(xP, yP, xY, yY, color='orange', linestyle='--', lw=1.0)

    # Draw Incircle and the Concyclic Circle (D, P, X, Y)
    plot_circle(xI, yI, r_incircle, color='gray', linestyle='--', label='Incircle')
    plot_circle(cx_DPX, cy_DPX, r_concyclic, color='red', lw=1.5, label='Circle (D, P, X, Y)')

    # Plot labeled points
    points = {
        'A': (xA, yA),
        'B': (xB, yB),
        'C': (xC, yC),
        'I': (xI, yI),
        'D': (xD, yD),
        'P': (xP, yP),
        'X': (xX, yX),
        'Y': (xY, yY),
    }

    for label, (px, py) in points.items():
        plt.plot(px, py, 'o', color='darkblue', markersize=5)
        plt.text(px + 0.25, py + 0.25, label, fontsize=12, fontweight='bold')

    plt.title("USA TSTST 2017 - Problem 2: Concyclic Points (D, P, X, Y)", fontsize=13)
    plt.axis('off')
    plt.axis('equal')
    plt.legend(loc='upper right')
    plt.pause(1.5)

plt.show()
