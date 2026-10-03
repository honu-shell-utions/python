# =============================================================================
# Jim McCleery
# October 3, 2026
# Kailua-Kona, HI
#
# Geometry Problem Reference:
# https://mathnet.mit.edu/explorer.html?p=nmo_2016_615ff2
#
# Problem:
# Let ABCD be a cyclic quadrilateral satisfying AB = AD and AB + BC = CD.
# Determine angle CDA.
# =============================================================================

from math import acos, cos, degrees, pi, sin, sqrt, tan
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Geometry Helper Functions
# -----------------------------------------------------------------------------

def distance(point_a, point_b):
    """
    Calculate the straight-line (Euclidean) distance between two points.
    Each point is a tuple containing (x, y) coordinates.
    """
    x1, y1 = point_a
    x2, y2 = point_b
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def quadratic_equation(a, b, c):
    """
    Solve the quadratic equation: a*x^2 + b*x + c = 0.
    Returns (x1, x2, True) if real solutions exist, or (0, 0, False) if not.
    """
    try:
        discriminant = b**2 - 4 * a * c
        if discriminant < 0:
            return 0, 0, False

        root = sqrt(discriminant)
        x1 = (-b - root) / (2 * a)
        x2 = (-b + root) / (2 * a)

        # Sort so that x1 is always the smaller root
        if x1 > x2:
            x1, x2 = x2, x1

        return x1, x2, True
    except (ValueError, ZeroDivisionError):
        return 0, 0, False


def define_circle_from_points(point_a, point_b, point_c):
    """
    Find the unique circle passing through three non-collinear points.
    Returns the center point as an (x, y) tuple and the circle's radius.
    """
    x1, y1 = point_a
    x2, y2 = point_b
    x3, y3 = point_c

    temp = x2**2 + y2**2
    bc = (x1**2 + y1**2 - temp) / 2
    cd = (temp - x3**2 - y3**2) / 2

    determinant = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    center_x = (bc * (y2 - y3) - cd * (y1 - y2)) / determinant
    center_y = ((x1 - x2) * cd - (x2 - x3) * bc) / determinant

    center = (center_x, center_y)
    radius = distance(center, point_a)

    return center, radius


def line_circle_intersection(center, radius, line):
    """
    Find the two intersection points between a circle and a line y = m*x + b.
    Returns (P1, P2, True) if intersection points exist.
    """
    cx, cy = center
    m, b = line

    # Substitute y = m*x + b into the equation of a circle: (x - cx)^2 + (y - cy)^2 = r^2
    # Expanding produces a standard quadratic equation: A*x^2 + B*x + C = 0
    quad_a = 1 + m**2
    quad_b = -2 * cx + 2 * m * b - 2 * m * cy
    quad_c = cx**2 + b**2 - 2 * b * cy + cy**2 - radius**2

    x1, x2, success = quadratic_equation(quad_a, quad_b, quad_c)
    if not success:
        return (0, 0), (0, 0), False

    p1 = (x1, m * x1 + b)
    p2 = (x2, m * x2 + b)

    return p1, p2, True


def law_of_cosines(side1, side2, opposite_side):
    """
    Calculate the interior angle opposite to 'opposite_side' using the Law of Cosines.
    Returns the angle in radians.
    """
    try:
        cosine_val = (side1**2 + side2**2 - opposite_side**2) / (2 * side1 * side2)
        # Clamp to [-1, 1] to prevent tiny floating-point rounding errors from failing acos
        cosine_val = max(-1.0, min(1.0, cosine_val))
        return acos(cosine_val), True
    except (ValueError, ZeroDivisionError):
        return 0, False


# -----------------------------------------------------------------------------
# Plotting Helper Functions
# -----------------------------------------------------------------------------

def plot_line(point_a, point_b, color="black", linestyle="-", linewidth=1.5):
    """Draw a straight line segment connecting two points."""
    plt.plot([point_a[0], point_b[0]], [point_a[1], point_b[1]], color=color, linestyle=linestyle, linewidth=linewidth)


def plot_circle(center, radius, color="gray", linestyle="--"):
    """Draw the outline of a full circle given its center and radius."""
    angles = np.linspace(0, 2 * pi, 500)
    x_vals = center[0] + radius * np.cos(angles)
    y_vals = center[1] + radius * np.sin(angles)
    plt.plot(x_vals, y_vals, color=color, linestyle=linestyle, alpha=0.7)


def label_point(name, point, offset=(0.3, 0.3)):
    """
    Plot a marker for a point and display both its name and coordinate values.
    """
    x, y = point
    plt.plot(x, y, marker="o", color="blue", markersize=5)
    coord_text = f"{name} ({x:.2f}, {y:.2f})"
    plt.annotate(
        coord_text,
        (x, y),
        textcoords="offset points",
        xytext=(offset[0] * 15, offset[1] * 15),
        fontsize=9,
        fontweight="bold",
    )


# -----------------------------------------------------------------------------
# Main Simulation / Search Loop
# -----------------------------------------------------------------------------

AB = 10.0  # Set an arbitrary base segment length for AB

# Use random sampling to search for a configuration that satisfies:
# 1. Cyclic quadrilateral ABCD with AB = AD
# 2. AB + BC = CD
while True:
    gamma = uniform(pi / 4, pi / 2)
    alpha = pi / 2 - gamma

    point_a = (0.0, 0.0)
    point_b = (AB, 0.0)
    point_d = (AB * cos(2 * gamma), AB * sin(2 * gamma))

    # Determine the circumcircle through A, B, and D
    center, radius = define_circle_from_points(point_a, point_b, point_d)

    # Line through B at angle (pi/2 - alpha)
    slope_m = tan(pi / 2 - alpha)
    intercept_b = point_b[1] - slope_m * point_b[0]

    # Find intersection of this ray with the circumcircle to locate vertex C
    _, point_c, found = line_circle_intersection(center, radius, (slope_m, intercept_b))

    if not found:
        continue

    dist_ad = distance(point_a, point_d)
    dist_cd = distance(point_c, point_d)
    dist_ac = distance(point_a, point_c)
    dist_bc = distance(point_b, point_c)

    # Check whether the problem condition AB + BC == CD is satisfied
    if abs(dist_cd - (AB + dist_bc)) < 0.0001:
        break

# Compute angle CDA using the Law of Cosines on triangle ACD
angle_cda, _ = law_of_cosines(dist_ad, dist_cd, dist_ac)

# -----------------------------------------------------------------------------
# Visualization
# -----------------------------------------------------------------------------

plt.figure(figsize=(9, 8))

# Draw quadrilateral edges and diagonal AC
plot_line(point_a, point_b, color="black", linewidth=2)
plot_line(point_a, point_d, color="black", linewidth=2)
plot_line(point_b, point_c, color="black", linewidth=2)
plot_line(point_c, point_d, color="black", linewidth=2)
plot_line(point_a, point_c, color="darkorange", linestyle=":", linewidth=1.5)

# Draw the circumscribed circle
plot_circle(center, radius)

# Add coordinate and vertex labels
label_point("A", point_a, offset=(-1.0, -1.0))
label_point("B", point_b, offset=(0.5, -1.0))
label_point("C", point_c, offset=(0.5, 0.5))
label_point("D", point_d, offset=(-1.2, 0.5))

plt.title(f"Cyclic Quadrilateral ABCD\nAngle CDA = {degrees(angle_cda):.1f}° (Exact: 60°)", fontsize=13)
plt.axis("equal")
plt.axis("off")
plt.tight_layout()
plt.show()
