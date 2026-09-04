# Jim McCleery
# September 4, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2022_c68590
#
# Problem:
# In convex quadrilateral ABCD, AB = 11 and CD = 13.
# Point P is such that triangles ADP and BCP are congruent
# equilateral triangles.
#
# Find the common side length of the equilateral triangles.

from math import pi, radians, sin, cos, acos, degrees
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# The common side length of the two equilateral triangles.
#
# Solving
#
#     alpha + beta = 240 degrees
#
#     11^2 = 2s^2 - 2s^2 cos(alpha)
#     13^2 = 2s^2 - 2s^2 cos(beta)
#
# gives s = 7.
# -----------------------------------------------------------------------------

s = 7


# -----------------------------------------------------------------------------
# Find alpha and beta from the Law of Cosines.
#
# For an isosceles triangle with two sides of length s and opposite
# side length d,
#
#     d^2 = s^2 + s^2 - 2s^2 cos(angle)
#
# so
#
#     angle = acos((2s^2 - d^2) / (2s^2))
# -----------------------------------------------------------------------------

alpha = acos((2 * s**2 - 11**2) / (2 * s**2))
beta = acos((2 * s**2 - 13**2) / (2 * s**2))

print(f"alpha = {degrees(alpha):.3f} degrees")
print(f"beta  = {degrees(beta):.3f} degrees")
print(f"alpha + beta = {degrees(alpha + beta):.3f} degrees")


# -----------------------------------------------------------------------------
# Half-angles needed to position B and C.
# -----------------------------------------------------------------------------

alpha_half = (pi - alpha) / 2
beta_half = (pi - beta) / 2


# -----------------------------------------------------------------------------
# Coordinates
#
# Place equilateral triangle ADP so that AD lies on the x-axis.
#
# A = (0, 0)
# D = (7, 0)
#
# Since ADP is equilateral, P is 60 degrees above AD.
# -----------------------------------------------------------------------------

Ax, Ay = 0, 0
Dx, Dy = s, 0

Px = s * cos(pi / 3)
Py = s * sin(pi / 3)


# -----------------------------------------------------------------------------
# AB = 11.
#
# The direction of AB is determined by alpha_half.
# -----------------------------------------------------------------------------

Bx = 11 * cos(pi / 3 + alpha_half)
By = 11 * sin(pi / 3 + alpha_half)


# -----------------------------------------------------------------------------
# CD = 13.
#
# Start at D and move 13 units in the direction determined by beta_half.
# -----------------------------------------------------------------------------

Cx = Dx + 13 * cos(2 * pi / 3 - beta_half)
Cy = Dy + 13 * sin(2 * pi / 3 - beta_half)


# -----------------------------------------------------------------------------
# Print the coordinates.
# -----------------------------------------------------------------------------

print()
print(f"A = ({Ax:.3f}, {Ay:.3f})")
print(f"B = ({Bx:.3f}, {By:.3f})")
print(f"C = ({Cx:.3f}, {Cy:.3f})")
print(f"D = ({Dx:.3f}, {Dy:.3f})")
print(f"P = ({Px:.3f}, {Py:.3f})")


# -----------------------------------------------------------------------------
# Draw quadrilateral ABCD.
#
# The boundary is:
#
#     A -> B -> C -> D -> A
# -----------------------------------------------------------------------------

plt.plot(
    [Ax, Bx, Cx, Dx, Ax],
    [Ay, By, Cy, Dy, Ay],
    linewidth=2
)


# -----------------------------------------------------------------------------
# Draw the segments from P.
# These show the two equilateral triangles ADP and BCP.
# -----------------------------------------------------------------------------

plt.plot([Ax, Px, Dx], [Ay, Py, Dy], linewidth=2)
plt.plot([Bx, Px, Cx], [By, Py, Cy], linewidth=2)


# -----------------------------------------------------------------------------
# Shade equilateral triangle ADP.
# -----------------------------------------------------------------------------

plt.fill(
    [Ax, Dx, Px],
    [Ay, Dy, Py],
    color="red",
    alpha=0.45
)


# -----------------------------------------------------------------------------
# Shade equilateral triangle BCP.
# -----------------------------------------------------------------------------

plt.fill(
    [Bx, Cx, Px],
    [By, Cy, Py],
    color="red",
    alpha=0.45
)


# -----------------------------------------------------------------------------
# Plot and label the five points.
# -----------------------------------------------------------------------------

points = {
    "A": (Ax, Ay),
    "B": (Bx, By),
    "C": (Cx, Cy),
    "D": (Dx, Dy),
    "P": (Px, Py),
}

for label, (x, y) in points.items():
    plt.plot(x, y, "ko")
    plt.annotate(
        label,
        (x, y),
        xytext=(7, 7),
        textcoords="offset points",
        fontsize=13
    )


# -----------------------------------------------------------------------------
# Label the two given side lengths.
# -----------------------------------------------------------------------------

plt.text(
    (Ax + Bx) / 2,
    (Ay + By) / 2,
    "11",
    fontsize=12
)

plt.text(
    (Cx + Dx) / 2,
    (Cy + Dy) / 2,
    "13",
    fontsize=12
)


# -----------------------------------------------------------------------------
# Finish the graph.
#
# axis("equal") keeps the x- and y-scales equal so the equilateral
# triangles really look equilateral.
# -----------------------------------------------------------------------------

plt.title(f"The side length of each equilateral triangle is {s}.")
plt.axis("equal")
plt.axis("off")
plt.show()
