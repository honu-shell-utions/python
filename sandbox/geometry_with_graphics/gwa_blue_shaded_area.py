"""
Jim McCleery
April 14, 2026
Kailua-Kona, HI

Python solution to Calculate the blue shaded area | area quarter circle
from Geometry with Alex
Video: https://youtu.be/Q1cuHcBMYTY?si=7k9c3BX9C7gMOLtd

This problem can be solved analytically with two equations and two unknowns,
but what we are doing here is first playing a little guessing game and checking
to see how good our guess is.
"""

# -----------------------------------------------------------------------------
# IMPORTS
# -----------------------------------------------------------------------------
from math import pi, sqrt
from random import uniform
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# BASIC GEOMETRY TOOLS
# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """
    Return the Euclidean distance between two points.
    """
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def plot_line(x1, y1, x2, y2, **kwargs):
    """
    Draw the line segment from (x1, y1) to (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2], **kwargs)


def plot_circle(cx, cy, radius, start_angle=0, stop_angle=2 * pi, **kwargs):
    """
    Draw all or part of a circle.

    Parameters
    ----------
    cx, cy : float
        Center of the circle
    radius : float
        Radius of the circle
    start_angle, stop_angle : float
        Angles in radians
    """
    theta = np.linspace(start_angle, stop_angle, 1000)
    x = cx + radius * np.cos(theta)
    y = cy + radius * np.sin(theta)
    plt.plot(x, y, **kwargs)


def fill_quarter_circle(cx, cy, radius, start_angle, stop_angle, **kwargs):
    """
    Fill the region bounded by:
      1. the circular arc from start_angle to stop_angle
      2. the two radius segments from the center to the endpoints of the arc

    In this problem, that region is the blue quarter-circle.
    """
    theta = np.linspace(start_angle, stop_angle, 500)
    x_arc = cx + radius * np.cos(theta)
    y_arc = cy + radius * np.sin(theta)

    # Build a closed path: center -> arc -> center
    x_fill = np.concatenate(([cx], x_arc, [cx]))
    y_fill = np.concatenate(([cy], y_arc, [cy]))

    plt.fill(x_fill, y_fill, **kwargs)


def mark_point(x, y, label, dx=0.15, dy=0.15):
    """
    Mark a point with a small dot and a nearby text label.

    Parameters
    ----------
    x, y : float
        Coordinates of the point
    label : str
        Text to place near the point
    dx, dy : float
        Small shifts used to keep the label from sitting directly on the point
    """
    plt.plot(x, y, "ko", markersize=4)
    plt.text(x + dx, y + dy, label, fontsize=11)


# -----------------------------------------------------------------------------
# ANALYTIC SOLUTION
# -----------------------------------------------------------------------------
def analytic_radius():
    """
    Compute the radius r exactly using algebra.

    Geometry setup
    --------------
    The large circle is centered at (0, 0) with radius 10.

    The unknown small circle has:
        center = (x4, 0)
        radius = r

    Its top point is (x4, r), and that point lies on the large circle:
        x4^2 + r^2 = 100

    The radius-5 circle is centered at (0, 5).
    Since the two smaller circles are externally tangent,
        distance between centers = r + 5

    Therefore:
        sqrt(x4^2 + 25) = r + 5

    Squaring both sides gives:
        x4^2 + 25 = r^2 + 10r + 25
        x4^2 = r^2 + 10r

    But from the large circle:
        x4^2 = 100 - r^2

    So:
        100 - r^2 = r^2 + 10r
        2r^2 + 10r - 100 = 0
        r^2 + 5r - 50 = 0

    Solving:
        r = [-5 ± sqrt(25 + 200)] / 2
          = [-5 ± 15] / 2

    The positive solution is:
        r = 5
    """
    return 5.0


# -----------------------------------------------------------------------------
# NUMERICAL SEARCH BY GUESSING
# -----------------------------------------------------------------------------
def find_radius_by_guessing(tolerance=1e-4):
    """
    Approximate the radius r by random guessing.

    We repeatedly guess r in the interval [0, 10] and keep the first value
    that satisfies the tangency condition to within the given tolerance.
    """
    x5, y5 = 0, 5

    while True:
        r = uniform(0, 10)

        # The point (x3, y3) lies on the large circle x^2 + y^2 = 100
        # and has y-coordinate y3 = r.
        x3 = -sqrt(100 - r ** 2)
        y3 = r

        # The center of the unknown circle lies directly below that point
        # on the x-axis.
        x4, y4 = x3, 0

        # Tangency condition:
        # distance between centers = sum of radii
        d = distance(x4, y4, x5, y5)

        if abs(d - (r + 5)) < tolerance:
            return r, x3, y3, x4, y4, x5, y5


