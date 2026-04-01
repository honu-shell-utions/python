# Python solution to Andy's math problem
# Video: https://youtu.be/Y3YMP86IvdI?si=FFK-Pb3QEVUoJBPM
#
# This program explores an alternative solution numerically.
# It uses Python both to investigate the geometry and to draw the figure.
#
# Jim McCleery
# March 28, 2026
# Kona, HI

from math import sin, cos, pi, sqrt
from matplotlib.pyplot import *
from random import uniform

# -----------------------------------------------------------------------------
# Draw a line segment between two points.
# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# Compute the area of a polygon from its vertices using the shoelace formula.
# -----------------------------------------------------------------------------
def poly_area(vertices):
    n = len(vertices)
    area = 0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # wrap around to the first vertex
        area += x1 * y2 - y1 * x2

    return abs(area) / 2


# -----------------------------------------------------------------------------
# Return x- and y-coordinate lists suitable for matplotlib fill().
# The polygon is closed by repeating the first vertex at the end.
# -----------------------------------------------------------------------------
def poly_shade(vertices):
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords


# -----------------------------------------------------------------------------
# Alternate analytical setup
#
# Let:
#   s = side length of the hexagon
#   a = short side of the right triangle on the base
#
# Blue area:
#   formed by (x0,y0), (x5,y5), (x4,y4), (x6,y6)
#
# Yellow area:
#   formed by (x6,y6), (x2,y2), (x1,y1)
#
# Assume: s = side of hexagon, a = short side of right triangle: (x0,y0) to (x6,y6)
# blue area: s*sqrt(3)/2*s/2+a*s*sqrt(3)/2 = 2
# yellow area: 1/2*s*(s-a)sqrt(3)/2 = 1
# solving this system yeilds: s = 4/sqrt(3*sqrt(3))
#
# From the geometry:
#   blue area   = 2
#   yellow area = 1
#
# Solving the resulting system gives:
#   s = 4 / sqrt(3 * sqrt(3))
#     ≈ 1.754765350603
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# Exploration version
#
# Randomly sample values of s until the blue region has area 2.
# -----------------------------------------------------------------------------
while True:
    # If the total hexagon area is assumed to lie between 3 and 10,
    # then the side length s lies roughly between 1 and 2.
    s = uniform(1, 2)

    # Solve
    #   1 = (1/2) * s * (s - a) * sin(120°)
    # for a in terms of s.
    a = s - 4 / (s * sqrt(3))

    # Define the hexagon vertices.
    x0, y0 = 0, 0
    x1, y1 = s, 0

    # Build the remaining vertices using polar-coordinate steps.
    x2, y2 = x1 + s * cos(pi / 3), y1 + s * sin(pi / 3)
    x3, y3 = x2 + s * cos(2 * pi / 3), y2 + s * sin(2 * pi / 3)
    x4, y4 = x3 - s, y3
    x5, y5 = s * cos(2 * pi / 3), s * sin(2 * pi / 3)

    # Point on the base that determines the interior segments.
    x6, y6 = a, 0

    # Blue region
    vertices1 = [(x0, y0), (x6, y6), (x4, y4), (x5, y5)]
    area1 = poly_area(vertices1)

    if abs(area1 - 2) < 0.00001:
        break


# Yellow region
vertices2 = [(x1, y1), (x2, y2), (x6, y6)]

# Green region (the unknown area to be determined)
vertices3 = [(x6, y6), (x2, y2), (x3, y3), (x4, y4)]


# Fill the three regions with color.
fill(*poly_shade(vertices1), color='lightblue', edgecolor='blue', linewidth=2)
fill(*poly_shade(vertices2), color='yellow', edgecolor='yellow', linewidth=2)
fill(*poly_shade(vertices3), color='lightgreen', edgecolor='green', linewidth=2)


# Compute the unknown area.
area = round(poly_area(vertices3), 3)


# Label the points and region areas.
text(x0 - .1, y0 - 0.1, '(x0,y0)')
text(x1 - .1, y1 - 0.1, '(x1,y1)')
text(x2 + .1, y2, '(x2,y2)')
text(x3 - .1, y3 + .1, '(x3,y3)')
text(x4 - .1, y4 + .1, '(x4,y4)')
text(x5 - .4, y5, '(x5,y5)')
text(x6 - .1, y6 - 0.1, '(x6,y6)')
text(-0.3, 1.5, '2')
text(1.5, .25, '1')
text(1, 2, str(area))


# Draw the outer hexagon and the two interior segments.
plot_line(x0, y0, x1, y1)
plot_line(x1, y1, x2, y2)
plot_line(x2, y2, x3, y3)
plot_line(x3, y3, x4, y4)
plot_line(x4, y4, x5, y5)
plot_line(x5, y5, x0, y0)
plot_line(x6, y6, x4, y4)
plot_line(x6, y6, x2, y2)

axis('equal')
axis('off')
show()
