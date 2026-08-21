# Jim McCleery
# August 20, 2026
# Kailua-Kona, HI
#
# https://youtu.be/X-IrZQLQJXU?si=nGu6cs_5X1Tie-2d
#
# -----------------------------------------------------------------------------
# A right triangle has legs of length 1 and 2.
#
# A circle is tangent to the two perpendicular sides AB and BC.
# Its center O also lies on the hypotenuse AC.
#
# The program draws the figure and uses random points to illustrate
# the green shaded region outside the circle but inside the triangle.
# -----------------------------------------------------------------------------

from math import pi
from random import uniform

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Helper functions
# -----------------------------------------------------------------------------

def plot_line(x1, y1, x2, y2):
    """Draw a line segment between two points."""
    plt.plot([x1, x2], [y1, y2], color="blue", linewidth=3)


def plot_circle(center_x, center_y, radius):
    """Draw a circle with the given center and radius."""

    # np.linspace creates many angles from 0 to 2*pi.
    theta = np.linspace(0, 2 * pi, 500)

    # Convert each angle into an x- and y-coordinate on the circle.
    x = center_x + radius * np.cos(theta)
    y = center_y + radius * np.sin(theta)

    plt.plot(x, y, color="black", linewidth=2)


# -----------------------------------------------------------------------------
# Coordinates from the diagram
# -----------------------------------------------------------------------------

# Triangle vertices
A = (0, 0)
B = (0, -1)
C = (2, -1)

# The circle's radius.
#
# The center must be r units from both AB and BC, so its coordinates are
#
#       O = (r, -1 + r)
#
# The hypotenuse AC has equation
#
#       y = -x / 2
#
# Since O lies on AC:
#
#       r - 1 = -r / 2
#
# which gives r = 2/3.

r = 2 / 3

# Circle center
O = (r, r - 1)

# Tangent point on the vertical side AB
T = (0, r - 1)

# Tangent point on the horizontal side BC
P = (r, -1)


# Give the individual coordinates convenient names.
xA, yA = A
xB, yB = B
xC, yC = C
xO, yO = O
xT, yT = T
xP, yP = P


# -----------------------------------------------------------------------------
# Calculate the shaded area
# -----------------------------------------------------------------------------

# Area of the right triangle:
#
#       1/2 * base * height
#     = 1/2 * 2 * 1
#     = 1
#
triangle_area = 1

# The portion of the circle inside the triangle is one-half of the circle.
semicircle_area = pi * r**2 / 2

# Therefore the green area is:
shaded_area = triangle_area - semicircle_area


# -----------------------------------------------------------------------------
# Draw the triangle
# -----------------------------------------------------------------------------

plot_line(xA, yA, xB, yB)     # AB
plot_line(xB, yB, xC, yC)     # BC
plot_line(xA, yA, xC, yC)     # AC


# -----------------------------------------------------------------------------
# Draw the circle
# -----------------------------------------------------------------------------

plot_circle(xO, yO, r)

# Mark the center of the circle.
plt.plot(xO, yO, "ko")


# -----------------------------------------------------------------------------
# Monte Carlo illustration of the shaded region
# -----------------------------------------------------------------------------

# Random points are generated inside the rectangle
#
#       0 <= x <= 2
#      -1 <= y <= 0
#
# Only points that are:
#
#   1. inside triangle ABC, and
#   2. outside the circle
#
# are plotted.
#
throws = 20_000

for _ in range(throws):

    # Choose a random point in the surrounding rectangle.
    x = uniform(0, 2)
    y = uniform(-1, 0)

    # The hypotenuse AC has equation y = -x/2.
    #
    # Points below this line are inside the triangle.
    in_triangle = y < -x / 2

    # Circle equation:
    #
    #       (x - xO)^2 + (y - yO)^2 = r^2
    #
    # A point is outside the circle when its squared distance from
    # the center is greater than r^2.
    outside_circle = (
        (x - xO)**2 + (y - yO)**2 > r**2
    )

    # Plot only points belonging to the shaded region.
    if in_triangle and outside_circle:
        plt.plot(x, y, ".", color="limegreen", markersize=1)


# -----------------------------------------------------------------------------
# Add point and coordinate labels
# -----------------------------------------------------------------------------

plt.text(xA - 0.12, yA + 0.04, "A (0, 0)", fontsize=11)
plt.text(xB - 0.17, yB - 0.08, "B (0, -1)", fontsize=11)
plt.text(xC + 0.03, yC - 0.05, "C (2, -1)", fontsize=11)

plt.text(
    xO + 0.05,
    yO + 0.04,
    "O (2/3, -1/3)",
    fontsize=11
)

plt.text(
    xT - 0.36,
    yT,
    "T (0, -1/3)",
    fontsize=11
)

plt.text(
    xP - 0.12,
    yP - 0.10,
    "P (2/3, -1)",
    fontsize=11
)


# -----------------------------------------------------------------------------
# Finish the graph
# -----------------------------------------------------------------------------

plt.title(
    f"The shaded area is {shaded_area:.6f}\n"
    r"$1-\frac{\pi}{2}\left(\frac{2}{3}\right)^2"
    r"=1-\frac{2\pi}{9}$"
)

# Make one unit on the x-axis the same physical size as one unit on the y-axis.
plt.axis("equal")

# Leave some extra room so the coordinate labels are visible.
plt.xlim(-0.45, 2.25)
plt.ylim(-1.20, 0.55)

# Hide the usual graph axes and tick marks.
plt.axis("off")

plt.show()
