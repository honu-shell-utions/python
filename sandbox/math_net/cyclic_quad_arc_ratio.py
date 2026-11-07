# Jim McCleery
# November 7, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=cps_2011_5bb58f
# -----------------------------------------------------------------------------
# Problem Simulation:
# Points A, B, C, D lie on a circle in that order.
# The arc(AB) containing C, D is twice the arc(CD) not containing A, B.
# E is chosen such that AC = AE and BD = BE, lying on the same side of AB.
# The perpendicular line from E to AB bisects arc(CD) at M.
# This script searches numerically for a matching configuration and plots it,
# labeling all key vertices and showing that angle ACB = 108 degrees.
# -----------------------------------------------------------------------------

from math import pi, sqrt, sin, cos, tan, acos, degrees
from random import uniform
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------
# Core Geometric Helper Functions
# -----------------------------------------------------------------------------


def distance(point1, point2):
    """Calculates the straight-line distance between two points (x, y) using the

    Pythagorean theorem: distance = sqrt((x1 - x2)^2 + (y1 - y2)^2).
    """
    x1, y1 = point1
    x2, y2 = point2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def define_circle_from_points(A, B, C):
    """Finds the unique circle that passes through three points A, B, and C.

    Returns:
        center: (x, y) coordinates of the circle center
        radius: the radius of the circle
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


def law_of_cosines(side_a, side_b, side_c):
    """Calculates the angle (in radians) opposite to side_c in a triangle with

    sides side_a, side_b, and side_c using the Law of Cosines:
    cos(C) = (a^2 + b^2 - c^2) / (2 * a * b).
    """
    try:
        cos_val = (side_a**2 + side_b**2 - side_c**2) / (2 * side_a * side_b)
        # Clamp to [-1.0, 1.0] to prevent small floating point rounding issues
        cos_val = max(-1.0, min(1.0, cos_val))
        return acos(cos_val), True
    except (ValueError, ZeroDivisionError):
        return 0.0, False


def central_angle(radius, chord_length):
    """Returns the central angle subtended by a chord of given length in a

    circle with the given radius.
    """
    return law_of_cosines(radius, radius, chord_length)


def solve_quadratic(a, b, c):
    """Solves the standard quadratic equation a*x^2 + b*x + c = 0.

    Returns (x1, x2, True) where x1 <= x2 if real roots exist, else (0, 0,
    False).
    """
    discriminant = b**2 - 4 * a * c
    if discriminant < 0 or a == 0:
        return 0.0, 0.0, False

    root_disc = sqrt(discriminant)
    x1 = (-b - root_disc) / (2 * a)
    x2 = (-b + root_disc) / (2 * a)

    if x1 > x2:
        x1, x2 = x2, x1

    return x1, x2, True


def line_circle_intersection(center, radius, line):
    """Finds the intersection points of a circle and a line y = m*x + b.

    Line is passed as a tuple: (slope, intercept).
    """
    cx, cy = center
    m, b = line

    # Substitute y = m*x + b into (x - cx)^2 + (y - cy)^2 = r^2
    # to form A*x^2 + B*x + C = 0:
    A = 1 + m**2
    B = -2 * cx + 2 * m * b - 2 * m * cy
    C = cx**2 + b**2 - 2 * b * cy + cy**2 - radius**2

    x1, x2, ok = solve_quadratic(A, B, C)
    if not ok:
        return (0, 0), (0, 0), False

    P1 = (x1, m * x1 + b)
    P2 = (x2, m * x2 + b)
    return P1, P2, True


def line_intersection_from_points(A, B, C, D):
    """Finds the intersection point of two lines: line AB and line CD."""
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D

    try:
        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y4 - y3) / (x4 - x3)

        # Solve for x where y1 + slope1*(x - x1) = y3 + slope2*(x - x3)
        x = (y1 - slope1 * x1 - y3 + slope2 * x3) / (slope2 - slope1)
        y = y1 + slope1 * (x - x1)
        return (x, y), True
    except ZeroDivisionError:
        return (0, 0), False


# -----------------------------------------------------------------------------
# Plotting Helper Functions
# -----------------------------------------------------------------------------


def plot_circle(center, radius):
    """Plots a complete circle given its center and radius."""
    cx, cy = center
    angles = np.linspace(0, 2 * pi, 500)
    x = cx + radius * np.cos(angles)
    y = cy + radius * np.sin(angles)
    plt.plot(x, y, color="steelblue", linewidth=1.5)


def plot_segment(A, B, color="black", linestyle="-"):
    """Plots a straight line segment between point A and point B."""
    plt.plot([A[0], B[0]], [A[1], B[1]], color=color, linestyle=linestyle)


def label_point(point, label, offset=(0.2, 0.2)):
    """Plots a dot at the point and displays its name and coordinates."""
    x, y = point
    plt.plot(x, y, "o", color="darkred", markersize=5)
    coord_text = f"{label} ({x:0.2f}, {y:0.2f})"
    plt.text(
        x + offset[0],
        y + offset[1],
        coord_text,
        fontsize=9,
        fontweight="semibold",
    )


# -----------------------------------------------------------------------------
# Simulation and Geometric Search
# -----------------------------------------------------------------------------

tolerance = 0.0001
AB_length = 10.0
A = (0.0, 0.0)
B = (AB_length, 0.0)

for _ in range(10):
    plt.cla()
    # Random search loop to find the configuration satisfying the problem conditions
    while True:
        # 1. Pick a random candidate point C in the upper half-plane
        C = (uniform(AB_length / 2, AB_length), uniform(AB_length / 4, AB_length))

        # 2. Define the circumscribed circle passing through A, B, C
        center, r = define_circle_from_points(A, B, C)
        dist_AC = distance(A, C)
        dist_BC = distance(B, C)

        # 3. Compute angles of triangle ABC
        theta, _ = law_of_cosines(dist_AC, dist_BC, AB_length)
        alpha = pi - theta
        gamma, _ = law_of_cosines(dist_BC, AB_length, dist_AC)
        beta = pi - alpha - gamma

        # 4. Find point D on the circle using line from origin with angle beta
        _, D, ok_D = line_circle_intersection(center, r, (tan(beta), 0.0))
        if not ok_D:
            continue

        # 5. E is the intersection of lines AD and CB
        E, ok_E = line_intersection_from_points(A, D, C, B)
        if not ok_E:
            continue

        # 6. H is the projection of E onto AB (x-axis), and M is the point on the circle
        #    directly above E and H (where the perpendicular line intersects the arc CD)
        H = (E[0], 0.0)
        radial_term = r**2 - (E[0] - center[0]) ** 2
        if radial_term < 0:
            continue

        M = (E[0], center[1] + sqrt(radial_term))

        # Ensure D, M, C appear in proper left-to-right horizontal order
        if not (D[0] < M[0] < C[0]):
            continue

        # 7. Calculate central angles subtended by each arc segment
        arc_AD, _ = central_angle(r, distance(A, D))
        arc_DM, _ = central_angle(r, distance(M, D))
        arc_MC, _ = central_angle(r, distance(M, C))
        arc_CB, _ = central_angle(r, distance(C, B))

        # Check problem conditions:
        # (a) M bisects arc(CD) -> arc_DM == arc_MC
        # (b) arc(AB) containing C,D equals twice arc(CD) -> (arc_AD + arc_CB) == (arc_DM + arc_MC)
        if (
            abs(arc_DM - arc_MC) < tolerance
            and abs((arc_AD + arc_CB) - (arc_DM + arc_MC)) < tolerance
        ):
            break

    # -----------------------------------------------------------------------------
    # Visualization
    # -----------------------------------------------------------------------------

    plt.figure(figsize=(9, 8))

    # Draw circle and problem chords / lines
    plot_circle(center, r)
    plot_segment(A, B, color="black", linestyle="-")
    plot_segment(A, C, color="royalblue")
    plot_segment(E, B, color="darkgreen")
    plot_segment(B, D, color="royalblue")
    plot_segment(C, D, color="darkorange")
    plot_segment(A, E, color="darkgreen")
    plot_segment(H, M, color="purple", linestyle="--")

    # Annotate each vertex with its name and (x, y) coordinates
    label_point(A, "A", offset=(-0.8, -0.6))
    label_point(B, "B", offset=(0.2, -0.6))
    label_point(C, "C", offset=(0.2, 0.2))
    label_point(D, "D", offset=(-1.8, 0.2))
    label_point(E, "E", offset=(0.2, 0.2))
    label_point(H, "H", offset=(-0.3, -0.6))
    label_point(M, "M", offset=(-0.5, 0.3))

    angle_deg = degrees(theta)
    plt.title(f"CPS 2011 Problem: $\\angle ACB$ = {angle_deg:0.1f}°", fontsize=13)
    plt.axis("equal")
    plt.axis("off")
    plt.tight_layout()
    plt.pause(0.5)
plt.show()
