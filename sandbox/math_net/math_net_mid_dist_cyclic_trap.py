# =============================================================================
# Jim McCleery
# June 27, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2025_15952c
# =============================================================================

import random
from math import asin, cos, pi, sin, sqrt
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """Calculate the straight-line (Euclidean) distance between two points."""
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def quadratic_equation(A, B, C):
    """Solve the quadratic formula: A*x^2 + B*x + C = 0.

    Returns the two x-values and a success flag (True/False).
    """
    try:
        disc = B**2 - 4 * A * C  # Calculate the discriminant
        disc = sqrt(disc)
        x1 = (-B - disc) / (2 * A)
        x2 = (-B + disc) / (2 * A)
        # Ensure x1 is the smaller or equal value
        if x1 > x2:
            x1, x2 = x2, x1
        return x1, x2, True
    except ValueError:
        # If the discriminant is negative, no real roots exist
        return 0, 0, False


def line_circle_intersection(x1, y1, r, m, b):
    """Find the intersection points between a circle and a line (y = m*x + b).

    Circle is defined by center (x1, y1) and radius r.
    """
    A = 1 + m**2
    B = -2 * x1 + 2 * m * b - 2 * m * y1
    C = x1**2 + b**2 - 2 * b * y1 + y1**2 - r**2

    x2, x3, OK = quadratic_equation(A, B, C)
    if OK:
        y2 = m * x2 + b
        y3 = m * x3 + b
        return x2, y2, x3, y3, OK
    else:
        return 0, 0, 0, 0, False


# -----------------------------------------------------------------------------
# PLOTTING FUNCTIONS
# -----------------------------------------------------------------------------
def plot_circle(cx, cy, radius):
    """Draw a circle given its center coordinates and radius."""
    # Create 1500 evenly spaced angles from 0 to 2*pi (full circle)
    angles = np.linspace(0, 2 * pi, 1500)
    # Convert polar coordinates to Cartesian coordinates
    x_coords = radius * np.cos(angles) + cx
    y_coords = radius * np.sin(angles) + cy
    plt.plot(x_coords, y_coords, color="blue", alpha=0.3)


def plot_line(x1, y1, x2, y2):
    """Draw a straight line segment between two points."""
    plt.plot([x1, x2], [y1, y2], color="black")


# -----------------------------------------------------------------------------
# MAIN GEOMETRY SIMULATION
# -----------------------------------------------------------------------------
radius = 5
theta = asin(2 / 5)

# We use a Monte Carlo/Numerical search loop to find the exact configuration
while True:
    # Set the circle center at the origin
    x0, y0 = 0, 0

    # Define coordinates for points A and B based on the trapezoid's symmetry
    x1, y1 = 5 * cos(pi / 2 - theta), 5 * sin(pi / 2 - theta)
    x2, y2 = 5 * cos(pi / 2 + theta), 5 * sin(pi / 2 + theta)

    # Randomly guess a scale variable to find where points C and D sit
    x = random.uniform(2, 5)
    alpha = asin(x / 5)

    # Define coordinates for points D, C, and E
    x3, y3 = 5 * cos(alpha - pi / 2), 5 * sin(alpha - pi / 2)
    x4, y4 = 5 * cos(-alpha - pi / 2), 5 * sin(-alpha - pi / 2)
    x5, y5 = x3 + 2, y3  # Point E is 2 units away from D

    # Calculate the slope (m) and y-intercept (b) of line AE
    m = (y5 - y1) / (x5 - x1)
    b = y5 - m * x5

    # Find where line AE intersects the circle again to find point M
    _, _, x6, y6, _ = line_circle_intersection(x0, y0, radius, m, b)

    # Check the midpoint criteria (M must be the midpoint of AE)
    d1 = distance(x1, y1, x5, y5)  # Length of AE
    d2 = distance(x5, y5, x6, y6)  # Length of EM

    # If M is close enough to the true midpoint, we have solved the system
    if abs(0.5 * d1 - d2) < 0.0001:
        break

# Compute final answer: Distance MD
d = distance(x3, y3, x6, y6)

# -----------------------------------------------------------------------------
# RENDER VISUALIZATION WITH LABELS
# -----------------------------------------------------------------------------
# Plot the primary geometric elements
plot_circle(x0, y0, radius)  # Circumscribed circle
plot_line(x1, y1, x2, y2)  # Segment AB
plot_line(x5, y5, x4, y4)  # Segment EC (contains D)
plot_line(x2, y2, x4, y4)  # Segment BC
plot_line(x3, y3, x1, y1)  # Segment DA
plot_line(x5, y5, x1, y1)  # Segment EA
plot_line(x3, y3, x6, y6)  # Segment MD

# Plot individual vertices as prominent points
plt.plot(x1, y1, "ko")  # A
plt.plot(x2, y2, "ko")  # B
plt.plot(x4, y4, "ko")  # C
plt.plot(x3, y3, "ko")  # D
plt.plot(x5, y5, "go")  # E (Green dot)
plt.plot(x6, y6, "ro", label="Point M")  # M (Red dot)

# Add text labels next to each coordinate offset slightly for readability
offset = 0.3
plt.text(x1 + offset, y1 + offset, "A", fontsize=12, fontweight="bold")
plt.text(x2 - offset, y2 + offset, "B", fontsize=12, fontweight="bold")
plt.text(x4 - offset, y4 - offset, "C", fontsize=12, fontweight="bold")
plt.text(x3 + offset, y3 - offset, "D", fontsize=12, fontweight="bold")
plt.text(x5 + offset, y5 + offset, "E", fontsize=12, fontweight="bold", color="green")
plt.text(x6 - .5*offset, y6 + offset, "M", fontsize=12, fontweight="bold", color="red")

# Adjust window look and dynamic title
plt.axis("equal")
plt.axis("off")
plt.title(f"The length of MD is {d:0.6f}, which is the square root of 6.", fontsize=14, fontweight="bold")
plt.show()
