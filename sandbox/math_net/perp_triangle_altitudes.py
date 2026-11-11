# -----------------------------------------------------------------------------
# Jim McCleery
# November 10, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=slk_2025_5ff090
# -----------------------------------------------------------------------------
"""
This script models and visually verifies the geometry problem:
- Altitudes of an acute scalene triangle ABC meet at orthocenter H.
- M and N are midpoints of AB and CH.
- R is the foot of the perpendicular from H to line CM.
- T is the second intersection of line MN with the circumcircle of triangle CNR.
- P is the circumcenter of the triangle formed by lines CM, AH, and BH.
- We demonstrate that lines HP and CT are perpendicular (product of slopes = -1).
"""

from math import pi, sqrt, sin, cos, tan, acos
import numpy as np
import matplotlib.pyplot as plt


# =============================================================================
# HELPER GEOMETRY FUNCTIONS
# =============================================================================

def distance(A, B):
    """
    Calculate straight-line Euclidean distance between two points:
    d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    """
    x1, y1 = A
    x2, y2 = B
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def mid_point(A, B):
    """
    Find the midpoint of the line segment connecting points A and B.
    """
    x1, y1 = A
    x2, y2 = B
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def law_of_cosines(side_a, side_b, side_c):
    """
    Find the angle (in radians) opposite to 'side_c' using the Law of Cosines:
    c^2 = a^2 + b^2 - 2ab * cos(C)
    """
    try:
        cosine_val = (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)
        # Clamp values to [-1, 1] to avoid math domain errors from rounding
        cosine_val = max(-1.0, min(1.0, cosine_val))
        return acos(cosine_val), True
    except ZeroDivisionError:
        return 0, False


def intersection_of_lines(line1, line2):
    """
    Find the intersection of two lines given in slope-intercept form (m, b),
    where y = m*x + b.
    """
    m1, b1 = line1
    m2, b2 = line2

    if m1 == m2:
        return (0, 0), False  # Lines are parallel

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return (x, y), True


def line_intersection_from_points(A, B, C, D):
    """
    Find the intersection point of line AB and line CD.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D

    try:
        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y4 - y3) / (x4 - x3)

        x = (y1 - slope1 * x1 - y3 + slope2 * x3) / (slope2 - slope1)
        y = y1 + slope1 * (x - x1)
        return (x, y), True
    except ZeroDivisionError:
        return (0, 0), False


def define_circle_from_points(A, B, C):
    """
    Find the circumcenter and radius of the unique circle passing through
    three non-collinear points A, B, and C.
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


def quadratic_equation(A, B, C):
    """
    Solve quadratic equation A*x^2 + B*x + C = 0 using the quadratic formula.
    """
    try:
        discriminant = B**2 - 4 * A * C
        if discriminant < 0:
            return 0, 0, False

        root = sqrt(discriminant)
        x1 = (-B - root) / (2 * A)
        x2 = (-B + root) / (2 * A)
        return x1, x2, True
    except (ValueError, ZeroDivisionError):
        return 0, 0, False


def line_circle_intersection(C, radius, line):
    """
    Find intersection points between a circle (center C, radius) and a
    line y = m*x + b.
    """
    center_x, center_y = C
    m, b = line

    # Substitute y = m*x + b into (x - cx)^2 + (y - cy)^2 = r^2
    quad_A = 1 + m**2
    quad_B = -2 * center_x + 2 * m * b - 2 * m * center_y
    quad_C = (center_x**2 + b**2 - 2 * b * center_y + center_y**2 - radius**2)

    x1, x2, ok = quadratic_equation(quad_A, quad_B, quad_C)
    if not ok:
        return (0, 0), (0, 0), False

    P1 = (x1, m * x1 + b)
    P2 = (x2, m * x2 + b)
    return P1, P2, True


def plot_circle(center, radius, **kwargs):
    """
    Draw a full circle given its center (x, y) and radius.
    """
    angles = np.linspace(0, 2 * pi, 500)
    x_vals = center[0] + radius * np.cos(angles)
    y_vals = center[1] + radius * np.sin(angles)
    plt.plot(x_vals, y_vals, **kwargs)


def plot_line(A, B, **kwargs):
    """
    Draw a line segment between points A and B.
    """
    plt.plot([A[0], B[0]], [A[1], B[1]], **kwargs)


# =============================================================================
# MAIN GEOMETRY SETUP
# =============================================================================

# Step 1: Define side lengths for an acute scalene triangle ABC
AB_len = 8.5
BC_len = 9.7
AC_len = 6.7

