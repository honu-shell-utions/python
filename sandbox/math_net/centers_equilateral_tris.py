# -----------------------------------------------------------------------------
# Jim McCleery
# September 10, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_b63ed1
# -----------------------------------------------------------------------------

from math import pi, sqrt, cos, sin, acos
from random import uniform
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# GEOMETRIC HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def law_of_cosines(d1, d2, side):
    """
    Find the angle opposite 'side' in a triangle with side lengths d1, d2, and side.
    Formula: cos(angle) = (d1^2 + d2^2 - side^2) / (2 * d1 * d2)
    
    Returns:
        (angle_in_radians, True) if the side lengths form a valid triangle
        (0, False) if the geometry is invalid
    """
    try:
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        # acos requires values strictly in range [-1, 1]
        return acos(temp), True
    except (ValueError, ZeroDivisionError):
        return 0, False


def circle_through_points(point_a, point_b, point_c):
    """
    Calculate the center (x0, y0) and radius (r0) of the unique circle
    passing through three non-collinear points: point_a, point_b, and point_c.
    
    Returns:
        (x0, y0, r0, True) if circle exists
        (0, 0, 0, False) if points are collinear or invalid
    """
    x1, y1 = point_a
    x2, y2 = point_b
    x3, y3 = point_c

    try:
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2

        # Determinant equations to solve for the circumcenter
        M11 = x1 * y2 + x2 * y3 + x3 * y1 - (x2 * y1 + x3 * y2 + x1 * y3)
        M12 = s1 * y2 + s2 * y3 + s3 * y1 - (s2 * y1 + s3 * y2 + s1 * y3)
        M13 = s1 * x2 + s2 * x3 + s3 * x1 - (s2 * x1 + s3 * x2 + s1 * x3)

        center_x = 0.5 * M12 / M11
        center_y = -0.5 * M13 / M11
        radius = sqrt((x1 - center_x)**2 + (y1 - center_y)**2)
        return center_x, center_y, radius, True
    except ZeroDivisionError:
        return 0, 0, 0, False


# -----------------------------------------------------------------------------
# PLOTTING HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def plot_line(point1, point2, color='tab:blue', linewidth=1.5):
    """Draw a straight line segment between two (x, y) points."""
    x1, y1 = point1
    x2, y2 = point2
    plt.plot([x1, x2], [y1, y2], color=color, linewidth=linewidth)


def plot_circle(cx, cy, radius, color='tab:blue', linestyle='--'):
    """Draw a circle given its center (cx, cy) and radius."""
    angles = np.linspace(0, 2 * pi, 500)
    x_coords = radius * np.cos(angles) + cx
    y_coords = radius * np.sin(angles) + cy
    plt.plot(x_coords, y_coords, color=color, linestyle=linestyle)


def polygon_fill_coordinates(vertices):
    """
    Close a polygon loop by repeating the first vertex at the end,
    then return separated lists of x and y coordinates for filling.
    """
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords


def label_point(pt, label, offset=(0.2, 0.2)):
    """Plot a dot at the point and display its text label nearby."""
    plt.plot(pt[0], pt[1], 'o', color='#333333', markersize=5)
    plt.text(pt[0] + offset[0], pt[1] + offset[1], label, fontsize=11, fontweight='bold')


# -----------------------------------------------------------------------------
# MAIN ANIMATION / SIMULATION LOOP
# -----------------------------------------------------------------------------

