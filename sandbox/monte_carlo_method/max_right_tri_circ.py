# Jim McCleery
# July 22, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2021_706bb1

from math import pi, sqrt, cos, sin
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def quadratic_equation(A, B, C):
    """
    Solves the quadratic equation: A*x^2 + B*x + C = 0.
    Returns (x1, x2, True) if real roots exist, or (0, 0, False) otherwise.
    """
    try:
        # Calculate discriminant: B^2 - 4AC
        disc = B**2 - 4 * A * C
        disc_sqrt = sqrt(disc)
        
        # Calculate the two potential roots
        x1 = (-B - disc_sqrt) / (2 * A)
        x2 = (-B + disc_sqrt) / (2 * A)
        
        # Sort roots so x1 is always the smaller value
        if x1 > x2:
            x1, x2 = x2, x1
            
        return x1, x2, True
    except ValueError:
        # Occurs if discriminant is negative (no real solutions)
        return 0, 0, False


def line_circle_intersection(cx, cy, r, m, b):
    """
    Finds the intersection points between a circle and a line.
    
    Circle equation: (x - cx)^2 + (y - cy)^2 = r^2
    Line equation:   y = m*x + b
    
    Returns (x2, y2, x3, y3, True) if intersections exist, else (0, 0, 0, 0, False).
    """
    # Coefficients derived from substituting y = m*x + b into circle equation
    A = 1 + m**2
    B = -2 * cx + 2 * m * b - 2 * m * cy
    C = cx**2 + b**2 - 2 * b * cy + cy**2 - r**2
    
    x2, x3, ok = quadratic_equation(A, B, C)
    if ok:
        y2 = m * x2 + b
        y3 = m * x3 + b
        return x2, y2, x3, y3, True
    else:
        return 0, 0, 0, 0, False


def polygon_area(vertices):
    """
    Calculates the area of a polygon given a list of (x, y) vertices
    using the Shoelace Formula.
    """
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2.0


def polygon_fill_coordinates(vertices):
    """
    Prepares coordinate lists (x-list and y-list) for plotting/filling a polygon.
    Appends the first point to the end to close the shape loop.
    """
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords


def plot_circle(x, y, radius):
    """Plots a circle given its center (x, y) and radius."""
    angles = np.linspace(0, 2 * pi, 500)
    x_arr = radius * np.cos(angles) + x
    y_arr = radius * np.sin(angles) + y
    plt.plot(x_arr, y_arr, color='black', linewidth=1.5)


def plot_line(x1, y1, x2, y2, style='k-'):
    """Plots a straight line segment between two points (x1, y1) and (x2, y2)."""
    plt.plot([x1, x2], [y1, y2], style)


# =============================================================================
# MAIN SIMULATION LOOP
# =============================================================================

max_area = -1

# Run Monte Carlo simulation to search for the maximum triangle area
for _ in range(10**6):
    plt.cla()  # Clear current plot axis for fresh rendering
    
    # Randomly select angles for points B and C on the right circle
    alpha = uniform(0, pi / 2)
    beta = uniform(-pi / 2, 0)
    
    # Center of left circle (Circle 1)
    x0, y0 = 0, 0
    
    # Center O of right circle (Circle 2)
    x1, y1 = 171, 0
    
    # Point B (x2, y2) on Circle 2
    x2, y2 = x1 + 100 * cos(alpha), 100 * sin(alpha)
    
    # Point C (x3, y3) on Circle 2
    x3, y3 = x1 + 100 * cos(beta), 100 * sin(beta)
    
    # Calculate perpendicular slope to line segment BC
    if x3 - x2 == 0:
        continue  # Avoid division by zero
    
    m_bc = (y3 - y2) / (x3 - x2)
    if m_bc == 0:
        continue
    
    m_perp = -1 / m_bc
    b_perp = y2 - m_perp * x2
    
    # Find intersection point A (x4, y4) on Circle 1 along perpendicular line
    x4, y4, _, _, ok = line_circle_intersection(x0, y0, 71, m_perp, b_perp)
    if not ok:
        continue
    
    # Plot geometric construction
    plot_line(x2, y2, x3, y3)  # Side BC
    plot_line(x4, y4, x3, y3)  # Side AC
    plot_line(x2, y2, x4, y4)  # Side AB
    
    # Plot circles
    plot_circle(x0, y0, 71)    # Small circle on left
    plot_circle(x1, y1, 100)   # Large circle on right
    
    # Plot center point O
    plt.plot(x1, y1, 'ko', markersize=4)
    
    # Define triangle ABC vertices
    vertices = [(x2, y2), (x3, y3), (x4, y4)]
    area = polygon_area(vertices)
    
    if area > max_area:
        max_area = area
        
    # Highlight triangle ABC with red fill
    x_fill, y_fill = polygon_fill_coordinates(vertices)
    plt.fill(x_fill, y_fill, color='red', alpha=0.3, edgecolor='red', linewidth=2)

    # -------------------------------------------------------------------------
    # LABELS (A, B, C, O) based on geometric diagram
    # -------------------------------------------------------------------------
    plt.text(x4 - 12, y4 - 8, 'A', fontsize=14, fontweight='bold')  # Point A on left circle
    plt.text(x2 - 5, y2 + 5, 'B', fontsize=14, fontweight='bold')   # Point B on top right circle
    plt.text(x3 + 5, y3 - 5, 'C', fontsize=14, fontweight='bold')   # Point C on bottom right circle
    plt.text(x1 - 12, y1 - 12, 'O', fontsize=14, fontweight='bold') # Center O of right circle

    # Plot formatting
    plt.title(f'Area of Triangle ABC: {area:.2f} | Current Max Area: {max_area:.2f}')
    plt.axis('equal')
    plt.axis('off')
    plt.pause(0.1)

plt.show()
