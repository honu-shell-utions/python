# Jim McCleery
# October 11, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=jbm_2016_9ca113

from math import pi, sqrt, sin, cos, acos
from random import uniform
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------


def distance(A, B):
    """Calculates the straight-line Euclidean distance between two points (x, y)."""
    return sqrt((A[0] - B[0]) ** 2 + (A[1] - B[1]) ** 2)


def law_of_cosines(d1, d2, side):
    """Computes an interior angle in radians given three sides of a triangle."""
    try:
        cosine_val = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        # Clamp between -1 and 1 to prevent rounding errors outside valid acos domain
        cosine_val = max(-1.0, min(1.0, cosine_val))
        return acos(cosine_val), True
    except (ValueError, ZeroDivisionError):
        return 0.0, False


def define_circle_from_points(A, B, C):
    """Finds the center (x, y) and radius R of a circle passing through three points."""
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    temp = x2**2 + y2**2
    bc = (x1**2 + y1**2 - temp) / 2
    cd = (temp - x3**2 - y3**2) / 2

    det = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    cx = (bc * (y2 - y3) - cd * (y1 - y2)) / det
    cy = ((x1 - x2) * cd - (x2 - x3) * bc) / det
    center = (cx, cy)
    radius = distance(center, A)

    return center, radius


def circle_circle_intersections(C0, r0, C1, r1):
    """Finds the two intersection points of two circles."""
    x0, y0 = C0
    x1, y1 = C1

    try:
        d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
        a = (r0**2 - r1**2 + d**2) / (2 * d)
        h = sqrt(r0**2 - a**2)

        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d

        P1 = (x2 + h * (y1 - y0) / d, y2 - h * (x1 - x0) / d)
        P2 = (x2 - h * (y1 - y0) / d, y2 + h * (x1 - x0) / d)
        return P1, P2, True
    except (ValueError, ZeroDivisionError):
        return (0, 0), (0, 0), False


def line_circle_intersection(C, radius, line):
    """
    Finds the intersection points of a circle centered at C and a line (y = m*x + b).
    Solves using the standard quadratic formula.
    """
    cx, cy = C
    m, b = line

    A = 1 + m**2
    B = -2 * cx + 2 * m * b - 2 * m * cy
    C_val = cx**2 + b**2 - 2 * b * cy + cy**2 - radius**2

    discriminant = B**2 - 4 * A * C_val
    if discriminant < 0:
        return (0, 0), (0, 0), False

    root_d = sqrt(discriminant)
    x1 = (-B - root_d) / (2 * A)
    x2 = (-B + root_d) / (2 * A)

    P1 = (x1, m * x1 + b)
    P2 = (x2, m * x2 + b)
    return P1, P2, True


# -----------------------------------------------------------------------------
# PLOTTING ROUTINES
# -----------------------------------------------------------------------------


def plot_line(A, B, color="black", linestyle="-", linewidth=1.0):
    """Draws a straight segment between points A and B."""
    plt.plot([A[0], B[0]], [A[1], B[1]], color=color, linestyle=linestyle, linewidth=linewidth)


def plot_circle(C, radius, color="blue", linestyle="-", linewidth=1.0):
    """Traces the circumference of a circle given its center and radius."""
    angles = np.linspace(0, 2 * pi, 600)
    xs = radius * np.cos(angles) + C[0]
    ys = radius * np.sin(angles) + C[1]
    plt.plot(xs, ys, color=color, linestyle=linestyle, linewidth=linewidth)


def plot_labeled_point(pt, name, offset=(0.15, 0.15), color="black"):
    """Plots a single point as a dot and writes its label nearby."""
    plt.plot(pt[0], pt[1], "o", color=color, markersize=5)
    plt.text(pt[0] + offset[0], pt[1] + offset[1], name, fontsize=11, fontweight="bold", color=color)


# -----------------------------------------------------------------------------
# MAIN GEOMETRIC SIMULATION
# -----------------------------------------------------------------------------

error = 0.05
solved = False

