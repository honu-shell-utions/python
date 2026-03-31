"""
Interactive geometry drawing for a rectangle and two tangent circles

Change the values of:
    R
    r
    height

and rerun the program to see a new figure.

The program computes the rectangle width x so that:
- a circle of radius R sits in the lower-left corner
- a circle of radius r sits in the upper-right corner
- the two circles are tangent

Jim McCleery
March 28, 2026
Kona, HI
"""

from math import pi, sqrt
import numpy as np
import matplotlib.pyplot as plt


def plot_line(x1, y1, x2, y2):
    """
    Draw the line segment joining two points.
    """
    plt.plot([x1, x2], [y1, y2], color="black")


def plot_circle(center_x, center_y, radius, start=0, stop=2 * pi, num_points=1000):
    """
    Draw a circle (or part of a circle).

    The circle is approximated by many closely spaced points.
    """
    theta = np.linspace(start, stop, num_points)
    x_vals = center_x + radius * np.cos(theta)
    y_vals = center_y + radius * np.sin(theta)
    plt.plot(x_vals, y_vals, color="black")


def compute_width(R, r, height):
    """
    Compute the rectangle width x.

    Geometry:
    - Large circle center: (R, R)
    - Small circle center: (x - r, height - r)

    Since the circles are tangent, the distance between centers is R + r.

    So:
        (R + r)^2 = (x - R - r)^2 + (height - R - r)^2

    Therefore:
        (x - R - r)^2 = (R + r)^2 - (height - R - r)^2

    If the right-hand side is negative, there is no real solution.
    """
    horizontal_squared = (R + r) ** 2 - (height - R - r) ** 2

    if horizontal_squared < 0:
        return None

    x = R + r + sqrt(horizontal_squared)
    return x


# ---------------------------------------------------------------------
# Student inputs: change these values and rerun
# ---------------------------------------------------------------------

R = 8
r = 5
height = 20


# ---------------------------------------------------------------------
# Compute the width
# ---------------------------------------------------------------------

x = compute_width(R, r, height)

if x is None:
    print("No real rectangle width exists for these values.")
    print("The circles are too far apart vertically to be tangent.")
    print(f"R = {R}, r = {r}, height = {height}")
else:
    # -----------------------------------------------------------------
    # Explain the calculation
    # -----------------------------------------------------------------
    #
    # Large circle center: (R, R)
    # Small circle center: (x - r, height - r)
    #
    # Tangency means:
    #     distance between centers = R + r
    #
    # So:
    #     (R + r)^2 = (x - R - r)^2 + (height - R - r)^2
    #
    # which gives:
    #     x = R + r + sqrt((R + r)^2 - (height - R - r)^2)
    # -----------------------------------------------------------------

    print(f"R = {R}")
    print(f"r = {r}")
    print(f"height = {height}")
    print(f"width x = {x:.6f}")

    # Rectangle corners
    bottom_left = (0, 0)
    bottom_right = (x, 0)
    top_right = (x, height)
    top_left = (0, height)

    # Draw rectangle
    plot_line(*bottom_left, *bottom_right)
    plot_line(*bottom_right, *top_right)
    plot_line(*top_right, *top_left)
    plot_line(*top_left, *bottom_left)

    # Draw circles
    plot_circle(R, R, R)
    plot_circle(x - r, height - r, r)

    # Labels
    plt.text(-0.8, height / 2, f"{height}")
    plt.text(R - 1.2, R, f"R = {R}")
    plt.text(x - r - 1.2, height - r, f"r = {r}")

    # Title and formatting
    plt.title(f"Rectangle width x = {x:.3f}")
    plt.axis("equal")
    plt.show()