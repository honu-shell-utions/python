# =============================================================================
# Jim McCleery
# November 25, 2026
# Kailua-Kona, HI
#
# MIT MathNet Problem Explorer:
# https://mathnet.mit.edu/explorer.html?p=chn_2024_9eb338
# =============================================================================

# Import standard math functions and constants needed for geometry
from math import acos, cos, degrees, pi, sin, sqrt, tan
# Import uniform to generate random decimal numbers within a given range
from random import uniform

# Import Matplotlib's pyplot module (nicknamed 'plt') for drawing figures
import matplotlib.pyplot as plt
# Import NumPy (nicknamed 'np') to generate evenly spaced arrays for circles
import numpy as np


# -----------------------------------------------------------------------------
def circum_circle(A, B, C):
    """
    Find the unique circle passing through three points A, B, and C.

    Parameters:
        A, B, C: points written as (x, y) tuples

    Returns:
        (center, radius, True) if the circle exists.
        ((0, 0), 0, False) if the three points lie on a straight line.
    """
    # Unpack each (x, y) point tuple into separate coordinate variables
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    try:
        # Pre-calculate x^2 + y^2 for each point to keep the formulas readable
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2

        # Compute matrix determinants to solve for the circle's center
        M11 = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
        M12 = s1 * y2 + s2 * y3 + s3 * y1 - s2 * y1 - s3 * y2 - s1 * y3
        M13 = s1 * x2 + s2 * x3 + s3 * x1 - s2 * x1 - s3 * x2 - s1 * x3

        # Calculate the center (x, y); divides by zero if points are collinear
        center_x = 0.5 * M12 / M11
        center_y = -0.5 * M13 / M11
        center = (center_x, center_y)

        # The radius is the distance from the center to any vertex on the circle
        radius = distance(A, center)

        return center, radius, True

    except (ValueError, ZeroDivisionError):
        return (0, 0), 0, False


# -----------------------------------------------------------------------------
def distance(A, B):
    """
    Calculate the straight-line distance between two points A and B.

    Parameters:
        A, B: points written as (x, y) tuples
    """
    # Unpack the coordinates of both points
    x1, y1 = A
    x2, y2 = B

    # Apply the Pythagorean theorem: sqrt((dx)^2 + (dy)^2)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# -----------------------------------------------------------------------------
def intersection_of_lines(line1, line2):
    """
    Find where two lines in slope-intercept form (y = m*x + b) intersect.

    Parameters:
        line1, line2: tuples written as (m, b) where m is slope and b is y-intercept

    Returns:
        ((x, y), True) if they intersect, or ((0, 0), False) if parallel.
    """
    # Unpack slope (m) and y-intercept (b) for both lines
    m1, b1 = line1
    m2, b2 = line2

    # Parallel lines have equal slopes and never cross
    if m1 == m2:
        return (0, 0), False

    # Set m1*x + b1 = m2*x + b2 and solve for x, then substitute back to get y
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1

    return (x, y), True


# -----------------------------------------------------------------------------
def law_of_cosines(d1, d2, side):
    """
    Find an angle of a triangle using the Law of Cosines:
        side^2 = d1^2 + d2^2 - 2 * d1 * d2 * cos(angle)

    Parameters:
        d1, d2: lengths of the two sides adjacent to the angle
        side: length of the side opposite the angle

    Returns:
        (angle_in_radians, True) if valid, or (0, False) otherwise.
    """
    try:
        # Rearrange the Law of Cosines to solve for cos(angle)
        cosine_value = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)

        # Clamp between -1 and 1 to prevent tiny floating-point rounding errors
        # (like 1.0000000000000002) from crashing acos()
        cosine_value = max(-1.0, min(1.0, cosine_value))

        # Convert the cosine ratio back into an angle in radians
        angle = acos(cosine_value)
        return angle, True

    except (ValueError, ZeroDivisionError):
        return 0, False


# -----------------------------------------------------------------------------
def line_intersection_from_points(A, B, C, D):
    """
    Find the intersection of the line through A & B and the line through C & D.

    Parameters:
        A, B, C, D: points written as (x, y) tuples

    Returns:
        ((x, y), True) if the lines intersect, or ((0, 0), False) if vertical/parallel.
    """
    # Unpack all four (x, y) points
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D

    try:
        # Calculate rise-over-run slopes for both lines
        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y4 - y3) / (x4 - x3)

        # Solve the two point-slope equations simultaneously for x and y
        x = (y1 - slope1 * x1 - y3 + slope2 * x3) / (slope2 - slope1)
        y = y1 + slope1 * (x - x1)

        return (x, y), True

    except ZeroDivisionError:
        return (0, 0), False


# -----------------------------------------------------------------------------
def plot_circle(C, radius, start=0, stop=2 * pi):
    """
    Draw the outline of a circle (or circular arc) using Matplotlib.

    Parameters:
        C: center written as (x, y)
        radius: radius of the circle
        start, stop: starting and ending angles in radians
    """
    center_x, center_y = C

    # Create 1,500 evenly spaced angles so the curve looks smooth
    angles = np.linspace(start, stop, 1500)

    # Convert polar coordinates (radius, angle) to Cartesian (x, y) arrays
    x_values = radius * np.cos(angles) + center_x
    y_values = radius * np.sin(angles) + center_y

    plt.plot(x_values, y_values)


