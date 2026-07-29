# Jim McCleery
# July 29, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2025_256fdd

from math import sqrt
import matplotlib.pyplot as plt
import numpy as np
from random import uniform


# -----------------------------------------------------------------------------
# FUNCTION DEFINITIONS
# -----------------------------------------------------------------------------
def circle_circle_intersections(x0, y0, r0, x1, y1, r1):
    """
    Calculate and return the intersection points of two circles.

    Parameters:
        (x0, y0), r0 : Center and radius of the first circle.
        (x1, y1), r1 : Center and radius of the second circle.

    Returns:
        (x3, y3, x4, y4, True) if intersections exist, otherwise (0, 0, 0, 0, False).
    """
    try:
        # Distance between the two circle centers
        d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

        # Distance from center 0 to the midpoint line connecting intersection points
        a = (r0**2 - r1**2 + d**2) / (2 * d)

        # Half-distance between the two intersection points
        h = sqrt(r0**2 - a**2)

        # Midpoint coordinate between the two intersection points
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d

        # Calculate coordinates of both intersection points
        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d
        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d

        return x3, y3, x4, y4, True
    except ZeroDivisionError:
        # Returns False if circles are concentric or distance calculations fail
        return 0, 0, 0, 0, False


def plot_circle(x, y, radius):
    """
    Plots a circle given its center (x, y) and radius using a dashed line style.
    """
    # Create an array of 1,500 evenly spaced angles from 0 to 2*pi (a full turn)
    angles = np.linspace(0, 2 * np.pi, 1500)

    # Convert polar coordinates (radius & angle) to Cartesian coordinates (x & y)
    x_coords = radius * np.cos(angles) + x
    y_coords = radius * np.sin(angles) + y

    # Plot the circle using a dotted style to match geometric diagrams
    plt.plot(x_coords, y_coords, linestyle=":", color="gray")


def plot_line(x1, y1, x2, y2, color="black", linestyle="-"):
    """
    Plots a straight line segment between point (x1, y1) and point (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2], color=color, linestyle=linestyle)


# -----------------------------------------------------------------------------
# MAIN CALCULATION / SIMULATION LOOP
# -----------------------------------------------------------------------------
# Goal: Find the side length AB of rectangle ABCD such that line segments
# AX and BX are perpendicular (forming a 90-degree angle at X).
while True:
    # Randomly pick a trial length for side AB between 38 and 40
    AB = uniform(38, 40)

    # Coordinates of rectangle ABCD corners:
    # A is at the top-left origin (0, 0)
    xA, yA = 0, 0
    # B is top-right (AB, 0)
    xB, yB = AB, 0
    # C is bottom-right (AB, -24)
    xC, yC = AB, -24
    # D is bottom-left (0, -24)
    xD, yD = 0, -24

    # Center coordinates for circle O1 and circle O2
    xO1, yO1 = 5, -12
    xO2, yO2 = AB - 9, -12

    # Find intersection X between circle O1 (radius 13) and circle O2 (radius 15)
    # circle_circle_intersections returns 2 points; we take the lower point (xX, yX)
    xX, yX, _, _, ok = circle_circle_intersections(xO1, yO1, 13, xO2, yO2, 15)

    # Calculate slopes of lines AX and BX
    slope_AX = (yX - yA) / (xX - xA)
    slope_BX = (yX - yB) / (xX - xB)

    # Two lines are perpendicular if the product of their slopes equals -1.
    # Check if (slope_AX * slope_BX + 1) is close enough to 0:
    if abs(slope_AX * slope_BX + 1) < 0.00001:
        break  # Solution found!


# -----------------------------------------------------------------------------
# ADDITIONAL POINT CALCULATIONS FOR LABELS
# -----------------------------------------------------------------------------
# P1 is directly above O1 on the top edge AB
xP1, yP1 = xO1, 0

# P2 is directly above O2 on the top edge AB
xP2, yP2 = xO2, 0

# M is the intersection of the circles on top edge AB
xM, yM = (xA + xB) / 2, 0


# -----------------------------------------------------------------------------
# DRAWING AND PLOTTING FIGURES
# -----------------------------------------------------------------------------
plt.figure(figsize=(9, 6))

# Plot rectangle sides
plot_line(xA, yA, xB, yB)  # AB
plot_line(xB, yB, xC, yC)  # BC
plot_line(xC, yC, xD, yD)  # CD
plot_line(xD, yD, xA, yA)  # DA

# Plot lines connecting center points O1 and O2
plot_line(xO1, yO1, xO2, yO2)

# Plot blue lines forming right angle at X
plot_line(xA, yA, xX, yX, color="blue")
plot_line(xB, yB, xX, yX, color="blue")

# Plot dashed red lines showing circle radii to projection points
plot_line(xO1, yO1, xP1, yP1, color="red", linestyle="--")
plot_line(xO2, yO2, xP2, yP2, color="red", linestyle="--")

# Plot green lines to intersection point M
plot_line(xO1, yO1, xM, yM, color="green")
plot_line(xO2, yO2, xM, yM, color="green")

# Plot circles O1 and O2
plot_circle(xO1, yO1, 13)
plot_circle(xO2, yO2, 15)

# -----------------------------------------------------------------------------
# LABELS AND ANNOTATIONS (Matching the target image)
# -----------------------------------------------------------------------------
# Plot point markers
points_x = [xA, xB, xC, xD, xO1, xO2, xP1, xP2, xM, xX]
points_y = [yA, yB, yC, yD, yO1, yO2, yP1, yP2, yM, yX]
plt.scatter(points_x, points_y, color="black", s=20, zorder=5)

# Label text placements
plt.text(xA - 1.0, yA + 0.5, "$A$", fontsize=12, fontweight="bold")
plt.text(xB + 0.5, yB + 0.5, "$B$", fontsize=12, fontweight="bold")
plt.text(xC + 0.5, yC - 1.2, "$C$", fontsize=12, fontweight="bold")
plt.text(xD - 1.0, yD - 1.2, "$D$", fontsize=12, fontweight="bold")

plt.text(xO1 - 1.5, yO1 - 0.5, "$O_1$", fontsize=12, fontweight="bold")
plt.text(xO2 + 0.5, yO2 - 0.5, "$O_2$", fontsize=12, fontweight="bold")

plt.text(xP1 - 0.4, yP1 + 0.8, "$P_1$", fontsize=12, fontweight="bold")
plt.text(xP2 - 0.4, yP2 + 0.8, "$P_2$", fontsize=12, fontweight="bold")
plt.text(xM - 0.4, yM + 0.8, "$M$", fontsize=12, fontweight="bold")

plt.text(xX - 0.3, yX - 1.5, "$X$", fontsize=12, fontweight="bold")

# Formatting output display
plt.title(f"The side AB = {AB:0.5f}", fontsize=14)
plt.axis("equal")
plt.axis("off")
plt.show()
