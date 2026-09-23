# Jim McCleery
# September 23, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2018_6840f9
#
# -----------------------------------------------------------------------------
# Geometry Problem
#
# Triangle ABC has side lengths:
#
#       AB = 5
#       BC = 8
#       CA = 7
#
# X is the second intersection of the external angle bisector of angle B
# with the circumcircle of triangle ABC.
#
# Y is the foot of the perpendicular from X to BC.
#
# Find YC.
# -----------------------------------------------------------------------------


from math import sqrt, acos, sin, cos, pi, tan
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def distance(A, B):
    """
    Return the distance between two points.

    Each point is represented by a tuple:

        (x, y)
    """

    x1, y1 = A
    x2, y2 = B

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


# -----------------------------------------------------------------------------
def law_of_cosines(a, b, c):
    """
    Find the angle between sides a and b when the opposite side is c.

    The Law of Cosines says:

        c^2 = a^2 + b^2 - 2ab cos(theta)

    Solving for theta gives:

        theta = arccos((a^2 + b^2 - c^2) / (2ab))

    The returned angle is in radians.
    """

    cosine_value = (a**2 + b**2 - c**2) / (2 * a * b)

    return acos(cosine_value)


# -----------------------------------------------------------------------------
def circle_through_points(A, B, C):
    """
    Find the center and radius of the circle through A, B, and C.

    Returns:

        center, radius
    """

    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    # This determinant is nonzero when the three points
    # are not on the same straight line.
    denominator = 2 * (
        x1 * (y2 - y3)
        + x2 * (y3 - y1)
        + x3 * (y1 - y2)
    )

    center_x = (
        (x1**2 + y1**2) * (y2 - y3)
        + (x2**2 + y2**2) * (y3 - y1)
        + (x3**2 + y3**2) * (y1 - y2)
    ) / denominator

    center_y = (
        (x1**2 + y1**2) * (x3 - x2)
        + (x2**2 + y2**2) * (x1 - x3)
        + (x3**2 + y3**2) * (x2 - x1)
    ) / denominator

    center = (center_x, center_y)

    radius = distance(center, A)

    return center, radius


# -----------------------------------------------------------------------------
def line_circle_intersections(center, radius, m, b):
    """
    Find the two intersections of a circle and the line

        y = m*x + b

    Returns the two intersection points.
    """

    center_x, center_y = center

    # Substitute y = m*x + b into the circle equation:
    #
    #     (x - center_x)^2 + (y - center_y)^2 = radius^2
    #
    # The result is a quadratic equation in x.

    A = 1 + m**2

    B = (
        -2 * center_x
        + 2 * m * (b - center_y)
    )

    C = (
        center_x**2
        + (b - center_y)**2
        - radius**2
    )

    discriminant = B**2 - 4 * A * C

    x1 = (-B - sqrt(discriminant)) / (2 * A)
    x2 = (-B + sqrt(discriminant)) / (2 * A)

    y1 = m * x1 + b
    y2 = m * x2 + b

    return (x1, y1), (x2, y2)


# -----------------------------------------------------------------------------
def perpendicular_foot(P, A, B):
    """
    Find the foot of the perpendicular from point P to line AB.

    The result is the projection of P onto the line through A and B.
    """

    # Direction vector from A to B.
    AB = np.array(B) - np.array(A)

    # Vector from A to P.
    AP = np.array(P) - np.array(A)

    # t tells us how far along line AB the projection lies.
    t = np.dot(AP, AB) / np.dot(AB, AB)

    # A + t(AB) gives the projected point.
    foot = np.array(A) + t * AB

    return tuple(foot)


# -----------------------------------------------------------------------------
def plot_circle(center, radius):
    """
    Plot a complete circle.
    """

    center_x, center_y = center

    angles = np.linspace(0, 2 * pi, 1000)

    x_values = center_x + radius * np.cos(angles)
    y_values = center_y + radius * np.sin(angles)

    plt.plot(x_values, y_values)


# -----------------------------------------------------------------------------
def plot_line(A, B):
    """
    Plot a line segment from A to B.
    """

    plt.plot(
        [A[0], B[0]],
        [A[1], B[1]]
    )


