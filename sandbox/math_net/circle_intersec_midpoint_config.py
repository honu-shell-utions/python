# -----------------------------------------------------------------------------
# Jim McCleery
# September 29, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=btw_2006_ef71a7
#
# Problem verification:
# Let ABC be a triangle, B1 the midpoint of AB, and C1 the midpoint of AC.
# P is the intersection (other than A) of circumcircles ABC1 and AB1C.
# P1 is the intersection (other than A) of line AP with circumcircle AB1C1.
# This program verifies numerically that 2 * AP = 3 * AP1.
# -----------------------------------------------------------------------------

from math import pi, sqrt, sin, cos
from random import uniform
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------

def distance(A, B):
    """
    Calculate the straight-line distance between two points A and B.
    Each point is represented as a tuple: (x, y).
    """
    x1, y1 = A
    x2, y2 = B
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def mid_point(A, B):
    """
    Calculate the midpoint between two points A and B.
    Formula: ((x1 + x2) / 2, (y1 + y2) / 2)
    """
    x1, y1 = A
    x2, y2 = B
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def circle_through_points(A, B, C):
    """
    Find the unique circle (circumcircle) passing through 3 points: A, B, and C.
    
    Returns:
        (center, radius, True) where center is (center_x, center_y).
        ((0, 0), 0, False) if the points are collinear or cannot form a circle.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    try:
        # Sum of squares for each point coordinate
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2

        # Determinants used to find the circle center
        M11 = (
            x1 * y2 + x2 * y3 + x3 * y1
            - x2 * y1 - x3 * y2 - x1 * y3
        )
        M12 = (
            s1 * y2 + s2 * y3 + s3 * y1
            - s2 * y1 - s3 * y2 - s1 * y3
        )
        M13 = (
            s1 * x2 + s2 * x3 + s3 * x1
            - s2 * x1 - s3 * x2 - s1 * x3
        )

        center_x = 0.5 * M12 / M11
        center_y = -0.5 * M13 / M11
        center = (center_x, center_y)

        # The radius is the distance from the center to any vertex
        radius = distance(A, center)

        return center, radius, True

    except (ValueError, ZeroDivisionError):
        return (0, 0), 0, False


def circle_circle_intersections(C0, r0, C1, r1):
    """
    Find the two points where two circles intersect each other.
    
    Parameters:
        C0: (x, y) center of the first circle
        r0: radius of the first circle
        C1: (x, y) center of the second circle
        r1: radius of the second circle
        
    Returns:
        (P1, P2, True) where P1 and P2 are (x, y) tuples.
    """
    x0, y0 = C0
    x1, y1 = C1

    try:
        # Distance between circle centers
        d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

        # Distance from C0 along center-line to the chord connecting intersection points
        a = (r0**2 - r1**2 + d**2) / (2 * d)

        # Half-length of the chord connecting the two intersection points
        h = sqrt(r0**2 - a**2)

        # Base point on the line connecting the centers
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d

        # The two intersection coordinates
        P1 = (
            x2 + h * (y1 - y0) / d,
            y2 - h * (x1 - x0) / d
        )
        P2 = (
            x2 - h * (y1 - y0) / d,
            y2 + h * (x1 - x0) / d
        )

        return P1, P2, True

    except (ValueError, ZeroDivisionError):
        return (0, 0), (0, 0), False


def quadratic_equation(A, B, C):
    """
    Solve a standard quadratic equation: A*x^2 + B*x + C = 0.
    Returns: (root1, root2, True) where root1 <= root2.
    """
    try:
        discriminant = B**2 - 4 * A * C
        square_root = sqrt(discriminant)

        x1 = (-B - square_root) / (2 * A)
        x2 = (-B + square_root) / (2 * A)

        if x1 > x2:
            x1, x2 = x2, x1

        return x1, x2, True
    except (ValueError, ZeroDivisionError):
        return 0, 0, False


def line_circle_intersection(C, radius, line):
    """
    Find the intersection points between a circle and a line (y = m*x + b).
    
    Parameters:
        C: circle center (x, y)
        radius: circle radius
        line: tuple (m, b) for slope and intercept
        
    Returns:
        (P1, P2, True) where P1 and P2 are (x, y) coordinates.
    """
    center_x, center_y = C
    m, b = line

    # Substitute y = m*x + b into (x - h)^2 + (y - k)^2 = r^2
    A = 1 + m**2
    B = -2 * center_x + 2 * m * b - 2 * m * center_y
    C_val = center_x**2 + b**2 - 2 * b * center_y + center_y**2 - radius**2

    x1, x2, ok = quadratic_equation(A, B, C_val)
    if not ok:
        return (0, 0), (0, 0), False

    P1 = (x1, m * x1 + b)
    P2 = (x2, m * x2 + b)
    return P1, P2, True


# -----------------------------------------------------------------------------
# Plotting Helpers
# -----------------------------------------------------------------------------

def plot_circle(C, radius):
    """Plot the circumference of a circle given its center and radius."""
    center_x, center_y = C
    angles = np.linspace(0, 2 * pi, 500)
    x_values = radius * np.cos(angles) + center_x
    y_values = radius * np.sin(angles) + center_y
    plt.plot(x_values, y_values, linestyle="--", alpha=0.5)


def plot_line(A, B, style="k-"):
    """Plot a straight line segment connecting point A to point B."""
    plt.plot([A[0], B[0]], [A[1], B[1]], style)


def label_point(pt, name, offset=(0.2, 0.2)):
    """Plot a dot and place an adjacent text label at the point."""
    plt.plot(pt[0], pt[1], 'ko', markersize=4)
    plt.text(pt[0] + offset[0], pt[1] + offset[1], name, fontsize=11, fontweight='bold')


# -----------------------------------------------------------------------------
# Main Simulation Loop
# -----------------------------------------------------------------------------

for _ in range(100):
    plt.cla()

    # Generate random side length AB and interior angles alpha and beta
    AB = uniform(5, 20)
    alpha = uniform(0.2, pi / 2)
    beta = uniform(0.2, pi / 2)
    gamma = pi - alpha - beta

    # Keep angles acute/non-degenerate for clean visualization
    if gamma <= 0 or gamma > pi / 2:
        continue

    # Law of Sines: calculate side AC
    AC = AB * sin(beta) / sin(gamma)

    # Triangle vertices
    A = (0.0, 0.0)
    B = (AB, 0.0)
    C = (AC * cos(alpha), AC * sin(alpha))

    # Midpoints
    B1 = mid_point(A, B)
    C1 = mid_point(A, C)

    # Circumcircle of triangle AB1C
    Z1, r1, _ = circle_through_points(A, B1, C)
    plot_circle(Z1, r1)

    # Circumcircle of triangle ABC1
    Z2, r2, _ = circle_through_points(A, B, C1)
    plot_circle(Z2, r2)

    # Circumcircle of triangle AB1C1
    Z3, r3, _ = circle_through_points(A, B1, C1)
    plot_circle(Z3, r3)

    # Point P: the intersection of circumcircles (AB1C) and (ABC1) other than A
    inter1, inter2, _ = circle_circle_intersections(Z2, r2, Z1, r1)
    # Pick the intersection point that is not vertex A (0, 0)
    P = inter2 if distance(inter1, A) < 1e-4 else inter1

    # Line through A(0, 0) and P: y = m*x + 0
    if abs(P[0]) < 1e-6:
        continue  # Skip nearly vertical lines to avoid division by zero
    m = P[1] / P[0]
    line_AP = (m, 0.0)

    # Point P1: intersection of line AP with circumcircle (AB1C1) other than A
    p_cand1, p_cand2, _ = line_circle_intersection(Z3, r3, line_AP)
    P1 = p_cand2 if distance(p_cand1, A) < 1e-4 else p_cand1

    # Compute distances AP and AP1
    d1 = distance(A, P)
    d2 = distance(A, P1)

    # Draw triangle edges and the ray AP
    plot_line(A, B, "b-")
    plot_line(B, C, "b-")
    plot_line(C, A, "b-")
    plot_line(A, P, "r--")

    # Add labels for all key coordinates
    label_point(A, "A", (-0.6, -0.6))
    label_point(B, "B", (0.3, -0.4))
    label_point(C, "C", (0.0, 0.4))
    label_point(B1, "$B_1$", (0.0, -0.8))
    label_point(C1, "$C_1$", (-0.7, 0.2))
    label_point(P, "P", (0.3, 0.3))
    label_point(P1, "$P_1$", (-0.6, 0.4))

    # Display dynamic title showing 2 * AP and 3 * AP1
    plt.title(f"2 x AP = {2 * d1:0.4f},  3 x AP1 = {3 * d2:0.4f}")
    plt.axis("off")
    plt.axis("equal")
    plt.pause(1)

plt.show()
