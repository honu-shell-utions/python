# -----------------------------------------------------------------------------
# Jim McCleery
# September 14, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_f78571
#
# Geometry experiment:
#
# ABC is an acute scalene triangle with centroid G.
#
# Ray BG meets the circumcircle of ABC again at P.
# Ray CG meets the circumcircle of ABC again at Q.
#
# D is the foot of the altitude from A to BC.
# Ray GD meets the circumcircle of ABC again at E.
#
# F is the circumcenter of triangle ADE.
#
# The program checks numerically that F lies on line PQ.
# -----------------------------------------------------------------------------

from math import sqrt
from random import uniform

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
def distance(A, B):
    """Return the distance between points A and B."""
    x1, y1 = A
    x2, y2 = B

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# -----------------------------------------------------------------------------
def circumcircle(A, B, C):
    """
    Find the circle through three non-collinear points.

    Returns:
        center, radius
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    # These formulas come from solving the equations
    # saying that A, B, and C are all the same distance
    # from the center of the circle.
    d = 2 * (
        x1 * (y2 - y3)
        + x2 * (y3 - y1)
        + x3 * (y1 - y2)
    )

    ux = (
        (x1**2 + y1**2) * (y2 - y3)
        + (x2**2 + y2**2) * (y3 - y1)
        + (x3**2 + y3**2) * (y1 - y2)
    ) / d

    uy = (
        (x1**2 + y1**2) * (x3 - x2)
        + (x2**2 + y2**2) * (x1 - x3)
        + (x3**2 + y3**2) * (x2 - x1)
    ) / d

    center = (ux, uy)
    radius = distance(center, A)

    return center, radius


# -----------------------------------------------------------------------------
def foot_of_perpendicular(P, A, B):
    """
    Return the foot of the perpendicular from point P to line AB.

    The answer is the point on line AB closest to P.
    """
    px, py = P
    ax, ay = A
    bx, by = B

    # Vector from A to B.
    dx = bx - ax
    dy = by - ay

    # t tells us how far along line AB the perpendicular foot lies.
    t = ((px - ax) * dx + (py - ay) * dy) / (dx**2 + dy**2)

    return ax + t * dx, ay + t * dy


# -----------------------------------------------------------------------------
def ray_circle_intersection(start, through, center, radius):
    """
    Find the first intersection of a ray with a circle.

    The ray starts at 'start' and points toward 'through'.

    If the starting point itself is on the circle, that intersection
    is ignored and the NEXT intersection along the ray is returned.
    """
    sx, sy = start
    tx, ty = through
    cx, cy = center

    # Direction vector of the ray.
    dx = tx - sx
    dy = ty - sy

    # A point on the ray has coordinates
    #
    #     (sx + t*dx, sy + t*dy)
    #
    # where t >= 0.
    #
    # Substitute this into the circle equation.  This gives
    # a quadratic equation in t.
    a = dx**2 + dy**2

    b = 2 * (
        dx * (sx - cx)
        + dy * (sy - cy)
    )

    c = (
        (sx - cx) ** 2
        + (sy - cy) ** 2
        - radius**2
    )

    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        raise ValueError("The ray does not meet the circle.")

    root = sqrt(max(0, discriminant))

    t1 = (-b - root) / (2 * a)
    t2 = (-b + root) / (2 * a)

    # We want an intersection in the forward direction of the ray.
    # A very small t is ignored because it represents the starting
    # point when the starting point is already on the circle.
    positive_t = [
        t for t in (t1, t2)
        if t > 1e-9
    ]

    if not positive_t:
        raise ValueError("No forward intersection with the ray.")

    # Choose the first circle intersection encountered along the ray.
    t = min(positive_t)

    return sx + t * dx, sy + t * dy


# -----------------------------------------------------------------------------
def point_line_distance(P, A, B):
    """
    Return the perpendicular distance from point P to line AB.

    If this distance is essentially zero, P lies on line AB.
    """
    px, py = P
    ax, ay = A
    bx, by = B

    numerator = abs(
        (bx - ax) * (ay - py)
        - (ax - px) * (by - ay)
    )

    denominator = distance(A, B)

    return numerator / denominator


# -----------------------------------------------------------------------------
def plot_circle(center, radius, linestyle="-"):
    """Draw a circle."""
    cx, cy = center

    theta = np.linspace(0, 2 * np.pi, 500)

    x = cx + radius * np.cos(theta)
    y = cy + radius * np.sin(theta)

    plt.plot(x, y, linestyle=linestyle)


# -----------------------------------------------------------------------------
def plot_segment(A, B, linestyle="-"):
    """Draw the line segment joining points A and B."""
    plt.plot(
        [A[0], B[0]],
        [A[1], B[1]],
        linestyle=linestyle
    )


# -----------------------------------------------------------------------------
def label_point(name, P, dx=0.08, dy=0.08):
    """
    Plot a point and label it with both its name and coordinates.

    Example:

        A
        (1.23, 4.56)
    """
    x, y = P

    plt.plot(x, y, "o")

    plt.text(
        x + dx,
        y + dy,
        f"{name}\n({x:.2f}, {y:.2f})",
        fontsize=8
    )


# -----------------------------------------------------------------------------
def is_acute_triangle(A, B, C):
    """
    Return True if triangle ABC is acute.

    For an acute triangle, the square of every side must be less
    than the sum of the squares of the other two sides.
    """
    a2 = distance(B, C) ** 2
    b2 = distance(A, C) ** 2
    c2 = distance(A, B) ** 2

    return (
        a2 < b2 + c2
        and b2 < a2 + c2
        and c2 < a2 + b2
    )


# -----------------------------------------------------------------------------
# Generate one acute scalene triangle.
#
# Placing B and C on the x-axis makes the diagram convenient to view.
# A is placed above the x-axis.
# -----------------------------------------------------------------------------

while True:

    B = (0.0, 0.0)
    C = (uniform(6, 10), 0.0)

    A = (
        uniform(1, C[0] - 1),
        uniform(3, 8)
    )

    if not is_acute_triangle(A, B, C):
        continue

    # Avoid triangles that are nearly isosceles.
    AB = distance(A, B)
    AC = distance(A, C)
    BC = distance(B, C)

    if (
        abs(AB - AC) < 0.5
        or abs(AB - BC) < 0.5
        or abs(AC - BC) < 0.5
    ):
        continue

    break


# -----------------------------------------------------------------------------
# Construct the important points.
# -----------------------------------------------------------------------------

# Centroid G is the average of the three vertex coordinates.
G = (
    (A[0] + B[0] + C[0]) / 3,
    (A[1] + B[1] + C[1]) / 3
)


# D is the foot of the altitude from A to BC.
D = foot_of_perpendicular(A, B, C)


# Circumcircle of triangle ABC.
O, R = circumcircle(A, B, C)


# Ray BG meets the circumcircle again at P.
P = ray_circle_intersection(B, G, O, R)


# Ray CG meets the circumcircle again at Q.
Q = ray_circle_intersection(C, G, O, R)


# Ray GD meets the circumcircle at E.
E = ray_circle_intersection(G, D, O, R)


# F is the circumcenter of triangle ADE.
F, r_ADE = circumcircle(A, D, E)


# -----------------------------------------------------------------------------
# Numerical check.
#
# If the theorem is correct, F should lie on line PQ.
# Therefore the distance from F to line PQ should be essentially zero.
# -----------------------------------------------------------------------------

error = point_line_distance(F, P, Q)

print()
print("Coordinates")
print("-----------")

for name, point in [
    ("A", A),
    ("B", B),
    ("C", C),
    ("D", D),
    ("E", E),
    ("F", F),
    ("G", G),
    ("P", P),
    ("Q", Q),
]:
    print(f"{name} = ({point[0]:.6f}, {point[1]:.6f})")

print()
print(f"Distance from F to line PQ = {error:.12g}")

if error < 1e-9:
    print("Numerical check: F lies on line PQ.")
else:
    print("Numerical check: something is wrong.")


# -----------------------------------------------------------------------------
# Draw the figure.
# -----------------------------------------------------------------------------

plt.figure(figsize=(11, 8))


# Triangle ABC.
plot_segment(A, B)
plot_segment(B, C)
plot_segment(C, A)


# Altitude AD.
plot_segment(A, D, linestyle="--")


# Rays/segments used in the construction.
plot_segment(B, P, linestyle="--")
plot_segment(C, Q, linestyle="--")
plot_segment(G, E, linestyle="--")


# Line PQ.
#
# Draw slightly beyond P and Q so it is easy to see that F is on it.
PQ = np.array(Q) - np.array(P)

line_start = np.array(P) - 0.3 * PQ
line_end = np.array(Q) + 0.3 * PQ

plot_segment(line_start, line_end)


# Circumcircle of ABC.
plot_circle(O, R)


# Circumcircle of ADE.
plot_circle(F, r_ADE, linestyle="--")


# Label all important points and show their coordinates.
label_point("A", A)
label_point("B", B)
label_point("C", C)
label_point("D", D)
label_point("E", E)
label_point("F", F)
label_point("G", G)
label_point("P", P)
label_point("Q", Q)


# The axes use the same scale horizontally and vertically,
# so circles really look circular.
plt.axis("equal")

plt.title(
    "Centroid / Circumcircle Construction\n"
    f"distance from F to PQ = {error:.2e}"
)

plt.xlabel("x-coordinate")
plt.ylabel("y-coordinate")

plt.grid(alpha=0.25)

plt.show()
