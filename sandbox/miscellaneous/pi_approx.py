"""
This program is inspired by a video from the YouTube 
channel "Andy Math" (https://www.youtube.com/@AndyMath) that explores approximating pi using inscribed and circumscribed polygons.

Compare the area of an inscribed regular n-gon and a circumscribed regular n-gon
around the unit circle.

For each value of n, the program draws:
1. the unit circle
2. the inscribed regular n-gon
3. the circumscribed regular n-gon
4. radii that help show the geometry

It also displays the two polygon areas:
- inner area  = area of the inscribed polygon
- outer area  = area of the circumscribed polygon

As n increases, both areas approach the area of the unit circle, which is pi.
"""

from math import sin, tan, pi, cos

import numpy as np
import matplotlib.pyplot as plt


def plot_partial_circle(x_center, y_center, radius, start_angle, stop_angle):
    """
    Draw part (or all) of a circle.

    Parameters
    ----------
    x_center, y_center : float
        Coordinates of the circle center
    radius : float
        Radius of the circle
    start_angle, stop_angle : float
        Starting and ending angles in radians
    """
    angles = np.linspace(start_angle, stop_angle, 1500)
    x_values = radius * np.cos(angles) + x_center
    y_values = radius * np.sin(angles) + y_center
    plt.plot(x_values, y_values)


def plot_line(x1, y1, x2, y2):
    """
    Draw a line segment from (x1, y1) to (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2])


# Loop through different numbers of sides for the polygons.
# Starting at n = 3 gives triangles first.
max_sides = 10**2
for n in range(3, max_sides + 1):
    # Draw the unit circle centered at the origin.
    plot_partial_circle(0, 0, 1, 0, 2 * pi)

    # Central angle between consecutive vertices.
    theta = 2 * pi / n

    for k in range(n):
        # Two consecutive vertices on the inscribed polygon.
        x1, y1 = cos(theta * k), sin(theta * k)
        x2, y2 = cos(theta * (k + 1)), sin(theta * (k + 1))

        # Corresponding points on the circumscribed polygon.
        #
        # The factor 1 / cos(theta / 2) is the radius of the circle passing
        # through the tangent points of the outer polygon construction.
        x3 = (1 / cos(theta / 2)) * cos(theta * k)
        y3 = (1 / cos(theta / 2)) * sin(theta * k)
        x4 = (1 / cos(theta / 2)) * cos(theta * (k + 1))
        y4 = (1 / cos(theta / 2)) * sin(theta * (k + 1))

        # Mark one outer vertex.
        plt.plot(x4, y4, ".")

        # Draw radii to the outer polygon vertices.
        plot_line(0, 0, x3, y3)
        plot_line(0, 0, x4, y4)

        # Draw one side of the inscribed polygon.
        plot_line(x1, y1, x2, y2)

        # Draw one side of the circumscribed polygon.
        plot_line(x3, y3, x4, y4)

    # Area of the inscribed regular n-gon in the unit circle:
    # n congruent isosceles triangles, each with area (1/2) sin(theta)
    inner_area = 0.5 * sin(theta) * n

    # Area of the circumscribed regular n-gon:
    # n congruent right-triangle-based pieces leading to tan(theta/2)
    outer_area = tan(theta / 2) * n

    plt.title(
        f"n = {n}   inner area = {inner_area:.4f}   outer area = {outer_area:.4f}"
    )
    plt.axis("equal")
    if k<max_sides//10:
        plt.pause(0.5)
    else:
        plt.pause(0.01)
    if k < max_sides-1:
        plt.cla()

plt.show()