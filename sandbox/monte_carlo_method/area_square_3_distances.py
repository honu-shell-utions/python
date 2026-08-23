# Jim McCleery
# August 22, 2026
# Kailua-Kona, HI
#
# https://youtu.be/zUbCNnLFJk4?si=CuYGn7y0mMbPX-w-
#
# Monte Carlo solution for the area of square ABCD.
#
# Given:
#     EA = 6
#     EB = 3
#     EC = 5
#
# We randomly guess the side length of the square until the geometry
# produces a point E whose distance from B is very close to 3.
# -----------------------------------------------------------------------------

from math import sqrt
from random import uniform
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """Return the straight-line distance between two points."""
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# -----------------------------------------------------------------------------
def circle_circle_intersections(x0, y0, r0, x1, y1, r1):
    """
    Find the two intersection points of two circles.

    Circle 1:
        center = (x0, y0)
        radius = r0

    Circle 2:
        center = (x1, y1)
        radius = r1

    Returns:
        (point1, point2)

    Each point is an (x, y) tuple.

    If the circles do not intersect, return None.
    """

    # Distance between the two circle centers.
    d = distance(x0, y0, x1, y1)

    # If the circles are too far apart, they cannot intersect.
    if d > r0 + r1:
        return None

    # If one circle is completely inside the other, they cannot intersect.
    if d < abs(r0 - r1):
        return None

    # Distance from the first center to the midpoint of the chord
    # formed by the two intersections.
    a = (r0**2 - r1**2 + d**2) / (2 * d)

    # Half the length of that chord.
    h_squared = r0**2 - a**2

    # Floating-point arithmetic can occasionally produce a tiny
    # negative number such as -1e-15 instead of zero.
    if h_squared < 0:
        return None

    h = sqrt(h_squared)

    # Point on the line between the two circle centers.
    x2 = x0 + a * (x1 - x0) / d
    y2 = y0 + a * (y1 - y0) / d

    # The two actual circle intersections.
    x3 = x2 + h * (y1 - y0) / d
    y3 = y2 - h * (x1 - x0) / d

    x4 = x2 - h * (y1 - y0) / d
    y4 = y2 + h * (x1 - x0) / d

    return (x3, y3), (x4, y4)


# -----------------------------------------------------------------------------
# MONTE CARLO SEARCH
# -----------------------------------------------------------------------------

tolerance = 0.000001
tries = 0

while True:

    tries += 1

    # Randomly guess the side length of the square.
    side = uniform(3, 6)

    # Coordinate system based on the graphic:
    #
    #       A -------- D
    #       |          |
    #       |          |
    #       B -------- C
    #
    # Point E lies below and to the left.
    #
    # EA = 6
    # EC = 5
    # EB must equal 3.

    A = (0, 0)
    B = (0, -side)
    C = (side, -side)
    D = (side, 0)

    # Point E must lie on:
    #
    #   a circle of radius 6 centered at A
    #   a circle of radius 5 centered at C
    #
    intersections = circle_circle_intersections(
        A[0], A[1], 6,
        C[0], C[1], 5
    )

    if intersections is None:
        continue

    E1, E2 = intersections

    # We want the intersection lying to the left of the square.
    if E1[0] < E2[0]:
        E = E1
    else:
        E = E2

    # Check whether the third required distance, EB = 3,
    # is satisfied closely enough.
    EB = distance(E[0], E[1], B[0], B[1])

    if abs(EB - 3) < tolerance:
        break


# -----------------------------------------------------------------------------
# RESULTS
# -----------------------------------------------------------------------------

area = side**2

print(f"Number of random guesses = {tries:,}")
print(f"Side length              = {side:.6f}")
print(f"Area                     = {area:.6f}")
print()

print("Coordinates")
print(f"A = ({A[0]:.6f}, {A[1]:.6f})")
print(f"B = ({B[0]:.6f}, {B[1]:.6f})")
print(f"C = ({C[0]:.6f}, {C[1]:.6f})")
print(f"D = ({D[0]:.6f}, {D[1]:.6f})")
print(f"E = ({E[0]:.6f}, {E[1]:.6f})")

print()
print(f"EA = {distance(*E, *A):.6f}")
print(f"EB = {distance(*E, *B):.6f}")
print(f"EC = {distance(*E, *C):.6f}")


# -----------------------------------------------------------------------------
# DRAW THE DIAGRAM
# -----------------------------------------------------------------------------

# Draw the square.
square_x = [A[0], B[0], C[0], D[0], A[0]]
square_y = [A[1], B[1], C[1], D[1], A[1]]

plt.fill(
    square_x,
    square_y,
    color="lightsteelblue",
    edgecolor="black",
    linewidth=2
)

# Draw the three given segments from E.
plt.plot([E[0], A[0]], [E[1], A[1]], color="black")
plt.plot([E[0], B[0]], [E[1], B[1]], color="black")
plt.plot([E[0], C[0]], [E[1], C[1]], color="black")


# -----------------------------------------------------------------------------
# LABEL THE FIVE POINTS
# -----------------------------------------------------------------------------

plt.text(
    A[0] + 0.10, A[1] - 0.25,
    f"A\n({A[0]:.2f}, {A[1]:.2f})"
)

plt.text(
    B[0] + 0.10, B[1] + 0.15,
    f"B\n({B[0]:.2f}, {B[1]:.2f})"
)

plt.text(
    C[0] - 0.70, C[1] + 0.15,
    f"C\n({C[0]:.2f}, {C[1]:.2f})"
)

plt.text(
    D[0] - 0.70, D[1] - 0.25,
    f"D\n({D[0]:.2f}, {D[1]:.2f})"
)

plt.text(
    E[0] - 0.65, E[1] - 0.20,
    f"E\n({E[0]:.2f}, {E[1]:.2f})"
)


# -----------------------------------------------------------------------------
# LABEL THE GIVEN LENGTHS
# -----------------------------------------------------------------------------

plt.text(
    (E[0] + A[0]) / 2 - 0.35,
    (E[1] + A[1]) / 2,
    "6",
    fontsize=12
)

plt.text(
    (E[0] + B[0]) / 2 + 0.10,
    (E[1] + B[1]) / 2,
    "3",
    fontsize=12
)

plt.text(
    (E[0] + C[0]) / 2,
    (E[1] + C[1]) / 2 - 0.25,
    "5",
    fontsize=12
)


# -----------------------------------------------------------------------------
# FINISH THE GRAPH
# -----------------------------------------------------------------------------

plt.title(
    f"Monte Carlo estimate\n"
    f"Side = {side:.5f}, Area = {area:.5f}, Tries = {tries:,}"
)

plt.axis("equal")
plt.axis("off")
plt.show()
