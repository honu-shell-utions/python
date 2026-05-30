# -----------------------------------------------------------------------------
# Jim McCleery
# May 29, 2026
# Kailua-Kona, HI
# 
# Geometry problem explorer:
# https://mathnet.mit.edu/explorer.html?p=usa_2025_2f42c8
# -----------------------------------------------------------------------------

# Import math tools for geometry calculations
from math import pi, radians, sqrt, sin, cos, tan, acos, degrees
# Import matplotlib for drawing and plotting figures
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """
    Calculate and return the straight-line distance between two points:
    Point 1 (x1, y1) and Point 2 (x2, y2).
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# -----------------------------------------------------------------------------
def law_of_cosines(d1, d2, side):
    """
    Find the angle opposite to 'side' in a triangle where the other 
    two known side lengths are d1 and d2.
    
    Returns:
        (angle_in_radians, True) if a valid triangle exists.
        (0, False) if the math fails (e.g., impossible side lengths).
    """
    try:
        # Rearranged Law of Cosines formula: cos(C) = (a^2 + b^2 - c^2) / (2ab)
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except ValueError:
        return 0, False

# -----------------------------------------------------------------------------
def define_circle_from_points(x1, y1, x2, y2, x3, y3):
    """
    Find and return the center (cx, cy) and radius of a unique circle
    that passes exactly through three separate points.
    """
    temp = x2 * x2 + y2 * y2
    bc = (x1 * x1 + y1 * y1 - temp) / 2
    cd = (temp - x3 * x3 - y3 * y3) / 2
    det = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    cx = (bc * (y2 - y3) - cd * (y1 - y2)) / det
    cy = ((x1 - x2) * cd - (x2 - x3) * bc) / det
    radius = sqrt((cx - x1) ** 2 + (cy - y1) ** 2)
    
    return cx, cy, radius

# -----------------------------------------------------------------------------
def quadratic_equation(A, B, C):
    """
    Solve a standard quadratic equation: A*x^2 + B*x + C = 0.
    
    Returns:
        (x1, x2, True) where x1 <= x2 if real roots exist.
        (0, 0, False) if there are no real roots.
    """
    try:
        disc = B**2 - 4 * A * C  # Calculate the discriminant
        disc = sqrt(disc)
        x1 = (-B - disc) / (2 * A)
        x2 = (-B + disc) / (2 * A)
        
        # Ensure x1 is always the smaller or equal root
        if x1 > x2:
            x1, x2 = x2, x1
        return x1, x2, True
    except ValueError:
        return 0, 0, False

# -----------------------------------------------------------------------------
def line_circle_intersection(x1, y1, r, m, b):
    """
    Find where a circle and a line intersect.
    Circle center is (x1, y1) with radius r.
    Line equation is in slope-intercept form: y = m*x + b.
    
    Returns:
        (x2, y2, x3, y3, True) if intersections are found.
        (0, 0, 0, 0, False) otherwise.
    """
    # Substitute y = mx + b into the circle equation to get quadratic coefficients
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

# -----------------------------------------------------------------------------
def plot_circle(x, y, radius, start=0, stop=2*pi):
    """
    Draw a circular arc from a 'start' angle to a 'stop' angle (in radians)
    centered around (x, y).
    """
    import numpy as np  # Imported locally just for rendering coordinates
    angle = np.linspace(start, stop, 1500)
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    plt.plot(x_arr, y_arr)

# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Draw a straight line segment from (x1, y1) to (x2, y2) on the plot.
    """
    plt.plot([x1, x2], [y1, y2])

# -----------------------------------------------------------------------------
def find_angle(x1, y1, x2, y2, radius):
    """
    Find the angle of a circular arc (in degrees) spanned by two points 
    (x1, y1) and (x2, y2) on a circle of a given radius.
    """
    d = distance(x1, y1, x2, y2)
    theta, _ = law_of_cosines(radius, radius, d)
    theta = degrees(theta)
    return theta

# =============================================================================
# MAIN GEOMETRY SETUP AND CALCULATIONS
# =============================================================================

# Define the three angles of the primary triangle in radians
alpha = radians(84)
beta = radians(60)
gamma = radians(36)

# Set base length BC to 1, then use Law of Sines to find sides AB and AC
BC = 1
AB = BC * sin(gamma) / sin(alpha)
# Note: original code defined AC, though it isn't directly used for calculations
AC = BC * sin(beta) / sin(alpha)

