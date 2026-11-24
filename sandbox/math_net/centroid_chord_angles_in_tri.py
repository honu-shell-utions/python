"""
Jim McCleery
November 23, 2026
Kailua-Kona, HI

Geometry Visualization: MIT MathNet Problem cps_2016_d90cda
https://mathnet.mit.edu/explorer.html?p=cps_2016_d90cda

Problem Statement:
Let ABC be an acute-angled triangle with AB < AC. Tangent to its circumcircle
Omega at A intersects the line BC at D. Let G be the centroid of ABC and let
AG meet Omega again at H != A. Suppose the line DG intersects the lines AB and
AC at E and F, respectively. Prove that angle EHG = angle GHF.
"""

# Import standard math functions and constants needed for geometry
from math import acos, atan, cos, degrees, pi, sin, sqrt
# Import uniform to pick random side lengths within a given range
from random import uniform
# Import Matplotlib's pyplot module (aliased as 'plt') for drawing figures
import matplotlib.pyplot as plt
# Import NumPy (aliased as 'np') for creating evenly spaced arrays of angles
import numpy as np


# -----------------------------------------------------------------------------
# Geometry Helper Functions
# -----------------------------------------------------------------------------

def distance(A, B):
    """
    Calculate the straight-line distance between two points A and B.

    Parameters:
        A, B: points written as (x, y) tuples
    """
    # Unpack the (x, y) coordinates from each tuple into individual variables
    x1, y1 = A
    x2, y2 = B

    # Apply the Pythagorean theorem: sqrt((dx)^2 + (dy)^2)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def law_of_cosines(d1, d2, opposite_side):
    """
    Find an angle (in radians) of a triangle using the Law of Cosines:
        c^2 = a^2 + b^2 - 2ab * cos(C)
    The returned angle is opposite 'opposite_side'.

    Returns:
        (angle_in_radians, True) if the sides form a valid triangle
        (0, False) otherwise
    """
    try:
        # Rearrange the Law of Cosines formula to solve for cos(angle)
        cosine_value = (d1**2 + d2**2 - opposite_side**2) / (2 * d1 * d2)

        # Tiny floating-point rounding errors can produce values like 1.0000000000000002.
        # Clamp the value strictly between -1 and 1 so acos() will not crash.
        cosine_value = max(-1.0, min(1.0, cosine_value))

        # Inverse cosine (acos) converts the cosine ratio back into an angle in radians
        return acos(cosine_value), True

    except (ValueError, ZeroDivisionError):
        return 0, False


def angle_between_points(A, B, C):
    """
    Calculate angle ABC (with vertex at B) in degrees.

    Parameters:
        A, B, C: points written as (x, y) tuples
    """
    # Measure the three side lengths of triangle ABC
    side_AB = distance(A, B)
    side_BC = distance(B, C)
    side_AC = distance(A, C)

    # Find the angle at vertex B (which is opposite side AC) and convert to degrees
    angle_rad, _ = law_of_cosines(side_AB, side_BC, side_AC)
    return degrees(angle_rad)


