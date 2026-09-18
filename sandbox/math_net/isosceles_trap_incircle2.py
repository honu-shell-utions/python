# -----------------------------------------------------------------------------
# Jim McCleery
# June 25, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2025_a7ad4d
# -----------------------------------------------------------------------------

from math import sqrt
import matplotlib.pyplot as plt
from random import uniform
import numpy as np


# -----------------------------------------------------------------------------
def line_circle_intersection(x1, y1, r, m, b):
    """
    Finds where a line (y = m*x + b) intersects a circle with center (x1, y1) and radius r.
    """
    try:
        A = 1 + m**2
        B = -2 * x1 + 2 * m * b - 2 * m * y1
        C = x1**2 + b**2 - 2 * b * y1 + y1**2 - r**2

        disc = B**2 - 4 * A * C
        disc = sqrt(disc)

        x2 = (-B - disc) / (2 * A)
        x3 = (-B + disc) / (2 * A)

        if x2 > x3:
            x2, x3 = x3, x2

        y2 = m * x2 + b
        y3 = m * x3 + b

        return x2, y2, x3, y3, True
    except:
        return 0, 0, 0, 0, False


# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """
    Calculates the straight-line distance between two coordinate points.
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# -----------------------------------------------------------------------------
def plot_circle(x, y, radius, start=0, stop=2 * np.pi):
    """
    Plots a circular path around a center point (x, y).
    """
    angles = np.linspace(start, stop, 1500)
    x_coordinates = radius * np.cos(angles) + x
    y_coordinates = radius * np.sin(angles) + y
    plt.plot(x_coordinates, y_coordinates)


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Plots a straight line segment from point 1 (x1, y1) to point 2 (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# MAIN SCRIPT EXECUTION
# -----------------------------------------------------------------------------

circle_radius = 3
center_x, center_y = 0, 0

# Fixed coordinates for the top and bottom circle tangent points from the diagram
kx, ky = 0, circle_radius       # Point K (Top tangent point)
mx, my = 0, -circle_radius      # Point M (Bottom tangent point)

while True:
    r = uniform(22.3, 22.5)
    s = 24 - r

    if r == s:
        continue

    # Assigning vertices based on the diagram labels
    x1, y1 = -r / 2, -circle_radius   # Point C (Bottom-Left)
    x2, y2 = r / 2, -circle_radius    # Point D (Bottom-Right)
    x3, y3 = s / 2, circle_radius     # (Top-Right vertex)
    x4, y4 = -s / 2, circle_radius    # Point B (Top-Left)

    # Calculate line equation for the left side of the trapezoid (Line CB)
    slope = (y4 - y1) / (x4 - x1)
    y_intercept = y1 - slope * x1

    # xa, ya will converge onto Point L (Left tangent point) when tangent
    xa, ya, xb, yb, is_intersecting = line_circle_intersection(
        center_x, center_y, circle_radius, slope, y_intercept
    )

    if not is_intersecting:
        continue

    # Break loop when the line is perfectly tangent to the circle at point L
    if distance(xa, ya, xb, yb) < 0.001:
        # Due to symmetry, Point N is the horizontal reflection of Point L
        nx, ny = -xa, ya              # Point N (Right tangent point)
        break

# --- Plotting and Labeling the Diagram Points ---

# Draw the geometric shapes
plot_circle(center_x, center_y, circle_radius)
plot_line(x1, y1, x2, y2)  # Side CD
plot_line(x3, y3, x2, y2)  # Side AD
plot_line(x3, y3, x4, y4)  # Side AB
plot_line(x1, y1, x4, y4)  # Side CB

# Visual labels for the diagram points
plt.plot(x1, y1, 'ko') \
    and plt.text(x1, y1 - 0.4, 'C', fontsize=12, ha='center')   # Point C
plt.plot(x2, y2, 'ko') \
    and plt.text(x2, y2 - 0.4, 'D', fontsize=12, ha='center')   # Point D
plt.plot(kx, ky, 'ko') \
    and plt.text(kx, ky + 0.2, 'K', fontsize=12, ha='center')   # Point K
plt.plot(mx, my, 'ko') \
    and plt.text(mx, my - 0.4, 'M', fontsize=12, ha='center')   # Point M
plt.plot(xa, ya, 'ko') \
    and plt.text(xa - 0.3, ya, 'L', fontsize=12, va='center')   # Point L
plt.plot(nx, ny, 'ko') \
    and plt.text(nx + 0.3, ny, 'N', fontsize=12, va='center')   # Point N

# Formatting the output graph
plt.axis("equal")
plt.axis("off")
plt.title(f"r^2 + s^2 = {r**2 + s**2:0.2f}")

plt.show()
