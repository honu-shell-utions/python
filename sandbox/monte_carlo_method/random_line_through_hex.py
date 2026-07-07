# -----------------------------------------------------------------------------
# Jim McCleery
# July 7, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2025_72e3b1
# -----------------------------------------------------------------------------

from math import cos, pi, sin
from random import uniform
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS USED IN THE SIMULATION
# -----------------------------------------------------------------------------


def intersection_of_lines(m1, b1, m2, b2):
    """Return the intersection point of two non-parallel lines in slope-intercept form.

    Each line is given by y = m*x + b.
    Returns:
        (x, y, True) if the lines intersect
        (0, 0, False) if the lines are parallel
    """
    if m1 == m2:
        return 0, 0, False
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y, True


def line_intersection_from_points_v2(x1, y1, x2, y2, x3, y3, x4, y4):
    """Return the intersection of two lines, each defined by two points.

    Line 1 goes through (x1, y1) and (x2, y2).
    Line 2 goes through (x3, y3) and (x4, y4).
    """
    try:
        # Calculate slopes (rise over run)
        m1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - m1 * x1

        m2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - m2 * x3

        # Use slope-intercept solver to find the precise intersection point
        x, y, OK = intersection_of_lines(m1, b1, m2, b2)
        if not OK:
            return 0, 0, False
        return x, y, True
    except ZeroDivisionError:
        # Handles vertical lines safely to prevent program crashes
        return 0, 0, False


def point_in_polygon(x, y, polygon):
    """Return True if point (x, y) lies inside the polygon, otherwise False.

    Uses the Ray-Casting Algorithm to count line-boundary crossings.
    """
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        x_intersect = (y - p1y) * (p2x - p1x) / (
                            p2y - p1y
                        ) + p1x
                        if p1x == p2x or x <= x_intersect:
                            inside = not inside
        p1x, p1y = p2x, p2y

    return inside


def plot_line(x1, y1, x2, y2):
    """Plot a straight line segment between two points using matplotlib."""
    plt.plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# MAIN SIMULATION PROGRAM
# -----------------------------------------------------------------------------

# Define the geometry size of our regular hexagon
side = 10

# Calculate the 6 outer vertices of the hexagon using polar coordinates
x1, y1 = side, 0
x2, y2 = side * cos(pi / 3), side * sin(pi / 3)
x3, y3 = side * cos(2 * pi / 3), side * sin(2 * pi / 3)
x4, y4 = side * cos(3 * pi / 3), side * sin(3 * pi / 3)
x5, y5 = side * cos(4 * pi / 3), side * sin(4 * pi / 3)
x6, y6 = side * cos(5 * pi / 3), side * sin(5 * pi / 3)

vertices = [(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6)]

hits = 0  # Tracker for successful segment intersections
trials = 10**6  # Total number of iterations to run

# Loop for Monte Carlo simulation
for k in range(1, trials):
    plt.cla()  # Clear current axes for visual updating

    # Pick a random Point 1 inside the hexagon boundary
    while True:
        x7, y7 = uniform(-side, side), uniform(-side, side)
        if point_in_polygon(x7, y7, vertices):
            break

    # Pick a random Point 2 inside the hexagon boundary
    while True:
        x8, y8 = uniform(-side, side), uniform(-side, side)
        if point_in_polygon(x8, y8, vertices):
            break

    # --- Test Pair 1: Side (x1,y1)-(x2,y2) and opposite Side (x4,y4)-(x5,y5) ---
    x9, y9, hit = line_intersection_from_points_v2(
        x7, y7, x8, y8, x1, y1, x2, y2
    )
    if hit and (min(x1, x2) < x9 < max(x1, x2)):
        x10, y10, hit = line_intersection_from_points_v2(
            x7, y7, x8, y8, x4, y4, x5, y5
        )
        if hit and (min(x4, x5) < x10 < max(x4, x5)):
            hits += 1
            plt.plot(x9, y9, "o")
            plt.plot(x10, y10, "o")
            plot_line(x9, y9, x10, y10)

    # --- Test Pair 2: Side (x3,y3)-(x2,y2) and opposite Side (x6,y6)-(x5,y5) ---
    x9, y9, hit = line_intersection_from_points_v2(
        x7, y7, x8, y8, x3, y3, x2, y2
    )
    if hit and (min(x2, x3) < x9 < max(x2, x3)):
        x10, y10, hit = line_intersection_from_points_v2(
            x7, y7, x8, y8, x6, y6, x5, y5
        )
        if hit and (min(x5, x6) < x10 < max(x5, x6)):
            hits += 1
            plt.plot(x9, y9, "o")
            plt.plot(x10, y10, "o")
            plot_line(x9, y9, x10, y10)

    # --- Test Pair 3: Side (x1,y1)-(x6,y6) and opposite Side (x4,y4)-(x3,y3) ---
    x9, y9, hit = line_intersection_from_points_v2(
        x7, y7, x8, y8, x1, y1, x6, y6
    )
    if hit and (min(x1, x6) < x9 < max(x1, x6)):
        x10, y10, hit = line_intersection_from_points_v2(
            x7, y7, x8, y8, x4, y4, x3, y3
        )
        if hit and (min(x3, x4) < x10 < max(x3, x4)):
            hits += 1
            plt.plot(x9, y9, "o")
            plt.plot(x10, y10, "o")
            plot_line(x9, y9, x10, y10)

    # Render the randomized points inside the hexagon
    plt.plot(x7, y7, "o")
    plt.plot(x8, y8, "o")

    # Draw the static outer boundary lines of the hexagon shape
    plot_line(x1, y1, x2, y2)
    plot_line(x3, y3, x2, y2)
    plot_line(x3, y3, x4, y4)
    plot_line(x5, y5, x4, y4)
    plot_line(x5, y5, x6, y6)
    plot_line(x1, y1, x6, y6)

    # Configure plot dimensions and title showing running experimental math probability
    plt.axis("equal")
    plt.axis("off")
    plt.title(f"After {k} trials the probability of a hit is: {hits/k:0.6f}")

    # Pauses the loop briefly to visually render frames cleanly
    plt.pause(0.2)

plt.show()
