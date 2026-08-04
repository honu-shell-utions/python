# -----------------------------------------------------------------------------
# Jim McCleery
# August 3, 2026
# Kailua-Kona, HI
#
# https://youtu.be/4rVKyodTuq0?si=_YGpun8T-nAnGnpP
# -----------------------------------------------------------------------------

from math import pi, sqrt, atan, cos, sin
from random import uniform
from matplotlib.pyplot import plot, title, axis, show
import numpy as np


def point_in_polygon(x, y, polygon):
    """
    Determines if a point (x, y) lies inside a given polygon using 
    the ray-casting algorithm.

    Parameters:
        x, y: The coordinates of the point to test.
        polygon: A list of (x, y) tuples defining the polygon vertices.

    Returns:
        True if the point is inside the polygon, False otherwise.
    """
    n = len(polygon)
    inside = False

    # Start with the first vertex
    p1x, p1y = polygon[0]

    # Check each edge of the polygon
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        
        # Check if the horizontal ray through (x, y) crosses this polygon edge
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        # Calculate the x-intersection point of the edge with the ray
                        x_intersect = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= x_intersect:
                            inside = not inside
                            
        # Move to the next edge
        p1x, p1y = p2x, p2y

    return inside


def plot_circle(x, y, radius, start=0, stop=2 * pi):
    """
    Plots an arc or complete circle using matplotlib.

    Parameters:
        x, y: Center coordinates of the circle.
        radius: Radius of the circle.
        start, stop: Start and end angles in radians (default is full circle).
    """
    # Create 1,500 evenly spaced angle points between start and stop
    angle = np.linspace(start, stop, 1500)
    
    # Convert polar coordinates (angle, radius) to Cartesian coordinates (x, y)
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    
    # Plot the circle outline
    plot(x_arr, y_arr)


def plot_line(x1, y1, x2, y2):
    """
    Plots a straight line segment between two points (x1, y1) and (x2, y2).
    """
    plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# Main Program: Monte Carlo Area Estimation
# -----------------------------------------------------------------------------

# Define side lengths and geometry of the right triangle
a = 3 + 2 * sqrt(3)
b = 2 + sqrt(3)
c = sqrt(a**2 + b**2)         # Hypotenuse
d = c - a                     # Difference between hypotenuse and leg 'a'
theta = atan(b / a)           # Angle of the hypotenuse with the base

# Radius derived from circle tangency geometry:
# (b - r)^2 = r^2 + d^2  ==>  r = (b^2 - d^2) / (2 * b)
r = (b**2 - d**2) / (2 * b)

# Key geometric points
x0, y0 = 0, 0                 # Origin
x1, y1 = a, 0                 # Bottom-right vertex
x2, y2 = a, b                 # Top-right vertex
x3, y3 = a, r                 # Center of the tangent circle
x4, y4 = a * cos(theta), a * sin(theta)  # Point along the hypotenuse

# Define the right triangle vertices
tri = [(x0, y0), (x1, y1), (x2, y2)]

# Monte Carlo Simulation Parameters
throws = 10**6                # Number of random points to generate (1 million)
hits = 0                      # Counter for points falling in the target region

# Run Monte Carlo simulation by sampling points in a bounding box
for _ in range(1, throws + 1):
    x = uniform(a - r, a)      # Random x coordinate in bounding box
    y = uniform(r, b)          # Random y coordinate in bounding box

    # Filter out points that are outside the triangle or below y4
    if not point_in_polygon(x, y, tri) or y < y4:
        continue

    # Check if point lies outside the circle: (x - a)^2 + (y - r)^2 > r^2
    if (x - a)**2 + (y - r)**2 > r**2:
        hits += 1
        plot(x, y, '.')        # Plot successful target points

# Plot geometric boundaries
plot_circle(x3, y3, r)
plot_line(x0, y0, x1, y1)
plot_line(x2, y2, x1, y1)
plot_line(x0, y0, x2, y2)

# Calculate estimated area: ratio of hits * area of bounding box
box_area = r * (b - r)
area = (hits / throws) * box_area

# Format plot display
title(f'Shaded area is {area:0.5f}.')
axis('equal')
axis('off')
show()
