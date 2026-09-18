# Jim McCleery
# August 25, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2025_a7ad4d
#
# An isosceles trapezoid has an inscribed circle of radius 3
# and an area of 72.  Find r^2 + s^2, where r and s are
# the lengths of the two parallel sides.

# -----------------------------------------------------------------------------

from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.patches import Circle


# -----------------------------------------------------------------------------
# The circle has radius 3, so the distance between the two
# parallel sides of the trapezoid is the diameter, 6.
#
# Area of a trapezoid:
#
#        area = (1/2)(r + s)(height)
#
# Therefore:
#
#        72 = (1/2)(r + s)(6)
#
# so:
#
#        r + s = 24
#
# The geometry of the isosceles trapezoid gives:
#
#        r = 12 - 6*sqrt(3)
#        s = 12 + 6*sqrt(3)

radius = 3

r = 12 - 6 * sqrt(3)       # shorter parallel side
s = 12 + 6 * sqrt(3)       # longer parallel side


# -----------------------------------------------------------------------------
# Coordinate system
#
# Put the center of the circle at O = (0, 0).
#
# Since the radius is 3, the parallel sides lie on:
#
#        y =  3
#        y = -3
#
# Centering the trapezoid on the y-axis makes the coordinates
# particularly simple.
#
#
#             D -------- C
#              \        /
#               \   O  /
#                \    /
#             A ---------- B
#
#
# A and B are the endpoints of the longer base s.
# C and D are the endpoints of the shorter base r.

O = (0, 0)

A = (-s / 2, -radius)
B = ( s / 2, -radius)

C = ( r / 2,  radius)
D = (-r / 2,  radius)


# -----------------------------------------------------------------------------
# Draw the trapezoid.

x_trapezoid = [A[0], B[0], C[0], D[0], A[0]]
y_trapezoid = [A[1], B[1], C[1], D[1], A[1]]

plt.plot(x_trapezoid, y_trapezoid, linewidth=2)


# -----------------------------------------------------------------------------
# Draw the inscribed circle.
#
# The Circle object needs:
#     center = (0, 0)
#     radius = 3

circle = Circle(
    O,
    radius,
    fill=False,
    linewidth=2
)

plt.gca().add_patch(circle)


# -----------------------------------------------------------------------------
# Mark the center of the circle.

plt.plot(O[0], O[1], "o")
plt.text(0.3, 0.2, "O (0, 0)", fontsize=11)


# -----------------------------------------------------------------------------
# Label the four vertices with their coordinates.
#
# The numerical values are included to make the coordinate
# locations easy to see on the graph.

plt.text(
    A[0] - 0.5,
    A[1] - 0.7,
    f"A ({A[0]:.2f}, {A[1]:.0f})",
    ha="right"
)

plt.text(
    B[0] + 0.5,
    B[1] - 0.7,
    f"B ({B[0]:.2f}, {B[1]:.0f})",
    ha="left"
)

plt.text(
    C[0] + 0.4,
    C[1] + 0.4,
    f"C ({C[0]:.2f}, {C[1]:.0f})",
    ha="left"
)

plt.text(
    D[0] - 0.4,
    D[1] + 0.4,
    f"D ({D[0]:.2f}, {D[1]:.0f})",
    ha="right"
)


# -----------------------------------------------------------------------------
# Label the two parallel sides.

plt.text(
    0,
    radius + 0.35,
    f"r = {r:.2f}",
    ha="center",
    fontsize=12
)

plt.text(
    0,
    -radius - 0.75,
    f"s = {s:.2f}",
    ha="center",
    fontsize=12
)


# -----------------------------------------------------------------------------
# Show the radius of the incircle.

plt.plot([0, 0], [0, radius], linestyle="--")

plt.text(
    0.25,
    radius / 2,
    "3",
    fontsize=12
)


# -----------------------------------------------------------------------------
# Calculate the requested quantity.

answer = r**2 + s**2

print(f"r = {r}")
print(f"s = {s}")
print(f"r^2 + s^2 = {answer:.0f}")


# -----------------------------------------------------------------------------
# Finish the graph.

plt.title(
    f"Isosceles Trapezoid with Inscribed Circle\n"
    f"$r^2 + s^2 = {answer:.0f}$"
)

plt.axis("equal")
plt.axis("off")

plt.show()
