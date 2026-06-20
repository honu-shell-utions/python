# -----------------------------------------------------------------------------
# Jim McCleery
# June 20, 2026
# Kailua-Kona, HI
# 
# Math Problem Reference:
# https://mathnet.mit.edu/explorer.html?p=usa_2024_e18b0d
# -----------------------------------------------------------------------------

# Import math functions for geometry calculations
from math import sqrt, tan, radians  

# Import matplotlib functions for plotting shapes
from matplotlib.pyplot import plot, fill, title, axis, show  

# Import uniform to select random floating-point numbers
from random import uniform  

# Import numpy for handling arrays and vector operations
import numpy as np  


# -----------------------------------------------------------------------------
def rotate_polygon(points, angle_degrees, center=(0, 0)):
    """
    Rotates a list of (x, y) coordinates around a specific center point.
    
    Args:
        points: A list of (x, y) tuples representing the shape vertices.
        angle_degrees: The angle to rotate the shape by (in degrees).
        center: The (x, y) coordinates of the rotation pivot point.
    """
    # Convert inputs into numpy arrays so we can do math on all points at once
    points = np.array(points, dtype=float)
    center = np.array(center, dtype=float)

    # Math formulas (like cos and sin) require angles in radians, not degrees
    theta = np.radians(angle_degrees)
    
    # Create a 2D rotation matrix
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    # 1. Move points so the center is at (0,0): (points - center)
    # 2. Multiply by the rotation matrix: @ rotation_matrix.T
    # 3. Move points back to their original center: + center
    rotated = (points - center) @ rotation_matrix.T + center
    
    # Convert the numpy array back into a standard Python list
    return rotated.tolist()


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Calculates the area of a polygon using the Shoelace Formula.
    
    Args:
        vertices: A list of (x, y) coordinates ordered around the perimeter.
    """
    n = len(vertices)
    area = 0
    
    # Loop through every vertex in the polygon
    for i in range(n):
        x1, y1 = vertices[i]
        
        # Get the next vertex. The '%' operator loops back to index 0 at the end.
        x2, y2 = vertices[(i + 1) % n]
        
        # Apply the cross-multiplication step of the shoelace formula
        area += x1 * y2 - y1 * x2
        
    # The absolute value ensures a positive area, divided by 2 per the formula
    return abs(area) / 2


# -----------------------------------------------------------------------------
def polygon_draw(points):
    """
    Draws the outline of a polygon and marks its corner vertices.
    """
    if len(points) < 3:
        raise ValueError("A polygon needs at least 3 points.")

    # Separate the (x, y) tuples into individual lists of X and Y values
    x = [p[0] for p in points]
    y = [p[1] for p in points]

    # Add the first point back to the end of the lists to close the shape outline
    x.append(points[0][0])
    y.append(points[0][1])

    # Plot the lines with circular markers ("o") at each corner
    plot(x, y, marker="o")


# -----------------------------------------------------------------------------
def polygon_fill_coordinates(vertices):
    """
    Prepares a list of vertices to be filled with color by closing the loop.
    """
    # zip(*vertices) separates a list of [(x1,y1), (x2,y2)] into (x1, x2) and (y1, y2)
    x_coords, y_coords = zip(*vertices)
    
    # Convert tuples to lists and explicitly append the first point to close the shape
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    
    return x_coords, y_coords


# -----------------------------------------------------------------------------
# Main Simulation Execution
# -----------------------------------------------------------------------------

# Define the side length and rotation angle constants
side = 14
alpha = 15

# This loop runs continuously until it finds a random angle that matches the target area
while True:
    # Pick a random floating-point angle between 0 and 60 degrees
    theta = uniform(0, 60)
    
    # Establish the 3 corner points of the initial baseline equilateral triangle
    points01 = [(-7, -7 / sqrt(3)), (7, -7 / sqrt(3)), (0, 14 / sqrt(3))]
    
    # Rotate the original triangle by the constant alpha angle (15 degrees)
    points02 = rotate_polygon(points01, alpha)
    
    # Rotate that second triangle a bit further by our random experimental theta angle
    points03 = rotate_polygon(points02, theta)

    # Unpack the coordinates of the vertices from the two rotated triangles
    (x4, y4), (x5, y5), (x6, y6) = points02
    (x7, y7), (x8, y8), (x9, y9) = points03
    
    # Group the points in an alternating sequence to form an interwoven hexagon
    points04 = [(x4, y4), (x7, y7), (x5, y5), (x8, y8), (x6, y6), (x9, y9)]
    
    # Calculate the area of this overlapping hexagon shape
    area = polygon_area(points04)
    
    # Target value check: is our current area close to 91 * sqrt(3)?
    # abs(difference) < 0.1 allows for a tiny margin of rounding error.
    if abs(area - 91 * sqrt(3)) < 0.1:
        break  # Found it! Exit the infinite loop.
    
# -----------------------------------------------------------------------------
# Matplotlib Visualization Formatting
# -----------------------------------------------------------------------------

# Draw outlines for the second triangle, third triangle, and intersection hexagon
polygon_draw(points02)
polygon_draw(points03)
polygon_draw(points04)

# Color the interior of the resulting hexagon solid red
fill(*polygon_fill_coordinates(points04), color='red', edgecolor='red', linewidth=2)

# Display the mathematical results in the window title header
title(f'tan(theta) = {tan(radians(theta)):0.5f}, which is 5*sqrt(3)/11.')

# Ensure the aspect ratio is uniform so shapes look perfectly proportioned (not stretched)
axis('equal')

# Turn off the chart's background grid and axis number markings
axis('off')

# Render the final window layout on screen
show()
