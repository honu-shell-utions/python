# Jim McCleery
# September 19, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2007_d2921c
#
# -----------------------------------------------------------------------------
# Geometry construction for the 2007 USA Mathematical Talent Search problem.
#
# The diagram contains the points:
# A, B, C, D, M, P, and Q
#
# The final calculation is QM * MP.
# -----------------------------------------------------------------------------


from math import radians, sqrt, sin, cos, tan
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def distance(point1, point2):
    """
    Return the straight-line distance between two points.

    Each point is written as an (x, y) pair.

    Example:
        distance((0, 0), (3, 4)) returns 5
    """
    x1, y1 = point1
    x2, y2 = point2

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# -----------------------------------------------------------------------------
def circle_through_points(point1, point2, point3):
    """
    Find the circle passing through three non-collinear points.

    Returns:
        center, radius

    where center is an (x, y) pair.
    """
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    # These expressions come from solving the equations for a circle
    # passing through all three points.
    s1 = x1**2 + y1**2
    s2 = x2**2 + y2**2
    s3 = x3**2 + y3**2

    determinant = (
        x1 * y2
        + x2 * y3
        + x3 * y1
        - x2 * y1
        - x3 * y2
        - x1 * y3
    )

    if abs(determinant) < 1e-12:
        raise ValueError("The three points are collinear.")

    numerator_x = (
        s1 * y2
        + s2 * y3
        + s3 * y1
        - s2 * y1
        - s3 * y2
        - s1 * y3
    )

    numerator_y = (
        s1 * x2
        + s2 * x3
        + s3 * x1
        - s2 * x1
        - s3 * x2
        - s1 * x3
    )

    center_x = 0.5 * numerator_x / determinant
    center_y = -0.5 * numerator_y / determinant

    center = (center_x, center_y)
    radius = distance(center, point1)

    return center, radius


# -----------------------------------------------------------------------------
def quadratic_roots(a, b, c):
    """
    Solve the quadratic equation:

        a*x^2 + b*x + c = 0

    Returns the two real roots in increasing order.
    """
    discriminant = b**2 - 4 * a * c

    if discriminant < 0:
        raise ValueError("The quadratic equation has no real roots.")

    root = sqrt(discriminant)

    x1 = (-b - root) / (2 * a)
    x2 = (-b + root) / (2 * a)

    return min(x1, x2), max(x1, x2)


# -----------------------------------------------------------------------------
def line_circle_intersections(center, radius, slope, intercept):
    """
    Find the two intersection points between a circle and a line.

    Circle:
        center = (center_x, center_y)
        radius = radius

    Line:
        y = slope*x + intercept

    Returns:
        point1, point2
    """
    center_x, center_y = center

    # Substitute y = slope*x + intercept into the circle equation.
    # The result is a quadratic equation in x.
    a = 1 + slope**2

    b = (
        -2 * center_x
        + 2 * slope * intercept
        - 2 * slope * center_y
    )

    c = (
        center_x**2
        + intercept**2
        - 2 * intercept * center_y
        + center_y**2
        - radius**2
    )

    x1, x2 = quadratic_roots(a, b, c)

    y1 = slope * x1 + intercept
    y2 = slope * x2 + intercept

    return (x1, y1), (x2, y2)


# -----------------------------------------------------------------------------
def line_intersection(slope1, intercept1, slope2, intercept2):
    """
    Find the intersection of two lines.

    The lines are:

        y = slope1*x + intercept1
        y = slope2*x + intercept2
    """
    if abs(slope1 - slope2) < 1e-12:
        raise ValueError("The two lines are parallel.")

    x = (intercept2 - intercept1) / (slope1 - slope2)
    y = slope1 * x + intercept1

    return x, y


# -----------------------------------------------------------------------------
def plot_line(point1, point2):
    """
    Draw a line segment joining two points.
    """
    x1, y1 = point1
    x2, y2 = point2

    plt.plot([x1, x2], [y1, y2], color="black", linewidth=1)


# -----------------------------------------------------------------------------
def plot_circle(center, radius):
    """
    Draw a complete circle.
    """
    center_x, center_y = center

    angles = np.linspace(0, 2 * np.pi, 500)

    x = center_x + radius * np.cos(angles)
    y = center_y + radius * np.sin(angles)

    plt.plot(x, y, color="black", linewidth=1)