# Define coordinate points for the vertices of the main triangle
x0, y0 = 0, 0                          # Vertex B
x1, y1 = BC, 0                         # Vertex C
x2, y2 = AB * cos(beta), AB * sin(beta) # Vertex A

# Draw the main outer triangle sides
plot_line(x0, y0, x1, y1)
plot_line(x2, y2, x1, y1)
plot_line(x0, y0, x2, y2)

# Calculate the midpoints of the three outer sides
ABx_mid, ABy_mid = (x0 + x2) / 2, (y0 + y2) / 2
ACx_mid, ACy_mid = (x1 + x2) / 2, (y1 + y2) / 2
BCx_mid, BCy_mid = BC / 2, 0

# Plot standard dots ('o') at each of the midpoints
plt.plot(ABx_mid, ABy_mid, 'o')
plt.plot(ACx_mid, ACy_mid, 'o')
plt.plot(BCx_mid, BCy_mid, 'o')

# Connect the midpoints to form an inner triangle
plot_line(ABx_mid, ABy_mid, ACx_mid, ACy_mid)
plot_line(ACx_mid, ACy_mid, BCx_mid, BCy_mid)
plot_line(ABx_mid, ABy_mid, BCx_mid, BCy_mid)

# Find the 9-point circle passing through these three triangle midpoints
x3, y3, r = define_circle_from_points(ABx_mid, ABy_mid, ACx_mid, ACy_mid, BCx_mid, BCy_mid)
plot_circle(x3, y3, r)

# --- Line Intersections with the Circle ---

# 1. Intersection with the line AB (slope = tan(beta), intercept = 0)
m = tan(beta)
b = 0
_, _, x4, y4, _ = line_circle_intersection(x3, y3, r, m, b)
plt.plot(x4, y4, 'o')

# 2. Intersection with line AC (slope = tan(pi - gamma))
m = tan(pi - gamma)
b = y1 - m * x1
x5, y5, _, _, _ = line_circle_intersection(x3, y3, r, m, b)
plt.plot(x5, y5, 'o')

# 3. Intersection with flat base line BC (slope = 0, intercept = 0)
m = 0
b = 0
x6, y6, _, _, _ = line_circle_intersection(x3, y3, r, m, b)
plt.plot(x6, y6, 'o')

# --- Final Arc Angle Computations ---
theta = 0
# Add angle contribution of Arc DE
theta += find_angle(ACx_mid, ACy_mid, BCx_mid, BCy_mid, r)
# Add 2 times angle contribution of Arc HJ
theta += 2 * find_angle(x5, y5, x4, y4, r)
# Add 3 times angle contribution of Arc FG
theta += 3 * find_angle(ABx_mid, ABy_mid, x6, y6, r)

# --- Add Appropriate Coordinate Labels to the Graphic ---

# Slight offsets to keep text clear of the points
plt.text(x0 - 0.03, y0 - 0.03, 'B', fontsize=12, fontweight='bold', ha='right')
plt.text(x1 + 0.03, y1 - 0.03, 'C', fontsize=12, fontweight='bold', ha='left')
plt.text(x2, y2 + 0.03, 'A', fontsize=12, fontweight='bold', va='bottom', ha='center')

# Midpoints
plt.text(ABx_mid - 0.03, ABy_mid, 'F', fontsize=12, fontweight='bold', ha='right', va='center')
plt.text(ACx_mid + 0.03, ACy_mid, 'E', fontsize=12, fontweight='bold', ha='left', va='center')
plt.text(BCx_mid, BCy_mid + 0.03, 'D', fontsize=12, fontweight='bold', va='bottom', ha='center')

# Secondary intersections (Altitude feet)
plt.text(x4 + 0.02, y4 - 0.03, 'J', fontsize=12, fontweight='bold', ha='left', va='top')
plt.text(x5 - 0.02, y5 - 0.03, 'H', fontsize=12, fontweight='bold', ha='right', va='top')
plt.text(x6 - 0.02, y6 + 0.03, 'G', fontsize=12, fontweight='bold', ha='right', va='bottom')

# --- Render and Display the Visual Diagram ---
plt.title(f'Arc DE + 2*Arc HJ + 3*Arc FG = {theta:0.0f} degrees.')
plt.axis('equal')  
plt.show()
# --- Render and Display the Visual Diagram ---
plt.title(f'Arc DE + 2*Arc HJ + 3*Arc FG = {theta:0.0f} degrees.')
plt.axis('equal')  # Ensures circles look round and not like ellipses
plt.show()
