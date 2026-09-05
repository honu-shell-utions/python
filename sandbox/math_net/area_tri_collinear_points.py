# Jim McCleery
# September 5, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2025_1bac32
#
# Problem:
# Six points A, B, C, D, E, and F lie on a straight line in that order.
#
# AC = 26
# BD = 22
# CE = 31
# DF = 33
# AF = 73
# CG = 40
# DG = 30
#
# Find the area of triangle BGE.

# -----------------------------------------------------------------------------
from math import sqrt
import matplotlib.pyplot as plt


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
        ((x3, y3), (x4, y4))
    """

    # Distance between the two circle centers.
    d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    # Distance from the first center to the midpoint
    # of the common chord.
    a = (r0**2 - r1**2 + d**2) / (2 * d)

    # Half the length of the common chord.
    h = sqrt(r0**2 - a**2)

    # Point on the line joining the two circle centers.
    x2 = x0 + a * (x1 - x0) / d
    y2 = y0 + a * (y1 - y0) / d

    # The two circle intersection points.
    x3 = x2 + h * (y1 - y0) / d
    y3 = y2 - h * (x1 - x0) / d

    x4 = x2 - h * (y1 - y0) / d
    y4 = y2 + h * (x1 - x0) / d

    return (x3, y3), (x4, y4)


# -----------------------------------------------------------------------------
def triangle_area(base, height):
    """
    Return the area of a triangle.

    Formula:
        area = 1/2 * base * height
    """
    return 0.5 * base * height


# -----------------------------------------------------------------------------
# Put A at the origin and place all six collinear points on the x-axis.
#
# Since AC = 26:
#     A = (0, 0)
#     C = (26, 0)
#
# Since AF = 73:
#     F = (73, 0)

A = (0, 0)
C = (26, 0)
F = (73, 0)


# -----------------------------------------------------------------------------
# Find the remaining points on the x-axis.
#
# BD = 22
# CE = 31  --> E = 26 + 31 = 57
# DF = 33  --> D = 73 - 33 = 40
# Therefore B = D - 22 = 18

B = (18, 0)
D = (40, 0)
E = (57, 0)


# -----------------------------------------------------------------------------
# Point G is 40 units from C and 30 units from D.
#
# Therefore G is an intersection of:
#
#     circle centered at C with radius 40
#     circle centered at D with radius 30

G1, G2 = circle_circle_intersections(
    C[0], C[1], 40,
    D[0], D[1], 30
)

# There are two possible points G, one above and one below the x-axis.
# Choose the one above the line for the drawing.
G = max(G1, G2, key=lambda point: point[1])


# -----------------------------------------------------------------------------
# Triangle BGE has horizontal base BE.
#
# B = (18, 0)
# E = (57, 0)
#
# Therefore:
#     BE = 57 - 18 = 39
#
# Since G = (58, 24), the perpendicular height to line BE is 24.

base_BE = E[0] - B[0]
height_G = abs(G[1])

area = triangle_area(base_BE, height_G)


# -----------------------------------------------------------------------------
# Display useful numerical information.

print(f"A = {A}")
print(f"B = {B}")
print(f"C = {C}")
print(f"D = {D}")
print(f"E = {E}")
print(f"F = {F}")
print(f"G = {G}")
print()

print(f"BE = {base_BE}")
print(f"Height from G to BE = {height_G}")
print(f"Area of triangle BGE = {area}")


# -----------------------------------------------------------------------------
# Draw the diagram.

# Draw the line containing A, B, C, D, E, and F.
plt.plot([-5, 78], [0, 0], linewidth=1)

# Draw and shade triangle BGE.
triangle_x = [B[0], G[0], E[0], B[0]]
triangle_y = [B[1], G[1], E[1], B[1]]

plt.fill(
    triangle_x,
    triangle_y,
    color="red",
    alpha=0.35
)

plt.plot(
    triangle_x,
    triangle_y,
    color="red",
    linewidth=2
)


# -----------------------------------------------------------------------------
# Plot and label the seven points.

points = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
    "F": F,
    "G": G,
}

for label, (x, y) in points.items():

    # Draw the point.
    plt.plot(x, y, "o")

    # Put labels slightly away from the points so they are easy to read.
    if label == "G":
        plt.text(x + 1, y + 1, label, fontsize=12)
    else:
        plt.text(x, y - 2, label, fontsize=12, ha="center")


# -----------------------------------------------------------------------------
# Finish the graph.

plt.title(f"Area of triangle BGE = {area:.0f}")
plt.axis("equal")
plt.axis("off")
plt.show()
