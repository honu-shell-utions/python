# -----------------------------------------------------------------------------
# Jim McCleery
# August 20, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2025_256fdd
#
# Geometry problem:
#
# Let ABCD be a rectangle with BC = 24.
# Point X lies inside the rectangle such that angle AXB = 90 degrees.
#
# The circumradius of triangle AXD is 13.
# The circumradius of triangle BXC is 15.
#
# Find AB.
# -----------------------------------------------------------------------------


import math
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Find the intersection of two circles whose centers lie on the same
# horizontal line.
#
# Circle 1:
#     center = (x1, y1), radius = r1
#
# Circle 2:
#     center = (x2, y2), radius = r2
#
# The function returns the two intersection points.
# -----------------------------------------------------------------------------
def circle_circle_intersections(x1, y1, r1, x2, y2, r2):
    distance_between_centers = math.hypot(x2 - x1, y2 - y1)

    # Distance from the first center to the vertical line through
    # the two intersection points.
    a = (
        r1**2
        - r2**2
        + distance_between_centers**2
    ) / (2 * distance_between_centers)

    # Height of the intersection points above/below that line.
    h_squared = r1**2 - a**2

    if h_squared < 0:
        raise ValueError("The two circles do not intersect.")

    h = math.sqrt(h_squared)

    # Point halfway between the two intersection points.
    x_mid = x1 + a * (x2 - x1) / distance_between_centers
    y_mid = y1 + a * (y2 - y1) / distance_between_centers

    # The two intersection points.
    x_upper = x_mid + h * (y2 - y1) / distance_between_centers
    y_upper = y_mid - h * (x2 - x1) / distance_between_centers

    x_lower = x_mid - h * (y2 - y1) / distance_between_centers
    y_lower = y_mid + h * (x2 - x1) / distance_between_centers

    return (x_upper, y_upper), (x_lower, y_lower)


# -----------------------------------------------------------------------------
# For a proposed value of d, find point X.
#
# We use the following coordinates:
#
#     A = (0, 0)
#     B = (14 + d, 0)
#     C = (14 + d, 24)
#     D = (0, 24)
#
# The circumcenter of triangle AXD is O1 = (5, 12).
# Its radius is 13.
#
# The circumcenter of triangle BXC is O2 = (5 + d, 12).
# Its radius is 15.
#
# Therefore X is the intersection of these two circles.
# -----------------------------------------------------------------------------
def find_point_X(d):
    O1 = (5, 12)          # Center of circle through A, X, D
    O2 = (5 + d, 12)      # Center of circle through B, X, C

    circle1_radius = 13
    circle2_radius = 15

    point1, point2 = circle_circle_intersections(
        O1[0], O1[1], circle1_radius,
        O2[0], O2[1], circle2_radius
    )

    # The intersection above the horizontal center line is the point
    # X that lies inside the rectangle.
    if point1[1] > point2[1]:
        return point1
    else:
        return point2


# -----------------------------------------------------------------------------
# The angle AXB is 90 degrees.
#
# If two vectors are perpendicular, their dot product is zero.
#
# Vectors XA and XB are:
#
#     A - X
#     B - X
#
# Therefore:
#
#     (A - X) dot (B - X) = 0
#
# This function gives the value of that dot product.
# We want to find the value of d for which it equals zero.
# -----------------------------------------------------------------------------
def right_angle_test(d):
    A = (0, 0)
    B = (14 + d, 0)

    X = find_point_X(d)
    x, y = X

    vector_XA = (A[0] - x, A[1] - y)
    vector_XB = (B[0] - x, B[1] - y)

    dot_product = (
        vector_XA[0] * vector_XB[0]
        + vector_XA[1] * vector_XB[1]
    )

    return dot_product


# -----------------------------------------------------------------------------
# Find the zero of right_angle_test(d) using the bisection method.
#
# We know from the geometry that the useful solution is between d = 24
# and d = 25.
#
# Bisection is a simple numerical method:
#     1. Look at the midpoint.
#     2. Decide which half contains the zero.
#     3. Repeat.
# -----------------------------------------------------------------------------
low = 24.0
high = 25.0

