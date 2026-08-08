"""
Jim McCleery
Today's date
Kailua-Kona, HI

https://mathnet.mit.edu/explorer.html?p=usa_2022_55a4fd
"""

from math import atan, cos, sin, pi
import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# HELPER FUNCTIONS FOR GEOMETRY AND DRAWING
# =============================================================================

def plot_line(x1, y1, x2, y2):
    """
    Draws a straight line segment connecting two points (x1, y1) and (x2, y2).
    """
    # plt.plot takes a list of X coordinates [x1, x2] and Y coordinates [y1, y2]
    plt.plot([x1, x2], [y1, y2], color='black')


def plot_circle(x, y, radius, start=0, stop=2*pi):
    """
    Draws a circle (or arc) centered at (x, y) with a given radius.
    
    Parameters:
        x, y   : Center coordinates of the circle
        radius : The radius of the circle
        start  : Starting angle in radians (default: 0)
        stop   : Ending angle in radians (default: 2*pi for a full circle)
    """
    # Generate 1,500 equally spaced angle values between 'start' and 'stop'
    angle = np.linspace(start, stop, 1500)
    
    # Trigonometry formulas to convert polar angles to Cartesian (x, y) points
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    
    # Plot the perimeter points of the circle
    plt.plot(x_arr, y_arr, color='black')


def polygon_area(vertices):
    """
    Calculates the surface area of a polygon given a list of (x, y) vertices
    using the Shoelace Formula (Gauss's area formula).
    """
    n = len(vertices)
    area = 0.0
    
    # Loop over every vertex and pair it with the next vertex in sequence
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # The % n loops back to the first vertex
        
        # Cross-multiplication step of the Shoelace algorithm
        area += x1 * y2 - y1 * x2
        
    # The final area is half the absolute value of the total cross-products
    return abs(area) / 2.0


def polygon_fill_coordinates(vertices):
    """
    Takes a list of (x, y) vertices and rearranges them into two separate lists:
    one for X values and one for Y values. It closes the shape by repeating the
    first vertex at the end.
    
    Returns:
        (x_coords, y_coords)
    """
    # zip(*vertices) unpacks [(x1,y1), (x2,y2)...] into x tuple and y tuple
    x_coords, y_coords = zip(*vertices)
    
    # Convert tuples to lists and append the starting point to close the shape
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    
    return x_coords, y_coords


# =============================================================================
# MAIN GEOMETRY SCRIPT & VISUALIZATION
# =============================================================================

# Define angle and basic circle radii
theta = atan(3 / 4)  # Calculate angle in radians whose tangent is 3/4
r1 = 6               # Radius of the small circle
r2 = 24              # Radius of the large circle

# Define Key Points in Cartesian Coordinates (x, y)
x0, y0 = 0, 0        # Center of small circle
x1, y1 = 30, 0       # Center of large circle
x2, y2 = -10, 0      # Convergence point to the left of small circle

# Calculate endpoint points extending outwards along positive and negative theta angles
x4, y4 = x2 + 32 * 1.2 * cos(theta), 32 * 1.2 * sin(theta)
x6, y6 = x2 + 32 * 1.2 * cos(-theta), 32 * 1.2 * sin(-theta)

# Vertices defining the triangular shape
x7, y7 = 6, 12
x8, y8 = 6, -12

# Draw structural construction lines
plot_line(x2, y2, x1, y1)  # Horizontal axis line
plot_line(x2, y2, x4, y4)  # Upper angled ray
plot_line(x2, y2, x6, y6)  # Lower angled ray
plot_line(x7, y7, x8, y8)  # Vertical segment forming triangle base

# Draw circular boundaries
plot_circle(x0, y0, r1)    # Small circle
plot_circle(x1, y1, r2)    # Large circle

# Define the vertices of the target triangle
vertices = [(x2, y2), (x7, y7), (x8, y8)]

# Calculate the area of the defined triangle
area = polygon_area(vertices)

# Fill the calculated triangle region with red color
x_fill, y_fill = polygon_fill_coordinates(vertices)
plt.fill(x_fill, y_fill, color='red', edgecolor='red', linewidth=2)

# Configure the visual plot display settings
plt.title(f'The area of the red triangle is {area:0.1f}.')
plt.axis('equal')  # Ensure scale aspect ratio is 1:1 so circles don't look like ovals
plt.axis('off')    # Hide the coordinate axes and ticks for clean output

# Render the plot window
plt.show()
