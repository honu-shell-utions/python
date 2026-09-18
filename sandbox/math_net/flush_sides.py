"""
Jim McCleery
April 22, 2026
Kailua-Kona, HI

What is the area of a square inscribed in a semicircle of radius 1,
with one of its sides flush with the diameter of the semicircle?
"""

from math import pi, sqrt

import matplotlib.pyplot as plt
import numpy as np


def plot_arc(ax, center_x, center_y, radius, start_angle, end_angle, **kwargs):
    """Plot a circular arc."""
    theta = np.linspace(start_angle, end_angle, 500)
    x_vals = center_x + radius * np.cos(theta)
    y_vals = center_y + radius * np.sin(theta)
    ax.plot(x_vals, y_vals, **kwargs)


def main():
    # Let s be the side length of the square.
    # The top corner of the square lies on the semicircle of radius 1, so:
    #
    #     s^2 + (s/2)^2 = 1
    #
    # which gives:
    #
    #     5s^2 / 4 = 1
    #     s^2 = 4/5
    #
    # Therefore, the area of the square is 4/5.
    radius = 1.0
    side = sqrt(4 / 5)
    area = side**2

    # Key points
    diameter_left = (-radius, 0.0)
    diameter_right = (radius, 0.0)

    bottom_left = (-side / 2, 0.0)
    bottom_right = (side / 2, 0.0)
    top_left = (-side / 2, side)
    top_right = (side / 2, side)

    square_x = [bottom_left[0], top_left[0], top_right[0], bottom_right[0], bottom_left[0]]
    square_y = [bottom_left[1], top_left[1], top_right[1], bottom_right[1], bottom_left[1]]

    fig, ax = plt.subplots()

    # Draw the diameter, square, and semicircle
    ax.plot(
        [diameter_left[0], diameter_right[0]],
        [diameter_left[1], diameter_right[1]],
        linewidth=2,
    )
    ax.plot(square_x, square_y, linewidth=2)
    plot_arc(ax, 0.0, 0.0, radius, 0, pi, linewidth=2)

    # Shade the square
    ax.fill(square_x, square_y, color="red", alpha=0.8)

    ax.set_title(f"Area of inscribed square = {area:.2f}")
    ax.set_aspect("equal")
    ax.axis("off")
    plt.show()


if __name__ == "__main__":
    main()
