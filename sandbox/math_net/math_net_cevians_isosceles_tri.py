# -----------------------------------------------------------------------------
# Jim McCleery
# June 14, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2004_924f92
# -----------------------------------------------------------------------------

from math import pi, sqrt, sin, cos
from matplotlib.pyplot import plot, title, axis, show, text
from random import uniform


# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """
    Calculate and return the straight-line (Euclidean) distance 
    between two points: (x1, y1) and (x2, y2).
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# -----------------------------------------------------------------------------
def intersection_of_lines(m1, b1, m2, b2):
    """
    Find where two lines intersect using their slope-intercept form (y = mx + b).
    """
    if m1 == m2:
        return 0, 0, False
        
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y, True


# -----------------------------------------------------------------------------
def line_intersection_from_points_v2(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Find where two lines intersect when given two points for each line.
    """
    try:
        m1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - m1 * x1
        
        m2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - m2 * x3
        
        x, y, OK = intersection_of_lines(m1, b1, m2, b2)
        if not OK:
            return 0, 0, False
        return x, y, True
    except ZeroDivisionError:
        return 0, 0, False


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Draw a straight line segment on the screen between two points.
    """
    plot([x1, x2], [y1, y2], color='black', linewidth=1.5)


# -----------------------------------------------------------------------------
# MAIN GEOMETRY SOLVER AND SIMULATION
# -----------------------------------------------------------------------------

theta = pi / 4  # Represents a fixed 45-degree angle
side = 9        # Given side length of the geometric figure

# Start a loop that runs until we randomly find a specific geometric condition
while True:
    alpha = uniform(0, pi / 4)
    beta = (pi - alpha) / 2
    
    # Outer Triangle Vertices Map
    x0, y0 = 0, 0                                                            # Point C (Bottom Right)
    x1, y1 = side * cos(pi - theta - alpha), side * sin(pi - theta - alpha)  # Point B (Top Apex)
    x2, y2 = side * cos(pi - theta), side * sin(pi - theta)                  # Point A (Left)
    
    x3, y3 = x1 + cos(-theta - alpha - beta), y1 + sin(-theta - alpha - beta)
    d = distance(x1, y1, x2, y2)
    x4, y4 = x1 + d * cos(-theta - alpha), y1 + d * sin(-theta - alpha)
    
    m1 = (y4 - y2) / (x4 - x2)
    b1 = y2 - m1 * x2
    m2 = (y3 - y0) / (x3 - x0)
    b2 = 0
    
    # Point P (Central Intersection)
    x5, y5, _ = intersection_of_lines(m1, b1, m2, b2)
    m3 = (y5 - y1) / (x5 - x1)
    
    if abs(m1 * m3 + 1) < 0.00001:
        break

# Point F (Intersection on side AB)
x6, y6, _ = line_intersection_from_points_v2(x1, y1, x5, y5, x2, y2, x0, y0)

# -----------------------------------------------------------------------------
# PLOTTING, LABELS, AND DISPLAY
# -----------------------------------------------------------------------------

# Draw main outer triangle sides
plot_line(x2, y2, x1, y1)  # Side AB
plot_line(x1, y1, x0, y0)  # Side BC
plot_line(x0, y0, x2, y2)  # Side CA

# Draw inner lines matching the image's layout
plot_line(x3, y3, x0, y0)  
plot_line(x4, y4, x2, y2)
plot_line(x1, y1, x6, y6)  # Cevian BF through P

# Place text labels exactly matching your reference image
# (Slight padding adjustments applied so text floats cleanly next to the points)
text(x2 - 0.4, y2, 'A', fontsize=12, fontweight='bold')
text(x1, y1 + 0.3, 'B', fontsize=12, fontweight='bold')
text(x0 + 0.2, y0 - 0.2, 'C', fontsize=12, fontweight='bold')
text(x5 + 0.1, y5 + 0.2, 'P', fontsize=12, fontweight='bold')
text(x4 + 0.1, y4 - 0.1, 'D', fontsize=12, fontweight='bold')
text(x6 - 0.2, y6 - 0.2, 'E', fontsize=12, fontweight='bold')
text(x3 - 0.2, y3 + 0.2, 'F', fontsize=12, fontweight='bold')

# Calculate final required measurement
final_distance = distance(x2, y2, x3, y3)

# Configure plot properties
title(f'The length of AF is {final_distance:0.3f}')
axis('equal')  
axis('off')    
show()
