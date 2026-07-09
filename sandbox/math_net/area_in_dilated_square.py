# =============================================================================
# Jim McCleery
# July 8, 2026
# Kailua-Kona, Hawaii
#
# MIT Math Explorer
# https://mathnet.mit.edu/explorer.html?p=usa_cb519b
#
# Problem
# -------
# Square ABCD has side length 1.
#
# A dilation about point A produces the larger square AB'C'D'.
#
# If BC' = 29, determine the area of triangle BDC'.
#
# The answer produced by this program is 41/2 = 20.5.
#
# (The official solution posted on the Explorer page gives 420, which appears
# to be incorrect.)
# =============================================================================

from math import sqrt
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def plot_line(p1, p2):
    """Draw a line segment between two points."""
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color="black")


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Compute the area of a polygon using the Shoelace Formula.

    The vertices must be listed in order around the polygon.
    """

    area = 0

    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % len(vertices)]

        area += x1 * y2 - y1 * x2

    return abs(area) / 2


# =============================================================================
# Determine the dilation factor.
#
# Let the scale factor be k.
#
# Coordinates:
#
#     B  = (1,0)
#     C' = (k,-k)
#
# Since BC' = 29,
#
#     (k-1)² + k² = 29²
#
# which simplifies to
#
#     2k² - 2k - 840 = 0
#
# Factoring gives
#
#     (k-21)(k+20)=0
#
# so
#
#     k = 21
# =============================================================================

k = 21


# =============================================================================
# Coordinates of the original square.
# =============================================================================

A = (0, 0)
B = (1, 0)
C = (1, -1)
D = (0, -1)


# =============================================================================
# Coordinates after dilation.
#
# Point A is the center of dilation, so it does not move.
# =============================================================================

Ap = A
Bp = (k, 0)
Cp = (k, -k)
Dp = (0, -k)


# =============================================================================
# Draw the original square.
# =============================================================================

plot_line(A, B)
plot_line(B, C)
plot_line(C, D)
plot_line(D, A)


# =============================================================================
# Draw the enlarged square.
# =============================================================================

plot_line(Ap, Bp)
plot_line(Bp, Cp)
plot_line(Cp, Dp)
plot_line(Dp, Ap)


# =============================================================================
# Draw triangle BDC'.
# =============================================================================

plot_line(B, D)
plot_line(B, Cp)
plot_line(D, Cp)


# =============================================================================
# Shade the triangle.
# =============================================================================

triangle = [B, D, Cp]

x = [p[0] for p in triangle]
y = [p[1] for p in triangle]

x.append(triangle[0][0])
y.append(triangle[0][1])

plt.fill(x, y, color="red", alpha=0.35)


# =============================================================================
# Draw all vertices.
# =============================================================================

for point in [A, B, C, D, Bp, Cp, Dp]:
    plt.plot(point[0], point[1], "ko", markersize=4)


# =============================================================================
# Label every point.
# =============================================================================

plt.text(A[0]-0.7, A[1]+0.45, f"A {A}", fontsize=10)

plt.text(B[0]+0.15, B[1]+0.45, f"B {B}", fontsize=10)

plt.text(C[0]+0.15, C[1]-1.0, f"C {C}", fontsize=10)

plt.text(D[0]-3.3, D[1]-1.0, f"D {D}", fontsize=10)

plt.text(Bp[0]+0.25, Bp[1]+0.45, f"B' {Bp}", fontsize=10)

plt.text(Cp[0]+0.25, Cp[1]-1.0, f"C' {Cp}", fontsize=10)

plt.text(Dp[0]-5.5, Dp[1]-1.0, f"D' {Dp}", fontsize=10)


# =============================================================================
# Compute the area.
# =============================================================================

area = polygon_area(triangle)


# =============================================================================
# Add explanatory text.
# =============================================================================

plt.plot(8,6)
plt.text(8.0, 5, "Given: BC' = 29", fontsize=12)
plt.text(8.0, 4, f"Dilation factor  k = {k}", fontsize=12)
plt.title(f"The triangle BDC' has an area of {area}.")

plt.axis("equal")
plt.axis("off")

plt.show()
