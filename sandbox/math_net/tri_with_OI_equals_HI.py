# -----------------------------------------------------------------------------
# Jim McCleery
# August 12, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_9b4b48
#
# Description:
# This program finds acute triangles ABC where the distance from the circumcenter (O)
# to the incenter (I) is equal to the distance from the orthocenter (H) to the 
# incenter (I), satisfying the geometric condition: OI = HI.
# -----------------------------------------------------------------------------

from math import pi, sqrt, cos, sin, acos, degrees
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


def law_of_cosines(side1, side2, opposite_side):
    """
    Calculates the angle (in radians) opposite to 'opposite_side' 
    using the Law of Cosines: c^2 = a^2 + b^2 - 2ab * cos(C)
    """
    try:
        cos_angle = (side1**2 + side2**2 - opposite_side**2) / (2 * side1 * side2)
        return acos(cos_angle), True
    except ValueError:
        return 0, False


def distance(x1, y1, x2, y2):
    """
    Calculates the straight-line (Euclidean) distance between two points (x1, y1) and (x2, y2).
    """
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


def incircle_of_triangle(x1, y1, x2, y2, x3, y3):
    """
    Calculates the incenter coordinates (I_x, I_y) and the inradius (r) of a triangle.
    """
    a = distance(x2, y2, x3, y3)
    b = distance(x1, y1, x3, y3)
    c = distance(x1, y1, x2, y2)

    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    inradius = area / s

    incenter_x = (a * x1 + b * x2 + c * x3) / (a + b + c)
    incenter_y = (a * y1 + b * y2 + c * y3) / (a + b + c)

    return incenter_x, incenter_y, inradius


def circle_through_points(x1, y1, x2, y2, x3, y3):
    """
    Calculates the circumcenter coordinates (O_x, O_y) and circumradius (R) 
    for the unique circle passing through three non-collinear vertices.
    """
    try:
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2
        
        M11 = x1 * y2 + x2 * y3 + x3 * y1 - (x2 * y1 + x3 * y2 + x1 * y3)
        M12 = s1 * y2 + s2 * y3 + s3 * y1 - (s2 * y1 + s3 * y2 + s1 * y3)
        M13 = s1 * x2 + s2 * x3 + s3 * x1 - (s2 * x1 + s3 * x2 + s1 * x3)
        
        x0 = 0.5 * M12 / M11
        y0 = -0.5 * M13 / M11
        r0 = sqrt((x1 - x0)**2 + (y1 - y0)**2)
        return x0, y0, r0, True
    except ZeroDivisionError:
        return 0, 0, 0, False


