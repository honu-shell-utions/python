# -----------------------------------------------------------------------------
# Jim McCleery
# September 2, 2026
# Kailua-Kona, HI
#
# https://youtu.be/_Ksja5P5054?si=e9XyR9WYoxDTF1x5
#
# Geometry problem:
# Find the area of the shaded quadrilateral ABCD.
#
# The rectangle is 3a units wide and 2a units high.
#
# A = (0, a)
# B = (2a, a)
# C = (3a, 2a)
# D = (3a, 0)
#
# The diagonal AC has length 7.
# -----------------------------------------------------------------------------

from math import sqrt
from random import uniform
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Calculate the area of a polygon using the shoelace formula.

    vertices is a list of (x, y) coordinate pairs written in order
    around the polygon.

    Example:
        vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    """

    area = 0
    number_of_vertices = len(vertices)

    for i in range(number_of_vertices):

        # Current vertex
        x1, y1 = vertices[i]

        # Next vertex.
        # The % operator makes the last vertex connect back to the first.
        x2, y2 = vertices[(i + 1) % number_of_vertices]

        area += x1 * y2 - y1 * x2

    return abs(area) / 2


# -----------------------------------------------------------------------------
def point_in_polygon(x, y, polygon):
    """
    Return True if the point (x, y) is inside a polygon.

    This uses the ray-casting method. Imagine drawing a horizontal ray
    from the point toward the right. If the ray crosses the polygon an
    odd number of times, the point is inside.
    """

    inside = False
    number_of_vertices = len(polygon)

    j = number_of_vertices - 1

    for i in range(number_of_vertices):

        xi, yi = polygon[i]
        xj, yj = polygon[j]

        # Check whether the horizontal ray from (x, y) crosses
        # the edge joining vertices i and j.
        crosses_edge = ((yi > y) != (yj > y))

        if crosses_edge:

            x_crossing = (
                (xj - xi) * (y - yi) / (yj - yi) + xi
            )

            if x < x_crossing:
                inside = not inside

        j = i

    return inside


# -----------------------------------------------------------------------------
# CALCULATE THE SCALE OF THE FIGURE
# -----------------------------------------------------------------------------

# AC has horizontal length 3a and vertical length a.
#
# By the Pythagorean theorem:
#
#       AC² = (3a)² + a²
#        7² = 10a²
#
# Therefore:
#
#       a = 7 / sqrt(10)

a = 7 / sqrt(10)


# -----------------------------------------------------------------------------
# DEFINE THE IMPORTANT POINTS
# -----------------------------------------------------------------------------

# The coordinate system has its origin at the lower-left corner
# of the rectangle.

A = (0, a)
B = (2 * a, a)
C = (3 * a, 2 * a)
D = (3 * a, 0)

# Corners of the surrounding rectangle
lower_left = (0, 0)
upper_left = (0, 2 * a)


# The shaded quadrilateral is A-C-B-D.
#
# The points must be listed in order around its boundary for
# the shoelace formula and for drawing the polygon.

shaded_polygon = [A, C, B, D]


# -----------------------------------------------------------------------------
# EXACT AREA USING THE SHOELACE FORMULA
# -----------------------------------------------------------------------------

analytic_area = polygon_area(shaded_polygon)


# -----------------------------------------------------------------------------
# MONTE CARLO ESTIMATE
# -----------------------------------------------------------------------------

# We randomly throw points into the entire rectangle.
#
# Rectangle area:
#
#       width × height
#       = 3a × 2a
#       = 6a²
#
# The fraction of random points that land inside the shaded polygon
# should approximately equal:
#
#       shaded area / rectangle area

throws = 1_000_000
hits = 0

rectangle_area = 6 * a**2

for _ in range(throws):

    # Pick a random point somewhere inside the rectangle.
    x = uniform(0, 3 * a)
    y = uniform(0, 2 * a)

    # Count it if it lands inside quadrilateral ABCD.
    if point_in_polygon(x, y, shaded_polygon):
        hits += 1


# Estimate the shaded area from the proportion of successful throws.
monte_carlo_area = hits / throws * rectangle_area


# -----------------------------------------------------------------------------
# DISPLAY THE NUMERICAL RESULTS
# -----------------------------------------------------------------------------

print(f"a = {a:.6f}")
print()

print("Coordinates:")
print(f"A = ({A[0]:.3f}, {A[1]:.3f})")
print(f"B = ({B[0]:.3f}, {B[1]:.3f})")
print(f"C = ({C[0]:.3f}, {C[1]:.3f})")
print(f"D = ({D[0]:.3f}, {D[1]:.3f})")
print()

print(f"Shaded polygon area:")
print(f"  Analytic    = {analytic_area:.3f}")
print(f"  Monte Carlo = {monte_carlo_area:.3f}")


# -----------------------------------------------------------------------------
# DRAW THE FIGURE
# -----------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(10, 6))


# -----------------------------------------------------------------------------
# Draw the surrounding 3a by 2a rectangle.
# -----------------------------------------------------------------------------

rectangle_x = [0, 3 * a, 3 * a, 0, 0]
rectangle_y = [0, 0, 2 * a, 2 * a, 0]

ax.plot(
    rectangle_x,
    rectangle_y,
    color="gray",
    linewidth=2
)


# -----------------------------------------------------------------------------
# Draw the internal grid lines shown in the original diagram.
# -----------------------------------------------------------------------------

# Vertical lines at x = a and x = 2a
ax.plot([a, a], [0, 2 * a], color="lightgray")
ax.plot([2 * a, 2 * a], [0, 2 * a], color="lightgray")

# Horizontal center line at y = a
ax.plot([0, 3 * a], [a, a], color="lightgray")


# -----------------------------------------------------------------------------
# Shade quadrilateral ABCD.
# -----------------------------------------------------------------------------

polygon_x = [point[0] for point in shaded_polygon]
polygon_y = [point[1] for point in shaded_polygon]

# Repeat the first point so the polygon closes.
polygon_x.append(shaded_polygon[0][0])
polygon_y.append(shaded_polygon[0][1])

ax.fill(
    polygon_x,
    polygon_y,
    color="skyblue",
    alpha=0.6
)


# -----------------------------------------------------------------------------
# Draw the red outer sides AC and AD.
# -----------------------------------------------------------------------------

ax.plot(
    [A[0], C[0]],
    [A[1], C[1]],
    color="red",
    linewidth=4
)

ax.plot(
    [A[0], D[0]],
    [A[1], D[1]],
    color="red",
    linewidth=4
)


# -----------------------------------------------------------------------------
# Draw the blue segments AB, BC, and BD.
# -----------------------------------------------------------------------------

ax.plot(
    [A[0], B[0]],
    [A[1], B[1]],
    color="blue",
    linewidth=4
)

ax.plot(
    [B[0], C[0]],
    [B[1], C[1]],
    color="blue",
    linewidth=4
)

ax.plot(
    [B[0], D[0]],
    [B[1], D[1]],
    color="blue",
    linewidth=4
)


# -----------------------------------------------------------------------------
# Label the four important coordinates.
# -----------------------------------------------------------------------------

ax.text(
    A[0] - 0.12,
    A[1],
    f"A\n(0, a)",
    fontsize=13,
    horizontalalignment="right",
    verticalalignment="center"
)

ax.text(
    B[0] + 0.10,
    B[1],
    f"B\n(2a, a)",
    fontsize=13,
    horizontalalignment="left",
    verticalalignment="center"
)

ax.text(
    C[0] + 0.10,
    C[1],
    f"C\n(3a, 2a)",
    fontsize=13,
    horizontalalignment="left",
    verticalalignment="center"
)

ax.text(
    D[0] + 0.10,
    D[1],
    f"D\n(3a, 0)",
    fontsize=13,
    horizontalalignment="left",
    verticalalignment="center"
)


# -----------------------------------------------------------------------------
# Label the side AC with its given length, 7.
# -----------------------------------------------------------------------------

ax.text(
    1.3 * a,
    1.55 * a,
    "7",
    color="red",
    fontsize=24,
    fontweight="bold"
)


# -----------------------------------------------------------------------------
# Finish the graph.
# -----------------------------------------------------------------------------

ax.set_title(
    f"Shaded Area: "
    f"analytic = {analytic_area:.3f}, "
    f"Monte Carlo = {monte_carlo_area:.3f}"
)

# Use the same scale horizontally and vertically so the geometry
# is not distorted.
ax.set_aspect("equal")

# Leave a little extra room around the drawing for the labels.
ax.set_xlim(-0.5 * a, 3.5 * a)
ax.set_ylim(-0.25 * a, 2.25 * a)

# Hide ordinary graph axes and tick marks.
ax.axis("off")

plt.show()
