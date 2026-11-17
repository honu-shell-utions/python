"""
Jim McCleery
November 17, 2026
Kailua-Kona, HI

IMO 2024 Problem 4 Visualization & Verification
https://mathnet.mit.edu/explorer.html?p=imo_2024_7db46b
"""

# Import standard math functions and constants needed for geometry
from math import pi, sqrt, sin, cos, tan, acos, degrees
# Import uniform() to generate random decimal numbers within a range
from random import uniform
# Import NumPy (aliased as 'np') for fast array math and trigonometry
import numpy as np
# Import Matplotlib's pyplot module (aliased as 'plt') for drawing figures
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def circum_circle(A, B, C):
    """
    Find the unique circle passing through three points A, B, and C.

    Parameters:
        A, B, C: three points written as (x, y) tuples

    Returns:
        (center, radius, True) where center is an (x, y) tuple.
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

        # Compute determinants to solve the system of circle equations
        M11 = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
        M12 = s1 * y2 + s2 * y3 + s3 * y1 - s2 * y1 - s3 * y2 - s1 * y3
        M13 = s1 * x2 + s2 * x3 + s3 * x1 - s2 * x1 - s3 * x2 - s1 * x3

        # Calculate the center coordinates (fails if M11 == 0, i.e., collinear points)
        center = (0.5 * M12 / M11, -0.5 * M13 / M11)

        # Since point A lies on the circle, its distance to the center is the radius
        radius = distance(A, center)

        return center, radius, True

    except (ValueError, ZeroDivisionError):
        return (0, 0), 0, False


# -----------------------------------------------------------------------------
def distance(A, B):
    """
    Return the straight-line distance between two points A and B.

    Parameters:
        A, B: points written as (x, y) tuples
    """
    x1, y1 = A
    x2, y2 = B

    # Apply the Pythagorean theorem: sqrt((dx)^2 + (dy)^2)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# -----------------------------------------------------------------------------
def in_circle(A, B, C):
    """
    Find the incircle of triangle ABC (the largest circle that fits inside,
    tangent to all three sides).

    Parameters:
        A, B, C: triangle vertices written as (x, y) tuples

    Returns:
        (center, radius) where center is the incenter I of the triangle.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    # Side 'a' is opposite vertex A, 'b' is opposite B, 'c' is opposite C
    a = distance(B, C)
    b = distance(A, C)
    c = distance(A, B)

    # Semiperimeter (half of the triangle's perimeter)
    s = (a + b + c) / 2

    # Heron's formula for the area of the triangle
    area = sqrt(s * (s - a) * (s - b) * (s - c))

    # Geometric identity: inradius = area / semiperimeter
    radius = area / s

    # The incenter is a weighted average of the vertices using opposite side lengths
    center_x = (a * x1 + b * x2 + c * x3) / (a + b + c)
    center_y = (a * y1 + b * y2 + c * y3) / (a + b + c)

    return (center_x, center_y), radius


# -----------------------------------------------------------------------------
def law_of_cosines(d1, d2, opposite_side):
    """
    Find an angle of a triangle using the Law of Cosines.
    The angle returned (in radians) is opposite 'opposite_side'.

    Returns:
        (angle_radians, True) if valid, or (0, False) otherwise.
    """
    try:
        cosine_value = (d1**2 + d2**2 - opposite_side**2) / (2 * d1 * d2)

        # Clamp strictly between -1 and 1 to prevent floating-point rounding errors
        cosine_value = max(-1.0, min(1.0, cosine_value))

        return acos(cosine_value), True

    except (ValueError, ZeroDivisionError):
        return 0, False