# -----------------------------------------------------------------------------
# MAIN PROGRAM
# -----------------------------------------------------------------------------
def main():
    """
    Solve the geometry problem in two ways:

    1. Numerical guessing
    2. Exact analytic solution

    Then draw the exact figure and label the important points.
    """
    # Fixed points on the large quarter circle
    x0, y0 = 0, 0
    x1, y1 = 0, 10
    x2, y2 = -10, 0

    # -------------------------------------------------------------------------
    # Part 1: numerical experiment
    # -------------------------------------------------------------------------
    guessed_r, _, _, _, _, x5, y5 = find_radius_by_guessing()

    # -------------------------------------------------------------------------
    # Part 2: exact algebraic solution
    # -------------------------------------------------------------------------
    exact_r = analytic_radius()

    # Build the exact geometry from r = 5
    x3 = -sqrt(100 - exact_r ** 2)
    y3 = exact_r
    x4, y4 = x3, 0

    shaded_area = pi * exact_r ** 2 / 4

    # -------------------------------------------------------------------------
    # Print a summary for students
    # -------------------------------------------------------------------------
    print("Geometry Investigation")
    print("-" * 68)
    print("This program solves the problem in two ways:")
    print("  1. By numerical guessing")
    print("  2. By exact algebra")
    print()

    print("Numerical guessing result:")
    print(f"  guessed radius r ≈ {guessed_r:.6f}")

    print("\nAnalytic result:")
    print(f"  exact radius r = {exact_r:.6f}")

    print("\nComparison:")
    print(f"  absolute error = {abs(guessed_r - exact_r):.6f}")

    print("\nExact geometry:")
    print(f"  center of unknown circle = ({x4:.6f}, {y4:.6f})")
    print(f"  top point on large circle = ({x3:.6f}, {y3:.6f})")

    print("\nBlue shaded area:")
    print(f"  area = pi*r^2/4 = {shaded_area:.6f}")
    print(f"  exact area = 25*pi/4 ≈ {shaded_area:.6f}")
    print("-" * 68)

    # -------------------------------------------------------------------------
    # Draw the shaded region exactly
    # -------------------------------------------------------------------------
    fill_quarter_circle(
        x4, y4, exact_r, 0, pi / 2,
        color="skyblue", alpha=0.8
    )

    # Draw the circle arcs
    plot_circle(x5, y5, 5, pi / 2, 3 * pi / 2, color="black", linewidth=2)
    plot_circle(x0, y0, 10, pi / 2, pi, color="black", linewidth=2)
    plot_circle(x4, y4, exact_r, 0, pi / 2, color="black", linewidth=2)

    # Draw line segments
    plot_line(x0, y0, x2, y2, color="black", linewidth=2)
    plot_line(x0, y0, x1, y1, color="black", linewidth=2)
    plot_line(x3, y3, x4, y4, color="black", linewidth=2)

    # -------------------------------------------------------------------------
    # Label important points and centers
    # -------------------------------------------------------------------------
    mark_point(x0, y0, "(0,0)", dx=0.15, dy=-0.45)
    mark_point(x1, y1, "(0,10)", dx=0.2, dy=0.1)
    mark_point(x2, y2, "(-10,0)", dx=-1.6, dy=-0.45)

    mark_point(x5, y5, "(0,5)", dx=0.2, dy=0.15)
    mark_point(x4, y4, f"({x4:.3f},0)", dx=-1.8, dy=-0.45)
    mark_point(x3, y3, f"({x3:.3f},{y3:.0f})", dx=-2.3, dy=0.2)

    # Additional explanatory labels
    plt.text(-2.2, 7.2, "circle of radius 5", fontsize=11)
    plt.text(-7.9, 8.9, "quarter circle of radius 10", fontsize=11)
    plt.text(x4 + 0.7, y4 + 2.0, f"unknown circle\nradius r = {exact_r:.0f}", fontsize=11)

    # Title and formatting
    plt.title(f"Blue Shaded Area = 25π/4 ≈ {shaded_area:.6f}", fontsize=14)
    plt.axis("equal")
    plt.xlim(-11, 1.5)
    plt.ylim(-1.2, 11)
    plt.grid(False)
    plt.show()


# -----------------------------------------------------------------------------
# RUN THE PROGRAM
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
