# -----------------------------------------------------------------------------
# Jim McCleery
# June 30, 2026
# Kailua-Kona, HI
# 
# https://mathnet.mit.edu/explorer.html?p=usa_2007_1954b5
# -----------------------------------------------------------------------------

# Import standard mathematical tools for geometry and trigonometry
from math import pi, sqrt, cos, sin, atan

# Import random number generator to pick random angles
from random import uniform

# Import matplotlib for drawing and animating the geometric shapes
from matplotlib.pyplot import plot, axis, show, text, title, pause, cla

# Import numpy to help generate smooth ranges of numbers for circles
import numpy as np


def circle_circle_intersections(x0, y0, r0, x1, y1, r1):
    """
    Calculates the two points where two circles intersect.
    
    Parameters:
        x0, y0 : Center of the first circle
        r0     : Radius of the first circle
        x1, y1 : Center of the second circle
        r1     : Radius of the second circle
    """
    try:
        # Step 1: Find the straight-line distance between the two circle centers
        d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
        
        # Step 2: Calculate distance from center 0 to the chord connecting the intersections
        a = (r0**2 - r1**2 + d**2) / (2 * d)
        
        # Step 3: Calculate the half-length of the intersection chord
        h = sqrt(r0**2 - a**2)
        
        # Step 4: Find the point where the chord crosses the line joining the centers
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d
        
        # Step 5: Offset from that point to get both individual intersection points
        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d
        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d
        
        return x3, y3, x4, y4, True
        
    except ZeroDivisionError:
        # Occurs if the circles share the exact same center point (d = 0)
        return 0, 0, 0, 0, False
    except ValueError:
        # Occurs if the circles are too far apart or one is entirely inside the other
        return 0, 0, 0, 0, False


def plot_circle(x, y, radius, start=0, stop=2*pi):
    """
    Plots a smooth circular arc on the screen using NumPy and Matplotlib.
    """
    # Create 1500 evenly spaced angles between the start and stop points
    angle = np.linspace(start, stop, 1500)
    
    # Convert polar coordinates (angle, radius) into standard Cartesian (X, Y) coordinates
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    
    # Plot the resulting points to draw the circle line
    plot(x_arr, y_arr)


def plot_line(x1, y1, x2, y2):
    """
    Plots a straight line segment between two coordinates: (x1, y1) and (x2, y2).
    """
    # Matplotlib expects a list of X-coordinates followed by a list of Y-coordinates
    plot([x1, x2], [y1, y2])


def intersection_of_lines(m1, b1, m2, b2):
    """
    Finds where two lines intersect using their slope-intercept equations (y = mx + b).
    
    Returns:
        (x, y, True) if they intersect, or (0, 0, False) if the lines are parallel.
    """
    # If slopes are identical, lines are parallel and never meet
    if m1 == m2:
        return 0, 0, False
        
    # Solve for X and Y using algebra
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y, True


def distance(x1, y1, x2, y2):
    """
    Calculates the straight-line (Euclidean) distance between two points.
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# -----------------------------------------------------------------------------
# MAIN RENDERING SIMULATION
# -----------------------------------------------------------------------------

# Define base geometric dimensions for the problem
radius = 5    # Radius of the primary circle centered at the origin
OA = 13       # Fixed distance from the origin (0,0) to target point A

# Run the visual simulation loop 100 times
for _ in range(10**2):
    cla()  # Clear the current graph axes before drawing a new frame
    
    # Loop continuously until a random configuration satisfies our target condition
    while True:
        # Pick a random angle between 0 and 90 degrees (expressed in radians)
        theta = uniform(0, pi / 2)

        # Set the coordinates for the primary circle's center at the origin
        x0, y0 = 0, 0

        # Calculate the coordinates for point A using trigonometry
        x1, y1 = OA * cos(theta), OA * sin(theta)

        # Find intersections between the primary circle and a secondary circle (centered at A, radius 12)
        x2, y2, x3, y3, _ = circle_circle_intersections(x0, y0, radius, x1, y1, 12)

        # Calculate geometric angle boundaries for a tangent/secant line condition
        alpha = atan(12 / 5) 
        beta = uniform(theta - alpha, theta + alpha)

        # Determine the coordinates of a random point on the primary circle's edge
        x4, y4 = radius * cos(beta), radius * sin(beta)

        # Compute the perpendicular line passing through this point
        m = (y4 - y0) / (x4 - x0)
        m1 = -1 / m
        b1 = y4 - m1 * x4
        
        # Line 2: Connects point A to the first circle-circle intersection
        m2 = (y2 - y1) / (x2 - x1)
        b2 = y1 - m2 * x1
        x5, y5, _ = intersection_of_lines(m1, b1, m2, b2) # Intersection point B

        # Line 3: Connects point A to the second circle-circle intersection
        m2 = (y3 - y1) / (x3 - x1)
        b2 = y1 - m2 * x1
        x6, y6, _ = intersection_of_lines(m1, b1, m2, b2) # Intersection point C

        # Measure the distance between intersection points B and C
        d = distance(x5, y5, x6, y6)
        
        # If the distance between B and C is exactly 7 (within a tiny rounding error), we found a match!
        if abs(d - 7) < 0.0001:
            break

    # Calculate total combined length: AC + AB
    total_dist = distance(x1, y1, x6, y6) + distance(x1, y1, x5, y5)
    
    # Render the geometric elements onto the screen
    plot(x4, y4, 'o')              # Draw the point on the circle edge
    plot_line(x0, y0, x1, y1)      # Draw line from origin to point A
    text(x5, y5 - 0.2, 'B')        # Label Point B
    text(x6, y6 + 0.2, 'C')        # Label Point C
    plot_line(x5, y5, x6, y6)      # Draw line segment BC
    plot_circle(x0, y0, radius)    # Draw the main circle
    plot(x0, y0, 'o')              # Draw the origin center point
    text(x1, y1 + 0.2, 'A')        # Label Point A
    plot_line(x2, y2, x1, y1)      # Draw secant/tangent boundary line 1
    plot_line(x3, y3, x1, y1)      # Draw secant/tangent boundary line 2
    
    # Configure graph display settings
    axis('equal')                  # Ensure circles aren't stretched out into ellipses
    axis('off')                    # Hide the background graph grid/axes lines
    title(f'AC + AB = {total_dist:0.3f}')  # Show calculated distance at the top
    pause(1)                       # Freeze the screen for 1 second before showing the next match
    
show()  # Keep the final window open when the program completes
