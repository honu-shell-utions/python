# -----------------------------------------------------------------------------
# Jim McCleery
# May 22, 2026
# Kailua-Kona, HI
#
# This program randomly searches for a square and an interior point that divide
# the square into three triangles with areas approximately 36, 20, and 27.
#
# Once the correct arrangement is found, the program draws the square and the
# triangle lines, then displays the area of the square.
# -----------------------------------------------------------------------------

from random import uniform

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Return the area of a polygon using the shoelace formula.

    The polygon must be given as a list of points in order around the polygon.

    Example:
        vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]

    Each point is an ordered pair:
        (x, y)
    """

    # The variable area will accumulate the shoelace sum.
    area = 0

    # n is the number of vertices in the polygon.
    n = len(vertices)

    # Go through each vertex of the polygon.
    for i in range(n):

        # Current vertex
        x1, y1 = vertices[i]

        # Next vertex.
        #
        # The expression (i + 1) % n makes the last vertex connect
        # back to the first vertex.
        x2, y2 = vertices[(i + 1) % n]

        # Add one term of the shoelace formula.
        area += x1 * y2 - y1 * x2

    # The shoelace formula gives twice the signed area.
    # abs() makes the area positive.
    return abs(area) / 2


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Draw a line segment from point (x1, y1) to point (x2, y2).
    """

    plt.plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# This is the allowed error when comparing areas.
#
# Since the program is using random decimal values, we do not expect the areas
# to be exactly 36, 20, and 27. Instead, we accept values that are very close.
error = 0.0001


# -----------------------------------------------------------------------------
# Random search
# -----------------------------------------------------------------------------
while True:

    # Choose a random value for a.
    #
    # The number a controls the placement of some of the points.
    a = uniform(5, 30)

    # Compute the side length of the square.
    #
    # This formula comes from the geometry of the problem.
    s = 238 / (a + 72 / a)

    # This condition avoids arrangements that do not make geometric sense
    # for the intended picture.
    if s < a:
        continue

    # -------------------------------------------------------------------------
    # Define the points used in the diagram.
    # -------------------------------------------------------------------------

    # Bottom-left corner of the square
    x0, y0 = 0, 0

    # Point on the top side of the square
    x1, y1 = s - a, s

    # Point on the right side of the square
    x2, y2 = s, s - 72 / a

    # Bottom-right corner of the square
    x3, y3 = s, 0

    # Top-right corner of the square
    x4, y4 = s, s

    # Top-left corner of the square
    x5, y5 = 0, s

    # Interior point
    x6, y6 = s - a, s - 72 / a

    # -------------------------------------------------------------------------
    # Define the three triangles whose areas we want to check.
    # -------------------------------------------------------------------------

    triangle1 = [(x6, y6), (x1, y1), (x2, y2)]
    triangle2 = [(x0, y0), (x1, y1), (x6, y6)]
    triangle3 = [(x0, y0), (x2, y2), (x6, y6)]

    # Compute the areas of the three triangles.
    area1 = polygon_area(triangle1)
    area2 = polygon_area(triangle2)
    area3 = polygon_area(triangle3)

    # Stop searching when the triangle areas are close enough
    # to the desired values.
    if (
        abs(area1 - 36) < error
        and abs(area2 - 20) < error
        and abs(area3 - 27) < error
    ):
        break


# -----------------------------------------------------------------------------
# Draw the diagram
# -----------------------------------------------------------------------------

# Draw the interior point.
plt.plot(x6, y6, "o")

# Draw the three small triangles.
plot_line(x6, y6, x1, y1)
plot_line(x0, y0, x6, y6)
plot_line(x0, y0, x1, y1)

plot_line(x0, y0, x2, y2)
plot_line(x2, y2, x6, y6)

plot_line(x1, y1, x2, y2)

# Draw the outside square.
plot_line(x0, y0, x3, y3)
plot_line(x3, y3, x4, y4)
plot_line(x4, y4, x5, y5)
plot_line(x5, y5, x0, y0)

# Make the x-scale and y-scale equal so the square looks like a square.
plt.axis("equal")

# Display the area of the square in the plot title.
plt.title(f"Area of Square = {s**2:0.3f}")

# Show the finished picture.
plt.show()