# -----------------------------------------------------------------------------
def plot_line(A, B):
    """
    Draw a straight line segment connecting two points A and B.

    Parameters:
        A, B: endpoints written as (x, y) tuples
    """
    x1, y1 = A
    x2, y2 = B

    # plt.plot expects a list of x-coordinates first, then a list of y-coordinates
    plt.plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
def plot_labeled_point(P, label, offset=(5, 5)):
    """
    Draw a dot at point P and place a text label slightly offset from the dot.

    Parameters:
        P: point coordinates written as (x, y)
        label: text string to display (e.g., 'A')
        offset: (dx, dy) shift in screen points so text does not overlap the dot
    """
    x, y = P

    # Plot a small black circular marker ('ko') at the point
    plt.plot(x, y, "ko", markersize=4)

    # Place the text label near the point using pixel/point offsets
    plt.annotate(
        label,
        xy=(x, y),
        xytext=offset,
        textcoords="offset points",
        fontsize=11,
        fontweight="bold",
    )


# -----------------------------------------------------------------------------
def random_acute_triangle():
    """
    Generate three (x, y) vertices of a random acute triangle.
    Places two vertices at (0, 0) and (1, 0), and picks a third vertex (x, y)
    above the semicircle of diameter 1 so all three angles are less than 90 degrees.
    """
    x = uniform(0.0, 1.0)
    min_y = sqrt(x * (1.0 - x))
    y = uniform(min_y, 1.0)

    # Repeat if floating-point rounding lands exactly on a boundary
    while not (0.0 < x < 1.0 and y * y > x * (1.0 - x)):
        x = uniform(0.0, 1.0)
        min_y = sqrt(x * (1.0 - x))
        y = uniform(min_y, 1.0)

    return (0.0, 0.0), (1.0, 0.0), (x, y)


# =============================================================================
# Main Simulation Loop
# =============================================================================

# Step 1: Generate an acute triangle ABC that satisfies AB < BC < CA
while True:
    B, C, A = random_acute_triangle()
    AB = distance(A, B)
    BC = distance(B, C)
    AC = distance(A, C)

    if AB < BC < AC:
        break

# Step 2: Find the circumcircle of triangle ABC and pre-calculate fixed angles
circumcenter, circumradius, _ = circum_circle(A, B, C)
theta, _ = law_of_cosines(circumradius, circumradius, AB)
angle_B, _ = law_of_cosines(AB, BC, AC)

# Step 3: Animate 100 valid positions of moving points D and E
for _ in range(100):
    # Clear the previous frame so lines do not pile up
    plt.cla()

    # Search for a random point D on side BC and point E on minor arc BC
    # such that angle BAD equals angle BED
    while True:
        # Pick a random angle along the lower minor arc BC
        alpha = uniform(3 * pi / 2 - theta / 2, 3 * pi / 2 + theta / 2)

        # Place D on segment BC (along the x-axis between B and C)
        D = (uniform(0.1 * BC, 0.9 * BC), 0)

        # Place E on the circumcircle using polar coordinates from the center
        E = (
            circumcenter[0] + circumradius * cos(alpha),
            circumcenter[1] + circumradius * sin(alpha),
        )

        # Measure angle BAD using the Law of Cosines
        angle_BAD, _ = law_of_cosines(AB, distance(A, D), D[0])

        # Measure angle BED using the Law of Cosines
        angle_BED, _ = law_of_cosines(distance(B, E), distance(D, E), D[0])

        # Accept this pair once the two angles match within a tiny tolerance
        if abs(angle_BAD - angle_BED) < 0.00001:
            break

    # Step 4: Find point F, where the line through D perpendicular to AB
    # meets the extension of side AC
    slope_AB = tan(angle_B)
    intercept_AB = 0

    # Perpendicular lines have negative reciprocal slopes: m2 = -1 / m1
    slope_perp = -1 / slope_AB
    intercept_perp = D[1] - slope_perp * D[0]

    # Q is the foot of the perpendicular from D onto line AB
    Q, _ = intersection_of_lines((slope_AB, intercept_AB), (slope_perp, intercept_perp))

    # Intersect line QD with line AC to locate point F
    F, _ = line_intersection_from_points(A, C, Q, D)

    # Step 5: Compute angle BEF to verify that it remains constant
    angle_BEF, _ = law_of_cosines(distance(B, E), distance(E, F), distance(B, F))

    # Step 6: Draw the circumcircle and all geometric line segments
    plot_circle(circumcenter, circumradius)
    plot_line(A, B)
    plot_line(B, C)
    plot_line(A, F)  # Includes side AC and its extension to F
    plot_line(B, E)
    plot_line(D, E)
    plot_line(A, D)
    plot_line(D, F)
    plot_line(E, F)

    # Step 7: Label all key points from the problem statement
    plot_labeled_point(A, "A", offset=(0, 8))
    plot_labeled_point(B, "B", offset=(-12, -10))
    plot_labeled_point(C, "C", offset=(6, -10))
    plot_labeled_point(D, "D", offset=(2, 6))
    plot_labeled_point(E, "E", offset=(-4, -14))
    plot_labeled_point(F, "F", offset=(6, -4))

    # Display the measured angle in the title and keep x/y scales equal
    plt.title(f"Angle BEF is equal to {degrees(angle_BEF):0.3f} degrees.")
    plt.axis("equal")
    plt.axis("off")

    # Pause 1 second so the viewer can watch each step of the animation
    plt.pause(1)

# Keep the final plot window open after the loop finishes
plt.show()
