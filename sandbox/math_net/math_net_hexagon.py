# Jim McCleery
# May 17, 2026
# Kailua-Kona, HI
#
# Source problem:
# https://mathnet.mit.edu/explorer.html?p=usa_2022_4b852b

# -----------------------------------------------------------------------------
# This program uses geometry to draw a figure made from three circles and
# a polygon. It searches for a value of r1 that makes one particular distance
# approximately equal to 2.
# -----------------------------------------------------------------------------

from math import sqrt, acos, cos, sin, pi
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """
    Return the distance between two points.

    The formula is the usual distance formula:
        distance = sqrt((x2 - x1)^2 + (y2 - y1)^2)
    """
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# -----------------------------------------------------------------------------
def circle_circle_intersections(x0, y0, r0, x1, y1, r1):
    """
    Find the intersection points of two circles.

    Circle 1 has center (x0, y0) and radius r0.
    Circle 2 has center (x1, y1) and radius r1.

    Returns:
        x3, y3, x4, y4, True     if the circles intersect
        0, 0, 0, 0, False        if they do not intersect
    """

    # Distance between the centers of the two circles
    d = distance(x0, y0, x1, y1)

    # If the centers are the same, this formula will not work.
    if d == 0:
        return 0, 0, 0, 0, False

    # Check whether the circles are too far apart or one is inside the other.
    if d > r0 + r1 or d < abs(r0 - r1):
        return 0, 0, 0, 0, False

    # Distance from the first center to the midpoint of the chord
    a = (r0**2 - r1**2 + d**2) / (2 * d)

    # Half-length of the chord between the two intersection points
    h_squared = r0**2 - a**2

    # Small negative values can occur because of floating-point roundoff.
    if h_squared < 0:
        return 0, 0, 0, 0, False

    h = sqrt(h_squared)

    # Point halfway between the two circle intersection points
    x2 = x0 + a * (x1 - x0) / d
    y2 = y0 + a * (y1 - y0) / d

    # The two actual intersection points
    x3 = x2 + h * (y1 - y0) / d
    y3 = y2 - h * (x1 - x0) / d

    x4 = x2 - h * (y1 - y0) / d
    y4 = y2 + h * (x1 - x0) / d

    return x3, y3, x4, y4, True


# -----------------------------------------------------------------------------
def circle_from_three_points(x1, y1, x2, y2, x3, y3):
    """
    Find the circle passing through three points.

    Returns:
        center_x, center_y, radius

    Note:
        The three points must not be on the same line.
    """

    temp = x2**2 + y2**2

    bc = (x1**2 + y1**2 - temp) / 2
    cd = (temp - x3**2 - y3**2) / 2

    determinant = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    center_x = (bc * (y2 - y3) - cd * (y1 - y2)) / determinant
    center_y = ((x1 - x2) * cd - (x2 - x3) * bc) / determinant

    radius = distance(center_x, center_y, x1, y1)

    return center_x, center_y, radius


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Return the area of a polygon using the shoelace formula.

    The vertices should be listed in order around the polygon.
    """

    area_sum = 0
    number_of_vertices = len(vertices)

    for i in range(number_of_vertices):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % number_of_vertices]

        area_sum += x1 * y2 - y1 * x2

    return abs(area_sum) / 2


# -----------------------------------------------------------------------------
def polygon_fill_coordinates(vertices):
    """
    Return x-values and y-values that matplotlib can use to fill a polygon.

    The first point is repeated at the end so the polygon closes.
    """

    x_values, y_values = zip(*vertices)

    x_values = list(x_values) + [x_values[0]]
    y_values = list(y_values) + [y_values[0]]

    return x_values, y_values


# -----------------------------------------------------------------------------
def plot_circle(center_x, center_y, radius, start_angle=0, stop_angle=2 * pi):
    """
    Plot a circle or part of a circle.

    Angles are measured in radians.
    """

    angles = np.linspace(start_angle, stop_angle, 1500)

    x_values = center_x + radius * np.cos(angles)
    y_values = center_y + radius * np.sin(angles)

    plt.plot(x_values, y_values)


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Plot a line segment from (x1, y1) to (x2, y2).
    """

    plt.plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------

# We are searching for a radius r1 between 11.5 and 12.
# The program tries many possible values until the target distance is close to 2.
possible_radii = np.linspace(11.5, 12, 10**6)

target_distance = 2
tolerance = 0.000001

for r1 in possible_radii:
    r2 = 15 - r1

    # Centers of the first two circles
    x0, y0 = 0, 0
    x1, y1 = r1 + r2, 0

    # This angle comes from the geometry of the problem.
    theta = acos((r1**2 - r2**2 + 15**2 - 16**2) / (30 * r1 + 32 * r2))

    # Point on the first circle
    x2 = r1 * cos(-theta)
    y2 = r1 * sin(-theta)

    # Point where the circle centered at (x2, y2) with radius 16
    # intersects the second circle.
    x3, y3, _, _, ok = circle_circle_intersections(x2, y2, 16, x1, y1, r2)

    if not ok:
        continue

    # Find the circle passing through points (x0, y0), (x2, y2), and (x3, y3).
    x4, y4, r3 = circle_from_three_points(x0, y0, x2, y2, x3, y3)

    # Find intersections between the third circle and the first circle.
    x5, y5, _, _, ok = circle_circle_intersections(x4, y4, r3, x0, y0, r1)

    if not ok:
        continue

    # Find intersections between the third circle and the second circle.
    _, _, x6, y6, ok = circle_circle_intersections(x4, y4, r3, x1, y1, r2)

    if not ok:
        continue

    # Check whether the distance between these two points is close to 2.
    d = distance(x5, y5, x6, y6)

    if abs(d - target_distance) < tolerance:
        break


# -----------------------------------------------------------------------------
# Compute and draw the final polygon
# -----------------------------------------------------------------------------

vertices = [
    (x0, y0),
    (x5, y5),
    (x6, y6),
    (x1, y1),
    (x3, y3),
    (x2, y2),
]

area = polygon_area(vertices)

# Fill the polygon.
plt.fill(
    *polygon_fill_coordinates(vertices),
    color="red",
    edgecolor="red",
    linewidth=2
)

# Draw the important line segments.
plot_line(x0, y0, x2, y2)
plot_line(x1, y1, x3, y3)
plot_line(x3, y3, x2, y2)
plot_line(x5, y5, x6, y6)
plot_line(x0, y0, x5, y5)
plot_line(x6, y6, x1, y1)

# Draw the three circles.
plot_circle(x0, y0, r1)
plot_circle(x1, y1, r2)
plot_circle(x4, y4, r3)

# Display the area in the title.
plt.title(f"area = {area:.2f}")

# Use equal scaling so circles look like circles instead of ellipses.
plt.axis("equal")

plt.show()
