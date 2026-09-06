# Jim McCleery
# September 6, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2025_2d76ea
#
# -----------------------------------------------------------------------------
# 2025 USA Mathematical Olympiad problem
#
# Triangle ABC is a right triangle with angle A = 90 degrees and BC = 38.
#
# Points K and L are inside the triangle and satisfy
#
#       AK = AL = BK = CL = KL = 14.
#
# This program uses a Monte-Carlo search to find a configuration satisfying
# BC = 38, then computes the area of quadrilateral BKLC.
# -----------------------------------------------------------------------------

from math import pi, sqrt, sin, cos
from random import uniform
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """Return the distance between two points."""
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Find the area of a polygon using the shoelace formula.

    The vertices must be listed in order around the polygon.
    """
    area = 0

    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]

        area += x1 * y2 - y1 * x2

    return abs(area) / 2


# -----------------------------------------------------------------------------
# Monte-Carlo search
#
# We randomly choose the angle alpha until the resulting hypotenuse BC
# is extremely close to 38.
#
# A is placed at the origin.
#
#       C
#       |
#       |     L
#       |    /
#       |   K
#       |
#       A----------------B
#
# AK = AL = 14.
#
# Since angle KAL = 60 degrees, triangle AKL is equilateral, so KL = 14.
#
# The formulas for B and C are chosen so that BK = 14 and CL = 14.
# -----------------------------------------------------------------------------

tolerance = 0.000001

while True:

    # Choose alpha randomly between 0 and 60 degrees.
    alpha = uniform(0, pi / 3)

    # beta is determined by the geometry of the construction.
    beta = pi / 6 - alpha

    # Point A is the right-angle vertex.
    A = (0, 0)

    # Point B lies on the positive x-axis.
    B = (
        28 * cos(alpha),
        0
    )

    # Point C lies on the positive y-axis.
    C = (
        0,
        28 * cos(beta)
    )

    # Point K is 14 units from A.
    K = (
        14 * cos(alpha),
        14 * sin(alpha)
    )

    # Point L is also 14 units from A.
    # L is 60 degrees counterclockwise from K.
    L = (
        14 * cos(alpha + pi / 3),
        14 * sin(alpha + pi / 3)
    )

    # Check the length of the hypotenuse BC.
    BC = distance(B[0], B[1], C[0], C[1])

    # Stop when BC is sufficiently close to 38.
    if abs(BC - 38) < tolerance:
        break


# -----------------------------------------------------------------------------
# Calculate the area of quadrilateral BKLC.
# -----------------------------------------------------------------------------

quadrilateral = [B, K, L, C]

area_BKLC = polygon_area(quadrilateral)

# The problem says that the area has the form n*sqrt(3).
n = area_BKLC / sqrt(3)


# -----------------------------------------------------------------------------
# Display some numerical results.
# -----------------------------------------------------------------------------

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"K = {K}")
print(f"L = {L}")
print()

print(f"BC = {BC:.6f}")
print(f"BK = {distance(*B, *K):.6f}")
print(f"CL = {distance(*C, *L):.6f}")
print(f"AK = {distance(*A, *K):.6f}")
print(f"AL = {distance(*A, *L):.6f}")
print(f"KL = {distance(*K, *L):.6f}")
print()

print(f"Area of BKLC = {area_BKLC:.6f}")
print(f"Area / sqrt(3) = {n:.6f}")
print(f"n = {round(n)}")


# -----------------------------------------------------------------------------
# Draw the triangle and quadrilateral.
# -----------------------------------------------------------------------------

# Draw triangle ABC.
plt.plot(
    [A[0], B[0], C[0], A[0]],
    [A[1], B[1], C[1], A[1]],
    linewidth=2
)

# Shade quadrilateral BKLC.
x_quad = [B[0], K[0], L[0], C[0]]
y_quad = [B[1], K[1], L[1], C[1]]

plt.fill(
    x_quad,
    y_quad,
    alpha=0.4
)

# Draw AK, AL, and KL.
plt.plot(
    [A[0], K[0]],
    [A[1], K[1]]
)

plt.plot(
    [A[0], L[0]],
    [A[1], L[1]]
)

plt.plot(
    [K[0], L[0]],
    [K[1], L[1]]
)


# -----------------------------------------------------------------------------
# Add labels to the five important points.
# -----------------------------------------------------------------------------

plt.text(A[0] - 0.8, A[1] - 0.8, "A", fontsize=14)
plt.text(B[0] + 0.4, B[1] - 0.5, "B", fontsize=14)
plt.text(C[0] - 0.8, C[1] + 0.4, "C", fontsize=14)
plt.text(K[0] + 0.4, K[1] - 0.3, "K", fontsize=14)
plt.text(L[0] - 1.0, L[1] + 0.4, "L", fontsize=14)


# -----------------------------------------------------------------------------
# Finish the graph.
# -----------------------------------------------------------------------------

plt.title(
    f"Area of BKLC ≈ {round(n)}√3"
)

plt.axis("equal")
plt.axis("off")

plt.show()
