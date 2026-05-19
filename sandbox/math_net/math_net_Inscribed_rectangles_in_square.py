# Jim McCleery
# May 18, 2026
# Kailua-Kona, HI

"""
Original problem link:
https://mathnet.mit.edu/explorer.html?p=usa_2021_e1cc31

This program uses a numerical search to construct a geometric figure.
It then shades a red rectangle and prints its area in the plot title.
"""

from math import acos, atan, cos, sin, sqrt
from random import uniform

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------

def distance(x1, y1, x2, y2):
    """
    Return the distance between two points.

    The distance formula comes from the Pythagorean Theorem:

        distance = sqrt((change in x)^2 + (change in y)^2)
    """
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# -----------------------------------------------------------------------------
def law_of_cosines(side1, side2, opposite_side):
    """
    Return the angle opposite 'opposite_side'.

    The Law of Cosines says:

        c^2 = a^2 + b^2 - 2ab cos(C)

    Solving for C gives:

        C = acos((a^2 + b^2 - c^2) / (2ab))

    Returns:
        (angle, True) if the angle can be computed
        (0, False) otherwise
    """
    denominator = 2 * side1 * side2

    if denominator == 0:
        return 0, False

    cosine_value = (side1**2 + side2**2 - opposite_side**2) / denominator

    # Floating-point arithmetic can sometimes produce a value like 1.0000000002.
    # The acos() function only accepts inputs from -1 to 1, so we clamp the value.
    cosine_value = max(-1, min(1, cosine_value))

    return acos(cosine_value), True


# -----------------------------------------------------------------------------
def intersection_of_lines(m1, b1, m2, b2):
    """
    Return the intersection point of two lines.

    Each line is written in slope-intercept form:

        y = m*x + b

    Returns:
        (x, y, True) if the lines intersect
        (0, 0, False) if the lines are parallel
    """
    if m1 == m2:
        return 0, 0, False

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1

    return x, y, True


# -----------------------------------------------------------------------------
def circle_circle_intersections(x0, y0, r0, x1, y1, r1):
    """
    Return the two intersection points of two circles.

    First circle:
        center = (x0, y0), radius = r0

    Second circle:
        center = (x1, y1), radius = r1

    Returns:
        (x3, y3, x4, y4, True) if the circles intersect
        (0, 0, 0, 0, False) otherwise
    """
    center_distance = distance(x0, y0, x1, y1)

    # The circles cannot intersect if their centers are the same point.
    if center_distance == 0:
        return 0, 0, 0, 0, False

    # The circles cannot intersect if they are too far apart.
    if center_distance > r0 + r1:
        return 0, 0, 0, 0, False

    # The circles cannot intersect if one circle is completely inside the other.
    if center_distance < abs(r0 - r1):
        return 0, 0, 0, 0, False

    # Find the point (x2, y2) along the line between the two circle centers.
    a = (r0**2 - r1**2 + center_distance**2) / (2 * center_distance)
    h_squared = r0**2 - a**2

    if h_squared < 0:
        return 0, 0, 0, 0, False

    h = sqrt(h_squared)

    x2 = x0 + a * (x1 - x0) / center_distance
    y2 = y0 + a * (y1 - y0) / center_distance

    # Move perpendicularly from (x2, y2) to get the two intersection points.
    x3 = x2 + h * (y1 - y0) / center_distance
    y3 = y2 - h * (x1 - x0) / center_distance

    x4 = x2 - h * (y1 - y0) / center_distance
    y4 = y2 + h * (x1 - x0) / center_distance

    return x3, y3, x4, y4, True


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Plot a line segment from point (x1, y1) to point (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
def polygon_fill_coordinates(vertices):
    """
    Convert a list of polygon vertices into x- and y-coordinate lists.

    Matplotlib's fill() function wants separate x-values and y-values.
    We also repeat the first point at the end so the polygon closes neatly.
    """
    x_coords, y_coords = zip(*vertices)

    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]

    return x_coords, y_coords


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------

ERROR_TOLERANCE = 0.00001

