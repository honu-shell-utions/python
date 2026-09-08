# Jim McCleery
# September 8, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2023_4c2636
#
# Regular Hexagon Monte Carlo Simulation
#
# Given:
#     Area of triangle PBC = 20
#     Area of triangle PAD = 23
#
# Goal:
#     Estimate the area of regular hexagon ABCDEF.
#
# -----------------------------------------------------------------------------

from math import sqrt
from random import uniform

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def triangle_area(a, b, c):
    """
    Find the area of a triangle from the coordinates of its three vertices.

    Each point is written as a tuple:
        (x, y)

    This formula is a version of the shoelace formula.
    """
    x1, y1 = a
    x2, y2 = b
    x3, y3 = c

    return abs(
        x1 * (y2 - y3)
        + x2 * (y3 - y1)
        + x3 * (y1 - y2)
    ) / 2


# -----------------------------------------------------------------------------
def point_in_polygon(point, polygon):
    """
    Return True if a point is inside a polygon.

    This uses the ray-casting method. Imagine drawing a horizontal ray
    from the point toward the right. If it crosses the boundary an odd
    number of times, the point is inside the polygon.
    """
    x, y = point
    inside = False

    j = len(polygon) - 1

    for i in range(len(polygon)):
        xi, yi = polygon[i]
        xj, yj = polygon[j]

        crosses = ((yi > y) != (yj > y))

        if crosses:
            x_crossing = (xj - xi) * (y - yi) / (yj - yi) + xi

            if x < x_crossing:
                inside = not inside

        j = i

    return inside


# -----------------------------------------------------------------------------
def make_hexagon(side):
    """
    Create the six vertices of a regular hexagon with side length 'side'.

    The orientation is

              E ----- D
             /         \
            F           C
             \         /
              A ----- B

    The coordinates are chosen so that AB is horizontal.
    """
    h = sqrt(3) * side / 2

    A = (0, 0)
    B = (side, 0)
    C = (1.5 * side, h)
    D = (side, 2 * h)
    E = (0, 2 * h)
    F = (-0.5 * side, h)

    return A, B, C, D, E, F


# -----------------------------------------------------------------------------
# Monte Carlo search
#
# The exact side length is somewhere between 8 and 9.
#
# For each trial:
#   1. Choose a random side length.
#   2. Construct the regular hexagon.
#   3. Choose a random point P.
#   4. Keep P only if it lies inside quadrilateral ABCD.
#   5. Compute the areas of PBC and PAD.
#   6. Remember the trial that comes closest to the required areas.
#
# More trials generally give a better approximation.

number_of_trials = 10**7

best_error = float("inf")
best_side = None
best_point = None
best_vertices = None
best_area_PBC = None
best_area_PAD = None


for _ in range(number_of_trials):

    # Choose a possible side length for the regular hexagon.
    side = uniform(8, 9)

    # Construct the hexagon.
    A, B, C, D, E, F = make_hexagon(side)

    # ABCD is the quadrilateral in which P must lie.
    quadrilateral = [A, B, C, D]

    # Choose a random point from a rectangle containing ABCD.
    x = uniform(0, 1.5 * side)
    y = uniform(0, sqrt(3) * side)
    P = (x, y)

    # Ignore the point if it is outside ABCD.
    if not point_in_polygon(P, quadrilateral):
        continue

    # Calculate the two triangle areas.
    area_PBC = triangle_area(P, B, C)
    area_PAD = triangle_area(P, A, D)

    # Measure how close this trial is to the required areas 20 and 23.
    #
    # A perfect trial would have error = 0.
    error = (area_PBC - 20) ** 2 + (area_PAD - 23) ** 2

    # Save this trial if it is the best one so far.
    if error < best_error:
        best_error = error
        best_side = side
        best_point = P
        best_vertices = (A, B, C, D, E, F)
        best_area_PBC = area_PBC
        best_area_PAD = area_PAD


# -----------------------------------------------------------------------------
# Calculate the area of the best hexagon found.
#
# A regular hexagon consists of six equilateral triangles.
#
# Area of one equilateral triangle:
#     sqrt(3) / 4 * side^2
#
# Therefore:
#     hexagon area = 6 * sqrt(3)/4 * side^2
#                  = 3*sqrt(3)/2 * side^2

hexagon_area = 3 * sqrt(3) / 2 * best_side**2


# -----------------------------------------------------------------------------
# Display the numerical results.

print(f"Side length          = {best_side:.6f}")
print(f"Area of triangle PBC = {best_area_PBC:.6f}")
print(f"Area of triangle PAD = {best_area_PAD:.6f}")
print(f"Area of hexagon      = {hexagon_area:.6f}")


# -----------------------------------------------------------------------------
# Draw the best Monte Carlo result.

A, B, C, D, E, F = best_vertices
P = best_point

# Draw and lightly shade the hexagon.
hexagon = [A, B, C, D, E, F, A]

x_hex = [point[0] for point in hexagon]
y_hex = [point[1] for point in hexagon]

plt.fill(x_hex, y_hex, alpha=0.20)
plt.plot(x_hex, y_hex, linewidth=2)


# Shade triangle PBC.
triangle_PBC = [P, B, C, P]

plt.fill(
    [point[0] for point in triangle_PBC],
    [point[1] for point in triangle_PBC],
    alpha=0.35,
)


# Shade triangle PAD.
triangle_PAD = [P, A, D, P]

plt.fill(
    [point[0] for point in triangle_PAD],
    [point[1] for point in triangle_PAD],
    alpha=0.35,
)


# Mark point P.
plt.plot(P[0], P[1], "o")


# -----------------------------------------------------------------------------
# Add the coordinate labels A, B, C, D, E, F, and P.

labels = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
    "F": F,
    "P": P,
}

for label, (x, y) in labels.items():
    plt.text(
        x + 0.10,
        y + 0.10,
        label,
        fontsize=14,
        fontweight="bold",
    )


# Add the given triangle areas to the picture.
mid_PBC_x = (P[0] + B[0] + C[0]) / 3
mid_PBC_y = (P[1] + B[1] + C[1]) / 3

mid_PAD_x = (P[0] + A[0] + D[0]) / 3
mid_PAD_y = (P[1] + A[1] + D[1]) / 3

plt.text(mid_PBC_x, mid_PBC_y, "20", fontsize=13)
plt.text(mid_PAD_x, mid_PAD_y, "23", fontsize=13)


# Finish the graph.
plt.title(f"Monte Carlo estimate: hexagon area = {hexagon_area:.1f}")
plt.axis("equal")
plt.axis("off")
plt.show()
