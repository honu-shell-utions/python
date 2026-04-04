"""
Jim McCleery
April 4, 2026
Kailua-Kona, HI

# Python solution to Math Booster problem
# Video: https://youtu.be/3uXL68wH1d8?si=4fPTDvVFj3mJbiEu
#
# This program explores an alternative solution numerically.
# It uses Python both to investigate the geometry and to draw the figure.
#
# Jim McCleery
# April 4, 2026
# Kona, HI
"""

from math import pi, sqrt, sin, cos, tan
from random import uniform

import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Drawing helpers
# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Draw the line segment joining (x1, y1) to (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2], color="black")


def plot_circle(cx, cy, radius, start_angle=0, end_angle=2 * pi):
    """
    Draw part of a circle centered at (cx, cy).

    Parameters
    ----------
    cx, cy : float
        Coordinates of the center.
    radius : float
        Radius of the circle.
    start_angle, end_angle : float
        Initial and terminal angles in radians.
    """
    angles = np.linspace(start_angle, end_angle, 1200)
    x_values = cx + radius * np.cos(angles)
    y_values = cy + radius * np.sin(angles)
    plt.plot(x_values, y_values, color="black")


# -----------------------------------------------------------------------------
# Main geometric experiment
# -----------------------------------------------------------------------------
def main():
    """
    Search numerically for an angle theta that makes two lines perpendicular.

    Geometry used in the experiment
    -------------------------------
    We construct several points on and around a semicircle:

        O  = center of the circle
        A  = right endpoint of the diameter
        B  = another point on the circle
        C  = a third point on the circle
        D  = left endpoint of the diameter
        E  = a point located 7 units from D in the direction theta

    The program repeatedly chooses a random angle theta in (0, pi/2),
    computes the corresponding radius r from the given formula, and then
    checks whether line CE is perpendicular to the line through O making
    angle theta with the positive x-axis.

    Once such a theta is found numerically, the figure is drawn.
    """

    # We will keep trying random values of theta until the perpendicularity
    # condition is satisfied to within a small numerical tolerance.
    tolerance = 1e-5

    while True:
        # Choose a random angle theta in the first quadrant.
        theta = uniform(0, pi / 2)

        # The radius comes from the problem's geometry.
        #
        # Using the identity cos(2 theta), the given formula is:
        #
        #     r = 22 / sqrt(2 + 2 cos(2 theta))
        #
        # This is taken directly from the underlying geometric relations.
        radius = 22 / sqrt(2 + 2 * cos(2 * theta))

        # Center of the circle.
        O_x, O_y = 0, 0

        # Right endpoint of the diameter.
        A_x, A_y = radius, 0

        # Another point on the circle at angle 2 theta.
        B_x = radius * cos(2 * theta)
        B_y = radius * sin(2 * theta)

        # A third point on the circle at angle (2 pi + 2 theta) / 3.
        C_x = radius * cos((2 * pi + 2 * theta) / 3)
        C_y = radius * sin((2 * pi + 2 * theta) / 3)

        # Left endpoint of the diameter.
        D_x, D_y = -radius, 0

        # Point E is placed 7 units from D in direction theta.
        E_x = D_x + 7 * cos(theta)
        E_y = 7 * sin(theta)

        # Slope of line CE.
        slope_CE = (C_y - E_y) / (C_x - E_x)

        # Slope of the ray making angle theta with the positive x-axis.
        slope_theta = tan(theta)

        # Two nonvertical lines are perpendicular exactly when
        #     m1 * m2 = -1.
        #
        # Because we are doing floating-point computation, we allow a small
        # tolerance rather than demanding exact equality.
        if abs(slope_CE * slope_theta + 1) < tolerance:
            break

    # -------------------------------------------------------------------------
    # Draw the final figure
    # -------------------------------------------------------------------------
    plot_circle(O_x, O_y, radius, 0, pi)      # upper semicircle
    plot_line(D_x, D_y, A_x, A_y)             # diameter
    plot_line(D_x, D_y, B_x, B_y)             # segment DB
    plot_line(E_x, E_y, C_x, C_y)             # segment EC

    # Label the length 7 near segment DE.
    label1_x = (E_x + D_x) / 2
    label1_y = (E_y + D_y) / 2 - 1
    plt.text(label1_x, label1_y, "7")

    # Label the length 15 near segment EB/related position used in the sketch.
    label2_x = (E_x + B_x) / 2
    label2_y = (E_y + B_y) / 2 - 1
    plt.text(label2_x, label2_y, "15")

    plt.title(f"Radius of Circle = {radius:.3f}")
    plt.axis("equal")
    plt.show()


# -----------------------------------------------------------------------------
# Run the program
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
