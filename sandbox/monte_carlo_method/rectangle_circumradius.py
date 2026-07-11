# Jim McCleery
# July 10, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2025_256fdd
# -----------------------------------------------------------------------------

from math import sqrt
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
def plot_circle(x, y, radius):
    """Draws a full circle given its center coordinates (x, y) and a radius."""
    # Generate 1500 angles spaced evenly between 0 and 2*pi (a full circle)
    angle = np.linspace(0, 2 * np.pi, 1500)

    # Trigonometry translates angles into X and Y grid coordinates
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y

    # Tell matplotlib to draw the circle line
    plt.plot(x_arr, y_arr)


def plot_line(x1, y1, x2, y2):
    """Draws a straight line segment between point 1 (x1, y1) and point 2 (x2, y2)."""
    plt.plot([x1, x2], [y1, y2])


def circle_circle_intersections(x0, y0, r0, x1, y1, r1):
    """Return the intersection points of two circles.

    Returns:
        (x3, y3, x4, y4, True) if intersections exist
        (0, 0, 0, 0, False) otherwise
    """
    try:
        d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
        if d == 0:
            return 0, 0, 0, 0, False

        a = (r0**2 - r1**2 + d**2) / (2 * d)
        h = sqrt(max(0.0, r0**2 - a**2))  # Prevents domain errors if r0^2 < a^2

        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d

        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d

        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d

        return x3, y3, x4, y4, True

    except ZeroDivisionError:
        return 0, 0, 0, 0, False


# -----------------------------------------------------------------------------
# MAIN SIMULATION LOOP
# -----------------------------------------------------------------------------
while True:
    d = uniform(23, 25)
    x0, y0 = 0, 0
    x1, y1 = d, 0

    # Define rectangle vertices based on d
    x2, y2 = -5, 12
    x3, y3 = d + 9, 12
    x4, y4 = d + 9, -12
    x5, y5 = -5, -12

    # Get circle intersections
    x6, y6, xb, yb, success = circle_circle_intersections(
        x0, y0, 13, x1, y1, 15
    )

    if not success:
        continue

    # Check if lines from intersection point to top corners are perpendicular
    m1 = (y6 - y2) / (x6 - x2)
    m2 = (y6 - y3) / (x6 - x3)

    if abs(m1 * m2 + 1) < 1e-8:
        break

# Plot results
plt.plot(x6, y6, "o")

plot_circle(x0, y0, 13)
plot_circle(x1, y1, 15)

# Outer rectangle
plot_line(x2, y2, x3, y3)
plot_line(x3, y3, x4, y4)
plot_line(x4, y4, x5, y5)
plot_line(x5, y5, x2, y2)

# Rays from intersection point to rectangle corners
plot_line(x6, y6, x2, y2)
plot_line(x6, y6, x3, y3)
plot_line(x6, y6, x5, y5)
plot_line(x6, y6, x4, y4)

plt.axis("equal")
plt.axis("off")
plt.title(f"AB = {d + 14:0.5f}")
plt.show()
