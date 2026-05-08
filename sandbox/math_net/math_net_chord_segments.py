"""
Jim McCleery
May 8, 2026
Kailua-Kona, HI

Product of Chord Segments in Nested Semicircles

A semicircle S1 is inscribed in semicircle S2, which is inscribed in
semicircle S3. The radii of S1 and S3 are 1 and 10, respectively, and
the diameters of S1 and S3 are parallel.

The endpoints of the diameter of S3 are A and B, and S2's arc is tangent
to AB at C. This program draws the configuration and computes AC * CB.

Python solution to:
https://mathnet.mit.edu/explorer.html?p=usa_2025_8ccef2
"""

from math import atan2, pi, sqrt

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Basic drawing utilities
# -----------------------------------------------------------------------------

def plot_arc(center, radius, start_angle, stop_angle, label=None):
    """
    Plot a circular arc.

    Angles are measured in radians from the positive x-axis.
    """
    theta = np.linspace(start_angle, stop_angle, 800)
    x_values = center[0] + radius * np.cos(theta)
    y_values = center[1] + radius * np.sin(theta)

    plt.plot(x_values, y_values, label=label)


def plot_segment(point1, point2, style="k-", linewidth=1.5):
    """
    Plot a line segment between two points.
    """
    plt.plot(
        [point1[0], point2[0]],
        [point1[1], point2[1]],
        style,
        linewidth=linewidth,
    )


def label_point(name, point, dx=0.15, dy=0.15):
    """
    Label a point on the diagram.
    """
    plt.scatter(point[0], point[1], color="black", s=20)
    plt.text(point[0] + dx, point[1] + dy, name, fontsize=12)


# -----------------------------------------------------------------------------
# Geometry of the problem
# -----------------------------------------------------------------------------

R3 = 10       # Radius of the largest semicircle S3
R1 = 1        # Radius of the smallest semicircle S1

# Put the largest semicircle S3 on diameter AB.
O3 = (0, 0)
A = (-R3, 0)
B = (R3, 0)

# From the geometry of the nested semicircles:
#
#   C = (x, 0)
#
# The answer is:
#
#   AC * CB = (10 + x)(10 - x) = 100 - x^2
#
# The configuration gives x^2 = 80, so AC * CB = 20.
C_x = sqrt(80)
C = (C_x, 0)

answer = (C_x - A[0]) * (B[0] - C_x)

# The center of S2 is directly above C because S2 is tangent to AB at C.
R2 = sqrt(10)
O2 = (C_x, R2)

# The center of S1 is also above C.  Since S1 has radius 1 and its
# diameter is horizontal, its center is:
O1 = (C_x, R2 - 3)

# Diameter endpoints of the smallest semicircle S1.
D = (O1[0] - R1, O1[1])
E = (O1[0] + R1, O1[1])

# The diameter of S2 is a chord of S3.  It is the radical axis of S2 and S3.
# Its equation is:
#
#   C_x * X + R2 * Y = C_x^2 + R2^2
#
# A direction vector along this line is perpendicular to (C_x, R2).
direction = np.array([R2, -C_x], dtype=float)
direction = direction / np.linalg.norm(direction)

# The endpoints F and G of S2's diameter are one radius R2 away from O2.
F = tuple(np.array(O2) - R2 * direction)
G = tuple(np.array(O2) + R2 * direction)

# Determine the angular interval for drawing the semicircle S2.
angle_F = atan2(F[1] - O2[1], F[0] - O2[0])
angle_G = atan2(G[1] - O2[1], G[0] - O2[0])

# -----------------------------------------------------------------------------
# Draw the figure
# -----------------------------------------------------------------------------

plt.figure(figsize=(9, 5))

# Semicircle S3
plot_arc(O3, R3, 0, pi, label="S3")

# Semicircle S1, whose diameter is DE
plot_arc(O1, R1, 0, pi, label="S1")

# Semicircle S2.  The relevant arc is the arc through C.
plot_arc(O2, R2, angle_F, angle_G + 2 * pi, label="S2")

# Diameters and chords
plot_segment(A, B, linewidth=2.0)        # Diameter AB of S3
plot_segment(D, E, "k-", linewidth=2.0)  # Diameter DE of S1
plot_segment(F, G, "k-", linewidth=2.0)  # Diameter FG of S2

# Label key vertices
label_point("A", A, dx=-0.6, dy=-0.45)
label_point("B", B, dx=0.25, dy=-0.45)
label_point("C", C, dx=0.15, dy=-0.45)

label_point("D", D, dx=-0.45, dy=0.15)
label_point("E", E, dx=0.15, dy=0.15)

label_point("F", F, dx=-0.6, dy=0.15)
label_point("G", G, dx=0.15, dy=0.15)

# Label centers lightly
label_point("O1", O1, dx=0.15, dy=0.15)
label_point("O2", O2, dx=0.15, dy=0.15)
label_point("O3", O3, dx=0.15, dy=-0.45)

plt.title(f"Nested Semicircles:  AC × CB = {answer:.0f}")
plt.axis("equal")
plt.grid(True, alpha=0.3)
plt.legend()
plt.show()
