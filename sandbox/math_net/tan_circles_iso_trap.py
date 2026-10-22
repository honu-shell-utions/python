# =============================================================================
# Jim McCleery
# October 22, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=rmm_2019_f4d767
# =============================================================================

from math import sqrt
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Core Geometric Helper Functions
# -----------------------------------------------------------------------------

def distance(A, B):
    """
    Calculate the straight-line distance between two points A and B.
    Each point is given as a tuple: (x, y).
    Uses the Pythagorean theorem: distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    """
    return sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


def mid_point(A, B):
    """
    Find the midpoint directly between two points A and B.
    Formula: ((x1 + x2) / 2, (y1 + y2) / 2)
    """
    return ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)


def circle_through_points(A, B, C):
    """
    Find the center (x, y) and radius of the circle passing through 3 points.
    Solves the circumcenter using determinant formulas.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    s1 = x1**2 + y1**2
    s2 = x2**2 + y2**2
    s3 = x3**2 + y3**2

    # Determinants for circumcenter calculation
    d = 2 * (x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2))
    if d == 0:
        return (0, 0), 0, False  # Points are collinear

    center_x = (s1 * (y2 - y3) + s2 * (y3 - y1) + s3 * (y1 - y2)) / d
    center_y = (s1 * (x3 - x2) + s2 * (x1 - x3) + s3 * (x2 - x1)) / d
    center = (center_x, center_y)

    radius = distance(A, center)
    return center, radius, True


def intersection_of_lines(line1, line2):
    """
    Find the intersection point (x, y) of two lines in slope-intercept form:
        y = m * x + b
    Lines are represented as tuples: (m, b).
    """
    m1, b1 = line1
    m2, b2 = line2

    if m1 == m2:
        return (0, 0), False  # Lines are parallel and do not intersect

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return (x, y), True


# -----------------------------------------------------------------------------
# Plotting Helper Functions
# -----------------------------------------------------------------------------

def plot_line(A, B, **kwargs):
    """Draw a line segment between points A and B."""
    plt.plot([A[0], B[0]], [A[1], B[1]], **kwargs)


def plot_circle(center, radius, **kwargs):
    """Draw a circle given its center (x, y) and radius."""
    angles = np.linspace(0, 2 * np.pi, 500)
    x = center[0] + radius * np.cos(angles)
    y = center[1] + radius * np.sin(angles)
    plt.plot(x, y, **kwargs)


def label_point(pt, name, offset=(0.5, 0.5)):
    """Plot a dot at the point and place a text label nearby."""
    plt.plot(pt[0], pt[1], 'ko', markersize=5)
    plt.text(pt[0] + offset[0], pt[1] + offset[1], name, fontsize=11, fontweight='bold')


# -----------------------------------------------------------------------------
# Geometric Construction
# Problem: Let ABCD be an isosceles trapezoid with AB || CD.
#          E is the midpoint of AC.
#          omega (w) is circumcircle of triangle ABE.
#          Omega (W) is circumcircle of triangle CDE.
#          P is the intersection of the tangent to omega at A and
#          the tangent to Omega at D.
# -----------------------------------------------------------------------------

# 1. Define dimensions of the isosceles trapezoid ABCD
base_AB = 24
base_CD = 16
horizontal_offset = (base_AB - base_CD) // 2
height_h = 8

# 2. Coordinates of the trapezoid vertices
A = (0, 0)
B = (base_AB, 0)
C = (base_AB - horizontal_offset, height_h)
D = (horizontal_offset, height_h)

# 3. E is the midpoint of diagonal AC
E = mid_point(A, C)

# 4. Circumcircles: omega (triangle ABE) and Omega (triangle CDE)
c_omega, r_omega, _ = circle_through_points(A, B, E)
c_Omega, r_Omega, _ = circle_through_points(D, E, C)

# 5. Tangent line to circle omega at point A
#    The tangent is perpendicular to the radius from center to A.
slope_radius_A = (A[1] - c_omega[1]) / (A[0] - c_omega[0])
slope_tangent_A = -1 / slope_radius_A
intercept_tangent_A = A[1] - slope_tangent_A * A[0]
line_tangent_A = (slope_tangent_A, intercept_tangent_A)

# Segment endpoints for visual display of the tangent at A
F1 = (-30, A[1] + slope_tangent_A * (-30 - A[0]))
F2 = (30, A[1] + slope_tangent_A * (30 - A[0]))

# 6. Tangent line to circle Omega at point D
#    The tangent is perpendicular to the radius from center to D.
slope_radius_D = (D[1] - c_Omega[1]) / (D[0] - c_Omega[0])
slope_tangent_D = -1 / slope_radius_D
intercept_tangent_D = D[1] - slope_tangent_D * D[0]
line_tangent_D = (slope_tangent_D, intercept_tangent_D)

# Segment endpoints for visual display of the tangent at D
F3 = (-20, D[1] + slope_tangent_D * (-20 - D[0]))
F4 = (30, D[1] + slope_tangent_D * (30 - D[0]))

# 7. Point P: intersection of the two tangents
P, _ = intersection_of_lines(line_tangent_A, line_tangent_D)

# -----------------------------------------------------------------------------
# Visualization & Coordinate Labeling
# -----------------------------------------------------------------------------

plt.figure(figsize=(10, 8))

# Draw the trapezoid ABCD
plot_line(A, B, color='black', linewidth=1.5)
plot_line(B, C, color='black', linewidth=1.5)
plot_line(C, D, color='black', linewidth=1.5)
plot_line(D, A, color='black', linewidth=1.5)

# Draw diagonal AC
plot_line(A, C, color='gray', linestyle='--', alpha=0.6)

# Draw circumcircles
plot_circle(c_omega, r_omega, color='blue', linestyle=':', label=r'Circle $omega$ (ABE)')
plot_circle(c_Omega, r_Omega, color='green', linestyle=':', label=r'Circle $Omega$ (CDE)')

# Draw tangents through P
plot_line(F1, F2, color='tab:blue', alpha=0.5, label='Tangent at A')
plot_line(F3, F4, color='tab:green', alpha=0.5, label='Tangent at D')

# Draw line PE (tangent to circle Omega)
plot_line(P, E, color='crimson', linewidth=2, label='Line PE (tangent to $Omega$)')

# Add coordinate point markers and labels based on the problem statement
label_point(A, 'A (0, 0)', offset=(-4.5, -1.5))
label_point(B, f'B ({B[0]}, {B[1]})', offset=(0.8, -1.0))
label_point(C, f'C ({C[0]}, {C[1]})', offset=(0.8, 0.5))
label_point(D, f'D ({D[0]}, {D[1]})', offset=(-3.5, 0.8))
label_point(E, f'E ({E[0]:.1f}, {E[1]:.1f})', offset=(0.8, -1.2))
label_point(P, f'P ({P[0]:.1f}, {P[1]:.1f})', offset=(-5.0, 1.0))

plt.title('RMM 2019 Problem: Tangency of PE to Circle $Omega$', fontsize=12)
plt.axis('equal')
plt.axis('off')
plt.legend(loc='upper right', frameon=True)
plt.tight_layout()
plt.show()