# -----------------------------------------------------------------------------
def line_circle_intersection(C, radius, line):
    """
    Find the two intersection points of a circle and a non-vertical line.

    Parameters:
        C: circle center written as (x, y)
        radius: radius of the circle
        line: tuple (m, b) representing y = m*x + b

    Returns:
        (P1, P2, True) if intersections exist, or ((0, 0), (0, 0), False) otherwise.
    """
    center_x, center_y = C
    m, b = line

    # Substitute y = m*x + b into (x - center_x)^2 + (y - center_y)^2 = radius^2
    # to form a quadratic equation A*x^2 + B*x + C_val = 0
    A = 1 + m**2
    B = -2 * center_x + 2 * m * b - 2 * m * center_y
    C_val = center_x**2 + b**2 - 2 * b * center_y + center_y**2 - radius**2

    # Compute the discriminant to check if real solutions exist
    discriminant = B**2 - 4 * A * C_val
    if discriminant < 0 or A == 0:
        return (0, 0), (0, 0), False

    sqrt_disc = sqrt(discriminant)
    x1 = (-B - sqrt_disc) / (2 * A)
    x2 = (-B + sqrt_disc) / (2 * A)

    # Plug both x-values back into y = m*x + b to get the full points
    P1 = (x1, m * x1 + b)
    P2 = (x2, m * x2 + b)

    return P1, P2, True


