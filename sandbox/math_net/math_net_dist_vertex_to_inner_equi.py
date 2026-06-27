# Jim McCleery
# June 26, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2025_2e4826

from math import pi, sin, cos, sqrt
from matplotlib.pyplot import plot, title, axis, show, text


# -----------------------------------------------------------------------------
# FUNCTIONS
# -----------------------------------------------------------------------------

def distance(x1, y1, x2, y2):
    """Calculate the straight-line distance between two coordinate points."""
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def plot_line(x1, y1, x2, y2):
    """Draw a straight line segment between two points."""
    plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# MAIN GEOMETRY SCRIPT
# -----------------------------------------------------------------------------

# Total base length BC = BE + EF + FC = 14 + 15 + 16 = 45
side = 45

# --- Define Coordinates for Triangle ABC ---
# Vertex B is at the origin (0,0), and the base BC sits on the x-axis.
xB, yB = 0, 0                                 # Point B
xC, yC = side, 0                              # Point C
xA, yA = 45 * cos(pi / 3), 45 * sin(pi / 3)   # Point A (top vertex of ΔABC)

# --- Geometric Transformation (60-degree Rotation around C) ---
# To find AD, this specific script models a 60-degree rotation of triangle ADC 
# around point C. Under this rotation, point A lands on B, and point D moves 
# to a new position, D_prime (D'). Thus, distance AD equals distance BD'.
x_prop1, y_prop1 = xC + 14 * cos(2 * pi / 3), 14 * sin(2 * pi / 3)
x_prop2, y_prop2 = xC + 29 * cos(2 * pi / 3), 29 * sin(2 * pi / 3)

# Coordinates for D' (the transformed position of point D)
xD_prime, yD_prime = x_prop1 - 15, y_prop1


# --- Plotting the Diagram ---
# Draw the main outer equilateral triangle ABC
plot_line(xB, yB, xC, yC)   # Base BC
plot_line(xA, yA, xC, yC)   # Side AC
plot_line(xB, yB, xA, yA)   # Side AB

# Draw the transformed triangle network that solves the problem
plot_line(x_prop1, y_prop1, xD_prime, yD_prime)
plot_line(x_prop2, y_prop2, xD_prime, yD_prime)
plot_line(xB, yB, xD_prime, yD_prime)   # Line segment BD'


# --- Adding Text Labels to the Diagram ---
# text(x, y, 'Label', fontsize, vertical/horizontal alignment)
# Slight offsets are added so the text doesn't sit directly on top of the lines.
text(xA, yA + 1, 'C', fontsize=12, ha='center', va='bottom')
text(xB - 1, yB - 1, 'A', fontsize=12, ha='right', va='top')
text(xC + 1, yC - 1, 'B', fontsize=12, ha='left', va='top')
text(xD_prime - 1, yD_prime + 1, "D", fontsize=12, ha='right', va='bottom')


# --- Calculate and Display Result ---
# Since distance(A, D) == distance(B, D_prime):
ad_distance = distance(xB, yB, xD_prime, yD_prime)

title(f'The distance AD is {ad_distance:0.3f}')
axis('equal')  # Keeps geometry square and undistorted
axis('off')    # Hides background grid lines
show()
