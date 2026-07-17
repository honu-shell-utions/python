# =============================================================================
# Jim McCleery
# July 16, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_3bad72
# =============================================================================

from math import pi, radians, sqrt, cos, sin, tan, acos
import matplotlib.pyplot as plt
from random import uniform
import numpy as np


# -----------------------------------------------------------------------------
# HELPER GEOMETRY FUNCTIONS
# -----------------------------------------------------------------------------

def distance(x1, y1, x2, y2):
    """
    Calculate the straight-line (Euclidean) distance between two points:
    Point 1 (x1, y1) and Point 2 (x2, y2).
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def law_of_cosines(d1, d2, side):
    """
    Calculate the angle opposite to 'side' in a triangle where the other 
    two known side lengths are d1 and d2.
    
    Returns:
        (angle_in_radians, True) if a valid triangle can be formed.
        (0, False) if the math fails.
    """
    try:
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except ValueError:
        return 0, False


def intersection_of_lines(m1, b1, m2, b2):
    """
    Find where two lines cross when given in slope-intercept form (y = m*x + b).
    
    Returns:
        (x, y, True) if they intersect.
        (0, 0, False) if they are parallel (equal slopes).
    """
    if m1 == m2:
        return 0, 0, False
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y, True


def line_intersection_from_points_v2(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Find the intersection point of two lines, each defined by two points.
    Line A goes through (x1, y1) and (x2, y2).
    Line B goes through (x3, y3) and (x4, y4).
    
    Returns:
        (x, y, True) if they intersect.
        (0, 0, False) if they are parallel or vertical math fails.
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
# PLOTTING FUNCTIONS
# -----------------------------------------------------------------------------

def plot_circle(x, y, radius, start=0, stop=2*pi):
    """
    Draw a circle (or part of a circle) centered at (x, y) with a given radius.
    """
    angle = np.linspace(start, stop, 1500)
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    plt.plot(x_arr, y_arr, color='gray', linestyle='--')


def plot_line(x1, y1, x2, y2, color='black'):
    """
    Draw a straight line segment from (x1, y1) to (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2], color=color)


# -----------------------------------------------------------------------------
# MAIN GEOMETRIC SIMULATION LOOP
# -----------------------------------------------------------------------------

# Initialize the minimum arc tracker with a maximum starting value (full circle)
min_arc = 2 * pi

# Loop up to 10,000 times to search for the smallest arc configuration
for _ in range(10**4):
    plt.cla()  # Clear the current plot axes to draw a fresh frame
    
    # Pick a random angle (theta) between 30 and 60 degrees (converted to radians)
    theta = uniform(radians(30), radians(60))
    
    # Center of unit circle
    x_O, y_O = 0.0, 0.0
    
    # Coordinates for Point P
    # Tangents from P make an angle of 45 deg, meaning the half-angle is 22.5 deg.
    # The distance OP = 1 / sin(22.5) = 1 / tan(15) which is fixed.
    x_P, y_P = 1 / tan(radians(15)), -1.0
    
    # P2 (second tangent point on circle from P)
    x_P2, y_P2 = 0.0, -1.0
    
    # P1 (first tangent point on circle from P)
    x_P1, y_P1 = 0.5, sqrt(3) / 2.0
    
    # Q1 (first tangent point on circle from Q)
    # The line OQ is rotated by 'theta' from the reference layout
    x_Q1, y_Q1 = cos(theta + radians(60)), sin(theta + radians(60))
    
    # Coordinates for Point Q
    # Tangents from Q make an angle of 30 deg, meaning the half-angle is 15 deg.
    # The distance OQ = 1 / sin(15) = 1 / cos(67.5) = 1 / cos(135/2).
    d_OQ = 1 / cos(radians(135 / 2))
    x_Q, y_Q = d_OQ * cos(theta + radians(60 + 135/2)), d_OQ * sin(theta + radians(60 + 135/2))
    
    # Q2 (second tangent point on circle from Q)
    x_Q2, y_Q2 = cos(radians(195) + theta), sin(radians(195) + theta)
    
    # Boundary helper intersections
    x_int7, y_int7, _ = line_intersection_from_points_v2(x_P, y_P, x_P2, y_P2, x_Q, y_Q, x_Q2, y_Q2)
    x_int8, y_int8, _ = line_intersection_from_points_v2(x_P, y_P, x_P1, y_P1, x_Q, y_Q, x_Q1, y_Q1)
    
    # Draw the unit circle centered at O
    plot_circle(x_O, y_O, 1)
    
    # Draw internal structure lines radiating from center O
    plot_line(x_O, y_O, x_P2, y_P2, color='blue')
    plot_line(x_O, y_O, x_P1, y_P1, color='blue')
    plot_line(x_O, y_O, x_Q1, y_Q1, color='red')
    plot_line(x_Q2, y_Q2, x_O, y_O, color='red')
    
    # Draw outer bounding tangent lines
    plot_line(x_int7, y_int7, x_P, y_P, color='gray')
    plot_line(x_int8, y_int8, x_P, y_P, color='gray')
    plot_line(x_int8, y_int8, x_Q, y_Q, color='gray')
    plot_line(x_int7, y_int7, x_Q, y_Q, color='gray')

    # Calculate distance and arc angle between point P2 and point Q2 on the circle boundary
    d_P2Q2 = distance(x_P2, y_P2, x_Q2, y_Q2)
    plt.plot(x_P2, y_P2, 'o', color='darkblue')  # Highlight P2 on the plot
    plt.plot(x_Q2, y_Q2, 'o', color='darkred')   # Highlight Q2 on the plot
    
    # Find the central angle (arc length) using the Law of Cosines
    arc, _ = law_of_cosines(1, 1, d_P2Q2)
    
    # Track the minimum angle discovered across all loop iterations
    if arc < min_arc:
        min_arc = arc
        
    # -------------------------------------------------------------------------
    # ADDING COORDINATE LABELS DIRECTLY TO PLOT
    # -------------------------------------------------------------------------
    # Font style settings for clean, professional math representation
    font_style = {'fontsize': 10, 'fontweight': 'bold', 'family': 'sans-serif'}
    
    # Draw text annotations with slight offsets to keep them readable
    plt.text(x_O - 0.15, y_O + 0.1, r"$O$", **font_style)
    plt.text(x_P + 0.1, y_P - 0.1, r"$P$", **font_style)
    plt.text(x_Q + 0.1, y_Q + 0.1, r"$Q$", **font_style)
    plt.text(x_P1 + 0.05, y_P1 + 0.05, r"$P_1$", **font_style)
    plt.text(x_P2 - 0.15, y_P2 - 0.15, r"$P_2$", **font_style)
    plt.text(x_Q1 + 0.05, y_Q1 + 0.05, r"$Q_1$", **font_style)
    plt.text(x_Q2 - 0.2, y_Q2 + 0.05, r"$Q_2$", **font_style)
    
    # Update the plot title with our current minimum, formatted to 6 decimal places
    plt.title(f'Minimum Arc P2Q2 = {min_arc:.06f}', fontsize=12, pad=10)
    
    # Maintain equal proportional scales and hide the outer grid box
    plt.axis('equal')
    plt.axis('off')
    
    # Briefly pause to let matplotlib render the graph animation frame
    plt.pause(0.1)

# Display the final plot state when the loop finishes
plt.show()
