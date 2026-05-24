"""
Jim McCleery
Today's date
Kailua-Kona, HI

https://mathnet.mit.edu/explorer.html?p=usa_2021_2fb58d
"""
# -----------------------------------------------------------------------------
# We import specific math functions we need (no need to import everything).
from math import pi, sqrt, acos, cos, sin
from matplotlib.pyplot import plot, title, axis, show, fill
from random import uniform
import numpy as np

# -----------------------------------------------------------------------------
def law_of_cosines(d1, d2, side):
    """
    Find the angle opposite a given side in a triangle using the Law of Cosines.

    Given a triangle with side lengths d1, d2, and 'side', this returns the
    angle (in radians) that is opposite the 'side' length.

    Returns:
        (angle_in_radians, True)  if the calculation succeeds
        (0, False)                if the inputs don't form a valid triangle
    """
    try:
        # The Law of Cosines: cos(angle) = (d1² + d2² - side²) / (2·d1·d2)
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except:
        # acos() fails if 'temp' is outside [-1, 1], meaning no valid triangle
        return 0, False


# -----------------------------------------------------------------------------
def quadratic_equation(A, B, C):
    """
    Solve the quadratic equation  A·x² + B·x + C = 0.

    Uses the quadratic formula:  x = (-B ± sqrt(B² - 4AC)) / (2A)

    Returns:
        (x1, x2, True)   with x1 ≤ x2 if two real solutions exist
        (0,  0,  False)  if no real solutions exist (negative discriminant)
    """
    try:
        discriminant = B**2 - 4 * A * C   # Must be ≥ 0 for real roots
        disc_root = sqrt(discriminant)
        x1 = (-B - disc_root) / (2 * A)
        x2 = (-B + disc_root) / (2 * A)
        if x1 > x2:
            x1, x2 = x2, x1               # Ensure x1 is the smaller root
        return x1, x2, True
    except:
        return 0, 0, False


# -----------------------------------------------------------------------------
def line_circle_intersection(x1, y1, r, m, b):
    """
    Find where a line crosses a circle.

    Circle: centered at (x1, y1) with radius r
    Line:   y = m·x + b  (slope m, y-intercept b)

    The method substitutes y = m·x + b into the circle equation
    (x - x1)² + (y - y1)² = r², then solves the resulting quadratic in x.

    Returns:
        (x2, y2, x3, y3, True)   coordinates of the two intersection points
        (0,  0,  0,  0,  False)  if the line doesn't intersect the circle
    """
    # Expand and collect terms to form  A·x² + B·x + C = 0
    A = 1 + m**2
    B = -2 * x1 + 2 * m * b - 2 * m * y1
    C = x1**2 + b**2 - 2 * b * y1 + y1**2 - r**2

    x2, x3, ok = quadratic_equation(A, B, C)
    if ok:
        y2 = m * x2 + b    # Compute y from the line equation
        y3 = m * x3 + b
        return x2, y2, x3, y3, ok
    else:
        return 0, 0, 0, 0, False


# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """
    Return the straight-line (Euclidean) distance between two points.

    Uses the Pythagorean theorem:  d = sqrt((Δx)² + (Δy)²)
    """
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Calculate the area of any polygon using the Shoelace Formula.

    'vertices' is a list of (x, y) corner points in order (either clockwise
    or counter-clockwise).  The formula sums cross-products of consecutive
    vertex pairs:  Area = |Σ (x_i · y_{i+1} - y_i · x_{i+1})| / 2
    """
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]   # Wrap around to the first vertex
        area += x1 * y2 - y1 * x2
    return abs(area) / 2


# -----------------------------------------------------------------------------
def point_in_polygon(x, y, polygon):
    """
    Determine whether the point (x, y) lies inside a polygon.

    Uses the ray-casting algorithm: draw an imaginary horizontal ray to the
    right of the point and count how many polygon edges it crosses.  An odd
    count means the point is inside; even means outside.
    """
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        # x-coordinate where the edge crosses the ray's height
                        x_intersect = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= x_intersect:
                            inside = not inside   # Toggle each time we cross
        p1x, p1y = p2x, p2y

    return inside


