# -----------------------------------------------------------------------------
# Jim McCleery
# August 14, 2026
# Kailua-Kona, HI
#
# Geometry Solver & Plotter
# Problem Source: https://mathnet.mit.edu/explorer.html?p=usa_2021_b47f86
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from math import acos, asin, cos, pi, sin, sqrt, tan

# =============================================================================
# HELPER FUNCTIONS
# =============================================================================

def distance(x1, y1, x2, y2):
    """
    Calculate the straight-line (Euclidean) distance between two points (x1, y1) and (x2, y2).
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def law_of_cosines(d1, d2, side):
    """
    Calculate the angle (in radians) opposite to 'side' in a triangle with side lengths d1, d2, and side.
    Formula: cos(theta) = (d1^2 + d2^2 - side^2) / (2 * d1 * d2)
    """
    try:
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except ValueError:
        return 0, False


def intersection_of_lines(m1, b1, m2, b2):
    """
    Find the intersection point (x, y) of two lines given in slope-intercept form (y = mx + b).
    """
    if m1 == m2:
        return 0, 0, False  # Lines are parallel and do not intersect at a single point
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y, True


def plot_line(x1, y1, x2, y2, color="black", linestyle="-"):
    """
    Draw a line segment connecting point (x1, y1) to point (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2], color=color, linestyle=linestyle)


def plot_circle(x, y, radius, color="gray", linestyle="--"):
    """
    Draw the circumference of a circle given its center (x, y) and radius.
    """
    angles = np.linspace(0, 2 * pi, 500)
    x_circle = radius * np.cos(angles) + x
    y_circle = radius * np.sin(angles) + y
    plt.plot(x_circle, y_circle, color=color, linestyle=linestyle)


# =============================================================================
# GEOMETRY COMPUTATIONS
# =============================================================================

# Step 1: Solve for angles and dimensions based on the problem statement
# Given: AO = R = 53 (circumradius), OM = 28, AM = 75
alpha, _ = law_of_cosines(53, 28, 75)

# Since OM is perpendicular to BC at midpoint M, triangle OMB is a right triangle:
# R^2 = OM^2 + (BC/2)^2 => (BC/2) = sqrt(53^2 - 28^2)
half_BC = sqrt(53**2 - 28**2)

# Find angle beta subtended by half of chord BC at the circumcenter
beta = asin(half_BC / 53)

# Angle gamma corresponds to the remaining angle around circumcenter O
gamma = 2 * pi - alpha - beta

# Compute side AB using the Law of Cosines
AB = sqrt(2 * (53**2) - 2 * (53**2) * cos(gamma))

# Step 2: Establish the Cartesian coordinates of all points
# O is placed at the origin (0, 0)
x_O, y_O = 0.0, 0.0

# Point A: Vertex A
x_A, y_A = -AB / 2, -AB / (2 * tan(gamma / 2))

# Point B: Vertex B
x_B, y_B = AB / 2, y_A

# Point C: Vertex C
x_C = x_B + 2 * half_BC * cos(gamma / 2 + beta)
y_C = y_B + 2 * half_BC * sin(gamma / 2 + beta)

# Point M: Midpoint of segment BC
x_M = x_B + half_BC * cos(gamma / 2 + beta)
y_M = y_B + half_BC * sin(gamma / 2 + beta)

# Step 3: Find point P
# P is an isogonal conjugate line intersection such that angle BAP = angle CAM and angle APO = 90 deg.
len_AC = distance(x_A, y_A, x_C, y_C)
len_AM = distance(x_A, y_A, x_M, y_M)
len_MC = half_BC

# Angle CAM in triangle ACM
angle_CAM, _ = law_of_cosines(len_AC, len_AM, len_MC)

# Line AP passes through A with slope determined by angle CAM
m1 = tan(angle_CAM)
b1 = y_A - m1 * x_A

# Line OP is perpendicular to AP and passes through O(0,0) (since angle APO = 90 deg)
m2 = -1 / m1
b2 = y_O - m2 * x_O

# Intersection of line AP and line OP gives the coordinates of point P
x_P, y_P, _ = intersection_of_lines(m1, b1, m2, b2)

# Step 4: Calculate the side lengths and perimeter of triangle BPC
side_PC = distance(x_C, y_C, x_P, y_P)
side_PB = distance(x_B, y_B, x_P, y_P)
side_BC = distance(x_B, y_B, x_C, y_C)

perimeter_BPC = side_PC + side_PB + side_BC

# =============================================================================
# PLOTTING AND LABELS
# =============================================================================

plt.figure(figsize=(9, 9))

# Draw the circumcircle (center O, radius 53)
plot_circle(x_O, y_O, 53, color="blue", linestyle=":")

# Draw triangle ABC
plot_line(x_A, y_A, x_B, y_B, color="black")  # Segment AB
plot_line(x_B, y_B, x_C, y_C, color="black")  # Segment BC
plot_line(x_C, y_C, x_A, y_A, color="black")  # Segment CA

# Draw median AM and reference line segments
plot_line(x_A, y_A, x_M, y_M, color="gray", linestyle="--")  # Median AM
plot_line(x_O, y_O, x_M, y_M, color="gray", linestyle="--")  # Distance OM
plot_line(x_A, y_A, x_P, y_P, color="orange", linestyle="--")  # Ray AP
plot_line(x_O, y_O, x_P, y_P, color="orange", linestyle="--")  # Ray OP (perpendicular to AP)

# Fill triangle BPC
plt.fill(
    [x_B, x_P, x_C],
    [y_B, y_P, y_C],
    color="red",
    alpha=0.35,
    edgecolor="red",
    linewidth=2,
    label=r"$\Delta BPC$",
)

# Plot and label all key points
points = {
    "A": (x_A, y_A, (-15, -15)),
    "B": (x_B, y_B, (10, -15)),
    "C": (x_C, y_C, (10, 10)),
    "M": (x_M, y_M, (12, 0)),
    "O": (x_O, y_O, (-15, 10)),
    "P": (x_P, y_P, (10, 5)),
}

for label, (px, py, offset) in points.items():
    plt.plot(px, py, "ko", markersize=5)
    plt.annotate(
        f"${label}$",
        (px, py),
        textcoords="offset points",
        xytext=offset,
        fontsize=12,
        fontweight="bold",
    )

# Formatting and layout
plt.title(
    f"Perimeter of $\\Delta BPC$ = {perimeter_BPC:0.3f}",
    fontsize=14,
    pad=15,
)
plt.axis("equal")
plt.axis("off")
plt.legend(loc="upper left")
plt.tight_layout()
plt.show()
