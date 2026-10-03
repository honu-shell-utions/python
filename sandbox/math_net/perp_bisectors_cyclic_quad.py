# Jim McCleery
# October 2, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=imo_2024_a60b6c

from math import pi, sqrt, sin, cos, tan, asin
import numpy as np
import matplotlib.pyplot as plt
from random import uniform


# -----------------------------------------------------------------------------
# Essential Geometry Helper Functions
# -----------------------------------------------------------------------------

def distance(A, B):
    """
    Calculate the Euclidean (straight-line) distance between two points:
    distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    """
    return sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


def mid_point(A, B):
    """
    Find the midpoint of segment AB by averaging the coordinates.
    """
    return ((A[0] + B[0]) / 2.0, (A[1] + B[1]) / 2.0)


def define_circle_from_points(A, B, C):
    """
    Find the center (x, y) and radius r of the circumcircle passing
    through three non-collinear points A, B, and C.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    temp = x2**2 + y2**2
    bc = (x1**2 + y1**2 - temp) / 2.0
    cd = (temp - x3**2 - y3**2) / 2.0

    determinant = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    center_x = (bc * (y2 - y3) - cd * (y1 - y2)) / determinant
    center_y = ((x1 - x2) * cd - (x2 - x3) * bc) / determinant
    center = (center_x, center_y)

    radius = distance(center, A)
    return center, radius


def quadratic_equation(A, B, C):
    """
    Solve Ax^2 + Bx + C = 0 using the quadratic formula.
    Returns (x1, x2, True) if real roots exist, else (0, 0, False).
    """
    discriminant = B**2 - 4 * A * C
    if discriminant < 0:
        return 0, 0, False

    root_disc = sqrt(discriminant)
    x1 = (-B - root_disc) / (2 * A)
    x2 = (-B + root_disc) / (2 * A)
    return min(x1, x2), max(x1, x2), True


def line_circle_intersection(center, radius, line):
    """
    Find the intersection points of circle (center, radius)
    and line y = m*x + b.
    """
    cx, cy = center
    m, b = line

    # Substitute y = m*x + b into (x - cx)^2 + (y - cy)^2 = r^2
    A = 1 + m**2
    B = -2 * cx + 2 * m * b - 2 * m * cy
    C_val = cx**2 + b**2 - 2 * b * cy + cy**2 - radius**2

    x1, x2, ok = quadratic_equation(A, B, C_val)
    if not ok:
        return (0, 0), (0, 0), False

    P1 = (x1, m * x1 + b)
    P2 = (x2, m * x2 + b)
    return P1, P2, True


def perpendicular_bisector(P1, P2):
    """
    Return the line (slope, intercept) representing the
    perpendicular bisector of segment P1-P2.
    """
    mid = mid_point(P1, P2)
    dx = P2[0] - P1[0]
    dy = P2[1] - P1[1]

    # The slope of segment P1-P2 is dy / dx.
    # The perpendicular slope is -dx / dy.
    m_perp = -dx / dy
    b_perp = mid[1] - m_perp * mid[0]
    return (m_perp, b_perp)


def intersection_of_lines(line1, line2):
    """
    Find the intersection point (x, y) of two lines:
    y = m1*x + b1 and y = m2*x + b2.
    """
    m1, b1 = line1
    m2, b2 = line2

    if abs(m1 - m2) < 1e-12:
        return (0, 0), False

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return (x, y), True


def cross_product_2d(A, B, P):
    """
    Compute the 2D cross product of vector AB and AP:
    (B_x - A_x) * (P_y - A_y) - (B_y - A_y) * (P_x - A_x).
    The sign reveals which side of line AB point P lies on.
    """
    return (B[0] - A[0]) * (P[1] - A[1]) - (B[1] - A[1]) * (P[0] - A[0])


# -----------------------------------------------------------------------------
# Main Figure Generation Loop
# -----------------------------------------------------------------------------

for attempt in range(10**4):
    # 1. Randomly sample side lengths and angles to define triangle ABD
    BD = uniform(2, 10)
    AD = uniform(BD + 0.5, 20)  # Guarantee BD < AD
    alpha = uniform(0.2, pi / 2 - 0.1)  # Angle DBA < 90 degrees

    # Law of Sines to find angle BAD (beta)
    sin_beta = BD * sin(alpha) / AD
    if sin_beta >= 1.0:
        continue
    beta = asin(sin_beta)
    gamma = pi - alpha - beta
    AB = AD * sin(gamma) / sin(alpha)

    # Place vertices in the coordinate system
    B = (0.0, 0.0)
    D = (BD * cos(pi - alpha), BD * sin(pi - alpha))
    A = (-AB, 0.0)

    # 2. Find circumcircle through A, B, and D
    circumcenter, R = define_circle_from_points(A, B, D)

    # 3. Choose ray AC with angle theta inside angle BAD
    theta = uniform(0.05, beta - 0.05)
    m_AC = tan(theta)
    b_AC = A[1] - m_AC * A[0]
    line_AC = (m_AC, b_AC)

    # The ray intersects the circumcircle at vertex A and vertex C
    P1, P2, ok = line_circle_intersection(circumcenter, R, line_AC)
    if not ok:
        continue
    # Pick the intersection point distinct from A
    C = P2 if distance(P1, A) < 1e-4 else P1

    AC = distance(A, C)
    # Check problem condition: AC < BD < AD
    if not (AC < BD < AD):
        continue

    # Side check for C with respect to line AD
    side_C = cross_product_2d(A, D, C)

    # 4. Construct Point E:
    # E lies on line through D parallel to AB (horizontal line)
    # DE = AC, and E, C are on opposite sides of line AD.
    E1 = (D[0] + AC, D[1])
    E2 = (D[0] - AC, D[1])
    E = E1 if cross_product_2d(A, D, E1) * side_C < 0 else E2

    # Verify opposite-side condition
    if cross_product_2d(A, D, E) * side_C >= 0:
        continue

    # 5. Construct Point F:
    # F lies on line through A parallel to CD
    # AF = BD, and F, C are on opposite sides of line AD.
    cd_len = distance(C, D)
    if cd_len < 1e-6:
        continue
    u_cd = ((D[0] - C[0]) / cd_len, (D[1] - C[1]) / cd_len)

    F1 = (A[0] + BD * u_cd[0], A[1] + BD * u_cd[1])
    F2 = (A[0] - BD * u_cd[0], A[1] - BD * u_cd[1])
    F = F1 if cross_product_2d(A, D, F1) * side_C < 0 else F2

    # Verify opposite-side condition
    if cross_product_2d(A, D, F) * side_C >= 0:
        continue

    # 6. Find perpendicular bisectors of BC and EF
    bisector_BC = perpendicular_bisector(B, C)
    bisector_EF = perpendicular_bisector(E, F)

    # Find their intersection point K
    K, ok = intersection_of_lines(bisector_BC, bisector_EF)
    if not ok:
        continue

    # Check that K lies on the circumcircle: distance(circumcenter, K) == R
    dist_K_to_center = distance(circumcenter, K)
    print(f"Circumcircle Radius: {R:.4f}")
    print(f"Distance from Center to Intersection Point K: {dist_K_to_center:.4f}")
    print(f"Difference: {abs(dist_K_to_center - R):.2e}")

    # -------------------------------------------------------------------------
    # Plotting & Visualization
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 10))

    # Helper function to plot lines
    def draw_segment(P1, P2, color="gray", linestyle="-", lw=1.2):
        ax.plot([P1[0], P2[0]], [P1[1], P2[1]], color=color, linestyle=linestyle, linewidth=lw)

    # Draw cyclic quadrilateral ABCD
    draw_segment(A, B, color="black", lw=1.6)
    draw_segment(B, C, color="black", lw=1.6)
    draw_segment(C, D, color="black", lw=1.6)
    draw_segment(D, A, color="black", lw=1.6)

    # Draw diagonals and problem-defined segments
    draw_segment(A, C, color="blue", linestyle="--", lw=1.0)
    draw_segment(B, D, color="blue", linestyle="--", lw=1.0)
    draw_segment(D, E, color="purple", lw=1.4)
    draw_segment(A, F, color="orange", lw=1.4)
    draw_segment(E, F, color="brown", lw=1.4)

    # Draw circumcircle
    angles = np.linspace(0, 2 * pi, 600)
    ax.plot(
        circumcenter[0] + R * np.cos(angles),
        circumcenter[1] + R * np.sin(angles),
        color="steelblue",
        linestyle="-.",
        label="Circumcircle",
    )

    # Draw perpendicular bisectors intersecting at K
    mid_BC = mid_point(B, C)
    mid_EF = mid_point(E, F)
    draw_segment(mid_BC, K, color="crimson", linestyle=":", lw=1.8)
    draw_segment(mid_EF, K, color="crimson", linestyle=":", lw=1.8)

    # Plot and annotate all named vertices
    labeled_points = {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "E": E,
        "F": F,
        "K": K,
        "I (center)": circumcenter,
    }

    for name, pt in labeled_points.items():
        marker = "ro" if name == "K" else "ko"
        ax.plot(pt[0], pt[1], marker)
        ax.annotate(
            f" {name}\n ({pt[0]:.2f}, {pt[1]:.2f})",
            xy=pt,
            xytext=(6, 6),
            textcoords="offset points",
            fontsize=9,
            weight="bold" if name == "K" else "normal",
        )

    ax.set_aspect("equal", "box")
    ax.set_title("IMO 2024 Problem 4: Intersection K lies on the Circumcircle")
    ax.grid(True, linestyle="--", alpha=0.4)
    plt.show()

    # Successfully plotted a valid configuration, exit loop
    break
