# Jim McCleery
# April 2, 2026
# Kailua-Kona, HI
#
# Python solution to Total Red Area from AndyMath
# Video: https://youtu.be/9N8g8s5Mf2w?si=T1lXXu8ciWc6V8vB
#
# This program explores an alternative solution numerically.
# It uses Python both to investigate the geometry and to draw the figure.


from math import pi, sqrt
from random import uniform
import numpy as np
import matplotlib.pyplot as plt


def distance(x1, y1, x2, y2):
    """
    Return the Euclidean distance between two points (x1, y1) and (x2, y2).
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def plot_line(x1, y1, x2, y2):
    """
    Draw the line segment joining two points.
    """
    plt.plot([x1, x2], [y1, y2], color="black")


def plot_circle(cx, cy, radius, start=0, stop=2 * pi):
    """
    Draw a circular arc.

    Parameters
    ----------
    cx, cy : float
        Coordinates of the center.
    radius : float
        Radius of the circle.
    start, stop : float
        Starting and ending angles in radians.
    """
    angles = np.linspace(start, stop, 1000)
    x_vals = cx + radius * np.cos(angles)
    y_vals = cy + radius * np.sin(angles)
    plt.plot(x_vals, y_vals, color="black")


def main():
    """
    Construct the figure, plot the red region numerically, and display
    the exact red area.
    """

    # -------------------------------------------------------------------------
    # Step 1. Determine the fixed radius r1.
    #
    # The two side semicircles each have area 36, so together they form
    # one full circle of area 72:
    #
    #     pi * r1^2 = 72
    #
    # Therefore:
    #
    #     r1 = sqrt(72 / pi)
    #
    # The enclosing rectangle has height 2*r1.
    # -------------------------------------------------------------------------
    r1 = sqrt(72 / pi)
    height = 2 * r1

    # -------------------------------------------------------------------------
    # Step 2. Search numerically for the rectangle width.
    #
    # Let:
    #   r2 = width / 2              be the radius of the bottom semicircle
    #   r3 = (width - 2*r1) / 2     be the radius of the upper-left semicircle
    #
    # The correct width is the one for which these two circles are tangent.
    # Tangency occurs when the distance between their centers equals r2 + r3.
    # -------------------------------------------------------------------------
    while True:
        width = uniform(2 * r1, 4 * r1)

        r2 = width / 2
        r3 = (width - 2 * r1) / 2

        # Rectangle corners
        x0, y0 = 0, 0
        x1, y1 = width, 0
        x2, y2 = width, height
        x3, y3 = 0, height

        # Centers of the circular arcs
        x4, y4 = width / 2, 0         # bottom semicircle
        x5, y5 = width - r1, height   # top-right semicircle
        x6, y6 = r3, height           # upper-left inner semicircle
        x7, y7 = 0, height / 2        # left semicircle
        x8, y8 = width, height / 2    # right semicircle

        d = distance(x4, y4, x6, y6)

        if abs(d - (r2 + r3)) < 1e-4:
            break

    # -------------------------------------------------------------------------
    # Step 3. Draw the outer rectangle and the five circular arcs.
    # -------------------------------------------------------------------------
    plot_line(x0, y0, x1, y1)
    plot_line(x1, y1, x2, y2)
    plot_line(x2, y2, x3, y3)
    plot_line(x3, y3, x0, y0)

    plot_circle(x4, y4, r2, 0, pi)               # bottom semicircle
    plot_circle(x5, y5, r1, 0, pi)               # top-right semicircle
    plot_circle(x6, y6, r3, 0, -pi)              # upper-left inner semicircle
    plot_circle(x7, y7, r1, pi / 2, 3 * pi / 2)  # left semicircle
    plot_circle(x8, y8, r1, -pi / 2, pi / 2)     # right semicircle

    # -------------------------------------------------------------------------
    # Step 4. Shade the red region by random sampling.
    #
    # This is only for visualization.  The exact area is computed below.
    #
    # A sampled point is colored red if it lies inside either:
    #   (1) the bottom semicircle of radius r2, or
    #   (2) the upper-left semicircle of radius r3.
    # -------------------------------------------------------------------------
    for _ in range(10**5):
        x = uniform(0, width)
        y = uniform(0, height)

        in_bottom_circle = (x - x4) ** 2 + (y - y4) ** 2 < r2 ** 2
        in_upper_left_circle = (x - x6) ** 2 + (y - y6) ** 2 < r3 ** 2

        if in_bottom_circle or in_upper_left_circle:
            plt.plot(x, y, ".", color="tab:red", markersize=2)

    # -------------------------------------------------------------------------
    # Step 5. Compute the exact red area.
    #
    # The red region is the union of two semicircles, so:
    #
    #     red area = (pi / 2) * (r2^2 + r3^2)
    # -------------------------------------------------------------------------
    red_area = (pi / 2) * (r2 ** 2 + r3 ** 2)

    plt.title("Red Area = " + str(round(red_area, 3)))
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    main()
