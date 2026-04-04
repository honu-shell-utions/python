
"""
Estimate the shaded red area from the MindYourDecisions problem
using a Monte Carlo simulation.

Video:
https://youtu.be/ouc6iX4dlMw?si=rcrGMFD60QXKhqWA

Author: Jim McCleery
Date: March 30, 2026
Location: Kona, HI

Approach
--------
We sample random points uniformly in the 2 x 2 square in the first quadrant.

A sampled point is considered only if it lies inside the quarter-circle
of radius 2 centered at the origin.

Within that quarter-circle, the shaded region is the set of points that are:
    - inside both semicircles, or
    - outside both semicircles

So this is an XOR-style boundary problem, except the shaded region is where
membership in the two semicircles matches.
"""

from math import pi
from random import uniform

import numpy as np
import matplotlib.pyplot as plt


def plot_line(x1, y1, x2, y2):
    """Plot a line segment between two points."""
    plt.plot([x1, x2], [y1, y2], "k-")


def plot_partial_circle(cx, cy, radius, start_angle, stop_angle, num_points=800):
    """
    Plot a circular arc.

    Parameters
    ----------
    cx, cy : float
        Center of the circle.
    radius : float
        Circle radius.
    start_angle, stop_angle : float
        Start and stop angles in radians.
    num_points : int
        Number of points used to draw the arc.
    """
    angles = np.linspace(start_angle, stop_angle, num_points)
    x = cx + radius * np.cos(angles)
    y = cy + radius * np.sin(angles)
    plt.plot(x, y, "k-")


def main():
    """Run the Monte Carlo simulation and display the geometry."""
    # ------------------------------------------------------------------
    # Key geometry points
    # ------------------------------------------------------------------
    # Quarter-circle center
    x0, y0 = 0, 0

    # Center of the bottom semicircle
    x1, y1 = 1, 0

    # Endpoints for the horizontal radius / boundary
    x2, y2 = 2, 0

    # Endpoints for the vertical radius / boundary
    x3, y3 = 0, 2

    # Center of the left semicircle
    x4, y4 = 0, 1

    # ------------------------------------------------------------------
    # Draw the fixed geometry
    # ------------------------------------------------------------------
    # Quarter-circle of radius 2 in the first quadrant
    plot_partial_circle(x0, y0, 2, 0, pi / 2)

    # Bottom semicircle of radius 1 centered at (1, 0)
    plot_partial_circle(x1, y1, 1, 0, pi)

    # Left semicircle of radius 1 centered at (0, 1)
    plot_partial_circle(x4, y4, 1, -pi / 2, pi / 2)

    # Bounding radii of the quarter-circle
    plot_line(x0, y0, x2, y2)
    plot_line(x0, y0, x3, y3)

    # ------------------------------------------------------------------
    # Monte Carlo sampling
    # ------------------------------------------------------------------
    # We sample uniformly in the 2x2 square [0, 2] x [0, 2].
    # The area of this square is 4, so:
    #
    #   estimated shaded area = (hits / throws) * 4
    #
    # Points outside the quarter-circle are simply ignored, but they still
    # count as part of the uniform sampling over the full square.
    throws = 100_000
    hits = 0

    for _ in range(throws):
        x = uniform(0, 2)
        y = uniform(0, 2)

        # Keep only points inside the quarter-circle x^2 + y^2 <= 4.
        if x * x + y * y > 4:
            continue

        # Test membership in the two semicircles.
        in_left_semi = (x - x4) ** 2 + (y - y4) ** 2 < 1
        in_bottom_semi = (x - x1) ** 2 + (y - y1) ** 2 < 1

        # The shaded region consists of points that are either:
        #   - in both semicircles, or
        #   - in neither semicircle
        #
        # In other words, shaded points are those for which the two
        # membership tests agree.
        if in_left_semi == in_bottom_semi:
            plt.plot(x, y, ".", markersize=1)
            hits += 1

    estimated_area = (hits / throws) * 4

    # ------------------------------------------------------------------
    # Final plot formatting
    # ------------------------------------------------------------------
    plt.title(f"Estimated shaded area = {estimated_area:.6f}")
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    main()

