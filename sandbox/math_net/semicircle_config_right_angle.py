# -----------------------------------------------------------------------------
# Jim McCleery
# August 16, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2001_265cfd
# -----------------------------------------------------------------------------

from math import pi, sqrt
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2, style="b-"):
    """Draw a straight line segment connecting two points (x1, y1) and (x2, y2)."""
    plt.plot([x1, x2], [y1, y2], style)


def plot_circle_arc(cx, cy, radius, start_angle=0, end_angle=pi):
    """Draw a circular arc centered at (cx, cy) from start_angle to end_angle (in radians)."""
    # Generate 500 evenly spaced angle values
    angles = np.linspace(start_angle, end_angle, 500)
    # Calculate corresponding x and y positions using trigonometry
    x_vals = cx + radius * np.cos(angles)
    y_vals = cy + radius * np.sin(angles)
    plt.plot(x_vals, y_vals, "b-")


def line_intersection_from_points(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Find the intersection point (x, y) of two lines:
      Line 1 passes through (x1, y1) and (x2, y2)
      Line 2 passes through (x3, y3) and (x4, y4)
    """
    m1 = (y2 - y1) / (x2 - x1)  # Slope of line 1
    m2 = (y4 - y3) / (x4 - x3)  # Slope of line 2

    # Solve for x where both line equations intersect: y1 + m1*(x - x1) = y3 + m2*(x - x3)
    x = (y1 - m1 * x1 - y3 + m2 * x3) / (m2 - m1)
    y = y1 + m1 * (x - x1)
    return x, y


# -----------------------------------------------------------------------------
# Geometry Calculations
# -----------------------------------------------------------------------------
# Given segment lengths from the problem statement
DF = (2 * sqrt(5) - sqrt(10)) / 4
BF = (2 - sqrt(2)) / 4

# In the right triangle FBD, BD = sqrt(DF^2 - BF^2)
a = sqrt(DF**2 - BF**2)  # Distance BD
b = 1.0 - a  # Distance AB (x-coordinate of B and E)
c = sqrt(1.0 - b**2)  # Height of E above the x-axis (since radius EA = 1)
de = sqrt(a**2 + c**2)  # Length of segment DE by the Pythagorean theorem

# Define coordinates for key points:
A = (0.0, 0.0)  # Center of the semicircle
D = (1.0, 0.0)  # Rightmost point of the base
B = (b, 0.0)  # Point on base segment AD
E = (b, c)  # Point on the semicircle arc (EBA forms a right angle)
F = (b, -BF)  # Point extending downward along line EB

# Point C is the intersection of line EA extended through A and line DF extended through F
C_x, C_y = line_intersection_from_points(A[0], A[1], E[0], E[1], D[0], D[1], F[0], F[1])
C = (C_x, C_y)

# -----------------------------------------------------------------------------
# Plotting the Geometric Figure
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))

# 1. Draw the semicircle arc and the diameter base line
plot_circle_arc(A[0], A[1], radius=1.0, start_angle=0, end_angle=pi)
plot_line(-1.0, 0.0, 1.0, 0.0)  # Base line of the semicircle

# 2. Draw line segments connecting the geometric points
plot_line(E[0], E[1], F[0], F[1])  # Line segment E-B-F
plot_line(E[0], E[1], C[0], C[1])  # Line segment extending from E through A to C
plot_line(D[0], D[1], C[0], C[1])  # Line segment from D through F to C
plot_line(E[0], E[1], D[0], D[1], style="r--")  # Segment DE (the target length)

# 3. Mark points with red dots
points = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F}
for label, (px, py) in points.items():
    ax.plot(px, py, "ro")

# 4. Add text labels for each point with slight offsets for readability
ax.text(A[0] - 0.06, A[1] + 0.04, "A", fontsize=12, fontweight="bold")
ax.text(B[0] + 0.03, B[1] + 0.04, "B", fontsize=12, fontweight="bold")
ax.text(C[0] - 0.08, C[1] - 0.06, "C", fontsize=12, fontweight="bold")
ax.text(D[0] + 0.04, D[1] + 0.02, "D", fontsize=12, fontweight="bold")
ax.text(E[0] + 0.02, E[1] + 0.04, "E", fontsize=12, fontweight="bold")
ax.text(F[0] + 0.04, F[1] - 0.03, "F", fontsize=12, fontweight="bold")

# 5. Figure styling
ax.set_aspect("equal")
ax.axis("off")
plt.title(f"The length of DE is {de:.6f}", fontsize=14)

plt.show()
