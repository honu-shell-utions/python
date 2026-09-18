# -----------------------------------------------------------------------------
# Jim McCleery
# May 10, 2026
# Kailua-Kona, HI
# -----------------------------------------------------------------------------
"""
An isosceles trapezoid has an inscribed circle tangent to each
of its four sides. The radius of the circle is 3, and the area
of the trapezoid is 72. Let the parallel sides of the trapezoid
have lengths r and s, with r ≠ s. Find r² + s².

https://mathnet.mit.edu/explorer.html?p=usa_2025_a7ad4d

This program demonstrates a numerical solution using bisection.

Since the circle has radius 3, the height of the trapezoid is 6.
The area is 72, so

    ((r + s) / 2) * 6 = 72

which gives

    r + s = 24.

We choose one base length r and set s = 24 - r.  Then we build the
isosceles trapezoid and use bisection to find the value of r for
which the left side is tangent to the circle.
"""
# -----------------------------------------------------------------------------

from math import hypot
import numpy as np
import matplotlib.pyplot as plt


RADIUS = 3.0
HEIGHT = 2 * RADIUS
AREA = 72.0
BASE_SUM = 2 * AREA / HEIGHT          # r + s = 24


# -----------------------------------------------------------------------------
def point_to_line_distance(px, py, x1, y1, x2, y2):
    """
    Return the perpendicular distance from point P = (px, py)
    to the line through points A = (x1, y1) and B = (x2, y2).
    """
    numerator = abs((y2 - y1) * px - (x2 - x1) * py + x2 * y1 - y2 * x1)
    denominator = hypot(y2 - y1, x2 - x1)
    return numerator / denominator


# -----------------------------------------------------------------------------
def trapezoid_vertices(r):
    """
    Build an isosceles trapezoid with lower base r and upper base s = 24 - r.

    The lower base lies on the x-axis from A to B.
    The upper base is centered above it at height 6.

    Vertices are returned in counterclockwise order:

        D -------- C
         \\      /
          \\    /
           A -- B
    """
    s = BASE_SUM - r
    horizontal_offset = (r - s) / 2

    A = (0.0, 0.0)
    B = (r, 0.0)
    C = (horizontal_offset + s, HEIGHT)
    D = (horizontal_offset, HEIGHT)

    return A, B, C, D


# -----------------------------------------------------------------------------
def tangency_error(r):
    """
    Return the signed error in the tangency condition.

    For a correct inscribed circle, the distance from the circle's center
    to either slanted side of the trapezoid must equal the radius.

    A zero of this function means the side is tangent to the circle.
    """
    A, B, C, D = trapezoid_vertices(r)

    center_x = r / 2
    center_y = RADIUS

    distance_to_left_side = point_to_line_distance(
        center_x,
        center_y,
        A[0],
        A[1],
        D[0],
        D[1],
    )

    return distance_to_left_side - RADIUS


# -----------------------------------------------------------------------------
def bisection_root(function, left, right, tolerance=1e-12, max_iterations=100):
    """
    Find a root of function(x) = 0 on the interval [left, right]
    using the bisection method.

    The function values at the two endpoints must have opposite signs.
    """
    f_left = function(left)
    f_right = function(right)

    if f_left * f_right > 0:
        raise ValueError("Bisection requires opposite signs at the endpoints.")

    for _ in range(max_iterations):
        midpoint = (left + right) / 2
        f_mid = function(midpoint)

        if abs(f_mid) < tolerance or (right - left) / 2 < tolerance:
            return midpoint

        if f_left * f_mid <= 0:
            right = midpoint
            f_right = f_mid
        else:
            left = midpoint
            f_left = f_mid

    return (left + right) / 2


# -----------------------------------------------------------------------------
def plot_circle(center_x, center_y, radius):
    """
    Plot a circle.
    """
    theta = np.linspace(0, 2 * np.pi, 600)
    x_values = center_x + radius * np.cos(theta)
    y_values = center_y + radius * np.sin(theta)

    plt.plot(x_values, y_values)


# -----------------------------------------------------------------------------
def plot_trapezoid(r, s, solution):
    """
    Plot the trapezoid, its incircle, and vertex labels.
    """
    A, B, C, D = trapezoid_vertices(r)

    center_x = r / 2
    center_y = RADIUS

    x_values = [A[0], B[0], C[0], D[0], A[0]]
    y_values = [A[1], B[1], C[1], D[1], A[1]]

    plt.figure(figsize=(8, 5))

    # Draw trapezoid and incircle.
    plt.plot(x_values, y_values, linewidth=2)
    plot_circle(center_x, center_y, RADIUS)

    # Label vertices.
    vertex_labels = {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
    }

    for label, (x, y) in vertex_labels.items():
        plt.scatter(x, y)
        plt.text(x, y + 0.25, label, fontsize=14, ha="center")

    # Label circle center.
    plt.scatter(center_x, center_y)
    plt.text(center_x, center_y, "  O", fontsize=14, va="center")

    plt.title(f"The sum of the squares of the two bases = {solution:.0f}")
    plt.axis("equal")
    plt.grid(True)
    plt.show()


# -----------------------------------------------------------------------------
def main():
    """
    Solve the problem numerically using bisection and plot the result.
    """
    # We look for the larger base r.  Since r + s = 24, this means r > 12.
    # The interval below brackets the root of the tangency condition.
    r = bisection_root(tangency_error, 12.0, 23.999999)

    s = BASE_SUM - r
    solution = r**2 + s**2

    plot_trapezoid(r, s, solution)


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
