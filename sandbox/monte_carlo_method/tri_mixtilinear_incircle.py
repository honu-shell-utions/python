# Jim McCleery
# September 17, 2026
# Kailua-Kona, HI
# https://mathnet.mit.edu/explorer.html?p=usa_2016_c46cfe

import matplotlib.pyplot as plt
import numpy as np
from math import acos, cos, sin, sqrt, tan


# -----------------------------------------------------------------------------
# Geometry helper functions
# -----------------------------------------------------------------------------

def distance(P, Q):
    """Return the Euclidean distance between points P and Q."""
    return sqrt((P[0] - Q[0]) ** 2 + (P[1] - Q[1]) ** 2)


def circle_through_points(A, B, C):
    """
    Return the circumcenter and radius of the circle through A, B, and C.

    Returns:
        center, radius

    Raises:
        ValueError: if A, B, and C are collinear.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    s1 = x1**2 + y1**2
    s2 = x2**2 + y2**2
    s3 = x3**2 + y3**2

    m11 = (
        x1 * y2 + x2 * y3 + x3 * y1
        - x2 * y1 - x3 * y2 - x1 * y3
    )

    if abs(m11) < 1e-12:
        raise ValueError("The three points are collinear.")

    m12 = (
        s1 * y2 + s2 * y3 + s3 * y1
        - s2 * y1 - s3 * y2 - s1 * y3
    )

    m13 = (
        s1 * x2 + s2 * x3 + s3 * x1
        - s2 * x1 - s3 * x2 - s1 * x3
    )

    x0 = 0.5 * m12 / m11
    y0 = -0.5 * m13 / m11

    center = (x0, y0)
    radius = distance(A, center)

    return center, radius


def law_of_cosines(a, b, c):
    """
    Return the angle opposite side c in a triangle with sides a, b, c.

    The angle is returned in radians.
    """
    cos_angle = (a**2 + b**2 - c**2) / (2 * a * b)

    # Protect against tiny floating-point excursions outside [-1, 1].
    cos_angle = max(-1.0, min(1.0, cos_angle))

    return acos(cos_angle)


def incircle_of_triangle(A, B, C):
    """Return the incenter and inradius of triangle ABC."""
    a = distance(B, C)  # opposite A
    b = distance(A, C)  # opposite B
    c = distance(A, B)  # opposite C

    semiperimeter = (a + b + c) / 2

    area = sqrt(
        semiperimeter
        * (semiperimeter - a)
        * (semiperimeter - b)
        * (semiperimeter - c)
    )

    radius = area / semiperimeter

    perimeter = a + b + c

    center = (
        (a * A[0] + b * B[0] + c * C[0]) / perimeter,
        (a * A[1] + b * B[1] + c * C[1]) / perimeter,
    )

    return center, radius


def orthocenter(A, B, C):
    """Return the orthocenter of triangle ABC."""
    ax, ay = A
    bx, by = B
    cx, cy = C

    # Altitude from A is perpendicular to BC.
    a1 = cx - bx
    b1 = cy - by
    c1 = ax * a1 + ay * b1

    # Altitude from B is perpendicular to AC.
    a2 = cx - ax
    b2 = cy - ay
    c2 = bx * a2 + by * b2

    det = a1 * b2 - a2 * b1

    if abs(det) < 1e-12:
        raise ValueError("Degenerate triangle.")

    x = (c1 * b2 - c2 * b1) / det
    y = (a1 * c2 - a2 * c1) / det

    return x, y


# -----------------------------------------------------------------------------
# Construct the geometry
# -----------------------------------------------------------------------------

def get_geometry(BC):
    """
    Construct triangle ABC for the given length BC.

    Fixed side lengths:
        AB = sqrt(3)
        AC = 2
    """
    AB = sqrt(3)
    AC = 2

    angle_B = law_of_cosines(AB, BC, AC)
    angle_C = law_of_cosines(AC, BC, AB)

    # Place BC on the x-axis.
    B = (0.0, 0.0)
    C = (BC, 0.0)
    A = (
        AB * cos(angle_B),
        AB * sin(angle_B),
    )

    # Incircle.
    I, r = incircle_of_triangle(A, B, C)

    # D is the point where the incircle touches BC.
    D = (
        r / tan(angle_B / 2),
        0.0,
    )

    # Mixtilinear incircle radii.
    r_B = r / cos(angle_B / 2) ** 2
    r_C = r / cos(angle_C / 2) ** 2

    # Mixtilinear incircle centers.
    O_B = (
        r_B / tan(angle_B / 2),
        r_B,
    )

    O_C = (
        C[0] - r_C / tan(angle_C / 2),
        r_C,
    )

    H = orthocenter(A, B, C)

    return A, B, C, D, H, I, r, O_B, O_C, r_B, r_C


def perpendicularity_error(BC):
    """
    Return DH · O_B O_C.

    The desired configuration satisfies DH perpendicular to O_B O_C,
    so this value is zero.
    """
    _, _, _, D, H, _, _, O_B, O_C, _, _ = get_geometry(BC)

    DH = (
        H[0] - D[0],
        H[1] - D[1],
    )

    OBOC = (
        O_C[0] - O_B[0],
        O_C[1] - O_B[1],
    )

    return DH[0] * OBOC[0] + DH[1] * OBOC[1]


# -----------------------------------------------------------------------------
# Solve for BC by bisection
# -----------------------------------------------------------------------------

def solve_for_BC(tolerance=1e-12):
    """Solve perpendicularity_error(BC) = 0 by bisection."""
    low = 2 - sqrt(3) + 1e-4
    high = 2 + sqrt(3) - 1e-4

    f_low = perpendicularity_error(low)
    f_high = perpendicularity_error(high)

    if f_low * f_high > 0:
        raise ValueError("The initial interval does not bracket a root.")

    while high - low > tolerance:
        mid = (low + high) / 2
        f_mid = perpendicularity_error(mid)

        if f_low * f_mid <= 0:
            high = mid
        else:
            low = mid
            f_low = f_mid

    return (low + high) / 2


# -----------------------------------------------------------------------------
# Plotting helpers
# -----------------------------------------------------------------------------

def draw_line(ax, P, Q, style="k-", lw=1.5):
    """Draw a line segment from P to Q."""
    ax.plot(
        [P[0], Q[0]],
        [P[1], Q[1]],
        style,
        linewidth=lw,
    )


def draw_circle(ax, center, radius, color="gray", lw=1.2, ls="--"):
    """Draw a circle."""
    theta = np.linspace(0, 2 * np.pi, 500)

    x = center[0] + radius * np.cos(theta)
    y = center[1] + radius * np.sin(theta)

    ax.plot(
        x,
        y,
        color=color,
        linewidth=lw,
        linestyle=ls,
    )


# -----------------------------------------------------------------------------
# Main
# -----------------------------------------------------------------------------

BC_solution = solve_for_BC()

A, B, C, D, H, I, r, O_B, O_C, r_B, r_C = get_geometry(BC_solution)

circumcenter, circumradius = circle_through_points(A, B, C)

fig, ax = plt.subplots(figsize=(8, 7))

# Triangle ABC.
draw_line(ax, A, B, lw=2)
draw_line(ax, B, C, lw=2)
draw_line(ax, C, A, lw=2)

# Perpendicular segments DH and O_B O_C.
draw_line(ax, D, H, style="crimson", lw=1.8)
draw_line(ax, O_B, O_C, style="teal", lw=1.8)

# Circles.
draw_circle(ax, I, r, color="purple", ls="-")          # incircle
draw_circle(ax, O_B, r_B, color="teal", ls=":")       # B-mixtilinear
draw_circle(ax, O_C, r_C, color="teal", ls=":")       # C-mixtilinear
draw_circle(
    ax,
    circumcenter,
    circumradius,
    color="steelblue",
    ls="-",
)                                                      # circumcircle

# Points and labels.
points = {
    "A":       (A, (-0.08, 0.05)),
    "B":       (B, (-0.12, -0.08)),
    "C":       (C, (0.05, -0.08)),
    "D":       (D, (-0.02, -0.12)),
    "H":       (H, (0.05, 0.02)),
    "I":       (I, (0.05, 0.02)),
    "$O_B$":   (O_B, (-0.15, 0.05)),
    "$O_C$":   (O_C, (0.05, 0.05)),
}

for label, (point, offset) in points.items():
    ax.plot(*point, "ko", markersize=4)

    ax.annotate(
        label,
        xy=point,
        xytext=(
            point[0] + offset[0],
            point[1] + offset[1],
        ),
        fontsize=12,
        fontweight="bold",
    )

ax.set_aspect("equal")
ax.axis("off")

ax.set_title(
    f"Solved Triangle Configuration: BC = {BC_solution:.5f}",
    fontsize=13,
    pad=15,
)

plt.tight_layout()
plt.show()
