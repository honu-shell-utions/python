# -----------------------------------------------------------------------------
# Jim McCleery
# June 24, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2022_bbefc1
# -----------------------------------------------------------------------------

# Import math functions for geometry calculations
from math import pi, sqrt, cos, sin, acos

# Import matplotlib functions for drawing and text annotation
from matplotlib.pyplot import plot, fill, title, axis, show, text

# Import uniform to generate random numbers for the simulation
from random import uniform


# -----------------------------------------------------------------------------
# GEOMETRY HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def distance(x1, y1, x2, y2):
    """Calculate the straight-line distance between two points."""
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def quadratic_equation(A, B, C):
    """Solve a standard quadratic equation: A*x^2 + B*x + C = 0."""
    try:
        disc = B**2 - 4 * A * C
        disc = sqrt(disc)
        x1 = (-B - disc) / (2 * A)
        x2 = (-B + disc) / (2 * A)
        if x1 > x2:
            x1, x2 = x2, x1
        return x1, x2, True
    except:
        return 0, 0, False


def line_circle_intersection(x1, y1, r, m, b):
    """Find where a circle and a line intersect."""
    A = 1 + m**2
    B = -2 * x1 + 2 * m * b - 2 * m * y1
    C = x1**2 + b**2 - 2 * b * y1 + y1**2 - r**2
    
    x2, x3, OK = quadratic_equation(A, B, C)
    if OK:
        y2 = m * x2 + b
        y3 = m * x3 + b
        return x2, y2, x3, y3, OK
    else:
        return 0, 0, 0, 0, False


def polygon_area(vertices):
    """Calculate the area of a polygon using the Shoelace formula."""
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2


# -----------------------------------------------------------------------------
# PLOTTING AND DRAWING HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def plot_circle(x, y, radius):
    """Draw a full circle given its center and radius."""
    import numpy as np
    angle = np.linspace(0, 2 * pi, 1500)
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    plot(x_arr, y_arr, color='gray', linestyle='--')


def plot_line(x1, y1, x2, y2, c='black'):
    """Draw a line segment connecting two points."""
    plot([x1, x2], [y1, y2], color=c)


def polygon_fill_coordinates(vertices):
    """Format vertices into X and Y arrays for structural filling."""
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords


# -----------------------------------------------------------------------------
# MAIN SIMULATION PROGRAM
# -----------------------------------------------------------------------------

# Problem Dimensions
AB = 17
BC = 25
AD = 25
CD = 31
theta = acos(7 / 25)  # Interior base angle of the trapezoid

# Trapezoid Coordinates (Mapping text problem to coordinates)
x0, y0 = 0, 0                                    # Point D
x1, y1 = CD, 0                                   # Point C
x2, y2 = x1 + BC * cos(pi - theta), BC * sin(pi - theta)  # Point B
x3, y3 = AD * cos(theta), AD * sin(theta)        # Point A

# Run the simulation loop to solve for positions matching PQ = 25
while True:
    # Pick a random length segment DP on side AD
    DP = uniform(0, 25)
    QC = 25 - DP  # Ensures AP = CQ because AD = 25, so AP = 25 - DP
    
    # Calculate current locations for P and Q
    x4, y4 = DP * cos(theta), DP * sin(theta)        # Point P
    x5, y5 = x1 + QC * cos(pi - theta), QC * sin(pi - theta)  # Point Q
    
    # Center of the circle (midpoint of PQ)
    x6, y6 = (x5 + x4) / 2, (y5 + y4) / 2
    
    PQ = distance(x4, y4, x5, y5)
    
    # Check if this configuration satisfies PQ = 25
    if abs(PQ - 25) > 0.0001:
        continue

    radius = PQ / 2
    
    # Find circle intersections with side AB (top line: y = y3)
    x7, y7, x8, y8, OK = line_circle_intersection(x6, y6, radius, 0, y3)
    if not OK or x7 < x3 or x8 > x2:
        continue
    
    # Find circle intersections with side CD (bottom line: y = 0)
    x9, y9, x10, y10, OK = line_circle_intersection(x6, y6, radius, 0, 0)
    if not OK or x9 < x0 or x10 > x1:
        continue

    # --- Draw the Trapezoid and Lines ---
    plot_circle(x6, y6, radius)
    plot_line(x0, y0, x1, y1)  # Side DC
    plot_line(x1, y1, x2, y2)  # Side CB
    plot_line(x2, y2, x3, y3)  # Side BA
    plot_line(x3, y3, x0, y0)  # Side AD
    plot_line(x4, y4, x5, y5, c='blue')  # Diameter line PQ

    # Intersecting chords that form the inner quadrilateral
    plot_line(x7, y7, x9, y9)
    plot_line(x8, y8, x10, y10)

    # --- Add Text Labels for Problem Coordinates ---
    text(x3 - 1, y3 + 0.5, 'A', fontsize=12, fontweight='bold')
    text(x2 + 0.5, y2 + 0.5, 'B', fontsize=12, fontweight='bold')
    text(x1 + 0.5, y1 - 1, 'C', fontsize=12, fontweight='bold')
    text(x0 - 1, y0 - 1, 'D', fontsize=12, fontweight='bold')
    text(x4 - 1.5, y4, 'P', fontsize=12, color='blue', fontweight='bold')
    text(x5 + 0.8, y5, 'Q', fontsize=12, color='blue', fontweight='bold')

    # Compile the 4 intersection vertices into the final convex quadrilateral
    vertices = [(x7, y7), (x8, y8), (x10, y10), (x9, y9)]
    
    # Color the requested target area red
    fill(*polygon_fill_coordinates(vertices), color='red', edgecolor='red', alpha=0.5, linewidth=2)
    
    # Output presentation details
    area = polygon_area(vertices)
    title(f'The area of the red quadrilateral is {area:0.1f}')
    
    axis('equal')
    axis('off')
    show()
    break
