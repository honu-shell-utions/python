"""
Jim McCleery
April 22, 2026
Kailua-Kona, HI

https://youtu.be/298kjoCnnjk?si=lj3unuijtbzDvbDY
"""

from math import acos, cos, degrees, radians, sin, sqrt
from random import uniform

import matplotlib.pyplot as plt


def distance(x1, y1, x2, y2):
    """Return the Euclidean distance between two points."""
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def law_of_cosines(side1, side2, opposite_side):
    """
    Return the angle opposite 'opposite_side' using the Law of Cosines.

    Parameters
    ----------
    side1, side2 : float
        The two sides enclosing the desired angle.
    opposite_side : float
        The side opposite the desired angle.

    Returns
    -------
    float
        The angle in radians.
    """
    value = (side1**2 + side2**2 - opposite_side**2) / (2 * side1 * side2)

    # Clamp the value to protect against small floating-point roundoff.
    value = max(-1.0, min(1.0, value))
    return acos(value)


def plot_line(x1, y1, x2, y2):
    """Plot a line segment between two points."""
    plt.plot([x1, x2], [y1, y2], color="black")


def generate_valid_configuration():
    """
    Generate a random geometric configuration satisfying the condition
    that alpha is essentially 20 degrees.

    Returns
    -------
    tuple
        Values of a, b and the four key points in the diagram.
    """
    target_angle = 20.0
    tolerance = 1e-4

    while True:
        a = uniform(0, 20)
        b = uniform(a, 30)

        x0, y0 = 0.0, 0.0
        x1 = (a + b) * cos(radians(10))
        y1 = (a + b) * sin(radians(10))
        x2, y2 = 0.0, a
        x3 = b * cos(radians(10))
        y3 = b * sin(radians(10))

        alpha = law_of_cosines(a + b, a + b, a)

        if abs(degrees(alpha) - target_angle) < tolerance:
            return a, b, (x0, y0), (x1, y1), (x2, y2), (x3, y3)


def main():
    """Create the figure and display the measure of angle A."""
    a, b, p0, p1, p2, p3 = generate_valid_configuration()

    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    # Length of the side from the upper-left point to point A.
    d = distance(x2, y2, x3, y3)

    # Compute angle A (beta) in the triangle with side lengths b, d, and a.
    beta = law_of_cosines(b, d, a)

    # Draw the figure.
    plot_line(x0, y0, x1, y1)
    plot_line(x2, y2, x1, y1)
    plot_line(x0, y0, x2, y2)
    plot_line(x3, y3, x2, y2)

    # Label point A and format the plot.
    plt.text(x3 - 3, y3, "A")
    plt.title(f"Measure of angle A = {degrees(beta):.3f} degrees")
    plt.axis("equal")
    plt.show()


if __name__ == "__main__":
    main()