# -----------------------------------------------------------------------------
def plot_circle(x, y, radius, start=0, stop=2 * pi):
    """
    Draw a circle (or arc) on the current matplotlib figure.

    Args:
        x, y   : center of the circle
        radius : radius of the circle
        start  : starting angle in radians (default 0)
        stop   : ending angle in radians (default 2π = full circle)
    """
    angle = np.linspace(start, stop, 1500)   # 1500 points for a smooth curve
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    plot(x_arr, y_arr)


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Draw a straight line segment between two points on the current figure.
    """
    plot([x1, x2], [y1, y2])


# =============================================================================
# MAIN PROGRAM
# =============================================================================

# --- Triangle side lengths (given) -------------------------------------------
AB = 3 + sqrt(3)
BC = 3 * sqrt(2)
AC = 2 * sqrt(3)

# The semicircle sits on side AB, so its radius is half of AB.
radius = AB / 2

# --- Find the triangle's vertex C using the Law of Cosines -------------------
# We need the angle at A (between sides AB and AC) to locate point C in the plane.
theta, _ = law_of_cosines(AB,AC,BC)

# Place the triangle in the coordinate plane:
#   A = (x0, y0) at the origin
#   B = (x1, y1) along the positive x-axis
#   C = (x2, y2) computed from angle theta and side length AC
x0, y0 = 0, 0
x1, y1 = AB, 0
x2, y2 = AC * cos(theta), AC * sin(theta)

# The midpoint of AB is the center of the semicircle.
x3, y3 = AB / 2, 0

# --- Find where the two triangle sides (from A and B toward C) cut the
#     semicircle, giving us the shaded region's curved boundary. ---------------

# Slope and intercept of line AC (passes through origin, so b1 = 0)
m1 = (y2 - y0) / (x2 - x0)
b1 = 0

# Slope and intercept of line BC
m2 = (y2 - y1) / (x2 - x1)
b2 = y1 - m2 * x1

# Intersection of line AC with the semicircle — we want the far intersection
_, _, x4, y4, _ = line_circle_intersection(x3, y3, radius, m1, b1)

# Intersection of line BC with the semicircle — we want the near intersection
x5, y5, _, _, _ = line_circle_intersection(x3, y3, radius, m2, b2)

# --- Compute the exact shaded area --------------------------------------------
# The shaded region is a quadrilateral (with one curved side) made up of:
#   • A quadrilateral: midpoint M → point on AC → vertex C → point on BC
#   • Minus a circular sector between the two intersection points

# Side lengths of the triangle formed by the two radii and the chord x4y4–x5y5
d1 = distance(x3, y3, x4, y4)
d2 = distance(x3, y3, x5, y5)
d3 = distance(x5, y5, x4, y4)

# Central angle of the sector (angle at the circle's center between the two radii)
alpha, _ = law_of_cosines(d1, d2, d3)

# Area of the circular sector:  (1/2) · r² · θ
sector_area = radius**2 * alpha / 2

# The four corners of the quadrilateral (in order)
vertices = [(x3, y3), (x4, y4), (x2, y2), (x5, y5)]

# Polygon area via the Shoelace Formula, then subtract the sector
quad_area = polygon_area(vertices)
area = quad_area - sector_area

# --- Draw the triangle and key construction lines ----------------------------
plot_line(x0, y0, x1, y1)    # Side AB (base)
plot_line(x2, y2, x1, y1)    # Side BC
plot_line(x0, y0, x2, y2)    # Side AC
plot_line(x3, y3, x4, y4)    # Radius to intersection on AC
plot_line(x3, y3, x5, y5)    # Radius to intersection on BC
plot_circle(x3, y3, radius, 0, pi)   # Upper semicircle on AB

# --- Monte Carlo Shading -----------------------------------------------------
# We randomly scatter points in a bounding box and check how many land in the
# shaded region (inside the quadrilateral but outside the circle).
# The fraction that land there, times the box area, estimates the shaded area.
throws = 10**6    # More throws → more accurate estimate
for _ in range(throws):
    x = uniform(0, AB)
    y = uniform(0, AB)
    # A point is in the shaded region if it's inside the quadrilateral AND
    # outside the circle (circle equation: (x - radius)² + y² > radius²)
    if point_in_polygon(x, y, vertices) and (x - radius)**2 + y**2 > radius**2:
        plot(x, y, '.', markersize=1, color='steelblue', alpha=0.3)

# --- Display the result -------------------------------------------------------
title(f'Shaded Area = {area:.9f}')
axis('equal')
show()