# -----------------------------------------------------------------------------
def label_point(name, P, dx=0.12, dy=0.12):
    """
    Plot a point and label it with its name and coordinates.

    dx and dy move the text slightly away from the point so that
    the label does not cover the point itself.
    """

    x, y = P

    plt.plot(x, y, "o")

    plt.text(
        x + dx,
        y + dy,
        f"{name} ({x:.2f}, {y:.2f})",
        fontsize=10
    )


# -----------------------------------------------------------------------------
# STEP 1
# Choose convenient coordinates for A and B.
#
# Put A at the origin and put AB along the x-axis.
#
# Since AB = 5:
#
#       A = (0, 0)
#       B = (5, 0)
# -----------------------------------------------------------------------------

A = (0, 0)
B = (5, 0)


# -----------------------------------------------------------------------------
# STEP 2
# Find point C.
#
# We know:
#
#       AB = 5
#       AC = 7
#       BC = 8
#
# alpha is angle BAC.
# -----------------------------------------------------------------------------

alpha = law_of_cosines(5, 7, 8)

C = (
    7 * cos(alpha),
    7 * sin(alpha)
)


# -----------------------------------------------------------------------------
# STEP 3
# Find the circumcircle of triangle ABC.
# -----------------------------------------------------------------------------

circle_center, radius = circle_through_points(A, B, C)


# -----------------------------------------------------------------------------
# STEP 4
# Find the external angle bisector at B.
#
# beta is the interior angle ABC.
# -----------------------------------------------------------------------------

beta = law_of_cosines(5, 8, 7)

# The external angle and the interior angle add to 180 degrees.
# Half of the external angle is therefore:
gamma = (pi - beta) / 2

# The external angle bisector has slope tan(gamma).
m = tan(gamma)

# Since it passes through B = (5, 0),
#
#       y = m*x + b
#
# so:
#
#       b = y - m*x
#
b = B[1] - m * B[0]


# -----------------------------------------------------------------------------
# STEP 5
# Find where the external angle bisector meets the circumcircle.
#
# One intersection is B itself.
# The other intersection is X.
# -----------------------------------------------------------------------------

P1, P2 = line_circle_intersections(
    circle_center,
    radius,
    m,
    b
)

# Choose whichever intersection is NOT B.
if distance(P1, B) > distance(P2, B):
    X = P1
else:
    X = P2


# -----------------------------------------------------------------------------
# STEP 6
# Drop a perpendicular from X to line BC.
#
# Its foot is Y.
# -----------------------------------------------------------------------------

Y = perpendicular_foot(X, B, C)


# -----------------------------------------------------------------------------
# STEP 7
# Calculate the required distance YC.
# -----------------------------------------------------------------------------

YC = distance(Y, C)


# -----------------------------------------------------------------------------
# Display numerical coordinates in the Python console.
# -----------------------------------------------------------------------------

print(f"A = ({A[0]:.5f}, {A[1]:.5f})")
print(f"B = ({B[0]:.5f}, {B[1]:.5f})")
print(f"C = ({C[0]:.5f}, {C[1]:.5f})")
print(f"X = ({X[0]:.5f}, {X[1]:.5f})")
print(f"Y = ({Y[0]:.5f}, {Y[1]:.5f})")

print()
print(f"YC = {YC:.5f}")


# -----------------------------------------------------------------------------
# STEP 8
# Draw the geometry.
# -----------------------------------------------------------------------------

plt.figure(figsize=(9, 8))

# Circumcircle
plot_circle(circle_center, radius)

# Triangle ABC
plot_line(A, B)
plot_line(B, C)
plot_line(C, A)

# External angle bisector segment BX
plot_line(B, X)

# Perpendicular XY
plot_line(X, Y)


# -----------------------------------------------------------------------------
# Add labels and coordinates to the important points.
# -----------------------------------------------------------------------------

label_point("A", A, -1.25, -0.35)
label_point("B", B, 0.12, -0.40)
label_point("C", C, -1.70, 0.15)
label_point("X", X, 0.15, 0.15)
label_point("Y", Y, 0.15, 0.15)


# -----------------------------------------------------------------------------
# Finish the graph.
# -----------------------------------------------------------------------------

plt.title(f"YC = {YC:.5f}")

# Equal scaling is important in geometry.
# Without it, circles can appear as ellipses and angles can look distorted.
plt.axis("equal")

# Add a light coordinate grid because we are displaying coordinates.
plt.grid(alpha=0.3)

plt.xlabel("x")
plt.ylabel("y")

plt.show()
