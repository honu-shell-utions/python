# -----------------------------------------------------------------------------
# Jim McCleery
# 2026-07-04
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2022_849b97
# -----------------------------------------------------------------------------

# Import only the specific functions needed from the math library
from math import sqrt, tan, pi, acos

# Import matplotlib functions for plotting graphs and geometry
from matplotlib.pyplot import text, axis, title, show, plot


# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """
    Calculate and return the straight-line (Euclidean) distance between 
    two points: (x1, y1) and (x2, y2).
    """
    # Uses the Pythagorean theorem: distance = sqrt((x2-x1)^2 + (y2-y1)^2)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# -----------------------------------------------------------------------------
def law_of_cosines(d1, d2, side):
    """
    Calculate the angle opposite to 'side' in a triangle where the other 
    two sides are 'd1' and 'd2' using the Law of Cosines.
    
    Returns:
        (angle_in_radians, True) if successful, or (0, False) if it fails.
    """
    try:
        # Rearranged Law of Cosines formula: cos(C) = (a^2 + b^2 - c^2) / (2ab)
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except ValueError:
        # If the math is impossible (e.g., sides can't form a triangle)
        return 0, False


# -----------------------------------------------------------------------------
def intersection_of_lines(m1, b1, m2, b2):
    """
    Find the intersection point of two lines given in slope-intercept form (y = mx + b).
    
    Returns:
        (x, y, True) if they intersect, or (0, 0, False) if they are parallel.
    """
    # If the slopes are identical, the lines are parallel and never cross
    if m1 == m2:
        return 0, 0, False
        
    # Solve for x by setting the two line equations equal: m1*x + b1 = m2*x + b2
    x = (b2 - b1) / (m1 - m2)
    # Substitute x back into one of the line equations to find y
    y = m1 * x + b1
    return x, y, True


# -----------------------------------------------------------------------------
def plot_line(point_a, point_b):
    """
    Helper function to draw a line segment between point_a and point_b using matplotlib.
    Each point should be a tuple or list containing coordinates: (x, y).
    """
    x1, y1 = point_a
    x2, y2 = point_b
    # matplotlib.pyplot.plot takes a list of X-coordinates and a list of Y-coordinates
    plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# MAIN GEOMETRY AND CALCULATION STEP
# -----------------------------------------------------------------------------

# Calculate the vertical height (h) of the trapezoid using the Pythagorean theorem
# The slanted sides are 333, and the horizontal offset is 75
h = sqrt(333**2 - 75**2)

# Define the coordinates for the four vertices of the trapezoid ABCD
A = (0, 0)
B = (500, 0)
C = (575, -h)
D = (-75, -h)

# Find the lengths of the diagonals AC and BD by unpacking coordinates using the '*' operator
diag01 = distance(*A, *C)
diag02 = distance(*B, *D)

# Compute internal angles of the trapezoid using the Law of Cosines
# Angle A is opposite to diagonal BD (diag02) in triangle ABD
angleA, _ = law_of_cosines(333, 500, diag02)
angleB = angleA  # By symmetry, Angle B equals Angle A

# Angle C is opposite to diagonal AC (diag01) in triangle ABC
angleC, _ = law_of_cosines(333, 650, diag01)
angleD = angleC  # By symmetry, Angle D equals Angle C

# --- Find Point P (Intersection of angle bisectors from A and D) ---
# Line 1: Bisector of Angle A. Slopes downwards, so it is negative.
m1 = -tan(angleA / 2)
b1 = 0  # Starts at the origin (0, 0)

# Line 2: Bisector of Angle D. Slopes upwards.
m2 = tan(angleD / 2)
# Calculate intercept b2 using point D(-75, -h) on the line: b = y - m*x
b2 = m2 * 75 - h

# Compute the coordinates of point P
x, y, _ = intersection_of_lines(m1, b1, m2, b2)
P = (x, y)

# --- Find Point Q (Intersection of angle bisectors from B and C) ---
# Line 1: Bisector of Angle B.
m1 = tan(pi + angleB / 2)
b1 = -m1 * 500  # Shifted based on point B(500, 0)

# Line 2: Bisector of Angle C.
m2 = tan(pi - angleC / 2)
b2 = -h - m2 * 575  # Shifted based on point C(575, -h)

# Compute the coordinates of point Q
x, y, _ = intersection_of_lines(m1, b1, m2, b2)
Q = (x, y)


# -----------------------------------------------------------------------------
# VISUALIZATION STEP
# -----------------------------------------------------------------------------

# Add letter labels onto the plot at each point's coordinates
text(*A, 'A')
text(*B, 'B')
text(*C, 'C')
text(*D, 'D')
text(*P, 'P')
text(*Q, 'Q')

# Draw the perimeter of the trapezoid ABCD
plot_line(A, B)
plot_line(B, C)
plot_line(C, D)
plot_line(A, D)

# Draw the angle bisector segments connecting to P and Q
plot_line(A, P)
plot_line(P, D)
plot_line(B, Q)
plot_line(C, Q)

# Calculate the final distance between point P and point Q
d = distance(*P, *Q)

# Configure the plot window properties
axis('equal')  # Ensures 1 unit horizontally matches 1 unit vertically (no stretching)
axis('off')    # Hides the grid lines and coordinate axis borders
title(f'Distance from P to Q is {d:0.3f}')  # Displays the final answer up top

# Display the window containing the drawn diagram
show()
