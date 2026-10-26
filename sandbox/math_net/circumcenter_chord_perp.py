# Jim McCleery
# October 26, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=ibe_1999_c3c584
#
# Problem visualization:
# O is the circumcenter of the acute-angled triangle ABC.
# The altitudes are AD, BE, and CF.
# The line EF cuts the circumcircle at P and Q.
# Show that OA is perpendicular to PQ.
# If M is the midpoint of BC, show that AP^2 = 2 * AD * OM.

from math import pi, sqrt, sin, cos, tan, acos
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# =============================================================================
# Helper Geometry Functions
# =============================================================================

def distance(A, B):
    """
    Calculate the straight-line (Euclidean) distance between two points.
    
    A point is represented as a tuple: (x, y).
    Using the Pythagorean theorem: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    """
    x1, y1 = A
    x2, y2 = B
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def mid_point(A, B):
    """
    Find the midpoint of the line segment connecting point A and point B.
    
    The coordinates of the midpoint are the averages of the x- and y-coordinates.
    """
    x1, y1 = A
    x2, y2 = B
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def law_of_cosines(side_a, side_b, side_opposite):
    """
    Find the angle (in radians) opposite to 'side_opposite' using the Law of Cosines.
    
    c^2 = a^2 + b^2 - 2*a*b*cos(C)  ==>  cos(C) = (a^2 + b^2 - c^2) / (2*a*b)
    
    Returns:
        (angle, True) if a valid triangle exists, or (0, False) if invalid.
    """
    try:
        cos_val = (side_a**2 + side_b**2 - side_opposite**2) / (2 * side_a * side_b)
        
        # Clamp values to [-1.0, 1.0] to guard against minor floating-point rounding errors
        cos_val = max(-1.0, min(1.0, cos_val))
        
        angle = acos(cos_val)
        return angle, True
    except (ValueError, ZeroDivisionError):
        return 0, False


