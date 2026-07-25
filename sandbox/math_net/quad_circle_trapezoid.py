# =============================================================================
# Jim McCleery
# July 25, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2022_bbefc1
# =============================================================================

from math import acos, cos, pi, sin, sqrt
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """Calculate the straight-line (Euclidean) distance between two points (x1, y1) and (x2, y2)."""
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def quadratic_equation(A, B, C):
    """
    Solve a quadratic equation: A*x^2 + B*x + C = 0.

    Returns:
        (x1, x2, True) with real roots x1 <= x2 if they exist,
        (0, 0, False) if there are no real roots.
    """
    try:
        disc = B**2 - 4 * A * C
        disc_sqrt = sqrt(disc)
        x1 = (-B - disc_sqrt) / (2 * A)
        x2 = (-B + disc_sqrt) / (2 * A)

        # Ensure x1 is the smaller root
        if x1 > x2:
            x1, x2 = x2, x1

        return x1, x2, True
    except ValueError:
        # Occurs if discriminant < 0 (complex roots)
        return 0, 0, False


def line_circle_intersection(cx, cy, r, m, b):
    """
    Find the intersection points between a circle (center (cx, cy), radius r)
    and a line defined by y = m*x + b.

    Returns:
        (x1, y1, x2, y2, True) if intersections exist,
        (0, 0, 0, 0, False) otherwise.
    """
    # Substitute y = m*x + b into circle equation: (x - cx)^2 + (y - cy)^2 = r^2
    A = 1 + m**2
    B = -2 * cx + 2 * m * b - 2 * m * cy
    C = cx**2 + b**2 - 2 * b * cy + cy**2 - r**2

    x_first, x_second, ok = quadratic_equation(A, B, C)
    if ok:
        y_first = m * x_first + b
        y_second = m * x_second + b
        return x_first, y_first, x_second, y_second, True
    else:
        return 0, 0, 0, 0, False


def polygon_area(vertices):
    """
    Calculate the area of a polygon given an ordered list of (x, y) vertices
    using the Shoelace formula.
    """
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2.0


def polygon_fill_coordinates(vertices):
    """
    Convert a list of vertices into x and y lists suitable for matplotlib's fill().
    Closes the loop by appending the first vertex to the end.
    """
    x_coords, y_coords = zip(*vertices)
    return list(x_coords) + [x_coords[0]], list(y_coords) + [y_coords[0]]


def plot_circle(cx, cy, radius):
    """Plot the outline of a circle given center (cx, cy) and radius."""
    angles = np.linspace(0, 2 * pi, 500)
    x_vals = radius * np.cos(angles) + cx
    y_vals = radius * np.sin(angles) + cy
    plt.plot(x_vals, y_vals)


def plot_line(x1, y1, x2, y2, color="blue"):
    """Plot a straight line segment between two points."""
    plt.plot([x1, x2], [y1, y2], color=color)


# -----------------------------------------------------------------------------
# MAIN GEOMETRY CALCULATIONS & SIMULATION
# -----------------------------------------------------------------------------

# Problem Setup:
# Isosceles trapezoid ABCD with:
# AB = 17 (top base), CD = 31 (bottom base), BC = DA = 25 (legs)
# We set D at origin (0,0) and C along the x-axis at (31,0).

# Base angle theta at vertices C and D
theta = acos((31**2 - 17**2) / (50 * 17 + 50 * 31))

# Coordinate definitions for trapezoid vertices:
xD, yD = 0, 0  # Point D
xC, yC = 31, 0  # Point C
xB, yB = 31 + 25 * cos(pi - theta), 25 * sin(pi - theta)  # Point B
xA, yA = 25 * cos(theta), 25 * sin(theta)  # Point A

# Run simulation to find valid points P and Q, then compute the inner quadrilateral area
for _ in range(10):
    # Find distance 'a' along leg DA such that chord PQ has length 25
    while True:
        a = uniform(0, 25)

        # Point P on side AD (AP = a)
        xP, yP = (25 - a) * cos(theta), (25 - a) * sin(theta)

        # Point Q on side BC (CQ = a)
        xQ, yQ = xC + a * cos(pi - theta), a * sin(pi - theta)

        # Check if length of segment PQ is equal to 25
        d_PQ = distance(xP, yP, xQ, yQ)
        if abs(d_PQ - 25) < 0.0001:
            break

    # Circle center (midpoint of PQ) and radius (half of diameter PQ = 25/2)
    x_mid, y_mid = (xP + xQ) / 2.0, (yP + yQ) / 2.0
    radius_PQ = 25.0 / 2.0

    # Intersections with top side AB (line y = yA)
    x_top1, y_top1, x_top2, y_top2, _ = line_circle_intersection(
        x_mid, y_mid, radius_PQ, 0, yA
    )

    # Intersections with bottom side CD (line y = yD = 0)
    x_bot1, y_bot1, x_bot2, y_bot2, _ = line_circle_intersection(
        x_mid, y_mid, radius_PQ, 0, 0
    )

    # Vertices of the convex quadrilateral formed inside the circle
    quad_vertices = [
        (x_top1, y_top1),
        (x_top2, y_top2),
        (x_bot2, y_bot2),
        (x_bot1, y_bot1),
    ]

    area = polygon_area(quad_vertices)

    # --- PLOTTING ---
    plt.figure(figsize=(8, 6))

    # Fill the inner quadrilateral with red
    fill_x, fill_y = polygon_fill_coordinates(quad_vertices)
    plt.fill(fill_x, fill_y, color="red", edgecolor="red", linewidth=2)

    # Plot circle with diameter PQ
    plot_circle(x_mid, y_mid, radius_PQ)

    # Plot trapezoid sides ABCD
    plot_line(xD, yD, xC, yC)  # Side CD
    plot_line(xC, yC, xB, yB)  # Side BC
    plot_line(xB, yB, xA, yA)  # Side AB
    plot_line(xA, yA, xD, yD)  # Side DA

    # Plot segment PQ
    plot_line(xP, yP, xQ, yQ, color="black")

    # Add vertex labels for clarity
    plt.text(xD - 1, yD - 1, "D", fontsize=12, fontweight="bold")
    plt.text(xC + 0.5, yC - 1, "C", fontsize=12, fontweight="bold")
    plt.text(xB + 0.5, yB + 0.5, "B", fontsize=12, fontweight="bold")
    plt.text(xA - 1, yA + 0.5, "A", fontsize=12, fontweight="bold")
    plt.text(xP - 1.5, yP, "P", fontsize=12, color="purple", fontweight="bold")
    plt.text(xQ + 0.5, yQ, "Q", fontsize=12, color="purple", fontweight="bold")

    plt.axis("equal")
    plt.axis("off")
    plt.title(f"The area of the red polygon is {area:0.3f}")
    plt.show()
