# -----------------------------------------------------------------------------
# Jim McCleery
# September 15, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2019_29d9cd
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
from math import sqrt, atan, cos, sin

# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------

def distance(x1, y1, x2, y2):
    """Calculate the straight-line (Euclidean) distance between two points."""
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def incircle_of_triangle(A, B, C):
    """
    Compute the incenter coordinates (x, y) and the inradius (r) of a triangle.
    Uses the side lengths and semi-perimeter formula: Area = r * s.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    # Lengths of sides opposite to vertices A, B, and C
    a = distance(x2, y2, x3, y3)
    b = distance(x1, y1, x3, y3)
    c = distance(x1, y1, x2, y2)

    # Semi-perimeter and Heron's formula for area
    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    inradius = area / s

    # Incenter is the weighted average of the vertices by opposite side lengths
    incenter_x = (a * x1 + b * x2 + c * x3) / (a + b + c)
    incenter_y = (a * y1 + b * y2 + c * y3) / (a + b + c)

    return incenter_x, incenter_y, inradius


def polygon_area(vertices):
    """Calculate the area of a polygon using the Shoelace Formula."""
    n = len(vertices)
    area = 0.0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Connect back to the first point
        area += x1 * y2 - y1 * x2
    return abs(area) / 2.0


def polygon_fill_coordinates(vertices):
    """
    Unpack vertex pairs into separate X and Y coordinate lists,
    repeating the first point at the end to close the polygon loop.
    """
    x_coords = [p[0] for p in vertices] + [vertices[0][0]]
    y_coords = [p[1] for p in vertices] + [vertices[0][1]]
    return x_coords, y_coords


def plot_point(pt, label, offset=(0.08, 0.08)):
    """Plot a single point with a marker and its text label."""
    x, y = pt
    plt.plot(x, y, 'o', color='black', markersize=4)
    plt.text(x + offset[0], y + offset[1], label, fontsize=10, weight='bold')


def plot_line(pt1, pt2):
    """Draw a straight line segment between two points."""
    plt.plot([pt1[0], pt2[0]], [pt1[1], pt2[1]], color='black', linewidth=1.5)


# -----------------------------------------------------------------------------
# Main Setup & Geometric Calculations
# -----------------------------------------------------------------------------

# Define triangle ABC: right-angled at B with sides AB = 3, BC = 4, CA = 5
A = (0, 0)
B = (3, 0)
C = (3, 4)

# Angle of the hypotenuse AC with the x-axis
theta = atan(4 / 3)

# Point P is the incenter of triangle ABC so that the distances (altitudes)
# from P to all three sides are equal to the inradius r.
px, py, r = incircle_of_triangle(A, B, C)
P = (px, py)

# For an equilateral triangle with altitude h = r, the side length is 2*r / sqrt(3)
side = 2 * r / sqrt(3)
half_side = side / 2

# Points on side BC (vertical line x = 3)
A1 = (3, py - half_side)
A2 = (3, py + half_side)

# Points on hypotenuse CA
# Center of side B1B2 along the line from the origin is at distance px / cos(theta)
B1 = ((px + half_side) * cos(theta), (px + half_side) * sin(theta))
B2 = ((px - half_side) * cos(theta), (px - half_side) * sin(theta))

# Points on side AB (horizontal line y = 0)
C1 = (px - half_side, 0)
C2 = (px + half_side, 0)

# -----------------------------------------------------------------------------
# Plotting & Visualization
# -----------------------------------------------------------------------------

fig, ax = plt.subplots(figsize=(7, 7))

# Draw the outer triangle ABC
plot_line(A, B)
plot_line(B, C)
plot_line(C, A)

# Plot and label triangle vertices and the center point P
plot_point(A, '$A$', offset=(-0.25, -0.15))
plot_point(B, '$B$', offset=(0.10, -0.15))
plot_point(C, '$C$', offset=(0.10, 0.05))
plot_point(P, '$P$', offset=(0.08, 0.08))

# Plot and label points defining the equilateral bases
plot_point(A1, '$A_1$', offset=(0.10, -0.05))
plot_point(A2, '$A_2$', offset=(0.10, -0.05))
plot_point(B1, '$B_1$', offset=(-0.25, 0.10))
plot_point(B2, '$B_2$', offset=(-0.25, 0.10))
plot_point(C1, '$C_1$', offset=(-0.05, -0.25))
plot_point(C2, '$C_2$', offset=(-0.05, -0.25))

# Order vertices counter-clockwise around the convex hexagon
hexagon_vertices = [C2, A1, A2, B1, B2, C1]

# Compute and display the hexagon's area
area = polygon_area(hexagon_vertices)

# Fill the hexagon
hx, hy = polygon_fill_coordinates(hexagon_vertices)
ax.fill(hx, hy, color='red', alpha=0.5, edgecolor='darkred', linewidth=2)

# Formatting
ax.set_title(f'Hexagon $A_1A_2B_1B_2C_1C_2$ Area: {area:.5f}', fontsize=12)
ax.set_aspect('equal', 'box')
ax.axis('off')

plt.tight_layout()
plt.show()
