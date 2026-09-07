# Jim McCleery
# September 7, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2025_cb7af6

# -----------------------------------------------------------------------------
# USA Mathematical Talent Search geometry problem
#
# The large triangle ABC is equilateral with side length 11.
#
# D is on BC with BD = 7.
# Points E and F lie on AC and AB, respectively.
#
# The smaller triangle DFE has a right angle at D.
#
# This program uses trigonometry to determine the coordinates of E and F
# and then calculates the distance DE.
# -----------------------------------------------------------------------------

from math import pi, sqrt, atan, sin, cos
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """Return the straight-line distance between two points."""
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


# -----------------------------------------------------------------------------
def plot_line(point1, point2):
    """Draw a line segment between two points."""
    x1, y1 = point1
    x2, y2 = point2

    plt.plot([x1, x2], [y1, y2], color="black")


# -----------------------------------------------------------------------------
# Determine the angles and length needed to locate E and F.
#
# These formulas come from:
#   1. the Law of Sines
#   2. the side relationships in a 30-60-90 triangle

alpha = atan(5 / (3 * sqrt(3)))
beta = pi / 2 - alpha

a = 7 / (2 * sin(2 * pi / 3 - alpha))


# -----------------------------------------------------------------------------
# Coordinates of the equilateral triangle ABC.
#
# Put B at the origin and BC along the x-axis.
#
# Since ABC is equilateral and BC = 11:
#
#       A
#      / \
#     /   \
#    B-----C

B = (0, 0)
C = (11, 0)
A = (11 / 2, 11 * sqrt(3) / 2)


# -----------------------------------------------------------------------------
# D lies on BC and BD = 7.

D = (7, 0)


# -----------------------------------------------------------------------------
# Calculate the coordinates of F and E.
#
# F lies on side AB.
# E lies on side AC.

F = (
    7 + a * sqrt(3) * cos(pi - alpha),
    a * sqrt(3) * sin(pi - alpha)
)

E = (
    7 + a * cos(beta),
    a * sin(beta)
)


# -----------------------------------------------------------------------------
# Draw the large equilateral triangle ABC.

plot_line(A, B)
plot_line(B, C)
plot_line(C, A)


# Draw the smaller triangle DFE.

plot_line(D, F)
plot_line(F, E)
plot_line(E, D)


# -----------------------------------------------------------------------------
# Plot dots at the six important points.

points = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
    "F": F
}

for label, (x, y) in points.items():
    plt.plot(x, y, "ko")


# -----------------------------------------------------------------------------
# Add labels near each point.
#
# The small offsets keep the letters from sitting directly on top of the dots.

label_offsets = {
    "A": (0.00, 0.25),
    "B": (-0.35, -0.35),
    "C": (0.20, -0.35),
    "D": (-0.10, -0.40),
    "E": (0.20, 0.05),
    "F": (-0.45, 0.05)
}

for label, (x, y) in points.items():
    dx, dy = label_offsets[label]
    plt.text(x + dx, y + dy, label, fontsize=14)


# -----------------------------------------------------------------------------
# Finish the graph.

plt.title(f"The distance from D to E is {a:.5f}")

# Use the same scale on both axes so the geometry is not distorted.
plt.axis("equal")

# Hide the ordinary x- and y-axes.
plt.axis("off")

plt.show()
