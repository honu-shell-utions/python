# -----------------------------------------------------------------------------
# Jim McCleery
# August 15, 2026
# Kailua-Kona, HI
#
# Problem:
# "In a triangle ABC, take point D on BC such that DB = 14, DA = 13, DC = 4, 
# and the circumcircle of ADB is congruent to the circumcircle of ADC. 
# What is the area of triangle ABC?"
#
# https://mathnet.mit.edu/explorer.html?p=usa_2008_2e3338
# -----------------------------------------------------------------------------

from math import pi, sin, cos, asin, sqrt
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------

def define_circle_from_points(x1, y1, x2, y2, x3, y3):
    """
    Finds the center (cx, cy) and radius of a circle passing through 
    three points (x1, y1), (x2, y2), and (x3, y3).
    """
    temp = x2 * x2 + y2 * y2
    bc = (x1 * x1 + y1 * y1 - temp) / 2
    cd = (temp - x3 * x3 - y3 * y3) / 2
    det = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    # Calculate center coordinates (cx, cy)
    cx = (bc * (y2 - y3) - cd * (y1 - y2)) / det
    cy = ((x1 - x2) * cd - (x2 - x3) * bc) / det
    
    # Distance formula from the center to any vertex gives the radius
    radius = sqrt((cx - x1) ** 2 + (cy - y1) ** 2)
    return cx, cy, radius


def polygon_area(vertices):
    """
    Calculates the area of a polygon using the Shoelace formula.
    vertices: list of (x, y) coordinate pairs.
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
    Prepares x and y coordinate lists for filling a polygon in matplotlib 
    by repeating the first vertex at the end to close the shape.
    """
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords


def plot_line(x1, y1, x2, y2, color='black', linestyle='-'):
    """Draws a straight line segment between two points (x1, y1) and (x2, y2)."""
    plt.plot([x1, x2], [y1, y2], color=color, linestyle=linestyle)


def plot_circle(x, y, radius, color='blue', linestyle='--'):
    """Draws the outline of a circle centered at (x, y) with a given radius."""
    angles = np.linspace(0, 2 * pi, 500)
    x_arr = radius * np.cos(angles) + x
    y_arr = radius * np.sin(angles) + y
    plt.plot(x_arr, y_arr, color=color, linestyle=linestyle)


# -----------------------------------------------------------------------------
# Main Simulation / Solver Loop
# -----------------------------------------------------------------------------

# Use Monte Carlo / random search to find the correct triangle geometry
# where the circumradii of triangles ADB and ADC are equal (congruent circumcircles).
while True:
    alpha = uniform(0, pi / 2)
    beta = asin(13 * sin(alpha) / 14)
    gamma = pi - alpha - beta
    
    # Calculate side AB using the Law of Sines in triangle ADB
    AB = 14 * sin(gamma) / sin(alpha)

    # Define vertex coordinates
    x0, y0 = 0, 0                                    # Vertex A
    x1, y1 = AB, 0                                   # Vertex B
    x2, y2 = x1 + 18 * cos(pi - beta), 18 * sin(pi - beta)  # Vertex C (BC = DB + DC = 14 + 4 = 18)
    x3, y3 = x1 + 14 * cos(pi - beta), 14 * sin(pi - beta)  # Point D (DB = 14)

    # Compute circumcircles for triangle ADB and triangle ADC
    x4, y4, r1 = define_circle_from_points(x1, y1, x0, y0, x3, y3)
    x5, y5, r2 = define_circle_from_points(x0, y0, x2, y2, x3, y3)

    # Stop once the radii of both circumcircles match closely
    if abs(r1 - r2) < 0.00001:
        break


# -----------------------------------------------------------------------------
# Visualization
# -----------------------------------------------------------------------------

# 1. Fill Triangle ABC with light red / transparent color
vertices = [(x0, y0), (x1, y1), (x2, y2)]
area = polygon_area(vertices)
plt.fill(*polygon_fill_coordinates(vertices), color='salmon', alpha=0.5, edgecolor='darkred', linewidth=2)

# 2. Draw Triangle Sides & Internal Segment AD
plot_line(x0, y0, x1, y1, color='darkred', linestyle='-')  # Side AB
plot_line(x1, y1, x2, y2, color='darkred', linestyle='-')  # Side BC
plot_line(x2, y2, x0, y0, color='darkred', linestyle='-')  # Side CA
plot_line(x0, y0, x3, y3, color='black',   linestyle='--') # Segment AD

# 3. Draw Circumcircles for ADB and ADC
plot_circle(x4, y4, r1, color='teal', linestyle=':')
plot_circle(x5, y5, r2, color='darkorange', linestyle=':')

# 4. Add Point Labels (A, B, C, D)
plt.text(x0 - 0.6, y0 - 0.5, 'A', fontsize=12, fontweight='bold')
plt.text(x1 + 0.3, y1 - 0.5, 'B', fontsize=12, fontweight='bold')
plt.text(x2 - 0.6, y2 + 0.4, 'C', fontsize=12, fontweight='bold')
plt.text(x3 + 0.3, y3 + 0.3, 'D', fontsize=12, fontweight='bold')

# Plot vertex markers
for (px, py) in [(x0, y0), (x1, y1), (x2, y2), (x3, y3)]:
    plt.plot(px, py, 'ko', markersize=5)

# 5. Graph Settings & Display
plt.title(f'Area of Triangle ABC = {area:.3f}', fontsize=14, pad=12)
plt.axis('off')
plt.axis('equal')
plt.show()
