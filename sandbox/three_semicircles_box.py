"""
Graphical illustration for a Mind Your Decisions geometry problem.

Video:
https://youtu.be/YNxtkBAQfaE?si=PUSi5GLg6uC0kM6x

The key result is that the shaded area is always pi.

Jim McCleery
March 29, 2026
Kona, HI
"""

from math import pi
from random import uniform

import numpy as np
import matplotlib.pyplot as plt


def plot_line(x1, y1, x2, y2):
    """Plot a line segment between two points."""
    plt.plot([x1, x2], [y1, y2], color="black")


def plot_partial_circle(cx, cy, radius, start_angle, stop_angle):
    """
    Plot a circular arc.

    Parameters
    ----------
    cx, cy : float
        Center of the circle.
    radius : float
        Radius of the circle.
    start_angle, stop_angle : float
        Start and stop angles in radians.
    """
    theta = np.linspace(start_angle, stop_angle, 1000)
    x = cx + radius * np.cos(theta)
    y = cy + radius * np.sin(theta)
    plt.plot(x, y, color="black")


# ---------------------------------------------------------------------
# Geometry behind the result
#
# Let:
#   R = radius of the medium semicircle
#   r = radius of the small semicircle
#
# The quarter-circle has radius 2r.
# From the diagram, the rectangle has dimensions 2R by 2r and area 4,
# so:
#
#   (2R)(2r) = 4
#   Rr = 1
#
# The large semicircle has diameter 2R + 2r, so its radius is R + r.
#
# Desired shaded area:
#
#   A = area(large semicircle)
#       - area(medium semicircle)
#       - area(small semicircle)
#
#     = (pi/2)(R + r)^2 - (pi/2)R^2 - (pi/2)r^2
#     = (pi/2)(R^2 + 2Rr + r^2 - R^2 - r^2)
#     = (pi/2)(2Rr)
#     = pi(Rr)
#     = pi
#
# So the shaded area is constant and always equals pi.
# ---------------------------------------------------------------------


num_frames = 50          # Number of random examples to display
samples_per_frame = 10_000  # Monte Carlo points used to visually fill the region

for frame in range(num_frames):
    # Pick any positive R in a reasonable display range.
    # Since Rr = 1, r is determined by r = 1 / R.
    R = uniform(1, 3)
    r = 1 / R

    # Important points in the figure
    # (chosen to match the original construction)
    x0, y0 = 0, 0               # corner where the quarter-circle is centered
    x1, y1 = r, 0               # center of the small semicircle
    x2, y2 = -R, 0              # center of the medium semicircle
    x3, y3 = 0, -2 * r
    x4, y4 = -2 * R, -2 * r
    x5, y5 = -2 * R, 0
    x6, y6 = 2 * r, 0
    x7, y7 = x1 - R, 0          # center of the large semicircle

    # Randomly sample points and plot those in the shaded region.
    # A point is shaded if it lies:
    #   inside the large semicircle,
    #   outside the medium semicircle,
    #   outside the small semicircle.
    for _ in range(samples_per_frame):
        x = uniform(x5, x1 + r)
        y = uniform(0, R + r)

        in_large_semicircle = (x - x7) ** 2 + (y - y7) ** 2 < (R + r) ** 2
        in_medium_semicircle = (x - x2) ** 2 + (y - y2) ** 2 < R ** 2
        in_small_semicircle = (x - x1) ** 2 + (y - y1) ** 2 < r ** 2

        if in_large_semicircle and not in_medium_semicircle and not in_small_semicircle:
            plt.plot(x, y, ".", color="tab:blue", markersize=2)

    # Label the rectangle area shown in the puzzle.
    plt.text(x2, -r, "4")

    # Optional marker at the center of the large semicircle
    plt.plot(x7, y7, "o", color="black", markersize=4)

    # Draw the straight edges
    plot_line(x5, y5, x6, y6)
    plot_line(x0, y0, x3, y3)
    plot_line(x3, y3, x4, y4)
    plot_line(x5, y5, x4, y4)

    # Draw the arcs
    plot_partial_circle(x7, y7, R + r, 0, pi)            # large semicircle
    plot_partial_circle(x1, y1, r, 0, pi)                # small semicircle
    plot_partial_circle(x2, y2, R, 0, pi)                # medium semicircle
    plot_partial_circle(x0, y0, 2 * r, 3 * pi / 2, 2 * pi)  # quarter-circle

    plt.title(f"Shaded Area = {pi}")
    plt.axis("equal")
    plt.pause(0.5)

    if frame < num_frames - 1:
        plt.cla()

plt.show()
