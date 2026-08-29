"""
Jim McCleery
August 28, 2026
Kailua-Kona, HI

USA Mathematical Talent Search
https://mathnet.mit.edu/explorer.html?p=usa_2021_706bb1

Monte-Carlo solution
"""

# -----------------------------------------------------------------------------
# Import the tools needed for this problem.
# -----------------------------------------------------------------------------

from math import pi, sin, cos, sqrt
from random import uniform

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
def quadratic_equation(a, b, c):
    """
    Solve the quadratic equation

        a*x^2 + b*x + c = 0

    Return the two real roots and True if real roots exist.
    Otherwise return 0, 0, False.
    """

    discriminant = b**2 - 4 * a * c

    # A negative discriminant means there are no real solutions.
    if discriminant < 0:
        return 0, 0, False

    root = sqrt(discriminant)

    x1 = (-b - root) / (2 * a)
    x2 = (-b + root) / (2 * a)

    # Put the smaller x-coordinate first.
    if x1 > x2:
        x1, x2 = x2, x1

    return x1, x2, True


# -----------------------------------------------------------------------------
def line_circle_intersection(cx, cy, radius, slope, intercept):
    """
    Find the intersections of a circle and a line.

    Circle:
        center = (cx, cy)
        radius = radius

    Line:
        y = slope*x + intercept

    Return:
        x1, y1, x2, y2, True

    if the line intersects the circle.
    """

    # Substitute y = slope*x + intercept into the circle equation
    #
    #     (x - cx)^2 + (y - cy)^2 = radius^2
    #
    # This produces a quadratic equation in x.

    a = 1 + slope**2

    b = (
        -2 * cx
        + 2 * slope * intercept
        - 2 * slope * cy
    )

    c = (
        cx**2
        + intercept**2
        - 2 * intercept * cy
        + cy**2
        - radius**2
    )

    x1, x2, ok = quadratic_equation(a, b, c)

    if not ok:
        return 0, 0, 0, 0, False

    y1 = slope * x1 + intercept
    y2 = slope * x2 + intercept

    return x1, y1, x2, y2, True


# -----------------------------------------------------------------------------
def triangle_area(A, B, C):
    """
    Find the area of triangle ABC using the shoelace formula.

    Each point is an (x, y) tuple.
    """

    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    return abs(
        x1 * y2
        + x2 * y3
        + x3 * y1
        - y1 * x2
        - y2 * x3
        - y3 * x1
    ) / 2


# -----------------------------------------------------------------------------
def plot_circle(cx, cy, radius):
    """
    Draw a circle with center (cx, cy).
    """

    theta = np.linspace(0, 2 * pi, 1000)

    x = cx + radius * np.cos(theta)
    y = cy + radius * np.sin(theta)

    plt.plot(x, y, color="black")


# =============================================================================
# Geometry of the problem
# =============================================================================

# O is the center of the large circle.
O = (0, 0)

# The large circle has radius 100.
large_radius = 100

# The small circle has radius 71.
small_radius = 71

# Since the two circles are externally tangent, their centers are
#
#          100 + 71 = 171
#
# units apart.
#
# Put the small circle to the left of O.

small_center = (-171, 0)


# =============================================================================
# Monte-Carlo search
# =============================================================================

NUMBER_OF_TRIALS = 10_000_000

max_area = 0

best_A = None
best_B = None
best_C = None