def define_circle_from_points(A, B, C):
    """
    Find the circumcenter (O) and radius (r) of the circle passing through
    three non-collinear points A, B, and C.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    temp = x2**2 + y2**2
    bc = (x1**2 + y1**2 - temp) / 2
    cd = (temp - x3**2 - y3**2) / 2

    # Determinant of the coordinate matrix
    determinant = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    center_x = (bc * (y2 - y3) - cd * (y1 - y2)) / determinant
    center_y = ((x1 - x2) * cd - (x2 - x3) * bc) / determinant

    center = (center_x, center_y)
    radius = distance(center, A)

    return center, radius


def intersection_of_lines(line1, line2):
    """
    Find the point where two lines intersect.
    
    Each line is given in slope-intercept form (m, b), representing: y = m*x + b
    
    Returns:
        (intersection_point, True) if they intersect, or ((0, 0), False) if parallel.
    """
    m1, b1 = line1
    m2, b2 = line2

    # Parallel lines have identical slopes and do not intersect
    if m1 == m2:
        return (0, 0), False

    # Equate m1*x + b1 = m2*x + b2 to solve for x
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1

    return (x, y), True


def quadratic_equation(A, B, C):
    """
    Solve a quadratic equation of the form: A*x^2 + B*x + C = 0
    
    Returns:
        (x1, x2, True) where x1 <= x2, or (0, 0, False) if roots are complex.
    """
    try:
        discriminant = B**2 - 4 * A * C
        if discriminant < 0:
            return 0, 0, False

        root = sqrt(discriminant)
        x1 = (-B - root) / (2 * A)
        x2 = (-B + root) / (2 * A)

        if x1 > x2:
            x1, x2 = x2, x1

        return x1, x2, True
    except (ValueError, ZeroDivisionError):
        return 0, 0, False


def line_circle_intersection(C, radius, line):
    """
    Find the intersection points of a circle and a line y = m*x + b.
    
    Substituting y = m*x + b into (x - h)^2 + (y - k)^2 = r^2 forms a quadratic equation.
    
    Returns:
        (P1, P2, True) if intersections exist, else ((0, 0), (0, 0), False).
    """
    center_x, center_y = C
    m, b = line

    quad_A = 1 + m**2
    quad_B = -2 * center_x + 2 * m * b - 2 * m * center_y
    quad_C = center_x**2 + b**2 - 2 * b * center_y + center_y**2 - radius**2

    x1, x2, ok = quadratic_equation(quad_A, quad_B, quad_C)
    if not ok:
        return (0, 0), (0, 0), False

    y1 = m * x1 + b
    y2 = m * x2 + b

    return (x1, y1), (x2, y2), True


# =============================================================================
# Plotting Helpers
# =============================================================================

def plot_line(A, B, color='black', linestyle='-', linewidth=1.2):
    """Plot a straight line segment between two points."""
    plt.plot([A[0], B[0]], [A[1], B[1]], color=color, linestyle=linestyle, linewidth=linewidth)


def plot_circle(C, radius, color='steelblue', linestyle='--'):
    """Plot a full circle with center C and given radius."""
    angles = np.linspace(0, 2 * pi, 500)
    x_vals = C[0] + radius * np.cos(angles)
    y_vals = C[1] + radius * np.sin(angles)
    plt.plot(x_vals, y_vals, color=color, linestyle=linestyle, linewidth=1)


def label_point(pt, name, offset=(0.3, 0.3), color='crimson'):
    """Plot a dot at the point and display its label."""
    plt.plot(pt[0], pt[1], 'o', color=color, markersize=5)
    plt.text(pt[0] + offset[0], pt[1] + offset[1], name, fontsize=11, fontweight='bold')


# =============================================================================
# Main Simulation Loop
# =============================================================================

plt.figure(figsize=(9, 8))

for _ in range(10):
    plt.clf()

    # Generate random side lengths for triangle ABC
    AB = uniform(6, 18)
    BC = uniform(6, 18)
    AC = uniform(6, 18)

    # Calculate angles alpha (at A) and beta (at B)
    alpha, ok1 = law_of_cosines(AB, AC, BC)
    if not ok1 or alpha >= pi / 2:
        continue  # Triangle must be acute-angled

    beta, ok2 = law_of_cosines(AB, BC, AC)
    if not ok2 or beta >= pi / 2:
        continue

    gamma = pi - alpha - beta
    if gamma >= pi / 2:
        continue  # All three angles must be acute (< 90 degrees)

    # 1. Triangle Vertices
    A = (0.0, 0.0)
    B = (AB, 0.0)
    C = (AC * cos(alpha), AC * sin(alpha))

    # 2. Circumcircle (O, r)
    O, r = define_circle_from_points(A, B, C)

    # 3. Altitude BE: Perpendicular from B to side AC
    slope_AC = tan(alpha)
    line_AC = (slope_AC, 0.0)
    slope_alt_B = -1.0 / slope_AC
    intercept_alt_B = B[1] - slope_alt_B * B[0]
    line_alt_B = (slope_alt_B, intercept_alt_B)
    E, _ = intersection_of_lines(line_AC, line_alt_B)

    # 4. Altitude CF: Perpendicular from C to side AB (along y = 0)
    F = (C[0], 0.0)

    # 5. Altitude AD: Perpendicular from A to side BC
    slope_BC = tan(pi - beta)
    intercept_BC = B[1] - slope_BC * B[0]
    line_BC = (slope_BC, intercept_BC)
    slope_alt_A = -1.0 / slope_BC
    line_alt_A = (slope_alt_A, 0.0)
    D, _ = intersection_of_lines(line_BC, line_alt_A)

    # 6. Line EF and its intersections with the circumcircle: P and Q
    slope_EF = (F[1] - E[1]) / (F[0] - E[0])
    intercept_EF = F[1] - slope_EF * F[0]
    line_EF = (slope_EF, intercept_EF)
    P, Q, ok_PQ = line_circle_intersection(O, r, line_EF)
    if not ok_PQ:
        continue

    # 7. Midpoint M of segment BC
    M = mid_point(B, C)

    # -------------------------------------------------------------------------
    # Draw Geometry
    # -------------------------------------------------------------------------
    # Triangle ABC sides
    plot_line(A, B, color='black', linewidth=1.5)
    plot_line(B, C, color='black', linewidth=1.5)
    plot_line(C, A, color='black', linewidth=1.5)

    # Circumcircle
    plot_circle(O, r, color='royalblue', linestyle='--')

    # Line segments specified in the theorem
    plot_line(P, Q, color='darkgreen', linestyle='-', linewidth=1.5)
    plot_line(O, A, color='purple', linestyle='-', linewidth=1.5)
    plot_line(A, D, color='gray', linestyle=':', linewidth=1.2)
    plot_line(B, E, color='gray', linestyle=':', linewidth=1.0)
    plot_line(C, F, color='gray', linestyle=':', linewidth=1.0)
    plot_line(O, M, color='darkorange', linestyle='--', linewidth=1.2)

    # Coordinate labels from the problem statement
    label_point(A, "A", offset=(-0.7, -0.6))
    label_point(B, "B", offset=(0.3, -0.6))
    label_point(C, "C", offset=(0.0, 0.5))
    label_point(O, "O", offset=(0.3, -0.5), color='royalblue')
    label_point(D, "D", offset=(0.3, 0.2), color='gray')
    label_point(E, "E", offset=(-0.7, 0.2), color='gray')
    label_point(F, "F", offset=(0.0, -0.7), color='gray')
    label_point(P, "P", offset=(-0.8, 0.2), color='darkgreen')
    label_point(Q, "Q", offset=(0.3, 0.2), color='darkgreen')
    label_point(M, "M", offset=(0.3, 0.2), color='darkorange')

    # -------------------------------------------------------------------------
    # Verify Mathematical Relations:
    # 1) OA perpendicular to PQ
    # 2) AP^2 = 2 * AD * OM
    # -------------------------------------------------------------------------
    AP = distance(A, P)
    AD = distance(A, D)
    OM = distance(O, M)

    val_AP2 = AP**2
    val_2_AD_OM = 2 * AD * OM

    plt.title(
        f"$AP^2 = {val_AP2:.4f}$   vs   $2 \\cdot AD \\cdot OM = {val_2_AD_OM:.4f}$\n"
        f"Difference: {abs(val_AP2 - val_2_AD_OM):.2e}",
        fontsize=12,
        pad=10
    )

    plt.axis('equal')
    plt.axis('off')
    plt.tight_layout()
    plt.pause(1.5)

plt.show()
