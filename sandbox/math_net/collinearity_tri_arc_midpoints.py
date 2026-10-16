# -----------------------------------------------------------------------------
# Jim McCleery
# October 16, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=bxm_2025_be509d
# -----------------------------------------------------------------------------

from math import acos, cos, pi, sin, sqrt
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Helper Geometry Functions
# =============================================================================

def distance(A, B):
    """
    Calculate the straight-line (Euclidean) distance between two points.
    
    Parameters:
        A, B: Points represented as (x, y) tuples.
    """
    x1, y1 = A
    x2, y2 = B
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def law_of_cosines(d1, d2, side):
    """
    Find the angle opposite to 'side' in a triangle using the Law of Cosines.
    
    Formula: c^2 = a^2 + b^2 - 2ab * cos(C)
    
    Returns:
        (angle_in_radians, True) if the side lengths form a valid triangle,
        (0.0, False) otherwise.
    """
    try:
        cosine_val = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        # Clamp value between -1.0 and 1.0 to guard against small floating-point rounding errors
        cosine_val = max(-1.0, min(1.0, cosine_val))
        return acos(cosine_val), True
    except (ValueError, ZeroDivisionError):
        return 0.0, False


def define_circle_from_points(A, B, C):
    """
    Find the circumcenter and radius of the circle passing through three points.
    
    Returns:
        ((center_x, center_y), radius)
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    temp = x2**2 + y2**2
    bc = (x1**2 + y1**2 - temp) / 2
    cd = (temp - x3**2 - y3**2) / 2

    determinant = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    center_x = (bc * (y2 - y3) - cd * (y1 - y2)) / determinant
    center_y = ((x1 - x2) * cd - (x2 - x3) * bc) / determinant
    center = (center_x, center_y)

    radius = distance(center, A)
    return center, radius


def incircle_of_triangle(A, B, C):
    """
    Find the incenter (I) and inradius of a triangle.
    
    Returns:
        ((center_x, center_y), radius)
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    # Side lengths opposite to vertices A, B, and C
    a = distance(B, C)
    b = distance(A, C)
    c = distance(A, B)

    # Semiperimeter and triangle area (via Heron's formula)
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    radius = area / s

    # The incenter is the weighted average of the vertices weighted by side lengths
    center_x = (a * x1 + b * x2 + c * x3) / (a + b + c)
    center_y = (a * y1 + b * y2 + c * y3) / (a + b + c)

    return (center_x, center_y), radius


def mid_point(A, B):
    """Return the midpoint of the line segment joining points A and B."""
    return ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)


# =============================================================================
# Plotting Helpers
# =============================================================================

def plot_circle(C, radius, **kwargs):
    """Draw a smooth circle outline given a center and radius."""
    angles = np.linspace(0, 2 * pi, 500)
    x_vals = radius * np.cos(angles) + C[0]
    y_vals = radius * np.sin(angles) + C[1]
    plt.plot(x_vals, y_vals, **kwargs)


def plot_line(A, B, **kwargs):
    """Draw a line segment connecting two points."""
    plt.plot([A[0], B[0]], [A[1], B[1]], **kwargs)


def label_point(P, label_text, offset=(0.3, 0.3), color="black"):
    """
    Plot a point marker and place its text label beside it.
    
    Parameters:
        P: (x, y) coordinates of the point
        label_text: text string to display
        offset: (dx, dy) spacing so the text does not overlap the dot
    """
    plt.plot(P[0], P[1], "o", color=color, markersize=5)
    plt.text(P[0] + offset[0], P[1] + offset[1], label_text, fontsize=10, weight="bold")


# =============================================================================
# Main Simulation & Construction
# =============================================================================

# Try random triangle side lengths
for _ in range(20):
    AB = uniform(8, 16)
    BC = uniform(8, 16)
    AC = uniform(8, 16)

    # Validate triangle inequality using Law of Cosines
    alpha, valid_a = law_of_cosines(AB, AC, BC)
    beta, valid_b = law_of_cosines(AB, BC, AC)
    if not (valid_a and valid_b):
        continue

    gamma = pi - alpha - beta

    # Position vertex A at the origin and B along the positive x-axis
    A = (0.0, 0.0)
    B = (AB, 0.0)
    C = (AC * cos(alpha), AC * sin(alpha))

    try:
        # Circumcircle (center CC, radius Rcc) and Incircle (incenter IC = I)
        CC, Rcc = define_circle_from_points(A, B, C)
        IC, Ric = incircle_of_triangle(A, B, C)
    except ZeroDivisionError:
        continue

    # Arc midpoints on the circumcircle:
    # F is the midpoint of arc AB (subtends angle gamma/2 from the opposite vertex)
    theta_F = -pi / 2
    F = (CC[0] + Rcc * cos(theta_F), CC[1] + Rcc * sin(theta_F))

    # D is the midpoint of arc BC
    theta_D = theta_F + (pi - beta)
    D = (CC[0] + Rcc * cos(theta_D), CC[1] + Rcc * sin(theta_D))

    # D' is diametrically opposite to D
    D_prime = (CC[0] + Rcc * cos(theta_D + pi), CC[1] + Rcc * sin(theta_D + pi))

    # E is the midpoint of arc CA
    theta_E = theta_D + (pi - gamma)
    E = (CC[0] + Rcc * cos(theta_E), CC[1] + Rcc * sin(theta_E))

    # M is the midpoint of chord [EF]
    M = mid_point(E, F)

    # -------------------------------------------------------------------------
    # Visualization
    # -------------------------------------------------------------------------
    plt.figure(figsize=(9, 9))

    # Plot triangle ABC
    plot_line(A, B, color="black", lw=1.5)
    plot_line(B, C, color="black", lw=1.5)
    plot_line(C, A, color="black", lw=1.5)

    # Plot circumcircle and incircle
    plot_circle(CC, Rcc, color="steelblue", linestyle="--", label="Circumcircle (Ω)")
    plot_circle(IC, Ric, color="orange", linestyle=":", label="Incircle")

    # Plot chord [EF] and collinear line through I, D', and M
    plot_line(E, F, color="gray", linestyle="-.", alpha=0.7, label="Chord [EF]")
    plot_line(D_prime, IC, color="crimson", lw=1.8, label="Collinear Line (I - M - D')")

    # Add labeled points
    label_point(A, "A", offset=(-0.6, -0.6))
    label_point(B, "B", offset=(0.3, -0.6))
    label_point(C, "C", offset=(0.0, 0.4))
    label_point(IC, "I (Incenter)", offset=(0.3, 0.2), color="darkorange")
    label_point(D, "D", offset=(0.3, 0.2), color="purple")
    label_point(D_prime, "D'", offset=(0.3, 0.2), color="crimson")
    label_point(E, "E", offset=(-0.8, 0.2), color="purple")
    label_point(F, "F", offset=(0.2, -0.6), color="purple")
    label_point(M, "M", offset=(-0.8, -0.4), color="darkgreen")

    # Titles and formatting
    plt.title(
        "Collinearity of Incenter I, Arc Opposite D', and Midpoint M of [EF]",
        fontsize=12,
        pad=15,
        weight="bold",
    )
    plt.legend(loc="upper left", frameon=True)
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.show()

