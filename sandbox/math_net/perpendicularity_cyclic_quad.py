# -----------------------------------------------------------------------------
# Jim McCleery
# June 16, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2012_f3c9b3
# -----------------------------------------------------------------------------

from math import cos, sin, radians
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------
# GEOMETRIC UTILITY FUNCTIONS
# -----------------------------------------------------------------------------

def intersection_of_lines(m1, b1, m2, b2):
    """
    Finds where two straight lines cross using their slopes (m) and intercepts (b).
    Lines are defined by the equation: y = m * x + b
    """
    if m1 == m2:
        return 0, 0, False
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y, True


def line_intersection_from_points(A, B, C, D):
    """
    Finds the intersection point of two lines defined by points.
    Line 1 goes through point A and B. Line 2 goes through point C and D.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D
    
    try:
        m1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - m1 * x1
        
        m2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - m2 * x3
        
        x, y, success = intersection_of_lines(m1, b1, m2, b2)
        if not success:
            return (0, 0), False
        return (x, y), True
    except ZeroDivisionError:
        return (0, 0), False


def slope(A, B):
    """
    Calculates the mathematical slope (gradient) between two points A and B.
    """
    try:
        x1, y1 = A
        x2, y2 = B
        return (y2 - y1) / (x2 - x1), True
    except ZeroDivisionError:
        return 0, False


# -----------------------------------------------------------------------------
# PLOTTING UTILITY FUNCTIONS
# -----------------------------------------------------------------------------

def plot_circle(cx, cy, r):
    """
    Plots a complete boundary circle given a center and radius.
    """
    angles = np.linspace(0, 2 * np.pi, 1500)
    x_coords = r * np.cos(angles) + cx
    y_coords = r * np.sin(angles) + cy
    plt.plot(x_coords, y_coords, color='darkblue', linewidth=1.5)


def plot_line(A, B, style='-', color='darkblue'):
    """
    Draws a straight line segment on the plot between point A and point B.
    """
    x1, y1 = A
    x2, y2 = B
    plt.plot([x1, x2], [y1, y2], linestyle=style, color=color, linewidth=1.2)


# -----------------------------------------------------------------------------
# MAIN GEOMETRIC CONSTRUCTION SCRIPT
# -----------------------------------------------------------------------------

circle_radius = 10

# Adjusted angles (in degrees) to match the visual layout of the diagram:
# A is upper-left (~155°), B is lower-left (~235°), 
# C is lower-right (~340°), D is top-center (~80°)
A = (circle_radius * cos(radians(155)), circle_radius * sin(radians(155)))
B = (circle_radius * cos(radians(235)), circle_radius * sin(radians(235)))
C = (circle_radius * cos(radians(340)), circle_radius * sin(radians(340)))
D = (circle_radius * cos(radians(80)),  circle_radius * sin(radians(80)))

# Find point P where interior diagonals AC and BD intersect
P, _ = line_intersection_from_points(A, C, B, D)

# Find point E on segment AB such that PE is perpendicular to AB
x1, y1 = A
x2, y2 = B
m1 = (y2 - y1) / (x2 - x1)
b1 = y1 - m1 * x1
m2 = -1 / m1
b2 = P[1] - m2 * P[0]
x, y, _ = intersection_of_lines(m1, b1, m2, b2)
E = (x, y)

# Find point F on segment CD such that PF is perpendicular to CD
x1, y1 = C
x2, y2 = D
m1 = (y2 - y1) / (x2 - x1)
b1 = y1 - m1 * x1
m2 = -1 / m1
b2 = P[1] - m2 * P[0]
x, y, _ = intersection_of_lines(m1, b1, m2, b2)
F = (x, y)

# Find secondary construction intersections Q and G
Q, _ = line_intersection_from_points(E, C, B, F)
G, _ = line_intersection_from_points(E, F, Q, P)

# -----------------------------------------------------------------------------
# RENDER VISUALIZATION
# -----------------------------------------------------------------------------

# Draw main circle
plot_circle(0, 0, circle_radius)

# Outer inscribed cyclic quadrilateral sides
plot_line(A, B)
plot_line(B, C)
plot_line(C, D)
plot_line(D, A)

# Main crossing diagonals (intersecting at P)
plot_line(C, A)
plot_line(D, B)

# Perpendicular projections from P to the sides
plot_line(P, E)
plot_line(P, F)

# Remaining construction lines matching the diagram layout
plot_line(E, C)
plot_line(E, F)
plot_line(B, F)
plot_line(G, Q)

# Labeling points for visual clarity matching the diagram
points_to_label = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E, 'F': F, 'P': P, 'Q': Q, 'G': G}
for label, pt in points_to_label.items():
    plt.plot(pt[0], pt[1], 'o', color='darkblue', markersize=4)
    plt.text(pt[0] * 1.08, pt[1] * 1.08, label, fontsize=12, weight='bold', ha='center')

# Calculate slopes of lines GQ and EF to verify orthogonality
slope_GQ, _ = slope(G, Q)
slope_EF, _ = slope(E, F)
product_of_slopes = slope_GQ * slope_EF

# Display the verified geometric relationship in the title
plt.title(f'The product of the slopes for lines GQ and EF is {product_of_slopes:.4f}')

plt.axis('equal')
plt.axis('off')
plt.show()
