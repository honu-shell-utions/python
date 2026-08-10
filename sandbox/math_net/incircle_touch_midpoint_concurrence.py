# -----------------------------------------------------------------------------
# Jim McCleery
# August 10, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_5517ae
# -----------------------------------------------------------------------------

from math import acos, cos, pi, sin, sqrt, tan
from random import uniform
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# GEOMETRY UTILITY FUNCTIONS
# -----------------------------------------------------------------------------


def distance(x1, y1, x2, y2):
    """Calculate the Euclidean distance between two points (x1, y1) and (x2, y2)."""
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def law_of_cosines(d1, d2, side):
    """
    Calculate the angle (in radians) opposite to 'side' in a triangle
    with side lengths d1, d2, and side. Returns (angle, True) if valid,
    or (0, False) if the triangle inequality is violated.
    """
    try:
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except ValueError:
        return 0, False


def incircle_of_triangle(x1, y1, x2, y2, x3, y3):
    """
    Calculate the incenter (center of the inside circle) and inradius
    for a triangle defined by three vertices.
    """
    a = distance(x2, y2, x3, y3)
    b = distance(x1, y1, x3, y3)
    c = distance(x1, y1, x2, y2)

    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    inradius = area / s

    # Weighted average of vertices gives the incenter coordinates
    incenter_x = (a * x1 + b * x2 + c * x3) / (a + b + c)
    incenter_y = (a * y1 + b * y2 + c * y3) / (a + b + c)

    return incenter_x, incenter_y, inradius


def intersection_of_lines(m1, b1, m2, b2):
    """
    Find the intersection point (x, y) of two lines given in y = m*x + b form.
    Returns (x, y, True) if they intersect, or (0, 0, False) if parallel.
    """
    if m1 == m2:
        return 0, 0, False
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y, True


def line_intersection_from_points(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Find the intersection point of two lines defined by points (P1-P2) and (P3-P4).
    """
    try:
        m1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - m1 * x1
        m2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - m2 * x3
        x, y, ok = intersection_of_lines(m1, b1, m2, b2)
        if not ok:
            return 0, 0, False
        return x, y, True
    except ZeroDivisionError:
        return 0, 0, False


# -----------------------------------------------------------------------------
# PLOTTING HELPERS
# -----------------------------------------------------------------------------


def plot_circle(x, y, radius, num_points=200):
    """Draw a circle centered at (x, y) with a given radius."""
    angles = [i * (2 * pi / num_points) for i in range(num_points + 1)]
    x_vals = [x + radius * cos(a) for a in angles]
    y_vals = [y + radius * sin(a) for a in angles]
    plt.plot(x_vals, y_vals, "r--")


def plot_line(x1, y1, x2, y2, style="k-"):
    """Draw a line segment between two points."""
    plt.plot([x1, x2], [y1, y2], style)


# -----------------------------------------------------------------------------
# MAIN SIMULATION / DEMONSTRATION
# -----------------------------------------------------------------------------

# Generate random triangles to verify the geometric theorem: BD = CE
for _ in range(100):
    plt.cla()
    
    # Generate three random side lengths
    a = uniform(5, 15)
    b = uniform(5, 15)
    c = uniform(5, 15)

    # Calculate angle at vertex B using the Law of Cosines
    angle_B, ok = law_of_cosines(c, a, b)
    if not ok:
        continue  # Skip invalid triangle combinations

    # Set coordinates for Vertices B, C, and A:
    # B is placed at the origin (0, 0)
    # C is along the x-axis at (a, 0)
    # A is positioned using trigonometry based on side length c and angle B
    xB, yB = 0.0, 0.0
    xC, yC = a, 0.0
    xA, yA = c * cos(angle_B), c * sin(angle_B)

    # Compute the incenter I(xI, yI) and inradius r
    xI, yI, r = incircle_of_triangle(xA, yA, xB, yB, xC, yC)

    # Point D: Point of tangency of the incircle on side BC (y = 0)
    xD, yD = xI, 0.0

    # Point M: Midpoint of the altitude from vertex A to side BC
    # Altitude foot on BC is at (xA, 0), so midpoint is (xA, yA / 2)
    xM, yM = xA, yA / 2.0

    # Point E: Intersection of line MI and line BC
    xE, yE, valid_E = line_intersection_from_points(
        xM, yM, xI, yI, xB, yB, xC, yC
    )

    if not valid_E:
        continue

    # Calculate distances BD and CE
    BD = distance(xB, yB, xD, yD)
    CE = distance(xC, yC, xE, yE)

    # Clear plot for current iteration
    plt.clf()

    # Draw triangle ABC sides
    plot_line(xB, yB, xC, yC, "k-")  # Side BC
    plot_line(xC, yC, xA, yA, "k-")  # Side CA
    plot_line(xA, yA, xB, yB, "k-")  # Side AB

    # Draw incircle
    plot_circle(xI, yI, r)

    # Draw line MI extended through E
    plot_line(xM, yM, xE, yE, "g--")

    # Draw altitude segment for context
    plot_line(xA, yA, xA, 0, "b:")

    # Add Coordinate Labels based on the problem statement
    plt.text(xA, yA + 0.3, "A", fontsize=12, fontweight="bold", ha="center")
    plt.text(xB - 0.3, yB - 0.3, "B", fontsize=12, fontweight="bold")
    plt.text(xC + 0.3, yC - 0.3, "C", fontsize=12, fontweight="bold")
    plt.text(xI, yI + 0.3, "I", fontsize=12, fontweight="bold")
    plt.text(xD, yD - 0.5, "D", fontsize=12, fontweight="bold", ha="center")
    plt.text(xM + 0.2, yM, "M", fontsize=12, fontweight="bold")
    plt.text(xE, yE - 0.5, "E", fontsize=12, fontweight="bold", ha="center")

    # Adjust view and display settings
    plt.axis("off")
    plt.axis("equal")
    plt.title(
        f"Theorem Verification: BD = {BD:.4f}, CE = {CE:.4f}", fontsize=11
    )
    plt.pause(1.5)
plt.show()