# -----------------------------------------------------------------------------
def label_point(name, point, dx=0.25, dy=0.25):
    """
    Plot a black dot and place its name nearby.

    dx and dy control how far the label is moved from the point.
    """
    x, y = point

    plt.plot(x, y, "ko", markersize=5)
    plt.text(x + dx, y + dy, name, fontsize=12)


# =============================================================================
# Construct the geometry
# =============================================================================

# D is placed at the origin.
D = (0, 0)


# DM is the horizontal distance from D to M.
DM = 6 / tan(radians(10))


# AD and DC are equal.
AD = 6 / sin(radians(10))
DC = AD


# AB comes from the triangle containing the 80-degree angle.
AB = 6 / sin(radians(80))


# MB is found using the Pythagorean theorem.
MB = sqrt(AB**2 - 6**2)


# A is 10 degrees above the horizontal ray from D.
A = (
    AD * cos(radians(10)),
    AD * sin(radians(10))
)


# C is 10 degrees below the horizontal ray from D.
C = (
    DC * cos(radians(-10)),
    DC * sin(radians(-10))
)


# M lies on the horizontal line through D.
M = (DM, 0)


# B is a short distance to the right of M.
B = (DM + MB, 0)


# -----------------------------------------------------------------------------
# Find the circle through A, M, and B.
# -----------------------------------------------------------------------------

circle_center, circle_radius = circle_through_points(A, M, B)


# -----------------------------------------------------------------------------
# Construct line MP.
#
# It passes through M and makes a 40-degree angle with the x-axis.
#
# The equation of a line is:
#
#     y = m*x + b
#
# where m is the slope and b is the y-intercept.
# -----------------------------------------------------------------------------

slope_MP = tan(radians(40))
intercept_MP = M[1] - slope_MP * M[0]


# Find the two places where line MP intersects the circle.
intersection1, intersection2 = line_circle_intersections(
    circle_center,
    circle_radius,
    slope_MP,
    intercept_MP
)


# One intersection is M.  The other is P.
if distance(intersection1, M) > distance(intersection2, M):
    P = intersection1
else:
    P = intersection2


# -----------------------------------------------------------------------------
# Construct line DC.
#
# It makes an angle of -10 degrees with the x-axis and passes through D.
# Since D = (0, 0), its y-intercept is zero.
# -----------------------------------------------------------------------------

slope_DC = tan(radians(-10))
intercept_DC = 0


# Q is where line MP meets line DC.
Q = line_intersection(
    slope_MP,
    intercept_MP,
    slope_DC,
    intercept_DC
)


# =============================================================================
# Draw the diagram
# =============================================================================

plt.figure(figsize=(12, 5))


# Draw the circle through A, M, and B.
plot_circle(circle_center, circle_radius)


# Draw the major line segments in the construction.
plot_line(D, A)
plot_line(D, C)
plot_line(D, B)

plot_line(A, C)
plot_line(A, B)
plot_line(B, C)

plot_line(Q, P)


# -----------------------------------------------------------------------------
# Add named coordinate labels to match the supplied diagram.
#
# The small dx and dy values move each letter so that it does not sit
# directly on top of its point.
# -----------------------------------------------------------------------------

label_point("D", D, dx=-1.0, dy=0.4)

label_point("A", A, dx=-0.4, dy=0.6)
label_point("P", P, dx=0.3, dy=0.3)

label_point("M", M, dx=-0.8, dy=0.5)
label_point("B", B, dx=0.3, dy=-0.5)

label_point("Q", Q, dx=-0.8, dy=-0.7)
label_point("C", C, dx=0.3, dy=-0.7)


# =============================================================================
# Calculate QM * MP
# =============================================================================

QM = distance(Q, M)
MP = distance(M, P)

product = QM * MP


# Put the result above the graph.
plt.title(f"QM × MP = {product:.1f}")


# Use the same scale horizontally and vertically so that the geometry
# is not visually distorted.
plt.axis("equal")


# Remove the ordinary x- and y-axes for a cleaner geometry diagram.
plt.axis("off")


# Add a little extra space around the drawing.
plt.margins(0.08)


# Display the finished figure.
plt.show()
