# Jim McCleery
# September 27, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=btw_2002_78e13e
#
# Problem statement from image:
# Let ABC be an acute triangle with \angle BAC > \angle BCA, and let D be a point on
# side AC such that |AB| = |BD|. Furthermore, let F be a point on the circumcircle
# of triangle ABC such that line FD is perpendicular to side BC and points F, B lie
# on different sides of line AC. Prove that line FB is perpendicular to side AC.

from math import acos, cos, pi, sin, sqrt, tan
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Geometry Helper Functions
# -----------------------------------------------------------------------------
def distance(A, B):
    """Calculate the straight-line distance between two points A and B.

    Each point is a tuple of coordinates: (x, y).
    """
    x1, y1 = A
    x2, y2 = B
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def quadratic_equation(A, B, C):
    """Solve the quadratic equation: A*x^2 + B*x + C = 0.

    Returns (x1, x2, True) sorted such that x1 <= x2 if real solutions exist.
    Otherwise returns (0, 0, False).
    """
    try:
        discriminant = B**2 - 4 * A * C
        if discriminant < 0:
            return 0, 0, False

        root_d = sqrt(discriminant)
        x1 = (-B - root_d) / (2 * A)
        x2 = (-B + root_d) / (2 * A)

        if x1 > x2:
            x1, x2 = x2, x1

        return x1, x2, True
    except (ValueError, ZeroDivisionError):
        return 0, 0, False


def circle_through_points(A, B, C):
    """Find the center (x, y) and radius r of the circle passing through points A, B, and C."""
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    try:
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2

        # 3x3 determinant minors for the circumcircle equation
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
        radius = distance(A, center)

        return center, radius, True
    except (ValueError, ZeroDivisionError):
        return (0, 0), 0, False


def intersection_of_lines(line1, line2):
    """Find the intersection point of two lines given in slope-intercept form (m, b).

    y = m1*x + b1
    y = m2*x + b2
    """
    m1, b1 = line1
    m2, b2 = line2

    if m1 == m2:
        return (0, 0), False  # Parallel lines do not meet

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return (x, y), True


def line_circle_intersection(C, radius, line):
    """Find the two points where the line y = m*x + b intersects the circle.

    C is the center tuple (cx, cy).
    """
    center_x, center_y = C
    m, b = line

    # Substitute y = m*x + b into (x - cx)^2 + (y - cy)^2 = r^2
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
# Plotting Helper Functions
# -----------------------------------------------------------------------------
def plot_point(P, label="", offset=(0.3, 0.3)):
    """Plot a single point as a red dot and annotate it with a text label and coordinates."""
    x, y = P
    plt.plot(x, y, "ro", markersize=5)
    if label:
        # Display the letter and coordinate rounded to 2 decimal places: e.g., A(0.00, 0.00)
        text = f"{label} ({x:.2f}, {y:.2f})"
        plt.text(x + offset[0], y + offset[1], text, fontsize=9, weight="bold")


def plot_line(P1, P2, style="b-", linewidth=1.5):
    """Plot a straight line segment connecting point P1 and point P2."""
    plt.plot([P1[0], P2[0]], [P1[1], P2[1]], style, linewidth=linewidth)


def plot_circle(C, radius, color="gray", linestyle="--"):
    """Plot the circumference of a circle given its center and radius."""
    angles = np.linspace(0, 2 * pi, 500)
    x_coords = C[0] + radius * np.cos(angles)
    y_coords = C[1] + radius * np.sin(angles)
    plt.plot(x_coords, y_coords, color=color, linestyle=linestyle, linewidth=1)


# -----------------------------------------------------------------------------
# Main Simulation Loop
# -----------------------------------------------------------------------------
for _ in range(10**3):
    plt.cla()

    # Step 1: Generate random acute angles alpha (angle A) and beta (angle B)
    alpha = uniform(0, pi / 2)
    beta = uniform(0, pi / 2)
    gamma = pi - alpha - beta  # Angle C

    # Ensure triangle ABC is acute and satisfies the condition angle A > angle C
    if not (0 < gamma < pi / 2 and alpha > gamma):
        continue

    # Step 2: Set side AB along the x-axis and find coordinates for A, B, and C
    AB = 10.0
    AC = AB * sin(beta) / sin(gamma)  # Law of Sines

    A = (0.0, 0.0)
    B = (AB, 0.0)
    C = (AC * cos(alpha), AC * sin(alpha))

    # Step 3: Circumcircle through A, B, C
    O, r, _ = circle_through_points(A, B, C)

    # Step 4: Locate point D on segment AC such that |AB| = |BD|
    # Triangle ABD is isosceles with |AB| = |BD|, so angle ADB = angle BAD = alpha.
    # Therefore, AD = 2 * AB * cos(alpha).
    AD = 2 * AB * cos(alpha)
    D = (AD * cos(alpha), AD * sin(alpha))

    # Step 5: Construct line through D perpendicular to BC
    # Line BC has direction angle (pi - beta), giving slope -tan(beta).
    # A line perpendicular to BC has slope m_perp = 1 / tan(beta).
    m_perp = 1.0 / tan(beta)
    b_perp = D[1] - m_perp * D[0]

    # Intersect this perpendicular line with the circumcircle to find F
    P1, P2, ok = line_circle_intersection(O, r, (m_perp, b_perp))
    if not ok:
        continue

    # Line AC runs along angle alpha; a point (x, y) is on the opposite side of AC
    # from B if its signed perpendicular distance (y - tan(alpha)*x) has the opposite
    # sign of B's. Since B has y=0 and x>0, y_B - m_AC * x_B < 0, so F must satisfy y - m_AC * x > 0.
    m_AC = tan(alpha)
    if (P1[1] - m_AC * P1[0]) > 0:
        F = P1
    else:
        F = P2

    # Step 6: Plot the geometric elements
    plot_circle(O, r)

    # Triangle sides
    plot_line(A, B, "k-", linewidth=1.5)
    plot_line(B, C, "k-", linewidth=1.5)
    plot_line(A, C, "k-", linewidth=1.5)

    # Auxiliary lines
    plot_line(B, D, "g--", linewidth=1.2)  # Segment BD showing |AB| = |BD|
    plot_line(F, D, "m-.", linewidth=1.2)  # Line FD perpendicular to BC
    plot_line(F, B, "r-", linewidth=2.0)   # Segment FB (to prove FB perpendicular to AC)

    # Add labeled points with coordinates
    plot_point(A, "A", offset=(-0.8, -0.6))
    plot_point(B, "B", offset=(0.3, -0.6))
    plot_point(C, "C", offset=(0.2, 0.4))
    plot_point(D, "D", offset=(0.3, -0.3))
    plot_point(F, "F", offset=(-1.2, 0.4))

    # Step 7: Verify perpendicularity
    # Line AC slope: m1 = tan(alpha)
    # Line FB slope: m2
    m1 = tan(alpha)
    m2 = (F[1] - B[1]) / (F[0] - B[0])
    product = m1 * m2

    plt.title(
        f"Product of slopes (m_AC * m_FB) = {product:0.3f}\n"
        f"Perpendicular condition verified: m1 * m2 = -1",
        fontsize=10,
    )

    plt.axis("equal")
    plt.axis("off")
    plt.pause(1)

plt.show()
