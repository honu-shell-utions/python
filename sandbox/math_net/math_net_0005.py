# -----------------------------------------------------------------------------
# Jim McCleery
# April 25, 2026
# Kailua-Kona, HI
# -----------------------------------------------------------------------------
"""
Construct a convex cyclic pentagon PABCD satisfying:

    AD = 70
    BC = 55
    AD || BC
    PA : PD = 3 : 4
    PB : PC = 5 : 6

The program draws the pentagon and computes PB.

https://mathnet.mit.edu/explorer.html?view=detail&problem=a7a7476e317e3a3580cae428877ca8c29b28852128482708b4ff8569b1ab0e37&mode=country&country=United+States

"""

from math import acos, cos, hypot, pi, sin, sqrt

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Basic geometry helpers
# -----------------------------------------------------------------------------
def chord_angle(radius, chord_length):
    """
    Return the central angle, in radians, subtended by a chord.

    For a chord of length c in a circle of radius r:

        c^2 = r^2 + r^2 - 2r^2 cos(theta)

    so

        theta = arccos((2r^2 - c^2) / (2r^2))
    """
    return acos((2 * radius**2 - chord_length**2) / (2 * radius**2))


def distance(point_1, point_2):
    """Return the Euclidean distance between two points."""
    x1, y1 = point_1
    x2, y2 = point_2
    return hypot(x2 - x1, y2 - y1)


def circle_circle_intersections(center_1, radius_1, center_2, radius_2):
    """
    Return the two intersection points of two circles.

    The circles are:

        circle 1: center_1, radius_1
        circle 2: center_2, radius_2
    """
    x0, y0 = center_1
    x1, y1 = center_2

    d = distance(center_1, center_2)

    a = (radius_1**2 - radius_2**2 + d**2) / (2 * d)
    h = sqrt(radius_1**2 - a**2)

    x2 = x0 + a * (x1 - x0) / d
    y2 = y0 + a * (y1 - y0) / d

    offset_x = -(y1 - y0) * h / d
    offset_y = (x1 - x0) * h / d

    point_a = (x2 + offset_x, y2 + offset_y)
    point_b = (x2 - offset_x, y2 - offset_y)

    return point_a, point_b


# -----------------------------------------------------------------------------
# Pentagon construction
# -----------------------------------------------------------------------------
def construct_pentagon(radius):
    """
    Construct the points A, B, C, D, and P for a given circumradius.

    The construction places AD and BC horizontally, with AD below BC.
    Point P is chosen as the lower circle-circle intersection so that the
    pentagon has the same orientation as the diagram.
    """
    theta = chord_angle(radius, 55)       # central angle for chord BC
    gamma = chord_angle(radius, 70)       # central angle for chord AD

    alpha = (gamma - theta) / 2

    # D and C are placed on the right side of the circle.
    D = (
        radius * cos(pi / 2 - theta / 2 - alpha),
        radius * sin(pi / 2 - theta / 2 - alpha),
    )

    C = (
        radius * cos(pi / 2 - theta / 2),
        radius * sin(pi / 2 - theta / 2),
    )

    # Reflect across the y-axis to get A and B.
    A = (-D[0], D[1])
    B = (-C[0], C[1])

    # Since PA : PD = 3 : 4, write PA = 3k and PD = 4k.
    # The value of k is determined from triangle APD.
    k = 70 / sqrt(25 - 24 * cos(theta / 2 + alpha))

    possible_P_points = circle_circle_intersections(A, 3 * k, D, 4 * k)

    # Choose the lower point, matching the intended convex pentagon.
    P = min(possible_P_points, key=lambda point: point[1])

    return A, B, C, D, P


def ratio_error(radius):
    """
    Return the error in the desired ratio:

        PB : PC = 5 : 6

    Equivalently,

        PC / PB = 6 / 5
    """
    A, B, C, D, P = construct_pentagon(radius)

    PB = distance(P, B)
    PC = distance(P, C)

    return PC / PB - 6 / 5


def find_radius(lower_bound=35.000001, upper_bound=40, tolerance=1e-12):
    """
    Find the circumradius using bisection.

    The radius must be greater than 35 because AD = 70 is a chord, and
    a chord cannot exceed the circle's diameter.
    """
    low = lower_bound
    high = upper_bound

    while high - low > tolerance:
        mid = (low + high) / 2

        if ratio_error(low) * ratio_error(mid) <= 0:
            high = mid
        else:
            low = mid

    return (low + high) / 2


# -----------------------------------------------------------------------------
# Plotting helpers
# -----------------------------------------------------------------------------
def plot_circle(center, radius):
    """Plot the circumcircle."""
    center_x, center_y = center

    angle = np.linspace(0, 2 * pi, 1000)
    x_values = center_x + radius * np.cos(angle)
    y_values = center_y + radius * np.sin(angle)

    plt.plot(x_values, y_values, linestyle="--", linewidth=1)


def plot_segment(point_1, point_2):
    """Plot a line segment between two points."""
    x1, y1 = point_1
    x2, y2 = point_2

    plt.plot([x1, x2], [y1, y2], color="black", linewidth=2)


def label_point(point, label, dx=1.5, dy=1.5):
    """Add a text label near a point."""
    x, y = point
    plt.text(x + dx, y + dy, label, fontsize=14, fontweight="bold")


def draw_pentagon(A, B, C, D, P, radius, PB):
    """Draw the cyclic pentagon and label its vertices."""
    plot_circle((0, 0), radius)

    # Draw the outside edges of pentagon PABCD.
    plot_segment(P, A)
    plot_segment(A, B)
    plot_segment(B, C)
    plot_segment(C, D)
    plot_segment(D, P)

    # Draw the two extra segments shown in the original diagram.
    plot_segment(P, B)
    plot_segment(P, C)
    plot_segment(D, A)

    # Label the five points.
    label_point(A, "A", dx=-6, dy=-1)
    label_point(B, "B", dx=-6, dy=1)
    label_point(C, "C", dx=2, dy=1)
    label_point(D, "D", dx=2, dy=-1)
    label_point(P, "P", dx=-3, dy=-6)

    plt.title(f"Distance from P to B: {PB:.6f}")
    plt.axis("equal")
    plt.grid(True, alpha=0.3)
    plt.show()


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------
def main():
    radius = find_radius()

    A, B, C, D, P = construct_pentagon(radius)

    PB = distance(P, B)
    PC = distance(P, C)

    draw_pentagon(A, B, C, D, P, radius, PB)

if __name__ == "__main__":
    main()