# -----------------------------------------------------------------------------
def line_intersection_from_points(A, B, C, D):
    """
    Find the intersection of line AB and line CD.

    Parameters:
        A, B: two points on the first line
        C, D: two points on the second line

    Returns:
        (P, True) if the lines intersect, or ((0, 0), False) if parallel/vertical.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D

    try:
        # Rise-over-run slope for each line
        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y4 - y3) / (x4 - x3)

        # Solve for the x-coordinate where both lines meet
        x = (y1 - slope1 * x1 - y3 + slope2 * x3) / (slope2 - slope1)
        y = y1 + slope1 * (x - x1)

        return (x, y), True

    except ZeroDivisionError:
        return (0, 0), False


# -----------------------------------------------------------------------------
def mid_point(A, B):
    """Return the midpoint halfway between points A and B."""
    x1, y1 = A
    x2, y2 = B
    return ((x1 + x2) / 2, (y1 + y2) / 2)


# -----------------------------------------------------------------------------
def plot_circle(C, radius, color="black", linestyle="-", start=0, stop=2 * pi):
    """Plot the outline of a circle or circular arc using Matplotlib."""
    center_x, center_y = C

    # Generate 1,500 evenly spaced angles for a smooth curve
    angles = np.linspace(start, stop, 1500)
    x_values = radius * np.cos(angles) + center_x
    y_values = radius * np.sin(angles) + center_y

    plt.plot(x_values, y_values, color=color, linestyle=linestyle)


# -----------------------------------------------------------------------------
def plot_line(A, B, color="black", linestyle="-"):
    """Plot a straight line segment between points A and B."""
    x1, y1 = A
    x2, y2 = B
    plt.plot([x1, x2], [y1, y2], color=color, linestyle=linestyle)


# -----------------------------------------------------------------------------
def polygon_fill_coordinates(vertices):
    """
    Convert a list of (x, y) vertices into closed (x_tuple, y_tuple) pairs
    ready to be unpacked into plt.fill().
    """
    x_coords = tuple(point[0] for point in vertices) + (vertices[0][0],)
    y_coords = tuple(point[1] for point in vertices) + (vertices[0][1],)
    return x_coords, y_coords


# -----------------------------------------------------------------------------
def label_point(point, text, offset=(0.25, 0.25)):
    """
    Plot a dot at 'point' and place a text label slightly offset from it
    so the letter doesn't overlap the lines.
    """
    x, y = point
    dx, dy = offset
    plt.plot(x, y, "ko", markersize=4)
    plt.text(x + dx, y + dy, text, fontsize=11, fontweight="bold")


# =============================================================================
# Main Loop: Generate random triangles with AB < AC < BC
# =============================================================================

for _ in range(10**3):
    plt.cla()
    
    # Pick random side lengths satisfying AB < AC < BC
    AB = uniform(6, 12)
    AC = uniform(AB + 1, 16)
    BC = uniform(AC + 1, 20)

    # Ensure the three lengths satisfy the triangle inequality
    if (AB + AC <= BC) or (AB + BC <= AC) or (AC + BC <= AB):
        continue

    # Find angle alpha at vertex A using the Law of Cosines
    alpha, _ = law_of_cosines(AB, AC, BC)

    # Place A at the origin and B along the positive x-axis
    A = (0.0, 0.0)
    B = (AB, 0.0)
    C = (AC * cos(alpha), AC * sin(alpha))

    # K and L are the midpoints of AB and AC, respectively
    K = mid_point(A, B)
    L = mid_point(A, C)

    # Find the incenter I and inradius r of incircle omega
    I, r = in_circle(A, B, C)

    # Find the circumcircle of triangle ABC
    circum_center, circum_radius, _ = circum_circle(A, B, C)

    # Line AI passes through A(0, 0) and I(Ix, Iy), so its slope is Iy / Ix
    slope_AI = I[1] / I[0]
    P1, P2, _ = line_circle_intersection(circum_center, circum_radius, (slope_AI, 0))

    # Pick the intersection point P that is NOT vertex A
    P = P1 if distance(P1, A) > 1e-6 else P2

    # --- Construct point Y on side BC ---
    # Since AB lies on the x-axis (y = 0), the line parallel to AB and tangent
    # to the incircle (on the interior side of the triangle) is y = 2*r
    Z1, _ = line_intersection_from_points(A, C, (-1, 2 * r), (1, 2 * r))
    Y, _ = line_intersection_from_points(B, C, (-1, 2 * r), (1, 2 * r))

    # --- Construct point X on side BC ---
    # The tangent parallel to AC meets the x-axis (line AB) at Z3
    Z3 = (I[0] + r / tan(pi / 2 - alpha / 2), 0.0)
    # Move from Z3 in the direction of AC (angle alpha) until hitting side BC at X
    Z3_dir = (Z3[0] + cos(alpha), sin(alpha))
    X, _ = line_intersection_from_points(Z3, Z3_dir, B, C)

    # Shade triangle KIL in red and triangle YPX in blue
    plt.fill(*polygon_fill_coordinates([K, I, L]), color="red", alpha=0.45, edgecolor="red", linewidth=2)
    plt.fill(*polygon_fill_coordinates([Y, P, X]), color="blue", alpha=0.45, edgecolor="blue", linewidth=2)

    # Compute angle KIL (at vertex I) in degrees
    angle_KIL_rad, _ = law_of_cosines(distance(K, I), distance(L, I), distance(K, L))
    angle_KIL = degrees(angle_KIL_rad)

    # Compute angle YPX (at vertex P) in degrees
    angle_YPX_rad, _ = law_of_cosines(distance(P, Y), distance(P, X), distance(X, Y))
    angle_YPX = degrees(angle_YPX_rad)

    # Draw the circumcircle (dashed), triangle ABC, incircle omega, and tangent segments
    plot_circle(circum_center, circum_radius, color="gray", linestyle="--")
    plot_circle(I, r, color="black")
    plot_line(A, B)
    plot_line(B, C)
    plot_line(A, C)
    plot_line(Z1, Y, color="green", linestyle=":")
    plot_line(Z3, X, color="green", linestyle=":")
    plot_line(A, P, color="gray", linestyle=":")

    # Add point labels matching the problem diagram
    label_point(A, "A", offset=(-0.6, -0.5))
    label_point(B, "B", offset=(0.3, -0.5))
    label_point(C, "C", offset=(0.0, 0.3))
    label_point(I, "I", offset=(0.2, -0.4))
    label_point(K, "K", offset=(-0.2, -0.6))
    label_point(L, "L", offset=(-0.6, 0.2))
    label_point(P, "P", offset=(0.3, -0.4))
    label_point(X, "X", offset=(0.3, 0.1))
    label_point(Y, "Y", offset=(0.3, 0.1))

    # Display the angle sum (should always equal 180.000 degrees)
    plt.title(f"∠KIL (red) + ∠YPX (blue) = {angle_KIL:.2f}° + {angle_YPX:.2f}° = {angle_KIL + angle_YPX:.3f}°")
    plt.axis("equal")
    plt.axis("off")
    plt.pause(1)
plt.show()
