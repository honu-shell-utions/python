"""
Jim McCleery
May 2, 2026
Kailua-Kona, HI

Geometry diagram inspired by:
https://youtu.be/Ah4jqBgWkgA?si=snCM1aPm0IbX-FWo
"""

from math import acos, atan2, cos, degrees, pi, sin, sqrt

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Wedge


# ---------------------------------------------------------------------
# Geometry utility functions
# ---------------------------------------------------------------------
def distance(point_a, point_b):
    """Return the Euclidean distance between two points."""
    x1, y1 = point_a
    x2, y2 = point_b
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def law_of_cosines(side_a, side_b, opposite_side):
    """
    Return the angle opposite `opposite_side`.

    The three side lengths form a triangle with sides:
        side_a, side_b, opposite_side
    """
    numerator = side_a**2 + side_b**2 - opposite_side**2
    denominator = 2 * side_a * side_b
    cosine_value = numerator / denominator

    # Protect against small floating-point roundoff errors.
    cosine_value = max(-1.0, min(1.0, cosine_value))

    return acos(cosine_value)


def plot_line(ax, point_a, point_b, color="black", linewidth=2):
    """Draw a line segment between two points."""
    x1, y1 = point_a
    x2, y2 = point_b
    ax.plot([x1, x2], [y1, y2], color=color, linewidth=linewidth)


def plot_circle_arc(ax, center, radius, start_angle=0, stop_angle=2 * pi, color="black"):
    """Draw a circle or circular arc."""
    center_x, center_y = center
    angles = np.linspace(start_angle, stop_angle, 500)
    x_values = center_x + radius * np.cos(angles)
    y_values = center_y + radius * np.sin(angles)
    ax.plot(x_values, y_values, color=color, linewidth=2)


def label_point(ax, point, label, dx=0.08, dy=0.08):
    """Plot and label a point."""
    x, y = point
    ax.scatter(x, y, color="black", s=25, zorder=5)
    ax.text(x + dx, y + dy, label, fontsize=12, fontweight="bold")


def draw_angle(ax, vertex, point_a, point_b, radius=0.45,
               facecolor="gold", edgecolor="darkorange", alpha=0.5,
               label=r"$\theta$"):
    """
    Highlight the smaller angle formed by vertex->point_a and vertex->point_b.

    A filled wedge is used so the angle is easy to see.
    """
    vx, vy = vertex
    ax1, ay1 = point_a
    bx1, by1 = point_b

    angle1 = degrees(atan2(ay1 - vy, ax1 - vx)) % 360
    angle2 = degrees(atan2(by1 - vy, bx1 - vx)) % 360

    # Use the smaller of the two possible angles.
    delta = (angle2 - angle1) % 360
    if delta > 180:
        angle1, angle2 = angle2, angle1
        delta = (angle2 - angle1) % 360

    wedge = Wedge(
        center=vertex,
        r=radius,
        theta1=angle1,
        theta2=angle1 + delta,
        facecolor=facecolor,
        edgecolor=edgecolor,
        linewidth=2,
        alpha=alpha,
        zorder=2,
    )
    ax.add_patch(wedge)

    # Place the theta label near the middle of the colored angle.
    mid_angle = np.radians(angle1 + delta / 2)
    label_radius = radius * 1.35
    label_x = vx + label_radius * np.cos(mid_angle)
    label_y = vy + label_radius * np.sin(mid_angle)
    ax.text(label_x, label_y, label, fontsize=14, color="darkred", fontweight="bold")


# ---------------------------------------------------------------------
# Construct the diagram
# ---------------------------------------------------------------------

# Base points
A = (0, 0)
B = (2, 0)
C = (5, 0)

# The angle alpha comes from a 3-4-5 triangle.
alpha = law_of_cosines(3, 5, 4)

# Points determined by alpha
D = (3 * cos(alpha), 3 * sin(alpha))
E = (2 * cos(alpha), 2 * sin(alpha))
F = (C[0] + 3 * cos(pi / 2 + alpha), 3 * sin(pi / 2 + alpha))

# Upper endpoints of the two outer sides
G = (0, 2)
H = (5, 3)

# Compute theta from triangle B-E-F.
BE = distance(B, E)
BF = distance(B, F)
EF = distance(E, F)

theta = law_of_cosines(BE, BF, EF)


# ---------------------------------------------------------------------
# Create the figure
# ---------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))

# Outer frame
plot_line(ax, A, C)
plot_line(ax, A, G)
plot_line(ax, C, H)

# Large interior triangle
plot_line(ax, A, D)
plot_line(ax, C, D)

# Smaller interior triangle
plot_line(ax, B, E)
plot_line(ax, B, F)
plot_line(ax, E, F)

# Circular arcs
plot_circle_arc(ax, A, 2, 0, pi / 2)
plot_circle_arc(ax, D, 1)
plot_circle_arc(ax, C, 3, pi / 2, pi)

# Highlight angle theta at vertex B
draw_angle(ax, B, E, F, radius=0.5)

# Label vertices
vertices = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
    "F": F,
    "G": G,
    "H": H,
}

for label, point in vertices.items():
    label_point(ax, point, label)

# Final formatting
ax.set_title(f"Angle theta = {degrees(theta):.2f} degrees")
ax.axis("equal")
ax.grid(True, alpha=0.25)

plt.show()
