"""
Monte Carlo approximation of pi

Based on a geometry problem from Andy Math:
https://youtu.be/4D6M0ndbgjE?si=ddWso1Q2Zsq364wV

Idea
----
Throw random "darts" at the square [-1,1] x [-1,1], which has area 4.

The unit circle x^2 + y^2 = 1 is inscribed in that square and has area pi.

So, if we throw many random points into the square, the fraction that land
inside the circle should be approximately:

    area of circle / area of square = pi / 4

Therefore,

    pi ≈ 4 * (hits / throws)

Jim McCleery
April 1, 2026
Kona, HI
"""

from math import pi
from random import uniform

import numpy as np
import matplotlib.pyplot as plt


# ---------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Draw a line segment from (x1, y1) to (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2], linewidth=1)


# ---------------------------------------------------------------------
def plot_circle(cx, cy, radius, start=0, stop=2 * pi, num_points=600):
    """
    Draw a circle or circular arc.

    Parameters
    ----------
    cx, cy : float
        Center of the circle.
    radius : float
        Radius of the circle.
    start, stop : float
        Starting and ending angles in radians.
    num_points : int
        Number of sample points used to draw the curve.
    """
    theta = np.linspace(start, stop, num_points)
    x_vals = cx + radius * np.cos(theta)
    y_vals = cy + radius * np.sin(theta)
    plt.plot(x_vals, y_vals, linewidth=1.5)


# ---------------------------------------------------------------------
def draw_square():
    """
    Draw the boundary of the square from (-1, -1) to (1, 1).

    This square has side length 2, so its area is 4.
    """
    plot_line(-1, -1, 1, -1)
    plot_line(1, -1, 1, 1)
    plot_line(1, 1, -1, 1)
    plot_line(-1, 1, -1, -1)


# ---------------------------------------------------------------------
def run_monte_carlo_pi_demo(num_throws=10**3, pause_time=0.02):
    """
    Animate a Monte Carlo estimate of pi.

    Parameters
    ----------
    num_throws : int
        Number of random points to throw.
    pause_time : float
        Delay between frames so the animation can be watched.
    """
    hits = 0

    for throw_number in range(1, num_throws + 1):
        # Pick a random point uniformly from the square [-1,1] x [-1,1].
        x = uniform(-1, 1)
        y = uniform(-1, 1)
        plot_line(-1, -1, 1, -1)  # Bottom edge of the square
        plot_line(1, -1, 1, 1)  # Right edge
        plot_line(1, 1, -1, 1)  # Top edge
        plot_line(-1, 1, -1, -1)  # Left edge
        plot_circle(0, 0, 1)  # Unit circle centered at the origin
        # A point is inside the unit circle if x^2 + y^2 < 1.
        if x**2 + y**2 < 1:
            hits += 1
            plt.plot(x, y, "go", markersize=3)  # Green dot = hit

        # Monte Carlo estimate:
        # fraction inside circle ≈ pi / 4
        pi_estimate = 4 * hits / throw_number

        plt.axis("equal")
        plt.xlim(-1.1, 1.1)
        plt.ylim(-1.1, 1.1)
        plt.title(
            f"Pi approximation after {throw_number} throws: {pi_estimate:.5f}"
        )

        plt.pause(pause_time)

    plt.show()


# ---------------------------------------------------------------------
#change the number of throws and pause time to see how the approximation evolves
run_monte_carlo_pi_demo(num_throws=10**3, pause_time=0.025)
# ---------------------------------------------------------------------