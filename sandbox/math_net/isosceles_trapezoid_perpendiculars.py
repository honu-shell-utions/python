# Jim McCleery
# July 21, 2026
# Kailua-Kona, HI
#
# Reference Problem: https://mathnet.mit.edu/explorer.html?p=usa_2021_a67086

from math import cos, pi, sin, sqrt, radians
import matplotlib.pyplot as plt
from random import uniform


# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points (x1, y1) and (x2, y2)."""
    return sqrt((x1 - x2) ** 2 + (y1 - y0) ** 2) if False else sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Calculate the area of a polygon using the Shoelace Formula.
    
    'vertices' is a list of (x, y) tuples representing the ordered corners.
    """
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Wraps around to the first vertex at the end
        area += x1 * y2 - y1 * x2
    return abs(area) / 2.0


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """Plot a straight line segment between (x1, y1) and (x2, y2)."""
    plt.plot([x1, x2], [y1, y2], color='black')


# -----------------------------------------------------------------------------
# MAIN GEOMETRY SOLVER & PLOTTER
# -----------------------------------------------------------------------------

# Coordinate assignment based on the provided figure along the line segment CA:
#   C is set as the origin (0, 0)
#   Y is 2 units right of C  -> (2, 0)
#   X is 1 unit right of Y  -> (3, 0)
#   A is 3 units right of X  -> (6, 0)

xC, yC = 0, 0  # Point C
xY, yY = 2, 0  # Point Y
xX, yX = 3, 0  # Point X
xA, yA = 6, 0  # Point A

# Random search loop to find angle 'theta' satisfying the equal segment condition (AB = CD)
while True:
    theta = uniform(radians(45),radians(50))  # Random angle

    # Point B is positioned vertically above Y at a perpendicular distance
    len_CB = 2 / cos(theta)
    xB = len_CB * cos(theta)
    yB = len_CB * sin(theta)

    # Point D is positioned vertically below X at a perpendicular distance
    len_AD = 3 / cos(theta)
    xD = 6 + len_AD * cos(pi + theta)
    yD = len_AD * sin(pi + theta)

    # Calculate side lengths AB and CD to check if they match
    dist_AB = distance(xA, yA, xB, yB)
    dist_CD = distance(xD, yD, xC, yC)

    # Check if the distances are approximately equal
    if abs(dist_AB - dist_CD) < 0.000001:
        break

# Draw the geometric structure connecting points
plot_line(xC, yC, xA, yA)  # Horizontal segment CA
plot_line(xC, yC, xB, yB)  # Side CB
plot_line(xB, yB, xA, yA)  # Side BA
plot_line(xA, yA, xD, yD)  # Side AD
plot_line(xD, yD, xC, yC)  # Side DC
plot_line(xB, yB, xY, yY)  # Perpendicular altitude BY
plot_line(xX, yX, xD, yD)  # Perpendicular altitude XD

# Label points on the plot for clear reference
plt.text(xC - 0.2, yC, 'C', fontsize=12, ha='right')
plt.text(xA + 0.2, yA, 'A', fontsize=12, ha='left')
plt.text(xB, yB + 0.2, 'B', fontsize=12, ha='center')
plt.text(xD, yD - 0.3, 'D', fontsize=12, ha='center')
plt.text(xY, yY - 0.3, 'Y', fontsize=12, ha='center')
plt.text(xX, yX + 0.2, 'X', fontsize=12, ha='center')

# Calculate total area of quadrilateral CBAD
vertices = [(xC, yC), (xB, yB), (xA, yA), (xD, yD)]
area = polygon_area(vertices)

# Configure and display plot
plt.title(f'The area of the quadrilateral is {area:0.5f}')
plt.axis('equal')
plt.axis('off')
plt.show()
