"""
Jim McCleery
May 11, 2026
Kailua-Kona, HI

https://youtu.be/Taatq1TetfE?si=Ub5ud-ogMCKo4_MR

This program draws a quarter circle and a triangle inside it.

Point D lies on the circular arc. We want D to be placed so that
angle ADC is a right angle.

The original version searched many equally spaced angles using np.linspace.
This version uses a bisection search, which is much faster and more precise.
"""

# -----------------------------------------------------------------------------
# Imports
# -----------------------------------------------------------------------------

from math import pi, cos, sin, acos, hypot
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Geometry helper functions
# -----------------------------------------------------------------------------

def distance(x1, y1, x2, y2):
    """
    Return the distance between two points.

    This is the ordinary distance formula:
        distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)

    hypot(a, b) is a convenient Python function that computes sqrt(a^2 + b^2).
    """
    return hypot(x2 - x1, y2 - y1)


def angle_at_vertex(ax, ay, vx, vy, bx, by):
    """
    Return the angle AVB in radians.

    The vertex of the angle is V.

    In this program, we will use this to measure angle ADC,
    where D is the vertex.
    """
    # Vector from V to A
    v_to_a_x = ax - vx
    v_to_a_y = ay - vy

    # Vector from V to B
    v_to_b_x = bx - vx
    v_to_b_y = by - vy

    # Dot product of the two vectors
    dot_product = v_to_a_x * v_to_b_x + v_to_a_y * v_to_b_y

    # Lengths of the two vectors
    length_va = hypot(v_to_a_x, v_to_a_y)
    length_vb = hypot(v_to_b_x, v_to_b_y)

    # Compute cosine of the angle using the dot product formula
    cos_angle = dot_product / (length_va * length_vb)

    # Roundoff error can sometimes make cos_angle slightly outside [-1, 1].
    # acos only accepts values in that interval, so we clamp the value.
    cos_angle = max(-1, min(1, cos_angle))

    return acos(cos_angle)


def polygon_area(vertices):
    """
    Return the area of a polygon using the shoelace formula.

    The vertices should be listed in order around the polygon.
    For this program, the polygon is just a triangle.
    """
    area_sum = 0

    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]

        area_sum += x1 * y2 - y1 * x2

    return abs(area_sum) / 2


def polygon_fill_coordinates(vertices):
    """
    Convert a list of vertices into x-values and y-values for plt.fill().

    The first point is added again at the end so the polygon closes.
    """
    x_values, y_values = zip(*vertices)

    x_values = list(x_values) + [x_values[0]]
    y_values = list(y_values) + [y_values[0]]

    return x_values, y_values


# -----------------------------------------------------------------------------
# Bisection search
# -----------------------------------------------------------------------------

def right_angle_error(theta, radius, ax, ay, cx, cy):
    """
    Measure how far angle ADC is from a right angle.

    D is placed on the circle using the angle theta:
        D = (radius * cos(theta), radius * sin(theta))

    If the returned value is:
        positive: angle ADC is bigger than 90 degrees
        negative: angle ADC is smaller than 90 degrees
        zero:     angle ADC is exactly 90 degrees
    """
    dx = radius * cos(theta)
    dy = radius * sin(theta)

    angle = angle_at_vertex(ax, ay, dx, dy, cx, cy)

    return angle - pi / 2


def bisection_search(function, low, high, tolerance=1e-12, max_steps=100):
    """
    Find an approximate root of a function using bisection.

    A root is a place where:
        function(x) = 0

    The bisection method works when function(low) and function(high)
    have opposite signs.
    """
    f_low = function(low)
    f_high = function(high)

    if f_low * f_high > 0:
        raise ValueError("Bisection search needs opposite signs at the endpoints.")

    for step in range(max_steps):
        mid = (low + high) / 2
        f_mid = function(mid)

        # If we are close enough, stop.
        if abs(f_mid) < tolerance:
            return mid

        # Keep the half-interval where the sign change occurs.
        if f_low * f_mid <= 0:
            high = mid
            f_high = f_mid
        else:
            low = mid
            f_low = f_mid

    # If max_steps is reached, return the best approximation.
    return (low + high) / 2


# -----------------------------------------------------------------------------
# Plotting helper functions
# -----------------------------------------------------------------------------

def plot_line(point1, point2):
    """
    Draw a line segment between two points.
    """
    x1, y1 = point1
    x2, y2 = point2

    plt.plot([x1, x2], [y1, y2], color="black")


def plot_arc(center, radius, start_angle, stop_angle):
    """
    Draw part of a circle.

    Angles are measured in radians.
    """
    center_x, center_y = center

    angles = np.linspace(start_angle, stop_angle, 500)

    x_values = center_x + radius * np.cos(angles)
    y_values = center_y + radius * np.sin(angles)

    plt.plot(x_values, y_values, color="black")


def label_point(label, point, x_offset=0.25, y_offset=0.25):
    """
    Plot and label a point.
    """
    x, y = point

    plt.plot(x, y, "ko")
    plt.text(x + x_offset, y + y_offset, label, fontsize=12)


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------

# Radius of the quarter circle
radius = 10

# Define the fixed points.
#
# O is the center of the circle.
# A and B are the endpoints of the quarter-circle arc.
# C is a point on the vertical radius.
O = (0, 0)
A = (radius, 0)
B = (0, radius)
C = (0, 5)

# We want to find point D on the arc from A to B.
# D has coordinates:
#     D = (radius * cos(theta), radius * sin(theta))
#
# We want angle ADC to be 90 degrees.
#
# Avoid theta = 0 exactly because then D would equal A,
# which would make the angle calculation degenerate.
small_angle = 1e-9
large_angle = pi / 2

# Create a one-variable function for bisection.
# This function returns 0 when angle ADC is exactly 90 degrees.
def error_for_this_theta(theta):
    return right_angle_error(theta, radius, A[0], A[1], C[0], C[1])


# Use bisection search to find theta.
theta = bisection_search(
    function=error_for_this_theta,
    low=small_angle,
    high=large_angle
)

# Now compute D using the theta found by bisection.
D = (radius * cos(theta), radius * sin(theta))

# The red triangle has vertices A, C, and D.
triangle_vertices = [A, C, D]

# Compute its area.
area = polygon_area(triangle_vertices)


# -----------------------------------------------------------------------------
# Draw the figure
# -----------------------------------------------------------------------------

plt.figure(figsize=(7, 7))

# Draw the two radii of the quarter circle.
plot_line(O, A)
plot_line(O, B)

# Draw the triangle.
plot_line(A, C)
plot_line(C, D)
plot_line(D, A)

# Draw the quarter-circle arc.
plot_arc(O, radius, 0, pi / 2)

# Fill the triangle in red.
plt.fill(
    *polygon_fill_coordinates(triangle_vertices),
    color="red",
    alpha=0.6,
    edgecolor="white",
    linewidth=2
)

# Label the vertices.
label_point("O", O, -0.6, -0.6)
label_point("A", A, 0.25, -0.5)
label_point("B", B, -0.6, 0.25)
label_point("C", C, -0.6, 0.1)
label_point("D", D, 0.25, 0.25)

# Add a title showing the area.
plt.title(f"Area of the red triangle = {area:.2f}")

# Make the scale the same on both axes.
# Without this, circles can appear stretched.
plt.axis("equal")

# Add a little extra space around the picture.
plt.xlim(-1, radius + 1)
plt.ylim(-1, radius + 1)

# Show a grid to make the geometry easier to see.
plt.grid(True)

plt.show()
