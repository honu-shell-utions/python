# =============================================================================
# Jim McCleery
# June 4, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_bcb7be
# =============================================================================

from math import sqrt
from matplotlib.pyplot import *
from random import uniform
import numpy as np


# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------

def quadratic_equation(A, B, C):
    """
    Solves a standard quadratic equation: A*x^2 + B*x + C = 0
    Returns the two answers (x1, x2) and a True/False success flag.
    """
    try:
        disc = B**2 - 4 * A * C
        disc = sqrt(disc)
        x1 = (-B - disc) / (2 * A)
        x2 = (-B + disc) / (2 * A)
        
        # Ensure x1 is always the smaller value
        if x1 > x2:
            x1, x2 = x2, x1
        return x1, x2, True
    except:
        # If the math fails (like taking the square root of a negative), return False
        return 0, 0, False


def line_circle_intersection(x1, y1, r, m, b):
    """
    Finds the two points where a line intersects a circle.
    Circle formula: center = (x1, y1), radius = r
    Line formula: y = m*x + b
    """
    A = 1 + m**2
    B = -2 * x1 + 2 * m * b - 2 * m * y1
    C = x1**2 + b**2 - 2 * b * y1 + y1**2 - r**2
    
    # Use our quadratic equation function to solve for x coordinates
    x2, x3, OK = quadratic_equation(A, B, C)
    
    if OK:
        # Calculate matching y coordinates using y = m*x + b
        y2 = m * x2 + b
        y3 = m * x3 + b
        return x2, y2, x3, y3, OK
    else:
        return 0, 0, 0, 0, False


def plot_circle(x, y, radius, start=0, stop=2*np.pi):
    """
    Plots a circular arc or full circle from a start angle to a stop angle.
    """
    # Create 1500 evenly spaced angles between start and stop
    angle = np.linspace(start, stop, 1500)
    
    # Convert angles to X and Y grid coordinates
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    
    # Use matplotlib to draw the line
    plot(x_arr, y_arr)


def plot_line(x1, y1, x2, y2):
    """
    Plots a straight line segment connecting two points: (x1, y1) and (x2, y2).
    """
    plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# MAIN PROGRAM LOGIC
# -----------------------------------------------------------------------------

# Set initial configurations
r = 1
throws = 10**4  # Number of random points to drop per loop to estimate area
accumulated_area = 0
x0, y0 = 0, 0   # Center of the main circle
counter = 0

# Run the simulation 1,000,000 times
for _ in range(10**6):
    cla()  # Clear the current graph axis so we can draw fresh shapes
    
    # Pick a random point (xa, ya) inside a 2x2 bounding square
    xa, ya = uniform(-1, 1), uniform(-1, 1)
    
    # Check if the point falls inside the unit circle; if not, skip this loop
    if xa**2 + ya**2 > 1:
        continue
    else:
        counter += 1

    # Calculate coordinates for horizontal and vertical lines intersecting the circle
    x1, y1 = sqrt(1 - ya**2), ya
    x2, y2 = -sqrt(1 - ya**2), ya
    x3, y3 = xa, sqrt(1 - xa**2)
    x4, y4 = xa, -sqrt(1 - xa**2)

    # Calculate intersections for two diagonal intersecting lines
    x5, y5, x6, y6, _ = line_circle_intersection(x0, y0, r, 1, ya - xa)
    x7, y7, x8, y8, _ = line_circle_intersection(x0, y0, r, -1, ya + xa)
    
    # Draw all the calculated lines and the main boundary circle
    plot_line(x1, y1, x2, y2)
    plot_line(x3, y3, x4, y4)
    plot_line(x5, y5, x6, y6)
    plot_line(x7, y7, x8, y8)
    plot_circle(x0, y0, r)
    plot(xa, ya, 'o')  # Draw our target point as a solid circle

    # Monte Carlo simulation to estimate shaded areas
    hits = 0
    for _ in range(throws):
        x, y = uniform(-1, 1), uniform(-1, 1)
        
        # Verify if the random throw lands inside the circle
        if x**2 + y**2 > 1:
            continue
            
        # Geometric conditions defining the target shaded boundaries
        in_area01 = (y > ya) and (y < ya + x - xa)
        in_area02 = (x < xa) and (y > ya - x + xa)
        in_area03 = (y < ya) and (y > ya + x - xa)
        in_area04 = (x > xa) and (y < ya - x + xa)
        
        # If the point lands in any of the four areas, count it as a "hit"
        if in_area01 or in_area02 or in_area03 or in_area04:
            plot(x, y, '.')  # Mark the hit point on the graph
            hits += 1

    # Calculate area based on hit ratio multiplied by the bounding square's area (4)
    accumulated_area += (hits / throws) * 4
    
    # Update the graph title text with current stats
    title(f'Average Shaded Area = {accumulated_area/counter:0.5f}')
    axis('equal')  # Ensure the circle looks perfectly round on the screen
    pause(0.5)     # Pause briefly so the viewer can see the live frame animation

# Keep the final window open when the program completes
show()
