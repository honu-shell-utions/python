# Jim McCleery
# August 31, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2007_39c926
#
# -----------------------------------------------------------------------------
# Three mutually tangent unit circles
#
# The circle centers are:
#
#                    N = (1, sqrt(3))
#                         /\
#                        /  \
#                       /    \
#                      C      A
#                     /        \
#                    /          \
#         Q -------- M ---- B ---- O -------- P
#
# The circles centered at M, N, and O are omega_1, omega_2, and omega_3.
#
# A is the tangency point of omega_2 and omega_3.
# B is the tangency point of omega_3 and omega_1.
# C is the tangency point of omega_1 and omega_2.
#
# Line AP intersects omega_2 again at R.
#
# The goal is to find the area of triangle PQR.
# -----------------------------------------------------------------------------

from math import sqrt

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
def line_circle_intersections(center, radius, slope, intercept):
    """
    Find the two intersection points of a circle and a line.

    The circle has:
        center = (cx, cy)
        radius = radius

    The line has equation:
        y = slope * x + intercept

    Returns:
        Two points, each written as an (x, y) tuple.
    """

    cx, cy = center

    # Substitute y = slope*x + intercept into the circle equation
    #
    #     (x - cx)^2 + (y - cy)^2 = radius^2
    #
    # This produces a quadratic equation:
    #
    #     A*x^2 + B*x + C = 0

    A = 1 + slope**2
    B = 2 * (slope * (intercept - cy) - cx)
    C = cx**2 + (intercept - cy)**2 - radius**2

    # The discriminant tells us whether the quadratic has real roots.
    discriminant = B**2 - 4 * A * C

    if discriminant < 0:
        raise ValueError("The line does not intersect the circle.")

    # Quadratic formula
    x1 = (-B - sqrt(discriminant)) / (2 * A)
    x2 = (-B + sqrt(discriminant)) / (2 * A)

    # Use the line equation to get the corresponding y-coordinates.
    y1 = slope * x1 + intercept
    y2 = slope * x2 + intercept

    return (x1, y1), (x2, y2)


# -----------------------------------------------------------------------------
def triangle_area(point1, point2, point3):
    """
    Find the area of a triangle from the coordinates of its three vertices.

    This is the shoelace formula specialized to a triangle.
    """

    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    area = abs(
        x1 * y2
        + x2 * y3
        + x3 * y1
        - y1 * x2
        - y2 * x3
        - y3 * x1
    ) / 2

    return area


# -----------------------------------------------------------------------------
def plot_circle(center, radius):
    """Draw a circle with the given center and radius."""

    cx, cy = center

    # Generate angles from 0 through one complete revolution.
    theta = np.linspace(0, 2 * np.pi, 500)

    # Convert the polar circle equation to x- and y-coordinates.
    x = cx + radius * np.cos(theta)
    y = cy + radius * np.sin(theta)

    plt.plot(x, y)


# -----------------------------------------------------------------------------
def draw_segment(point1, point2):
    """Draw a straight line segment between two points."""

    x1, y1 = point1
    x2, y2 = point2

    plt.plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
def add_label(name, point, dx=0.05, dy=0.05):
    """
    Put a point name next to its location on the graph.

    dx and dy move the text slightly so it does not sit directly
    on top of the point.
    """

    x, y = point
    plt.text(x + dx, y + dy, name, fontsize=12)


# =============================================================================
# DEFINE THE GEOMETRIC POINTS
# =============================================================================

# Each circle has radius 1.
radius = 1

# Centers of the three circles:
#
# omega_1 is centered at M
# omega_2 is centered at N
# omega_3 is centered at O
M = (0, 0)
N = (1, sqrt(3))
O = (2, 0)

# Because the circles have equal radii and are tangent,
# each tangency point is the midpoint of the two centers involved.

# A: tangency point of omega_2 and omega_3
A = (3 / 2, sqrt(3) / 2)

# B: tangency point of omega_3 and omega_1
B = (1, 0)

# C: tangency point of omega_1 and omega_2
C = (1 / 2, sqrt(3) / 2)

# Line MO is the x-axis.
#
# The circle centered at O meets this line at B and P.
# Since O = (2, 0) and the radius is 1:
P = (3, 0)

# The circle centered at M meets this line at B and Q.
# Since M = (0, 0) and the radius is 1:
Q = (-1, 0)


# =============================================================================
# FIND R
# =============================================================================

# R is the second point where line AP intersects omega_2.

# Find the slope of AP.
slope_AP = (P[1] - A[1]) / (P[0] - A[0])

# In y = mx + b, solve for b using point P.
intercept_AP = P[1] - slope_AP * P[0]

# Find both intersections of AP with the circle centered at N.
intersection1, intersection2 = line_circle_intersections(
    N,
    radius,
    slope_AP,
    intercept_AP,
)

# One of the intersections is A.
# The other one is R.
#
# For these coordinates the first intersection is R = (0, sqrt(3)).
R = intersection1


# =============================================================================
# COMPUTE THE AREA OF TRIANGLE PQR
# =============================================================================

area_PQR = triangle_area(P, Q, R)

print(f"M = {M}")
print(f"N = {N}")
print(f"O = {O}")
print()
print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print()
print(f"P = {P}")
print(f"Q = {Q}")
print(f"R = ({R[0]:.6f}, {R[1]:.6f})")
print()
print(f"Area of triangle PQR = {area_PQR:.6f}")
print(f"Exact area = 2*sqrt(3) = {2 * sqrt(3):.6f}")


# =============================================================================
# DRAW THE FIGURE
# =============================================================================

# Draw the three unit circles.
plot_circle(M, radius)
plot_circle(N, radius)
plot_circle(O, radius)

# Draw triangle MNO, whose vertices are the circle centers.
draw_segment(M, N)
draw_segment(N, O)
draw_segment(O, M)

# Draw the equilateral tangency triangle ABC.
draw_segment(A, B)
draw_segment(B, C)
draw_segment(C, A)

# Draw triangle PQR.
draw_segment(P, Q)
draw_segment(Q, R)
draw_segment(R, P)

# Shade triangle PQR.
plt.fill(
    [P[0], Q[0], R[0]],
    [P[1], Q[1], R[1]],
    color="red",
    alpha=0.35,
)

# Mark the important points.
points = [M, N, O, A, B, C, P, Q, R]

for x, y in points:
    plt.plot(x, y, "ko", markersize=4)

# Add geometric point labels.
add_label("M", M, -0.18, 0.08)
add_label("N", N, 0.05, 0.08)
add_label("O", O, 0.08, 0.08)

add_label("A", A, 0.07, 0.06)
add_label("B", B, 0.04, -0.18)
add_label("C", C, -0.15, 0.06)

add_label("P", P, 0.08, 0.05)
add_label("Q", Q, -0.18, 0.05)
add_label("R", R, -0.18, 0.05)

# Give the graph equal horizontal and vertical scales so the circles
# actually appear as circles rather than ellipses.
plt.axis("equal")

# Remove the ordinary x- and y-axes for a cleaner geometry diagram.
plt.axis("off")

plt.title(
    f"Area of triangle PQR = {area_PQR:.5f} = 2√3"
)

plt.show()
