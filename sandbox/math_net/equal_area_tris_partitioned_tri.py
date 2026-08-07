# -----------------------------------------------------------------------------
# Jim McCleery
# August 6, 2026
# Kailua-Kona, HI
#
# Geometry Solver: USA Mathematical Olympiad 2023 - Problem 2
# https://mathnet.mit.edu/explorer.html?p=usa_2023_2f9220
# -----------------------------------------------------------------------------

from math import atan, tan, sqrt
from random import uniform
import numpy as np
import matplotlib.pyplot as plt

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def line_intersection_from_points(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Finds the intersection point (x, y) of two lines defined by points:
    Line 1 through (x1, y1) and (x2, y2)
    Line 2 through (x3, y3) and (x4, y4)
    """
    try:
        # Calculate slopes for both lines: m = (y2 - y1) / (x2 - x1)
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)
        
        # Calculate x and y coordinates of intersection
        x = (y1 - m1 * x1 - y3 + m2 * x3) / (m2 - m1)
        y = y1 + m1 * x - m1 * x1
        return x, y, True
    except ZeroDivisionError:
        # Lines are parallel or vertical
        return 0, 0, False


def polygon_area(vertices):
    """
    Calculates the area of a polygon using the Shoelace Formula.
    Vertices must be given as an ordered list of (x, y) coordinates.
    """
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Next vertex (wraps around to start)
        area += x1 * y2 - y1 * x2
    return abs(area) / 2.0


def polygon_fill_coordinates(vertices):
    """
    Prepares x and y coordinate lists for Matplotlib's fill function
    by closing the shape (repeating the first vertex at the end).
    """
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords


def plot_line(x1, y1, x2, y2, color='blue', linestyle='-'):
    """Utility helper to plot a simple line segment between two points."""
    plt.plot([x1, x2], [y1, y2], color=color, linestyle=linestyle)


# =============================================================================
# MAIN GEOMETRY SOLVER & PLOTTING
# =============================================================================

# Search numerically for the target area 'x' that satisfies the problem conditions
while True:
    # Random guess for target area x
    x = uniform(3, 20)
    
    # Trigonometric calculations to establish segment lengths
    alpha = atan(17 + x / 2)
    BE = EC = sqrt((68 + 2 * x) / tan(alpha))
    BD = (68 + 2 * x) / BE

    # Assigning key point coordinates based on diagram labels:
    # Point A is at the top left vertex
    A_x, A_y = 0.0, 0.0
    
    # Point B is at the bottom-left right-angle corner
    B_x, B_y = 0.0, -(54 + 2 * x) / BE
    
    # Point C is at the bottom-right corner
    C_x, C_y = 2 * BE, B_y
    
    # Point D lies on segment AB
    D_x, D_y = 0.0, (-20 - x) / BE
    
    # Point E is the midpoint of segment BC
    E_x, E_y = BE, B_y

    # Point F is the intersection of line CD and the perpendicular line from E
    F_x, F_y, _ = line_intersection_from_points(
        C_x, C_y, D_x, D_y, 
        B_x, 14 / BE + B_y, C_x, 14 / BE + B_y
    )
    
    # Point G is the intersection of line AE and line CD
    G_x, G_y, _ = line_intersection_from_points(
        A_x, A_y, E_x, E_y, 
        D_x, D_y, C_x, C_y
    )
    
    # Define the first red triangle (Triangle ADG)
    triangle1_vertices = [(A_x, A_y), (D_x, D_y), (G_x, G_y)]
    area = polygon_area(triangle1_vertices)
    
    # Check if calculated area matches target value 'x'
    if abs(area - x) < 0.0001:
        break  # Solution found!

# Define the second red triangle (Triangle EFG)
triangle2_vertices = [(E_x, E_y), (F_x, F_y), (G_x, G_y)]

# Draw primary line segments forming the figure
plot_line(A_x, A_y, B_x, B_y)  # Line AB
plot_line(B_x, B_y, C_x, C_y)  # Line BC
plot_line(C_x, C_y, D_x, D_y)  # Line CD
plot_line(A_x, A_y, E_x, E_y)  # Line AE
plot_line(F_x, F_y, E_x, E_y)  # Line FE

# Highlight the two equal-area red triangles
plt.fill(*polygon_fill_coordinates(triangle1_vertices), color='red', alpha=0.7)
plt.fill(*polygon_fill_coordinates(triangle2_vertices), color='red', alpha=0.7)

# Add coordinate point labels (A, B, C, D, E, F, G) near each point
labels = {
    'A': (A_x - 0.2, A_y + 0.1),
    'B': (B_x - 0.2, B_y - 0.2),
    'C': (C_x + 0.1, C_y - 0.2),
    'D': (D_x - 0.2, D_y),
    'E': (E_x, E_y - 0.3),
    'F': (F_x + 0.1, F_y + 0.1),
    'G': (G_x + 0.1, G_y + 0.1),
}

for label, (lx, ly) in labels.items():
    plt.text(lx, ly, label, fontsize=12, fontweight='bold')

# Configure plot layout and display
plt.title(f'USA BMO 2023 - Problem 2\nEach red triangle area = {area:.3f}', fontsize=12)
plt.axis('off')
plt.show()
