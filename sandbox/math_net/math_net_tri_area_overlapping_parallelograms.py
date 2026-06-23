# -----------------------------------------------------------------------------
# Jim McCleery
# June 22, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2019_21e57b
# -----------------------------------------------------------------------------

from math import sin, cos, radians
import matplotlib

# Force Matplotlib to use a visible Window interface (TkAgg) 
# This must be placed BEFORE importing pyplot
matplotlib.use('TkAgg') 

import matplotlib.pyplot as plt
from random import uniform

# -----------------------------------------------------------------------------
def intersection_of_lines(m1, b1, m2, b2):
    """ Finds where two lines cross using their slopes (m) and y-intercepts (b). """
    if m1 == m2:
        return 0, 0, False
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y, True

def line_intersection_from_points_v2(x1, y1, x2, y2, x3, y3, x4, y4):
    """ Calculates the intersection of two lines when given two points for each line. """
    try:
        m1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - m1 * x1
        m2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - m2 * x3
        x, y, success = intersection_of_lines(m1, b1, m2, b2)
        if not success:
            return 0, 0, False
        return x, y, True
    except ZeroDivisionError:
        return 0, 0, False

def plot_line(x1, y1, x2, y2):
    """ Draws a straight line segment between point 1 and point 2. """
    plt.plot([x1, x2], [y1, y2], color="black")

def polygon_area(vertices):
    """ Calculates the area inside a polygon using the Shoelace Formula. """
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2

def polygon_fill_coordinates(vertices):
    """ Rearranges vertices into separate X and Y lists so matplotlib can fill it. """
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords

# -----------------------------------------------------------------------------
# Main Simulation Loop
# -----------------------------------------------------------------------------

# Create the dedicated window explicitly before the loop starts
fig = plt.figure()

# Explicit non-blocking show to force the window onto your screen layout
plt.show(block=False)

# Run the visualization
for i in range(10):
    plt.cla()  # Clear canvas
    
    alpha = radians(35)
    beta = radians(145)
    gamma = radians(110)

    AB = 25
    BC = 1234 / (AB * sin(beta))
    BF = 2804 / (BC * sin(alpha + gamma))

    x0, y0 = 0, 0
    x1, y1 = -AB, 0
    x2, y2 = x1 + BC * cos(alpha), y1 + BC * sin(alpha)
    x3, y3 = BC * cos(alpha), BC * sin(alpha)
    x4, y4 = BF * cos(-gamma), BF * sin(-gamma)
    x5, y5 = x4 + BC * cos(alpha), y4 + BC * sin(alpha)

    m = (y5 - y4) / (x5 - x4)
    x6 = uniform(x4, x5)
    y6 = m * (x6 - x4) + y4

    x7, y7, _ = line_intersection_from_points_v2(x6, y6, x0, y0, x1, y1, x2, y2)

    plot_line(x0, y0, x1, y1)
    plot_line(x2, y2, x1, y1)
    plot_line(x2, y2, x3, y3)
    plot_line(x0, y0, x3, y3)
    plot_line(x0, y0, x4, y4)
    plot_line(x4, y4, x5, y5)
    plot_line(x5, y5, x3, y3)

    triangle_points = [(x6, y6), (x7, y7), (x3, y3)]

    plt.fill(
        *polygon_fill_coordinates(triangle_points),
        color="red",
        edgecolor="red",
        linewidth=2,
    )

    area = polygon_area(triangle_points)
    plt.title(f"Area of red triangle: {area:0.3f}")

    plt.axis("equal")
    plt.axis("off")

    # Draw the modifications and hold the screen for 1 full second per iteration
    fig.canvas.draw()
    plt.pause(1)

# This final show call locks the 10th frame in place until you click the window close button
plt.show(block=True)