# Compute the internal angles of the triangle
alpha, _ = law_of_cosines(AB_len, AC_len, BC_len)
beta, _ = law_of_cosines(AB_len, BC_len, AC_len)

# Step 2: Establish coordinate system
# Place A at origin, B along positive x-axis, and compute C
A = (0.0, 0.0)
B = (AB_len, 0.0)
C = (AC_len * cos(alpha), AC_len * sin(alpha))

# Step 3: Find the orthocenter H (intersection of altitudes)
# The altitude from C is vertical: x = C[0].
# The altitude from B is perpendicular to AC (slope = -1 / tan(alpha)).
m_alt_b = -1.0 / tan(alpha)
H = (C[0], B[1] + m_alt_b * (C[0] - B[0]))

# Step 4: Midpoints M (of AB) and N (of CH)
M = mid_point(A, B)
N = mid_point(C, H)

# Step 5: Find point R (foot of perpendicular from H to median line CM)
m_cm = (C[1] - M[1]) / (C[0] - M[0])
b_cm = C[1] - m_cm * C[0]

m_perp = -1.0 / m_cm
b_perp = H[1] - m_perp * H[0]

R, _ = intersection_of_lines((m_cm, b_cm), (m_perp, b_perp))

# Step 6: Circumcircle of triangle CNR
CC, r_CNR = define_circle_from_points(C, N, R)

# Step 7: Find point T (second intersection of line MN with circumcircle of CNR)
m_mn = (M[1] - N[1]) / (M[0] - N[0])
b_mn = M[1] - m_mn * M[0]
T1, T2, _ = line_circle_intersection(CC, r_CNR, (m_mn, b_mn))

# Exclude point N to pick point T
T = T2 if distance(T1, N) < 1e-6 else T1

# Step 8: Circumcenter P of triangle formed by lines CM, AH, and BH
# Q1: Intersection of AH and BH (which is H)
# Q2: Intersection of CM and BH
# Q3: Intersection of AH and CM
Q1, _ = line_intersection_from_points(A, H, B, H)
Q2, _ = line_intersection_from_points(C, M, B, H)
Q3, _ = line_intersection_from_points(A, H, C, M)

P, r_circum = define_circle_from_points(Q1, Q2, Q3)

# Step 9: Verify perpendicularity of HP and CT via slope product
m_HP = (H[1] - P[1]) / (H[0] - P[0])
m_CT = (C[1] - T[1]) / (C[0] - T[0])
slope_product = m_HP * m_CT


# =============================================================================
# PLOTTING AND COORDINATE LABELS
# =============================================================================

plt.figure(figsize=(9, 8))

# Draw circles
plot_circle(CC, r_CNR, linestyle="--", color="steelblue", label="Circumcircle CNR")
plot_circle(P, r_circum, linestyle=":", color="mediumpurple", label="Circumcircle of Δ(AH, BH, CM)")

# Draw triangle ABC
plot_line(A, B, color="black", linewidth=1.5)
plot_line(B, C, color="black", linewidth=1.5)
plot_line(A, C, color="black", linewidth=1.5)

# Draw internal lines and segments
plot_line(C, M, color="gray", linestyle="-", label="Median CM")
plot_line(M, N, color="orange", linestyle="--", label="Line MN")
plot_line(H, P, color="crimson", linewidth=2, label="Line HP")
plot_line(C, T, color="forestgreen", linewidth=2, label="Line CT")
plot_line(H, R, color="gray", linestyle=":")
plot_line(A, H, color="gray", linestyle=":")
plot_line(B, H, color="gray", linestyle=":")

# Plot key points and add coordinate text labels
labeled_points = {
    "A": (A, (-15, -15)),
    "B": (B, (8, -10)),
    "C": (C, (-5, 10)),
    "H": (H, (8, 5)),
    "M": (M, (-5, -18)),
    "N": (N, (8, -2)),
    "R": (R, (-18, 5)),
    "T": (T, (8, -8)),
    "P": (P, (8, 5)),
}

for label, (pt, offset) in labeled_points.items():
    plt.plot(pt[0], pt[1], marker="o", markersize=5, color="black")
    # Display label along with its coordinates (x, y)
    text_label = f"{label} ({pt[0]:.2f}, {pt[1]:.2f})"
    plt.annotate(
        text_label,
        xy=pt,
        xytext=offset,
        textcoords="offset points",
        fontsize=8,
        fontweight="bold"
    )

# Configuration & Display
plt.title(
    f"Perpendicularity Verification: Lines HP and CT\n"
    f"Product of slopes m(HP) * m(CT) = {slope_product:0.2f}",
    fontsize=11
)
plt.axis("equal")
plt.axis("off")
plt.tight_layout()
plt.show()