def circum_circle(A, B, C):
    """
    Find the unique circle (circumcircle) passing through three points A, B, and C.

    Parameters:
        A, B, C: three non-collinear points written as (x, y) tuples

    Returns:
        (center, radius, True) if a valid circle exists
        ((0, 0), 0, False) if the three points lie on a straight line
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    try:
        # Pre-calculate x^2 + y^2 for each point to simplify the determinant formulas
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2

        # Compute determinants to solve the system of equations for the circle center
        M11 = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
        M12 = s1 * y2 + s2 * y3 + s3 * y1 - s2 * y1 - s3 * y2 - s1 * y3
        M13 = s1 * x2 + s2 * x3 + s3 * x1 - s2 * x1 - s3 * x2 - s1 * x3

        # Calculate the center coordinates (raises ZeroDivisionError if M11 == 0)
        center = (0.5 * M12 / M11, -0.5 * M13 / M11)

        # Since A lies on the circle, the distance from A to the center is the radius
        radius = distance(A, center)

        return center, radius, True

    except (ValueError, ZeroDivisionError):
        return (0, 0), 0, False


def quadratic_equation(A, B, C):
    """
    Solve the quadratic equation A*x^2 + B*x + C = 0 for real roots.

    Returns:
        (x1, x2, True) with x1 <= x2 if real solutions exist
        (0, 0, False) if there are no real solutions
    """
    try:
        # Compute the discriminant (the expression inside the square root)
        discriminant = B**2 - 4 * A * C

        # Raises ValueError if discriminant < 0 (meaning no real intersection)
        square_root = sqrt(discriminant)

        # Compute both roots using the quadratic formula
        x1 = (-B - square_root) / (2 * A)
        x2 = (-B + square_root) / (2 * A)

        # Ensure x1 is always the smaller (or equal) root
        if x1 > x2:
            x1, x2 = x2, x1

        return x1, x2, True

    except (ValueError, ZeroDivisionError):
        return 0, 0, False


def line_circle_intersection(center, radius, line):
    """
    Find the intersection points of a circle and a non-vertical line y = m*x + b.

    Parameters:
        center: circle center written as (x, y)
        radius: radius of the circle
        line: tuple (m, b) representing slope m and y-intercept b

    Returns:
        (P1, P2, True) where P1 has the smaller x-coordinate
        ((0, 0), (0, 0), False) if the line does not intersect the circle
    """
    cx, cy = center
    m, b = line

    # Substitute y = m*x + b into (x - cx)^2 + (y - cy)^2 = radius^2
    # and collect terms into the standard quadratic form A*x^2 + B*x + C_val = 0
    A = 1 + m**2
    B = -2 * cx + 2 * m * b - 2 * m * cy
    C_val = cx**2 + b**2 - 2 * b * cy + cy**2 - radius**2

    # Solve for the two x-coordinates where the line meets the circle
    x1, x2, ok = quadratic_equation(A, B, C_val)
    if not ok:
        return (0, 0), (0, 0), False

    # Plug each x-value back into y = m*x + b to get the corresponding y-values
    P1 = (x1, m * x1 + b)
    P2 = (x2, m * x2 + b)

    return P1, P2, True


def line_intersection_from_points(A, B, C, D):
    """
    Find the intersection point of line AB and line CD.

    Parameters:
        A, B: two points defining the first line
        C, D: two points defining the second line

    Returns:
        (P, True) if the lines intersect at point P = (x, y)
        ((0, 0), False) if the lines are parallel or vertical
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D

    try:
        # Compute the slope (rise / run) for each line
        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y4 - y3) / (x4 - x3)

        # Solve for the x-coordinate where the two point-slope equations are equal
        x = (y1 - slope1 * x1 - y3 + slope2 * x3) / (slope2 - slope1)

        # Plug x into the first line's equation to find y
        y = y1 + slope1 * (x - x1)

        return (x, y), True

    except ZeroDivisionError:
        return (0, 0), False


def polygon_fill_coordinates(*vertices):
    """
    Convert a sequence of (x, y) vertices into closed x and y coordinate tuples
    suitable for Matplotlib's plt.fill() function.
    """
    # Extract all x-coordinates and all y-coordinates into separate tuples
    x_coords = tuple(point[0] for point in vertices)
    y_coords = tuple(point[1] for point in vertices)

    # Repeat the first vertex at the end to close the polygon outline
    x_coords += (x_coords[0],)
    y_coords += (y_coords[0],)

    return x_coords, y_coords


# -----------------------------------------------------------------------------
# Plotting Helper Functions
# -----------------------------------------------------------------------------

def plot_circle(center, radius, start=0, stop=2 * pi):
    """Draw the outline of a circle or circular arc."""
    cx, cy = center

    # Generate 1,500 evenly spaced angles around the circle for a smooth curve
    angles = np.linspace(start, stop, 1500)

    # Convert polar coordinates (radius, angle) into Cartesian (x, y) points
    x_values = radius * np.cos(angles) + cx
    y_values = radius * np.sin(angles) + cy

    plt.plot(x_values, y_values, color="black", linewidth=1.2)


def plot_line(A, B, style="-", color="black", linewidth=1.2):
    """Draw a straight line segment between two points A and B."""
    x1, y1 = A
    x2, y2 = B
    plt.plot([x1, x2], [y1, y2], linestyle=style, color=color, linewidth=linewidth)


def plot_point(P, label=None, offset=(6, 6)):
    """
    Draw a dot at point P and optionally add a text label next to it.

    Parameters:
        P: (x, y) coordinates of the point
        label: string name of the point (e.g., 'A', 'B', 'G')
        offset: (dx, dy) pixel offset so the text does not overlap the dot
    """
    x, y = P
    plt.plot(x, y, "o", color="black", markersize=5)

    if label:
        plt.annotate(
            label,
            xy=P,
            textcoords="offset points",
            xytext=offset,
            fontsize=11,
            fontweight="bold",
        )


# -----------------------------------------------------------------------------
# Main Simulation Loop
# -----------------------------------------------------------------------------