def line_intersection_from_points(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Finds the intersection point (x, y) of two lines defined by points (x1, y1)-(x2, y2) 
    and (x3, y3)-(x4, y4).
    """
    try:
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)
        x = (y1 - m1 * x1 - y3 + m2 * x3) / (m2 - m1)
        y = y1 + m1 * x - m1 * x1
        return x, y, True
    except ZeroDivisionError:
        return 0, 0, False


def plot_circle(x, y, radius):
    """Draws a circle given its center (x, y) and radius."""
    angles = np.linspace(0, 2 * pi, 500)
    x_circle = x + radius * np.cos(angles)
    y_circle = y + radius * np.sin(angles)
    plt.plot(x_circle, y_circle)


def plot_line(x1, y1, x2, y2, style='-'):
    """Draws a line segment between point 1 and point 2."""
    plt.plot([x1, x2], [y1, y2], style)


# -----------------------------------------------------------------------------
# Main Simulation Loop: Randomly search for acute triangles satisfying OI = HI
# -----------------------------------------------------------------------------
for _ in range(1000):
    plt.cla()  # Clear current axes for animation

    while True:
        # Generate random side lengths for triangle ABC
        a = uniform(5, 15)
        b = uniform(5, 15)
        c = uniform(5, 15)

        # Compute internal angles using Law of Cosines
        beta, ok1 = law_of_cosines(a, c, b)
        gamma, ok2 = law_of_cosines(a, b, c)
        if not ok1 or not ok2:
            continue

        alpha = pi - beta - gamma

        # Ensure the triangle is acute (all angles < 90 degrees / pi/2 radians)
        if alpha > pi / 2 or beta > pi / 2 or gamma > pi / 2:
            continue

        # Coordinate assignment for triangle vertices A, B, C
        # Vertex C at origin (0, 0), Vertex A at (a, 0), Vertex B at polar position
        C_x, C_y = 0, 0
        A_x, A_y = a, 0
        B_x, B_y = c * cos(beta), c * sin(beta)

        # Point I: Incenter & Incircle radius (r)
        I_x, I_y, r_in = incircle_of_triangle(A_x, A_y, B_x, B_y, C_x, C_y)

        # Point O: Circumcenter & Circumradius (R)
        O_x, O_y, R_circum, _ = circle_through_points(A_x, A_y, B_x, B_y, C_x, C_y)

        # Altitude endpoints (feet of altitudes) from vertices to opposite sides
        alt1_x, alt1_y = A_x + a * cos(gamma) * cos(pi - gamma), a * cos(gamma) * sin(pi - gamma)
        alt2_x, alt2_y = a * cos(beta) * cos(beta), a * sin(beta) * cos(beta)
        alt3_x, alt3_y = c * cos(beta), 0

        # Point H: Orthocenter (intersection of altitudes)
        H_x, H_y, _ = line_intersection_from_points(C_x, C_y, alt1_x, alt1_y, A_x, A_y, alt2_x, alt2_y)

        # Measure key distances: OI and HI
        dist_OI = distance(O_x, O_y, I_x, I_y)
        dist_HI = distance(H_x, H_y, I_x, I_y)

        # Check condition: OI == HI (within tolerance)
        if abs(dist_OI - dist_HI) < 0.001:
            break

    # -------------------------------------------------------------------------
    # Visualization and Plotting
    # -------------------------------------------------------------------------

    # Plot Triangle Sides (ABC)
    plot_line(C_x, C_y, A_x, A_y)
    plot_line(A_x, A_y, B_x, B_y)
    plot_line(B_x, B_y, C_x, C_y)

    # Plot Altitudes
    plot_line(C_x, C_y, alt1_x, alt1_y, style='--')
    plot_line(A_x, A_y, alt2_x, alt2_y, style='--')
    plot_line(B_x, B_y, alt3_x, alt3_y, style='--')

    # Plot Circles (Incircle and Circumcircle)
    plot_circle(I_x, I_y, r_in)
    plot_circle(O_x, O_y, R_circum)

    # Plot Points: Incenter (I), Circumcenter (O), Orthocenter (H)
    plt.plot(I_x, I_y, 'ro', label='I (Incenter)')
    plt.plot(O_x, O_y, 'go', label='O (Circumcenter)')
    plt.plot(H_x, H_y, 'bo', label='H (Orthocenter)')

    # Add Text Labels for Points and Vertices
    plt.text(A_x, A_y, '  A', fontsize=12)
    plt.text(B_x, B_y, '  B', fontsize=12)
    plt.text(C_x, C_y, '  C', fontsize=12)
    plt.text(I_x, I_y, '  I', fontsize=10, color='red')
    plt.text(O_x, O_y, '  O', fontsize=10, color='green')
    plt.text(H_x, H_y, '  H', fontsize=10, color='blue')

    # Convert angle measurements to degrees for display
    deg_alpha = degrees(alpha)
    deg_beta = degrees(beta)
    deg_gamma = degrees(gamma)

    plt.title(f'Alpha = {round(deg_alpha)}°, Beta = {round(deg_beta)}°, Gamma = {round(deg_gamma)}°\nCondition: OI ≈ HI')
    plt.axis('equal')
    plt.axis('off')
    plt.pause(0.5)

plt.show()
