# -----------------------------------------------------------------------------
# Jim McCleery
# May 25, 2026
# Kailua-Kona, HI
# -----------------------------------------------------------------------------
# This program draws a geometric figure involving a semicircle and several
# line segments. It also computes the distance from point A to point B.
#
# The original program contained many useful geometry functions, but most of
# them were not used in this particular drawing. To make the code easier to
# read, this version keeps only the functions needed for this picture.
# -----------------------------------------------------------------------------

from math import pi, sqrt

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """
    Return the distance between two points.

    The points are (x1, y1) and (x2, y2).
    This uses the distance formula from coordinate geometry.
    """
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# -----------------------------------------------------------------------------
def quadratic_equation(a, b, c):
    """
    Solve the quadratic equation:

        a*x^2 + b*x + c = 0

    Returns:
        (x1, x2, True) if the equation has real solutions
        (0, 0, False) if the equation has no real solutions

    The Boolean value True or False lets the rest of the program know whether
    the calculation worked.
    """
    discriminant = b**2 - 4 * a * c

    # If the discriminant is negative, the roots are not real numbers.
    if discriminant < 0:
        return 0, 0, False

    square_root = sqrt(discriminant)
    x1 = (-b - square_root) / (2 * a)
    x2 = (-b + square_root) / (2 * a)

    # Return the smaller root first.
    if x1 > x2:
        x1, x2 = x2, x1

    return x1, x2, True


# -----------------------------------------------------------------------------
def line_circle_intersection(center_x, center_y, radius, slope, y_intercept):
    """
    Find the intersection points of a circle and a line.

    Circle:
        center = (center_x, center_y)
        radius = radius

    Line:
        y = slope*x + y_intercept

    Returns:
        (x1, y1, x2, y2, True) if the line intersects the circle
        (0, 0, 0, 0, False) if there is no real intersection
    """
    # Substitute y = slope*x + y_intercept into the circle equation:
    #
    #     (x - center_x)^2 + (y - center_y)^2 = radius^2
    #
    # After simplifying, we get a quadratic equation in x.
    a = 1 + slope**2
    b = -2 * center_x + 2 * slope * y_intercept - 2 * slope * center_y
    c = center_x**2 + y_intercept**2 - 2 * y_intercept * center_y + center_y**2 - radius**2

    x1, x2, success = quadratic_equation(a, b, c)

    if not success:
        return 0, 0, 0, 0, False

    y1 = slope * x1 + y_intercept
    y2 = slope * x2 + y_intercept

    return x1, y1, x2, y2, True


# -----------------------------------------------------------------------------
def plot_circle(center_x, center_y, radius, start_angle=0, stop_angle=2 * pi):
    """
    Plot all or part of a circle.

    Angles are measured in radians.
    For example, 0 to pi draws the upper semicircle.
    """
    angles = np.linspace(start_angle, stop_angle, 1500)
    x_values = center_x + radius * np.cos(angles)
    y_values = center_y + radius * np.sin(angles)
    plt.plot(x_values, y_values)


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Plot a line segment between two points.
    """
    plt.plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
def main():
    """
    Set up the points, draw the figure, and compute distance AB.
    """
    radius = 2 * sqrt(3)
    side = sqrt(6)

    # Define the main points used in the diagram.
    x0, y0 = 0, 0
    x1, y1 = -radius, 0
    x2, y2 = radius, 0      # Point B
    x3, y3 = -side, 0
    x4, y4 = -side, side
    x5, y5 = 0, side

    # Define the slanted line that intersects the circle at point A.
    slope = -side / radius
    y_intercept = y2 - slope * x2

    # Find the intersection of the slanted line with the circle.
    x6, y6, _, _, success = line_circle_intersection(
        x0, y0, radius, slope, y_intercept
    )

    if not success:
        print("The line does not intersect the circle.")
        return

    # Point A is (x6, y6), and point B is (x2, y2).
    plt.text(x2 + 0.1, y2, "B")
    plt.text(x6 - 0.1, y6, "A")

    # Draw the pieces of the diagram.
    plot_line(x6, y6, x2, y2)     # Segment AB
    plot_line(x1, y1, x2, y2)     # Diameter of the semicircle
    plot_line(x3, y3, x4, y4)     # Left vertical segment
    plot_line(x5, y5, x4, y4)     # Top horizontal segment
    plot_line(x5, y5, x0, y0)     # Diagonal segment
    plot_circle(x0, y0, radius, 0, pi)

    # Compute and display the distance from A to B.
    ab_distance = distance(x2, y2, x6, y6)
    plt.title(f"The distance from A to B is {ab_distance:0.3f}")

    # Keep the x- and y-scales equal so the circle does not look stretched.
    plt.axis("equal")
    plt.show()


# -----------------------------------------------------------------------------
# This line means: run main() only when this file is run directly.
# It is a common Python habit that helps keep programs organized.
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