for trial in range(NUMBER_OF_TRIALS):

    # ---------------------------------------------------------
    # Randomly choose B on the upper-right part of the
    # large circle.
    # ---------------------------------------------------------

    alpha = pi/2

    Bx = large_radius * cos(alpha)
    By = large_radius * sin(alpha)

    B = (Bx, By)


    # ---------------------------------------------------------
    # Randomly choose C on the lower-right part of the
    # large circle.
    # ---------------------------------------------------------

    beta = uniform(-pi / 2, 0)

    Cx = large_radius * cos(beta)
    Cy = large_radius * sin(beta)

    C = (Cx, Cy)


    # ---------------------------------------------------------
    # Find the slope of BC.
    # ---------------------------------------------------------

    slope_BC = (Cy - By) / (Cx - Bx)


    # ---------------------------------------------------------
    # AB is perpendicular to BC.
    #
    # If two lines are perpendicular, their slopes satisfy
    #
    #           m1 * m2 = -1
    #
    # so the slope of AB is:
    #
    #           -1 / slope_BC
    # ---------------------------------------------------------

    slope_AB = -1 / slope_BC


    # ---------------------------------------------------------
    # AB passes through B.
    #
    # A line has the form
    #
    #           y = mx + b
    #
    # so
    #
    #           b = y - mx.
    # ---------------------------------------------------------

    intercept_AB = By - slope_AB * Bx


    # ---------------------------------------------------------
    # Find where line AB intersects the small circle.
    # ---------------------------------------------------------

    Ax1, Ay1, Ax2, Ay2, ok = line_circle_intersection(
        small_center[0],
        small_center[1],
        small_radius,
        slope_AB,
        intercept_AB
    )

    # Sometimes the randomly selected line does not intersect
    # the small circle. In that case simply try another pair
    # of random points B and C.
    if not ok:
        continue


    # ---------------------------------------------------------
    # There can be two intersections with the small circle.
    #
    # A in the diagram is the leftmost intersection, so choose
    # the point having the smaller x-coordinate.
    #
    # line_circle_intersection() already returns the smaller
    # x-coordinate first.
    # ---------------------------------------------------------

    A = (Ax1, Ay1)


    # ---------------------------------------------------------
    # Calculate the area of triangle ABC.
    # ---------------------------------------------------------

    area = triangle_area(A, B, C)


    # ---------------------------------------------------------
    # If this triangle is better than every triangle seen so
    # far, remember it.
    # ---------------------------------------------------------

    if area > max_area:

        max_area = area

        best_A = A
        best_B = B
        best_C = C


# =============================================================================
# Display the best Monte-Carlo result
# =============================================================================

A = best_A
B = best_B
C = best_C


# Draw the two circles.
plot_circle(O[0], O[1], large_radius)

plot_circle(
    small_center[0],
    small_center[1],
    small_radius
)


# Draw and shade triangle ABC.
triangle_x = [A[0], B[0], C[0], A[0]]
triangle_y = [A[1], B[1], C[1], A[1]]

plt.fill(
    triangle_x,
    triangle_y,
    color="red",
    alpha=0.35
)

plt.plot(
    triangle_x,
    triangle_y,
    color="red",
    linewidth=2
)


# Draw the radii OB and OC, as in the original diagram.
plt.plot(
    [O[0], B[0]],
    [O[1], B[1]],
    color="black"
)

plt.plot(
    [O[0], C[0]],
    [O[1], C[1]],
    color="black"
)


# -----------------------------------------------------------------------------
# Label the important points.
#
# Along with A, B, C, and O, show the coordinates found by the
# Monte-Carlo search.
# -----------------------------------------------------------------------------

plt.scatter(
    [A[0], B[0], C[0], O[0]],
    [A[1], B[1], C[1], O[1]],
    color="black",
    zorder=5
)


plt.annotate(
    f"A = ({A[0]:.2f}, {A[1]:.2f})",
    A,
    xytext=(-5, -22),
    textcoords="offset points",
    ha="right",
    fontsize=10
)

plt.annotate(
    f"B = ({B[0]:.2f}, {B[1]:.2f})",
    B,
    xytext=(5, 10),
    textcoords="offset points",
    fontsize=10
)

plt.annotate(
    f"C = ({C[0]:.2f}, {C[1]:.2f})",
    C,
    xytext=(8, -15),
    textcoords="offset points",
    fontsize=10
)

plt.annotate(
    "O = (0, 0)",
    O,
    xytext=(-5, -20),
    textcoords="offset points",
    ha="center",
    fontsize=10
)


# -----------------------------------------------------------------------------
# Finish the graph.
# -----------------------------------------------------------------------------

plt.title(
    f"Monte-Carlo maximum area of triangle ABC ≈ {max_area:.2f}"
)

# Equal scaling is important.  Without this, circles can look like ellipses.
plt.axis("equal")

# Hide the normal x- and y-axes so the drawing looks like the problem diagram.
plt.axis("off")

plt.show()


# -----------------------------------------------------------------------------
# Print the numerical result as well.
# -----------------------------------------------------------------------------

print(f"Maximum area found = {max_area:.6f}")
print()
print(f"A = ({A[0]:.6f}, {A[1]:.6f})")
print(f"B = ({B[0]:.6f}, {B[1]:.6f})")
print(f"C = ({C[0]:.6f}, {C[1]:.6f})")
print(f"O = ({O[0]:.6f}, {O[1]:.6f})")