# Run up to 1,000 random acute triangle trials to visually verify angle EHG == angle GHF
for _ in range(10**3):
    # Clear the previous drawing from the Matplotlib figure
    plt.cla()

    # Pick random side lengths ensuring AB < AC
    AB = uniform(5, 20)
    BC = uniform(5, 20)
    AC = uniform(AB, 21)

    # Compute the interior angles at A (alpha), B (beta), and C (gamma)
    alpha, ok_a = law_of_cosines(AB, AC, BC)
    beta, ok_b = law_of_cosines(AB, BC, AC)
    if not ok_a or not ok_b:
        continue

    gamma = pi - alpha - beta

    # Skip triangles that are not strictly acute (all angles must be < 90 degrees / pi/2)
    if alpha >= pi / 2 or beta >= pi / 2 or gamma >= pi / 2:
        continue

    # Place vertex A at the origin (0, 0) and vertex B along the positive x-axis
    A = (0, 0)
    B = (AB, 0)
    C = (AC * cos(alpha), AC * sin(alpha))

    # Find the circumcircle Omega (center CC and radius CCr) of triangle ABC
    CC, CCr, _ = circum_circle(A, B, C)

    # The tangent line to Omega at A is perpendicular to the radius from A to CC.
    # Subtracting pi/2 rotates the radius angle by 90 degrees to get the tangent direction.
    tangent_angle = atan(CC[1] / CC[0]) - pi / 2
    Z = (cos(tangent_angle), sin(tangent_angle))

    # Point D is where the tangent at A intersects line BC
    D, _ = line_intersection_from_points(A, Z, C, B)

    # Skip diagrams where angle ADB is very narrow so the plot stays clean and readable
    if angle_between_points(A, D, B) < 20:
        continue

    # Point G is the centroid (average of the three vertices) of triangle ABC
    G = ((A[0] + B[0] + C[0]) / 3, (A[1] + B[1] + C[1]) / 3)

    # Line AG passes through the origin A = (0, 0) with slope m = G_y / G_x.
    # Intersecting AG with circumcircle Omega gives two points: A (smaller x) and H (larger x).
    slope_AG = G[1] / G[0]
    _, H, _ = line_circle_intersection(CC, CCr, (slope_AG, 0))

    # Line DG intersects side AB at E and side AC at F
    E, _ = line_intersection_from_points(A, B, D, G)
    F, _ = line_intersection_from_points(D, G, C, A)

    # Calculate the two target angles in degrees to verify they are equal
    angle_EHG = angle_between_points(E, H, G)
    angle_GHF = angle_between_points(G, H, F)

    # Shade triangles EHG (red) and GHF (blue) to highlight the two angles at H
    plt.fill(*polygon_fill_coordinates(E, H, G), color="red", alpha=0.35, edgecolor="red", linewidth=1.5)
    plt.fill(*polygon_fill_coordinates(G, H, F), color="blue", alpha=0.35, edgecolor="blue", linewidth=1.5)

    # Draw the circumcircle Omega and all geometric line segments
    plot_circle(CC, CCr)
    plot_line(A, B)
    plot_line(B, C)
    plot_line(A, C)
    plot_line(A, D, style="--", color="gray")  # Tangent line at A
    plot_line(B, D, style="--", color="gray")  # Extension of BC to D
    plot_line(D, F, color="darkgreen")         # Line D-E-G-F
    plot_line(A, H, color="purple")            # Chord A-G-H
    plot_line(E, H, color="red")
    plot_line(H, F, color="blue")

    # Plot and label all eight geometric points from the problem statement
    plot_point(A, "A", offset=(-14, -10))
    plot_point(B, "B", offset=(6, -12))
    plot_point(C, "C", offset=(0, 8))
    plot_point(D, "D", offset=(-14, -10))
    plot_point(E, "E", offset=(0, -14))
    plot_point(F, "F", offset=(-14, 4))
    plot_point(G, "G", offset=(4, 6))
    plot_point(H, "H", offset=(6, 4))

    # Label the circumcircle Omega near the top of the circle
    plt.annotate(
        r"$\Omega$",
        xy=(CC[0], CC[1] + CCr),
        textcoords="offset points",
        xytext=(0, 6),
        fontsize=12,
    )

    # Display the computed angles in the title, keep x/y scales equal, and pause briefly
    plt.title(f"Angle EHG = {angle_EHG:.3f}°, Angle GHF = {angle_GHF:.3f}°")
    plt.axis("equal")
    plt.axis("off")
    plt.pause(1)

plt.show()
