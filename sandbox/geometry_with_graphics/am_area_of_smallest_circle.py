"""
Jim McCleery
April 11, 2026
Kailua-Kona, HI

Python solution to
Video:https://youtu.be/PepDzPFxMJ4?si=a1WGndZ0cRoMqJdK

Andy shows how to derive the three radii, what we have here
is a little Python program that give a graphical display
of the five circles.

Jim McCleery
April 11, 2026
Kona, HI
"""

from math import pi, sqrt
from random import uniform
import numpy as np
import matplotlib.pyplot as plt


def draw_circle(center_x, center_y, radius):
    """Draw a circle."""
    t = np.linspace(0, 2 * pi, 400)
    x = center_x + radius * np.cos(t)
    y = center_y + radius * np.sin(t)
    plt.plot(x, y)


def draw_segment(x1, y1, x2, y2):
    """Draw a line segment between two points."""
    plt.plot([x1, x2], [y1, y2])


def label_point(name, x, y, dx=0.08, dy=0.08):
    """Write a point name and its coordinates near the point."""
    plt.plot(x, y, "ko", markersize=3)
    plt.text(x + dx, y + dy, f"{name} ({x:.2f}, {y:.2f})", fontsize=9)


# -------------------------------------------------------------------
# Andy's video shows how to derive the three different radii.
# Using those values, this program draws the circles and shades
# the smallest circle by random sampling.
# -------------------------------------------------------------------

r_big = 12 / sqrt(pi)
r_left = 6 / sqrt(pi)
r_small = 3 / sqrt(pi)

# Centers of the circles
O  = (0, 0)
A  = (r_big, 0)
B  = (-r_big, 0)
C  = (-r_left, 0)
D  = (-2 * r_big, 0)
E  = (2 * r_big, 0)
F  = (0, -r_big + r_small)

# Draw the horizontal baseline
draw_segment(D[0], D[1], E[0], E[1])

# Draw the circles
draw_circle(O[0], O[1], r_big)
draw_circle(A[0], A[1], r_big)
draw_circle(B[0], B[1], r_big)
draw_circle(C[0], C[1], r_left)
draw_circle(F[0], F[1], r_small)

# Label one region with its area
plt.text(-r_left-.4, r_left / 3, "36", fontsize=11)

# Shade the small circle numerically by plotting random points inside it
for _ in range(10**4):
    x = uniform(F[0] - r_small, F[0] + r_small)
    y = uniform(F[1] - r_small, F[1] + r_small)

    if (x - F[0]) ** 2 + (y - F[1]) ** 2 < r_small ** 2:
        plt.plot(x, y, ".", markersize=2)

# Final formatting
small_area = pi * r_small ** 2
plt.title(f"Area of the shaded circle: {small_area:.2f}")
plt.axis("equal")
plt.show()
