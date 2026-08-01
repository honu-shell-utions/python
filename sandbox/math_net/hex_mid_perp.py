# Jim McCleery
# July 31, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2016_735ea2

from math import pi, acos, sqrt
from matplotlib.pyplot import plot, fill, title, axis, pause, show, cla, text
from random import uniform
import numpy as np


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def distance(x1, y1, x2, y2):
    """
    Calculates the Euclidean distance (straight-line distance) between 
    two points: (x1, y1) and (x2, y2).
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def law_of_cosines(d1, d2, side):
    """
    Uses the Law of Cosines to find the angle opposite to 'side' 
    in a triangle with side lengths d1, d2, and 'side'.
    
    Returns the angle in radians along with a success flag (True/False).
    """
    try:
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except ValueError:
        return 0, False


def intersection_of_lines(m1, b1, m2, b2):
    """
    Finds the intersection point (x, y) of two lines given in slope-intercept 
    form (y = m*x + b).
    """
    if m1 == m2:
        return 0, 0, False
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y, True


def line_intersection_from_points(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Finds where two lines intersect given two points on line 1: (x1, y1), (x2, y2)
    and two points on line 2: (x3, y3), (x4, y4).
    """
    try:
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)
        x = (y1 - m1 * x1 - y3 + m2 * x3) / (m2 - m1)
        y = y1 + m1 * x - m1 * x1
        return x, y, True
    except ZeroDivisionError:
        return 0, 0, False


def plot_line(x1, y1, x2, y2):
    """
    Plots a straight line segment connecting point (x1, y1) to point (x2, y2).
    """
    plot([x1, x2], [y1, y2], color='blue')


def polygon_area(vertices):
    """
    Calculates the area of a polygon using the Shoelace formula.
    """
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2


def polygon_fill_coordinates(vertices):
    """
    Formats polygon vertices for matplotlib's fill() function by closing the loop.
    """
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords


# -----------------------------------------------------------------------------
# MAIN SIMULATION LOOP
# -----------------------------------------------------------------------------

for _ in range(10**4):
    cla()

    # --- 1. Define Triangle Vertices A, B, C ---
    A_x, A_y = 0, uniform(0, 10)
    B_x, B_y = uniform(0, 10), A_y + uniform(0, 5)
    C_x, C_y = uniform(0, 10), B_y - uniform(0, 5)

    # --- 2. Calculate Midpoints K, L, M ---
    K_x, K_y = (A_x + B_x) / 2, (A_y + B_y) / 2  # Midpoint of AB
    L_x, L_y = (C_x + B_x) / 2, (C_y + B_y) / 2  # Midpoint of BC
    M_x, M_y = (A_x + C_x) / 2, (A_y + C_y) / 2  # Midpoint of AC

    # Calculate side lengths
    d1 = distance(A_x, A_y, B_x, B_y)
    d2 = distance(B_x, B_y, C_x, C_y)
    d3 = distance(C_x, C_y, A_x, A_y)

    # Angles
    alpha, _ = law_of_cosines(d1, d3, d2)
    beta, _ = law_of_cosines(d1, d2, d3)
    gamma = pi - alpha - beta

    # Skip non-acute triangles
    if alpha > pi / 2 or beta > pi / 2 or gamma > pi / 2:
        continue

    # --- 3. Compute Slopes of Sides ---
    m1 = (B_y - A_y) / (B_x - A_x)
    m2 = (B_y - C_y) / (B_x - C_x)
    m3 = (C_y - A_y) / (C_x - A_x)

    # --- 4. Perpendicular Construction Points ---
    x6, y6, _ = intersection_of_lines(-1 / m3, K_y + K_x / m3, m3, A_y - m3 * A_x)
    x7, y7, _ = intersection_of_lines(-1 / m2, K_y + K_x / m2, m2, B_y - m2 * B_x)

    x8, y8, _ = intersection_of_lines(-1 / m3, L_y + L_x / m3, m3, A_y - m3 * A_x)
    x9, y9, _ = intersection_of_lines(-1 / m1, L_y + L_x / m1, m1, A_y - m1 * A_x)

    x10, y10, _ = intersection_of_lines(-1 / m1, M_y + M_x / m1, m1, A_y - m1 * A_x)
    x11, y11, _ = intersection_of_lines(-1 / m2, M_y + M_x / m2, m2, B_y - m2 * B_x)

    # --- 5. Inner Hexagon Vertices T, Q, S ---
    T_x, T_y, _ = line_intersection_from_points(K_x, K_y, x6, y6, M_x, M_y, x10, y10)
    Q_x, Q_y, _ = line_intersection_from_points(K_x, K_y, x7, y7, x9, y9, L_x, L_y)
    S_x, S_y, _ = line_intersection_from_points(L_x, L_y, x8, y8, M_x, M_y, x11, y11)

    # --- 6. Plot Lines & Points ---
    plot(K_x, K_y, 'ro')
    plot(L_x, L_y, 'ro')
    plot(M_x, M_y, 'ro')

    plot(T_x, T_y, 'ro')
    plot(Q_x, Q_y, 'ro')
    plot(S_x, S_y, 'ro')

    plot_line(A_x, A_y, B_x, B_y)
    plot_line(C_x, C_y, B_x, B_y)
    plot_line(A_x, A_y, C_x, C_y)

    plot_line(K_x, K_y, x6, y6)
    plot_line(K_x, K_y, x7, y7)

    plot_line(L_x, L_y, x8, y8)
    plot_line(L_x, L_y, x9, y9)

    plot_line(M_x, M_y, x10, y10)
    plot_line(M_x, M_y, x11, y11)

    # --- 7. Add Visual Text Labels to Coordinates ---
    offset = 0.2
    
    # Outer Vertices
    text(A_x - offset, A_y, 'A', fontsize=12, fontweight='bold')
    text(B_x + offset, B_y, 'B', fontsize=12, fontweight='bold')
    text(C_x + offset, C_y - offset, 'C', fontsize=12, fontweight='bold')

    # Midpoints
    text(K_x, K_y + offset, 'K', fontsize=12, fontweight='bold')
    text(L_x + offset, L_y, 'L', fontsize=12, fontweight='bold')
    text(M_x - offset, M_y - offset, 'M', fontsize=12, fontweight='bold')

    # Inner Vertices
    text(T_x - offset, T_y, 'T', fontsize=12, fontweight='bold')
    text(Q_x + offset, Q_y, 'Q', fontsize=12, fontweight='bold')
    text(S_x - offset, S_y - offset, 'S', fontsize=12, fontweight='bold')

    # --- 8. Measure and Fill Areas ---
    v_tri = [(A_x, A_y), (B_x, B_y), (C_x, C_y)]
    v_hex = [(K_x, K_y), (Q_x, Q_y), (L_x, L_y), (S_x, S_y), (M_x, M_y), (T_x, T_y)]

    a_tri = polygon_area(v_tri)
    a_hex = polygon_area(v_hex)

    fill(*polygon_fill_coordinates(v_hex), color='pink', alpha=0.5, edgecolor='red', linewidth=1.5)

    title(f'Area of triangle = {a_tri:0.3f}, Area of hexagon = {a_hex:0.3f}\nRatio = {a_tri/a_hex:0.3f}')
    axis('equal')
    axis('off')
    pause(0.5)

show()