# Run 100 random triangle demonstrations
for _ in range(100):
    plt.cla()  # Clear current plot axes for the next animation frame

    # Pick three random side lengths between 5 and 10
    side1 = uniform(5, 10)
    side2 = uniform(5, 10)
    side3 = uniform(5, 10)

    # Compute interior angles using the Law of Cosines
    alpha, ok1 = law_of_cosines(side1, side3, side2)
    beta, ok2 = law_of_cosines(side1, side2, side3)
    if not (ok1 and ok2):
        continue  # Skip invalid triangle configurations (violating triangle inequality)

    # Coordinates of the base triangle vertices
    A = (0, 0)
    B = (side1, 0)
    C = (side3 * cos(alpha), side3 * sin(alpha))

    # Outer equilateral triangle tips (erected on each side)
    D = (side1 + side1 * cos(4 * pi / 3), side1 * sin(4 * pi / 3))
    E = (side1 + side2 * cos(2 * pi / 3 - beta), side2 * sin(2 * pi / 3 - beta))
    F = (side3 * cos(pi / 3 + alpha), side3 * sin(pi / 3 + alpha))

    # Outer Napoleon centers
    G = (side1 / 2, -side1 / (2 * sqrt(3)))
    H = (side1 + (side2 / sqrt(3)) * cos(5 * pi / 6 - beta), (side2 / sqrt(3)) * sin(5 * pi / 6 - beta))
    I = ((side3 / sqrt(3)) * cos(alpha + pi / 6), (side3 / sqrt(3)) * sin(alpha + pi / 6))

    # Inner Napoleon centers
    Gp = (side1 / 2, side1 / (2 * sqrt(3)))
    Hp = (side1 + (side2 / sqrt(3)) * cos(7 * pi / 6 - beta), (side2 / sqrt(3)) * sin(7 * pi / 6 - beta))
    Ip = ((side3 / sqrt(3)) * cos(alpha - pi / 6), (side3 / sqrt(3)) * sin(alpha - pi / 6))

    # 1. Draw outer equilateral triangles
    plot_line(A, D)
    plot_line(B, D)
    plot_line(E, B)
    plot_line(E, C)
    plot_line(C, F)
    plot_line(A, F)

    # 2. Draw base triangle ABC
    plot_line(A, B, color='navy', linewidth=2)
    plot_line(C, B, color='navy', linewidth=2)
    plot_line(A, C, color='navy', linewidth=2)

    # 3. Draw and fill outer Napoleon triangle (G, H, I)
    plot_line(H, I, color='steelblue')
    plot_line(H, G, color='steelblue')
    plot_line(G, I, color='steelblue')
    outer_verts = [I, H, G]
    plt.fill(*polygon_fill_coordinates(outer_verts), color='lightblue', alpha=0.4)

    # 4. Draw and fill inner Napoleon triangle (G', H', I')
    plot_line(Hp, Ip, color='red')
    plot_line(Hp, Gp, color='red')
    plot_line(Gp, Ip, color='red')
    inner_verts = [Ip, Hp, Gp]
    plt.fill(*polygon_fill_coordinates(inner_verts), color='pink', alpha=0.4)

    # 5. Calculate and draw circumcircles
    x1, y1, r1, _ = circle_through_points(G, H, I)
    x2, y2, r2, _ = circle_through_points(Gp, Hp, Ip)
    plot_circle(x1, y1, r1, color='lightblue', linestyle='--')
    plot_circle(x2, y2, r2, color='red', linestyle='--')

    # 6. Add point coordinate labels from the diagram
    labels = {
        'A': (A, (-0.2, 0.3)),
        'B': (B, (-0.4, -0.4)),
        'C': (C, (0.2, -0.2)),
        'D': (D, (-0.5, 0.1)),
        'F': (F, (0.1, -0.4)),
        'G': (G, (-0.4, 0.1)),
        'H': (H, (0.1, 0.2)),
        'I': (I, (0.1, -0.4)),
        "G'": (Gp, (-0.5, 0.1)),
        "H'": (Hp, (0.1, -0.3)),
        "I'": (Ip, (-0.4, 0.2)),
    }
    for lbl, (pt, offset) in labels.items():
        label_point(pt, lbl, offset=offset)

    # Configure plot view
    plt.title(f'Circumcenters: Outer=({x1:0.2f}, {y1:0.2f}), Inner=({x2:0.2f}, {y2:0.2f})')
    plt.axis('off')
    plt.axis('equal')
    plt.pause(1.5)

plt.show()
