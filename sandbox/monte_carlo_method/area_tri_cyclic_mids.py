# -----------------------------------------------------------------------------
# Jim McCleery
# July 17, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_bf340b
# -----------------------------------------------------------------------------

from math import pi, sqrt, cos, sin, acos
from matplotlib.pyplot import *
from random import uniform

# =============================================================================
# HELPER GEOMETRY FUNCTIONS
# =============================================================================

def law_of_cosines(d1, d2, side):
    """
    Calculates the angle opposite to 'side' in a triangle with sides d1, d2, side.
    Returns (angle_in_radians, True) if successful, or (0, False) if impossible.
    """
    try:
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except:
        return 0, False


def distance(x1, y1, x2, y2):
    """
    Calculates the straight-line (Euclidean) distance between two points.
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def triangle_area_from_heron(a, b, c):
    """
    Calculates the area of a triangle using Heron's formula based on 3 side lengths.
    Returns (area, True) if successful, or (0, False) if impossible.
    """
    try:
        s = 0.5 * (a + b + c)
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        return area, True
    except:
        return 0, False


def plot_line(x1, y1, x2, y2):
    """
    Plots a straight line segment between two coordinate points.
    """
    plot([x1, x2], [y1, y2], color='black', linewidth=1.5)


def polygon_fill_coordinates(vertices):
    """
    Formats a list of (x, y) vertices into separate lists of X and Y coordinates
    and closes the polygon loop so it can be filled with color properly.
    """
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords


# =============================================================================
# MAIN SIMULATION AND GRAPHICS LOOP
# =============================================================================

# We run the loop 10 times to generate 10 different random triangle configurations
for _ in range(10):
    cla()  # Clear the current axes for the new drawing
    
    # 1. Randomly search for a small inner triangle (DEF) whose scaling lines 
    # create an outer triangle (ABC) with an area of exactly 1.0.
    while True:
        # Generate random side lengths between 0 and 1
        a = uniform(0, 1)
        b = uniform(0, 1)
        c = uniform(0, 1)
        
        # Check the Triangle Inequality Theorem (sum of two sides must exceed the third)
        if (a > b + c) or (b > a + c) or (c > a + b):
            continue  # Invalid triangle side lengths, try again
            
        # Determine internal angles using the Law of Cosines
        alpha, _ = law_of_cosines(a, c, b)
        beta, _ = law_of_cosines(a, b, c)

        # Define the coordinates of the inner triangle DEF
        x0, y0 = 0, 0                       # Point F
        x1, y1 = a, 0                       # Point D
        x2, y2 = c * cos(alpha), c * sin(alpha)  # Point E
        
        # Define the coordinates of the outer triangle ABC based on midpoint relationships:
        # F is the midpoint of CD, E is the midpoint of BF, D is the midpoint of AE
        x3, y3 = -a, 0                      # Point C
        x4, y4 = x1 + b * cos(-beta), b * sin(-beta)  # Point A
        x5, y5 = 2 * x2, 2 * y2              # Point B
        
        # Calculate the side lengths of the outer triangle ABC
        d1 = distance(x3, y3, x4, y4)  # Side CA
        d2 = distance(x4, y4, x5, y5)  # Side AB
        d3 = distance(x5, y5, x3, y3)  # Side BC
        
        # Calculate the total area of the large outer triangle
        big_area, _ = triangle_area_from_heron(d1, d2, d3)
        
        # If the large triangle's area is 1 (within a tiny rounding tolerance), we found it!
        if abs(big_area - 1) < 0.00001:
            break

    # 2. Draw the outer triangle ABC
    plot_line(x3, y3, x4, y4)  # Side CA
    plot_line(x4, y4, x5, y5)  # Side AB
    plot_line(x5, y5, x3, y3)  # Side BC

    # 3. Highlight and fill the inner triangle DEF with red
    vertices = [(x1, y1), (x2, y2), (x0, y0)]  # D, E, F
    fill(*polygon_fill_coordinates(vertices), color='red', edgecolor='red', linewidth=2, alpha=0.6)

    # 4. Add text labels to the coordinates for clarity
    # text(x, y, 'Label') places text directly onto the graph window
    text(x4, y4 + 0.03, 'A', fontsize=12, fontweight='bold', ha='center')
    text(x5 + 0.03, y5, 'B', fontsize=12, fontweight='bold', va='center')
    text(x3 - 0.05, y3, 'C', fontsize=12, fontweight='bold', ha='right')
    text(x1 + 0.02, y1 - 0.04, 'D', fontsize=12, fontweight='bold')
    text(x2 - 0.02, y2 + 0.03, 'E', fontsize=12, fontweight='bold')
    text(x0 - 0.04, y0 - 0.04, 'F', fontsize=12, fontweight='bold')

    # 5. Calculate the area of the small red inner triangle to display in the title
    little_area, _ = triangle_area_from_heron(a, b, c)
    title(f'Area of outer triangle ABC = 1.00000\nArea of inner red triangle DEF is {little_area:0.5f}')
    
    # Clean up display formatting
    axis('equal')  # Ensure 1 unit horizontally matches 1 unit vertically
    axis('off')    # Hide the standard X and Y axis gridlines and numbers
    pause(1)       # Pause for 1 second to show this instance before drawing the next one

show()
