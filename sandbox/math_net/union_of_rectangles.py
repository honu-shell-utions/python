"""
Jim McCleery
May 14, 2026
Kailua-Kona, HI

https://mathnet.mit.edu/explorer.html?p=usa_2022_d2aa03
"""

from math import atan, sqrt, sin, cos
from matplotlib.pyplot import plot, title, axis, show


def polygon_area(vertices):
    """
    Compute the area of a polygon using the shoelace formula.

    The vertices should be listed in order around the boundary
    of the polygon, either clockwise or counterclockwise.
    """
    area = 0
    n = len(vertices)

    # Sum the cross-products of consecutive vertices.
    # The modulo wraps the last vertex back to the first.
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2

    return abs(area) / 2


def plot_line(x1, y1, x2, y2):
    """
    Draw a thin gray line segment from (x1, y1) to (x2, y2).
    """
    plot([x1, x2], [y1, y2], color="gray", linewidth=1)


def polygon_draw(points):
    """
    Draw the outer polygon determined by the given points.

    The first point is repeated at the end so that matplotlib
    closes the polygon visually.
    """
    x = [p[0] for p in points] + [points[0][0]]
    y = [p[1] for p in points] + [points[0][1]]
    plot(x, y, marker="o", linewidth=3)


def rectangle_draw(points):
    """
    Draw a rectangle from its four corner points.

    The first point is repeated at the end so that the rectangle
    is drawn as a closed shape.
    """
    x = [p[0] for p in points] + [points[0][0]]
    y = [p[1] for p in points] + [points[0][1]]
    plot(x, y, linewidth=1.5)


# Initial rectangle dimensions and direction angle.
# The first rectangle has length 4, width 3, and lies along the x-axis.
length, width, theta = 4, 3, 0

# Store the vectors u_i that determine the corners of the rectangles.
# The first two points are the origin P and the first endpoint of R0.
corners = [(0, 0), (4, 0)]

# Generate u1, u2, u3, and u4.
#
# Each step rotates by the angle alpha and updates the rectangle dimensions.
# u4 is needed because it is the far corner of R3.
for _ in range(4):
    # The angle between the current length direction and the diagonal.
    alpha = atan(width / length)

    # The new length is the diagonal of the current rectangle.
    length = sqrt(length**2 + width**2)

    # The new width is the projection of the old width after rotation.
    width = width * cos(alpha)

    # Accumulate the total rotation angle.
    theta += alpha

    # Add the next vector u_i.
    corners.append((length * cos(theta), length * sin(theta)))


# Draw each rectangle without the spikey outer triangular parts.
#
# Rectangle R_i has corners:
#   origin, u_i, u_{i+1}, u_{i+1} - u_i
for i in range(1, 5):
    ux, uy = corners[i]
    vx, vy = corners[i + 1]

    rectangle = [
        (0, 0),
        (ux, uy),
        (vx, vy),
        (vx - ux, vy - uy)
    ]

    rectangle_draw(rectangle)


# The final boundary point of the outer polygon is u4 - u3,
# which is the other side vector of rectangle R3.
x1, y1 = corners[-1]
x2, y2 = corners[-2]
corners.append((x1 - x2, y1 - y2))


# Draw radial lines from the origin to the main corner vectors.
# The last two points are omitted because they are not radial u_i vectors.
for c in corners[:-2]:
    plot_line(0, 0, *c)


# Draw the outer boundary polygon.
polygon_draw(corners)

# Compute and display the area of the outer polygon.
area = polygon_area(corners)

title("Area of the polygon = " + str(area))
axis("equal")
show()
