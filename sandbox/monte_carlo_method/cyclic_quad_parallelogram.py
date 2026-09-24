# -----------------------------------------------------------------------------
# Jim McCleery
# September 24, 2026
# Kailua-Kona, HI
#
# Problem Reference:
# https://mathnet.mit.edu/explorer.html?p=btw_2016_1ce226
#
# Problem Statement:
# Let ABCD be a parallelogram such that angle BAD = 60 degrees.
# Let K and L be the midpoints of BC and CD, respectively.
# Assuming that ABKL is a cyclic quadrilateral, find angle ABD.
# -----------------------------------------------------------------------------

from math import pi, sqrt, acos, degrees
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Geometry Helper Functions
# -----------------------------------------------------------------------------

def distance(point_1, point_2):
    """
    Calculate the straight-line (Euclidean) distance between two points.

    Each point is given as a tuple of coordinates: (x, y).
    Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    """
    x1, y1 = point_1
    x2, y2 = point_2
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def mid_point(point_1, point_2):
    """
    Find the midpoint between two points.

    Formula: ((x1 + x2) / 2, (y1 + y2) / 2)
    """
    x1, y1 = point_1
    x2, y2 = point_2
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def define_circle_from_points(point_a, point_b, point_c):
    """
    Find the center (x, y) and radius (r) of the unique circle
    passing through three non-collinear points: point_a, point_b, and point_c.
    """
    x1, y1 = point_a
    x2, y2 = point_b
    x3, y3 = point_c

    temp = x2**2 + y2**2
    bc = (x1**2 + y1**2 - temp) / 2
    cd = (temp - x3**2 - y3**2) / 2

    # Determinant of the coordinate system equations
    determinant = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    center_x = (bc * (y2 - y3) - cd * (y1 - y2)) / determinant
    center_y = ((x1 - x2) * cd - (x2 - x3) * bc) / determinant

    center = (center_x, center_y)
    radius = distance(center, point_a)

    return center, radius


def distance_point_to_circle(center, radius, point):
    """
    Calculate the shortest distance from a point to the circumference of a circle.
    If the point lies exactly on the circle, this distance is 0.
    """
    return abs(distance(point, center) - radius)


def law_of_cosines(side_adjacent_1, side_adjacent_2, side_opposite):
    """
    Calculate the angle opposite to 'side_opposite' using the Law of Cosines:
        cos(C) = (a^2 + b^2 - c^2) / (2 * a * b)

    Returns:
        (angle_in_radians, True) if valid, or (0, False) if geometry is invalid.
    """
    try:
        cosine_value = (
            side_adjacent_1**2 + side_adjacent_2**2 - side_opposite**2
        ) / (2 * side_adjacent_1 * side_adjacent_2)

        # Clamp floating-point inaccuracies into the valid domain [-1.0, 1.0]
        cosine_value = max(-1.0, min(1.0, cosine_value))
        angle = acos(cosine_value)
        return angle, True
    except (ValueError, ZeroDivisionError):
        return 0, False


# -----------------------------------------------------------------------------
# Plotting Helper Functions
# -----------------------------------------------------------------------------

def plot_circle(center, radius):
    """Draw a full circle given its center (x, y) and radius."""
    center_x, center_y = center
    angles = np.linspace(0, 2 * pi, 500)
    x_coords = center_x + radius * np.cos(angles)
    y_coords = center_y + radius * np.sin(angles)
    plt.plot(x_coords, y_coords, color="navy", linestyle="--", alpha=0.6, label="Circumcircle")


def plot_line(point_1, point_2, **kwargs):
    """Draw a straight line segment connecting point_1 and point_2."""
    x1, y1 = point_1
    x2, y2 = point_2
    plt.plot([x1, x2], [y1, y2], **kwargs)


def label_point(name, point, offset=(0.2, 0.2)):
    """Add a text label with coordinates next to a point."""
    x, y = point
    plt.plot(x, y, marker="o", color="black", markersize=4)
    plt.text(
        x + offset[0],
        y + offset[1],
        f"{name} ({x:.2f}, {y:.2f})",
        fontsize=9,
        fontweight="medium"
    )


# -----------------------------------------------------------------------------
# Monte-Carlo Simulation Search
# -----------------------------------------------------------------------------
# We search for parameters 'a' (half the base length) and 'b' (side parameter)
# such that the 60-degree parallelogram ABCD places midpoint L on the
# circumcircle formed by points A, B, and K.

while True:
    a = uniform(2, 25)
    b = uniform(2, 25)

    # Parallelogram vertices where angle BAD = 60 degrees:
    # A is placed at the origin (0, 0)
    # B is along the x-axis at distance 2*a
    # D is at distance 2*b along a 60-degree heading: (2*b*cos(60), 2*b*sin(60)) = (b, b*sqrt(3))
    # C = B + D = (2*a + b, b*sqrt(3))
    A = (0.0, 0.0)
    B = (2 * a, 0.0)
    C = (2 * a + b, b * sqrt(3))
    D = (b, b * sqrt(3))

    # Midpoints of sides BC and CD
    K = mid_point(B, C)
    L = mid_point(D, C)

    # Unique circle defined by triangle ABK
    circle_center, circle_radius = define_circle_from_points(A, B, K)

    # Distance from point L to this circle
    dist_to_circle = distance_point_to_circle(circle_center, circle_radius, L)

    # If L lies on the circle within tolerance, ABKL is cyclic
    if dist_to_circle < 0.0001:
        break


# -----------------------------------------------------------------------------
# Visualization and Angle Calculation
# -----------------------------------------------------------------------------

plt.figure(figsize=(9, 8))

# Draw the circle passing through the cyclic quadrilateral vertices
plot_circle(circle_center, circle_radius)

# Draw parallelogram sides ABCD
plot_line(A, B, color="black", linewidth=1.5)
plot_line(B, C, color="black", linewidth=1.5)
plot_line(C, D, color="black", linewidth=1.5)
plot_line(D, A, color="black", linewidth=1.5)

# Draw cyclic quadrilateral connections and diagonal BD
plot_line(K, L, color="blue", linewidth=1.5)
plot_line(A, L, color="blue", linewidth=1.5)
plot_line(B, D, color="red", linestyle=":", linewidth=1.5, label="Diagonal BD")

# Shade the cyclic quadrilateral ABKL
poly_x = [A[0], B[0], K[0], L[0]]
poly_y = [A[1], B[1], K[1], L[1]]
plt.fill(poly_x, poly_y, color="lightblue", alpha=0.4, label="Cyclic Quad ABKL")

# Add coordinate labels to the image
label_point("A", A, offset=(-0.5, -0.7))
label_point("B", B, offset=(0.3, -0.6))
label_point("C", C, offset=(0.3, 0.2))
label_point("D", D, offset=(-2.5, 0.2))
label_point("K", K, offset=(0.3, 0.0))
label_point("L", L, offset=(-1.5, 0.4))

# Calculate angle ABD using the Law of Cosines on triangle ABD
side_ab = 2 * a
side_ad = 2 * b
side_bd = distance(B, D)
angle_abd_rad, _ = law_of_cosines(side_ab, side_bd, side_ad)
angle_abd_deg = degrees(angle_abd_rad)

# Set plot details
plt.title(f"Angle ABD = {angle_abd_deg:.3f}°", fontsize=13, pad=12)
plt.axis("equal")
plt.axis("off")
plt.legend(loc="upper left")
plt.tight_layout()

# Display the diagram
plt.show()