for _ in range(500):
    # 1. Randomly generate side lengths for triangle ABC
    bc = uniform(6, 9)
    ac = uniform(6, 9)
    ab = uniform(6, 9)

    beta, ok1 = law_of_cosines(ab, bc, ac)
    gamma, ok2 = law_of_cosines(bc, ac, ab)
    if not (ok1 and ok2):
        continue

    alpha = pi - beta - gamma

    # Triangle must be acute-angled
    if max(alpha, beta, gamma) >= pi / 2:
        continue

    # 2. Place vertices A, B, C on Cartesian plane
    B = (0.0, 0.0)
    C = (bc, 0.0)
    A = (ab * cos(beta), ab * sin(beta))

    # Circumcircle of triangle ABC: center O and radius R
    O, R = define_circle_from_points(A, B, C)

    # 3. Choose interior points D, E, F on sides BC, AC, and AB
    # D is on side BC
    d_param = uniform(0.2, 0.8)
    D = (d_param * bc, 0.0)

    # E is on side AC
    e_param = uniform(0.2, 0.8)
    E = (C[0] + e_param * (A[0] - C[0]), C[1] + e_param * (A[1] - C[1]))

    # F is on side AB
    f_param = uniform(0.2, 0.8)
    F = (f_param * A[0], f_param * A[1])

    # Radii for circles c1, c2, c3
    r3 = distance(F, A)  # Circle c1: centered at F with radius FA
    r1 = distance(D, B)  # Circle c2: centered at D with radius DB
    r2 = distance(E, C)  # Circle c3: centered at E with radius EC

    # 4. Find points K, L, M on the circumcircle (c)
    # Circle (c1) intersects (c) at A and K
    K1, K2, ok_k = circle_circle_intersections(O, R, F, r3)
    if not ok_k:
        continue
    K = K1 if distance(K1, A) > error else K2

    # Circle (c2) intersects (c) at B and L
    L1, L2, ok_l = circle_circle_intersections(O, R, D, r1)
    if not ok_l:
        continue
    L = L1 if distance(L1, B) > error else L2

    # Circle (c3) intersects (c) at C and M
    M1, M2, ok_m = circle_circle_intersections(O, R, E, r2)
    if not ok_m:
        continue
    M = M1 if distance(M1, C) > error else M2

    # 5. Find points A', B', C' along segments OA, OB, OC
    # Intersection of line OA with circle (c1)
    if abs(A[0] - O[0]) < 1e-6:
        continue
    m_oa = (A[1] - O[1]) / (A[0] - O[0])
    b_oa = A[1] - m_oa * A[0]
    p1, p2, ok_a = line_circle_intersection(F, r3, (m_oa, b_oa))
    if not ok_a:
        continue
    A_prime = p1 if distance(p1, A) > error else p2

    # Must lie on segment OA (strictly within radius R from O)
    if distance(O, A_prime) > R or distance(A, A_prime) > R:
        continue

    # Intersection of line OB with circle (c2)
    if abs(B[0] - O[0]) < 1e-6:
        continue
    m_ob = (B[1] - O[1]) / (B[0] - O[0])
    b_ob = B[1] - m_ob * B[0]
    p1, p2, ok_b = line_circle_intersection(D, r1, (m_ob, b_ob))
    if not ok_b:
        continue
    B_prime = p1 if distance(p1, B) > error else p2

    if distance(O, B_prime) > R or distance(B, B_prime) > R:
        continue

    # Intersection of line OC with circle (c3)
    if abs(C[0] - O[0]) < 1e-6:
        continue
    m_oc = (C[1] - O[1]) / (C[0] - O[0])
    b_oc = C[1] - m_oc * C[0]
    p1, p2, ok_c = line_circle_intersection(E, r2, (m_oc, b_oc))
    if not ok_c:
        continue
    C_prime = p1 if distance(p1, C) > error else p2

    if distance(O, C_prime) > R or distance(C, C_prime) > R:
        continue

    # 6. Construct circumcircles of the quadrilaterals:
    # BKFA', CLDB', and AMEC'
    BKF, rBKF = define_circle_from_points(B, K, F)
    CLD, rCLD = define_circle_from_points(C, L, D)
    AME, rAME = define_circle_from_points(A, M, E)

    # 7. Render Figure
    plt.figure(figsize=(9, 9))

    # Triangle ABC sides
    plot_line(A, B, color="black", linewidth=1.5)
    plot_line(B, C, color="black", linewidth=1.5)
    plot_line(C, A, color="black", linewidth=1.5)

    # Radii segments to vertices (OA, OB, OC)
    plot_line(A, O, color="gray", linestyle="--")
    plot_line(B, O, color="gray", linestyle="--")
    plot_line(C, O, color="gray", linestyle="--")

    # Circumcircle of triangle ABC
    plot_circle(O, R, color="black", linewidth=1.2)

    # Circumcircles of quadrilaterals BKFA', CLDB', AMEC'
    plot_circle(BKF, rBKF, color="tab:blue", linestyle="-", linewidth=1.2)
    plot_circle(CLD, rCLD, color="tab:green", linestyle="-", linewidth=1.2)
    plot_circle(AME, rAME, color="tab:red", linestyle="-", linewidth=1.2)

    # Plot labeled points
    plot_labeled_point(A, "A", offset=(0.1, 0.2))
    plot_labeled_point(B, "B", offset=(-0.35, -0.2))
    plot_labeled_point(C, "C", offset=(0.15, -0.2))
    plot_labeled_point(O, "O", offset=(0.15, -0.2), color="purple")

    plot_labeled_point(D, "D", offset=(0.0, -0.35), color="tab:green")
    plot_labeled_point(E, "E", offset=(0.15, 0.1), color="tab:red")
    plot_labeled_point(F, "F", offset=(-0.35, 0.1), color="tab:blue")

    plot_labeled_point(K, "K", offset=(0.15, 0.15), color="tab:blue")
    plot_labeled_point(L, "L", offset=(-0.35, 0.15), color="tab:green")
    plot_labeled_point(M, "M", offset=(0.15, -0.2), color="tab:red")

    plot_labeled_point(A_prime, "A'", offset=(0.15, 0.1), color="tab:blue")
    plot_labeled_point(B_prime, "B'", offset=(0.15, 0.1), color="tab:green")
    plot_labeled_point(C_prime, "C'", offset=(-0.35, 0.1), color="tab:red")

    plt.axis("equal")
    plt.axis("off")
    plt.title("Cyclic Quadrilaterals & Common Concurrent Point", fontsize=12)
    plt.show()

    solved = True
    break