# -----------------------------------------------------------------------------
# Step 1: Search for a value of theta that makes y9 close to the top of the
# square. The square has side length s.
# -----------------------------------------------------------------------------
while True:
    theta = uniform(0.29, 0.31)

    a = 3 * cos(theta)
    b = 3 * sin(theta)
    s = a + b / 3

    # Four corners of the square.
    x0, y0 = 0, 0
    x1, y1 = s, 0
    x2, y2 = s, s
    x3, y3 = 0, s

    # Points inside or on the square that help define the construction.
    x4, y4 = a, 0
    x5, y5 = s, a / 3
    x6, y6 = 0, b

    # Find one intersection point of two circles:
    #   circle centered at (x6, y6) with radius 1
    #   circle centered at (x5, y5) with radius 3
    _, _, x7, y7, circles_intersect = circle_circle_intersections(x6, y6, 1, x5, y5, 3)

    if not circles_intersect:
        continue

    # Construct point 8 from point 7.
    x8 = 0
    y8 = y7 + sqrt(1 + x7**2)

    # We only want point 8 to be inside the square.
    if y8 > s:
        continue

    # Use the Law of Cosines to find the angle alpha.
    d1 = distance(x7, y7, x8, y8)
    d2 = distance(x6, y6, x8, y8)
    alpha, angle_found = law_of_cosines(d1, d2, 1)

    if not angle_found:
        continue

    # Construct point 9 using the angle alpha.
    x9 = x8 + cos(alpha)
    y9 = y8 + sin(alpha)

    # Stop searching when y9 is very close to the top edge of the square.
    if abs(y9 - s) < ERROR_TOLERANCE:
        break


# -----------------------------------------------------------------------------
# Step 2: Construct point 10.
# -----------------------------------------------------------------------------
line_slope = (y9 - y8) / (x9 - x8)
gamma = atan(line_slope)

x10 = x7 + cos(gamma)
y10 = y7 + sin(gamma)


# -----------------------------------------------------------------------------
# Step 3: Search for point 11 so that two lengths become nearly equal.
# -----------------------------------------------------------------------------
while True:
    # Point 11 is chosen randomly along the top edge of the square.
    x11 = uniform(s / 2, s)
    y11 = s

    # Find the line perpendicular to the line through points 10 and 11.
    line_slope = (y11 - y10) / (x11 - x10)
    perpendicular_slope = -1 / line_slope

    # Point 12 lies on the right edge of the square.
    x12 = s
    y12 = perpendicular_slope * s + y11 - perpendicular_slope * x11

    # Line through points 5 and 7.
    m1 = (y7 - y5) / (x7 - x5)
    b1 = y5 - m1 * x5

    # Line through points 11 and 12.
    m2 = (y11 - y10) / (x11 - x10)
    b2 = y12 - m2 * x12

    # Point 13 is the intersection of the two lines.
    x13, y13, lines_intersect = intersection_of_lines(m1, b1, m2, b2)

    if not lines_intersect:
        continue

    d1 = distance(x10, y10, x11, y11)
    d2 = distance(x12, y12, x13, y13)

    # Stop searching when these two distances are nearly equal.
    if abs(d1 - d2) < ERROR_TOLERANCE:
        break


# -----------------------------------------------------------------------------
# Step 4: Draw the figure.
# -----------------------------------------------------------------------------

# Draw the main constructed lines.
plot_line(x13, y13, x12, y12)
plot_line(x10, y10, x11, y11)
plot_line(x10, y10, x13, y13)

# Draw the square.
plot_line(x0, y0, x1, y1)
plot_line(x1, y1, x2, y2)
plot_line(x2, y2, x3, y3)
plot_line(x3, y3, x0, y0)

# Draw the remaining construction lines.
plot_line(x11, y11, x12, y12)
plot_line(x4, y4, x5, y5)
plot_line(x4, y4, x6, y6)
plot_line(x6, y6, x7, y7)
plot_line(x5, y5, x7, y7)
plot_line(x8, y8, x7, y7)
plot_line(x8, y8, x9, y9)
plot_line(x7, y7, x10, y10)
plot_line(x10, y10, x9, y9)

# The red quadrilateral is intended to be a rectangle.
rectangle_vertices = [
    (x10, y10),
    (x11, y11),
    (x12, y12),
    (x13, y13),
]

plt.fill(
    *polygon_fill_coordinates(rectangle_vertices),
    color="red",
    edgecolor="red",
    linewidth=2,
)

# Since the rectangle has side lengths d1 and d2, its area is d1*d2.
area = d1 * d2

plt.title(f"Area of red rectangle = {area:0.5f}")
plt.axis("equal")
plt.show()
