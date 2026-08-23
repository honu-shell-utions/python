# -----------------------------------------------------------------------------
# Jim McCleery
# August 23, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2024_a3764b
#
# Triangle ABC:
#     AB = 5
#     BC = 8
#     angle ABC = 60 degrees
#
# Circle omega is tangent to AB and BC.
# It intersects CA at Y and X, with C, Y, X, A occurring in that order.
# The tangent point on AB is Z, and ZY is parallel to BC.
#
# Goal: find and plot the radius of omega.
# -----------------------------------------------------------------------------

from math import sqrt
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def label_point(name, point, dx=0.08, dy=0.08):
    """
    Plot a point and label it with its name and coordinates.

    dx and dy move the text slightly so it does not sit directly
    on top of the point.
    """
    x, y = point

    plt.plot(x, y, "o")

    label = f"{name} ({x:.3f}, {y:.3f})"
    plt.text(x + dx, y + dy, label, fontsize=9)


# -----------------------------------------------------------------------------
# Place AB on the x-axis.
#
# A = (0, 0)
# B = (5, 0)
#
# Since BC = 8 and angle ABC = 60 degrees, moving from B to C
# goes 4 units left and 4*sqrt(3) units up.
#
# Therefore:
#
#     C = (1, 4*sqrt(3))
#
A = (0.0, 0.0)
B = (5.0, 0.0)
C = (1.0, 4 * sqrt(3))


# -----------------------------------------------------------------------------
# Analytic solution for the radius.
#
# Because ZY is parallel to BC, triangles AZY and ABC are similar.
#
#       YZ     BC     8
#       --  =  --  =  -
#       AZ     AB     5
#
# Therefore:
#
#       AZ = (5/8) * YZ
#
# Since the angle between ZY and AB is 60 degrees and OY = OZ = r,
# triangle OZY is equilateral in the relevant geometry, giving
#
#       YZ = r*sqrt(3)
#
# Also:
#
#       tan(30 degrees) = r / (5 - AZ)
#
# Solving gives
#
#                40
#       r = -------------
#            13*sqrt(3)
#
radius = 40 / (13 * sqrt(3))


# -----------------------------------------------------------------------------
# Find Z.
#
# YZ = r*sqrt(3)
# AZ = (5/8)*YZ
#
YZ = radius * sqrt(3)
AZ = (5 / 8) * YZ

Z = (AZ, 0.0)


# -----------------------------------------------------------------------------
# The center O is directly above Z because the circle is tangent
# to the horizontal segment AB at Z.
#
O = (Z[0], radius)


# -----------------------------------------------------------------------------
# Find Y.
#
# ZY is parallel to BC.
#
# The vector from B to C is
#
#       C - B = (-4, 4*sqrt(3))
#
# Its length is 8, so a unit vector in that direction is
#
#       (-1/2, sqrt(3)/2)
#
# Move YZ units from Z in that direction.
#
Y = (
    Z[0] - YZ / 2,
    Z[1] + YZ * sqrt(3) / 2
)


# -----------------------------------------------------------------------------
# Find both intersections of line AC with circle omega.
#
# A point on AC can be written as
#
#       P(t) = A + t(C - A)
#
# For t = 0 we are at A.
# For t = 1 we are at C.
#
# Substitute P(t) into the circle equation
#
#       (x - Ox)^2 + (y - Oy)^2 = r^2
#
# This produces a quadratic equation in t.
#
Ax, Ay = A
Cx, Cy = C
Ox, Oy = O

dx = Cx - Ax
dy = Cy - Ay

fx = Ax - Ox
fy = Ay - Oy

a = dx**2 + dy**2
b = 2 * (fx * dx + fy * dy)
c = fx**2 + fy**2 - radius**2

discriminant = b**2 - 4 * a * c

t1 = (-b - sqrt(discriminant)) / (2 * a)
t2 = (-b + sqrt(discriminant)) / (2 * a)

# Along A -> C, the order is A, X, Y, C.
# Therefore X corresponds to the smaller value of t.
t_X = min(t1, t2)
t_Y = max(t1, t2)

X = (
    Ax + t_X * dx,
    Ay + t_X * dy
)

# This value of Y comes independently from the circle-line intersection.
# It agrees with the Y calculated above from ZY parallel to BC.
Y_check = (
    Ax + t_Y * dx,
    Ay + t_Y * dy
)


# -----------------------------------------------------------------------------
# Print the important numerical results.
#
print(f"Radius = {radius:.6f}")
print()

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"X = {X}")
print(f"Y = {Y}")
print(f"Z = {Z}")
print(f"O = {O}")


# -----------------------------------------------------------------------------
# Draw triangle ABC.
#
plt.plot(
    [A[0], B[0], C[0], A[0]],
    [A[1], B[1], C[1], A[1]]
)


# Draw segment ZY.
plt.plot(
    [Z[0], Y[0]],
    [Z[1], Y[1]]
)


# -----------------------------------------------------------------------------
# Draw circle omega.
#
circle = plt.Circle(
    O,
    radius,
    fill=False
)

plt.gca().add_patch(circle)


# -----------------------------------------------------------------------------
# Label the important points.
#
# Small offsets are chosen individually to make the diagram easier to read.
#
label_point("A", A, -0.55, -0.28)
label_point("B", B,  0.08, -0.28)
label_point("C", C,  0.08,  0.08)

label_point("X", X, -0.60, -0.05)
label_point("Y", Y, -0.85,  0.08)
label_point("Z", Z,  0.08, -0.30)
label_point("O", O,  0.08,  0.08)


# Label the circle itself.
plt.text(
    O[0] + radius * 0.75,
    O[1] + radius * 0.75,
    r"$\omega$",
    fontsize=14
)


# -----------------------------------------------------------------------------
# Finish the graph.
#
# Equal scaling is important in geometry drawings; otherwise circles
# can appear as ellipses and angles can look distorted.
#
plt.axis("equal")
plt.axis("off")

plt.title(
    rf"Radius of $\omega$ = "
    rf"$\frac{{40}}{{13\sqrt{{3}}}}$ "
    rf"$\approx {radius:.5f}$"
)

plt.show()
