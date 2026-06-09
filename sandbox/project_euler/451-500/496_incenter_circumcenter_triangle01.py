# -----------------------------------------------------------------------------
# Jim McCleery
# June 8, 2026
# Kailua-Kona, HI
#
# https://projecteuler.net/problem=496
# -----------------------------------------------------------------------------
from math import cos, sin, acos, sqrt, pi, gcd
import numpy as np
from matplotlib.pyplot import *
# -----------------------------------------------------------------------------
def law_of_cosines(d1, d2, side):
    """
    Calculates the angle opposite to 'side' using the Law of Cosines.
    Expects the three sides of a triangle: d1, d2, and the target side.
    Returns the angle in radians and a True success flag.
    """
    try:
        # Formula: cos(C) = (a^2 + b^2 - c^2) / (2ab)
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except ValueError:
        # If the side lengths cannot form a valid triangle, acos() will fail.
        return 0, False

# -----------------------------------------------------------------------------
def incircle_of_triangle(x1, y1, x2, y2, x3, y3):
    """
    Calculates the center point (incenter) and radius (inradius) 
    of the circle that perfectly fits inside the triangle.
    Takes the (x, y) coordinates of all three vertices.
    """
    # First, calculate the lengths of all three sides using the distance formula
    a = sqrt((x2 - x3) ** 2 + (y2 - y3) ** 2)
    b = sqrt((x1 - x3) ** 2 + (y1 - y3) ** 2)
    c = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    # Calculate the semi-perimeter (s) and area using Heron's Formula
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    inradius = area / s

    # The coordinates of the incenter are a weighted average of the vertices
    incenter_x = (a * x1 + b * x2 + c * x3) / (a + b + c)
    incenter_y = (a * y1 + b * y2 + c * y3) / (a + b + c)

    return incenter_x, incenter_y, inradius

# -----------------------------------------------------------------------------
def define_circle_from_points(x1, y1, x2, y2, x3, y3):
    """
    Calculates the center (cx, cy) and radius of the circumcircle 
    (the circle passing through all three vertices of the triangle).
    """
    temp = x2 * x2 + y2 * y2
    bc = (x1 * x1 + y1 * y1 - temp) / 2
    cd = (temp - x3 * x3 - y3 * y3) / 2
    det = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    cx = (bc * (y2 - y3) - cd * (y1 - y2)) / det
    cy = ((x1 - x2) * cd - (x2 - x3) * bc) / det
    radius = sqrt((cx - x1) ** 2 + (cy - y1) ** 2)
    
    return cx, cy, radius

# -----------------------------------------------------------------------------
def line_circle_intersection(x1, y1, r, m, b):
    """
    Finds where a line (y = mx + b) intersects a circle centered at (x1, y1) with radius r.
    Returns the two intersection coordinate pairs and a True success flag.
    """
    # Substituting the line equation into the circle equation yields a quadratic equation:
    # A*x^2 + B*x + C = 0
    A = 1 + m**2
    B = -2 * x1 + 2 * m * b - 2 * m * y1
    C = x1**2 + b**2 - 2 * b * y1 + y1**2 - r**2
    
    # Solve using the quadratic formula: x = (-B +/- sqrt(B^2 - 4AC)) / 2A
    try:
        disc = B**2 - 4 * A * C
        disc = sqrt(disc)
        x2 = (-B - disc) / (2 * A)
        x3 = (-B + disc) / (2 * A)
        
        # Calculate the corresponding y coordinates using y = mx + b
        y2 = m * x2 + b
        y3 = m * x3 + b
        return x2, y2, x3, y3, True
    except ValueError:
        # If the line does not touch the circle, taking sqrt of a negative discriminant fails
        return 0, 0, 0, 0, False

# -----------------------------------------------------------------------------
def plot_circle(x, y, radius, label=None, linestyle='-', color=None, start=0, stop=2*pi):
    """
    Plot part of a circle from angle 'start' to angle 'stop' in radians.
    """
    angle = np.linspace(start, stop, 1500)
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    plot(x_arr, y_arr, label=label, linestyle=linestyle, color=color)

# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """
    Calculates the standard straight-line distance between two points.
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2, label=None, linestyle='-', color=None):
    """
    Plot a line segment between two points using matplotlib.
    """
    plot([x1, x2], [y1, y2], label=label, linestyle=linestyle, color=color)

# -----------------------------------------------------------------------------
def compute_F(L):
    """
    Computes F(L) using a parameterized variation of Euclid's formula.
    
    The condition AC = DI is equivalent to the algebraic rule: a^2 = b(b + c)
    where a = BC, b = AC, and c = AB.
    """
    total_BC_sum = 0
    unique_triangles = set() 
    
    max_n = int(sqrt(L))
    
    for n in range(1, max_n + 1):
        for m in range(n + 1, 2 * n):
            if gcd(m, n) == 1:
                primitive_a = m * n
                primitive_b = n**2
                primitive_c = m**2 - n**2
                
                k = 1
                while True:
                    a = primitive_a * k
                    b = primitive_b * k
                    c = primitive_c * k
                    
                    if a > L:
                        break
                    
                    if a + b > c and a + c > b and b + c > a:
                        triangle = (a, b, c)
                        if triangle not in unique_triangles:
                            unique_triangles.add(triangle)
                            total_BC_sum += a
                    
                    k += 1
                    
    return total_BC_sum, unique_triangles

# -----------------------------------------------------------------------------
# MAIN EXECUTION BLOCK
# -----------------------------------------------------------------------------
max_BC = 100
res, triangles = compute_F(max_BC)

for BC, AC, AB in triangles:
    # Place vertex A at the origin (0,0)
    x0, y0 = 0, 0
    
    # Place vertex B on the flat X-axis at length AB
    x1, y1 = AB, 0
    
    # Find the angle at vertex A using the side lengths
    theta, _ = law_of_cosines(AB, AC, BC)
    
    # Use trigonometry to find the coordinates of vertex C
    x2, y2 = AC * cos(theta), AC * sin(theta)
    
    # Calculate key centers needed for Project Euler 496
    x3, y3, r = incircle_of_triangle(x0, y0, x1, y1, x2, y2)
    x4, y4, R = define_circle_from_points(x0, y0, x1, y1, x2, y2)
    
    # The line (AI) passes through origin (0,0) and the incenter (x3, y3).
    m = y3 / x3
    
    # Find where the line (AI) intersects the circumcircle. 
    _, _, x5, y5, _ = line_circle_intersection(x4, y4, R, m, 0)
    
    # Calculate the distance from the Incenter (I) to this circumcircle intersection (D)
    DI = distance(x3, y3, x5, y5)
    
    cla()
    
    # Plot Triangle ABC
    plot_line(x0, y0, x1, y1, label=f'AB = {AB}', color='black')
    plot_line(x1, y1, x2, y2, label=f'BC = {BC}', color='black')
    plot_line(x2, y2, x0, y0, label=f'AC = {AC}', color='black')
    
    # Plot Ray AD (Bisector through Incenter)
    plot_line(x0, y0, x5, y5, label='Bisector AD', linestyle='--', color='blue')
    
    # Plot Circles
    plot_circle(x3, y3, r, label=f'Incircle (r={r:.2f})', color='green')
    plot_circle(x4, y4, R, label=f'Circumcircle (R={R:.2f})', color='red')
    
    # Label key vertex and intersection points
    text(x0, y0, '  A (0,0)', verticalalignment='bottom', horizontalalignment='right', fontweight='bold')
    text(x1, y1, '  B', verticalalignment='bottom', horizontalalignment='left', fontweight='bold')
    text(x2, y2, '  C', verticalalignment='bottom', horizontalalignment='center', fontweight='bold')
    text(x3, y3, '  I (Incenter)', verticalalignment='center', color='green')
    text(x5, y5, '  D', verticalalignment='top', color='blue', fontweight='bold')
    
    # Plot point markers for clarity
    scatter([x0, x1, x2, x3, x5], [y0, y1, y2, y3, y5], color='purple', zorder=5)
    
    # Title and Layout
    title(f'Triangle: BC={BC}, AC={AC}, AB={AB}\nMaximum BC = {max_BC}')
    axis('equal')
    grid(True, linestyle=':', alpha=0.6)
    legend(loc='upper right')
    pause(1)
    
show()