for _ in range(60):
    middle = (low + high) / 2

    if right_angle_test(low) * right_angle_test(middle) <= 0:
        high = middle
    else:
        low = middle

d = (low + high) / 2


# -----------------------------------------------------------------------------
# Now calculate all of the coordinates using the solution for d.
# -----------------------------------------------------------------------------

A = (0, 0)
B = (14 + d, 0)
C = (14 + d, 24)
D = (0, 24)

X = find_point_X(d)

# Circumcenters of the two triangles.
O1 = (5, 12)
O2 = (5 + d, 12)

AB = B[0] - A[0]

# -----------------------------------------------------------------------------
# Draw the rectangle, the two triangles, and the two circumcircles.
# -----------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 7))

# Rectangle ABCD.
ax.plot(
    [A[0], B[0], C[0], D[0], A[0]],
    [A[1], B[1], C[1], D[1], A[1]],
    linewidth=2
)

# Lines AX and BX.
ax.plot([A[0], X[0]], [A[1], X[1]], linewidth=1.5)
ax.plot([B[0], X[0]], [B[1], X[1]], linewidth=1.5)

# Optional: draw the two triangles AXD and BXC.
ax.plot([A[0], X[0], D[0], A[0]],
        [A[1], X[1], D[1], A[1]],
        linestyle="--", linewidth=1)

ax.plot([B[0], X[0], C[0], B[0]],
        [B[1], X[1], C[1], B[1]],
        linestyle="--", linewidth=1)


# -----------------------------------------------------------------------------
# Draw the two circumcircles.
# -----------------------------------------------------------------------------

theta = [2 * math.pi * i / 400 for i in range(401)]

# Circle centered at O1 with radius 13.
circle1_x = [O1[0] + 13 * math.cos(t) for t in theta]
circle1_y = [O1[1] + 13 * math.sin(t) for t in theta]
ax.plot(circle1_x, circle1_y, linestyle=":", linewidth=1.5)

# Circle centered at O2 with radius 15.
circle2_x = [O2[0] + 15 * math.cos(t) for t in theta]
circle2_y = [O2[1] + 15 * math.sin(t) for t in theta]
ax.plot(circle2_x, circle2_y, linestyle=":", linewidth=1.5)


# -----------------------------------------------------------------------------
# Label the important points.
#
# The coordinates are included in the labels so that the connection between
# the geometry and the coordinate system is clear.
# -----------------------------------------------------------------------------

points = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "X": X,
}

for name, (x, y) in points.items():
    ax.plot(x, y, "o")
    ax.annotate(
        f"{name} = ({x:.2f}, {y:.2f})",
        (x, y),
        xytext=(7, 7),
        textcoords="offset points",
        fontsize=10
    )


# Label the two circumcenters.
ax.annotate(
    r"$O_1=(5,12)$",
    O1,
    xytext=(8, -18),
    textcoords="offset points",
    fontsize=10
)

ax.annotate(
    rf"$O_2=({O2[0]:.2f},12)$",
    O2,
    xytext=(8, -18),
    textcoords="offset points",
    fontsize=10
)


# -----------------------------------------------------------------------------
# Add dimension labels.
# -----------------------------------------------------------------------------

ax.annotate(
    f"AB = {AB:.3f}",
    ((A[0] + B[0]) / 2, 0),
    xytext=(0, -30),
    textcoords="offset points",
    ha="center",
    fontsize=12
)

ax.annotate(
    "BC = 24",
    (B[0], 12),
    xytext=(15, 0),
    textcoords="offset points",
    va="center",
    fontsize=12
)


# -----------------------------------------------------------------------------
# Finish the graph.
# -----------------------------------------------------------------------------

ax.set_title(
    f"Rectangle ABCD:  AB = {AB:.6f}",
    fontsize=14
)

ax.set_xlabel("x-coordinate")
ax.set_ylabel("y-coordinate")

ax.set_aspect("equal")
ax.grid(True, alpha=0.25)

# Give the labels and circles a little room around the figure.
ax.set_xlim(-3, AB + 5)
ax.set_ylim(-5, 29)

plt.tight_layout()
plt.show()
