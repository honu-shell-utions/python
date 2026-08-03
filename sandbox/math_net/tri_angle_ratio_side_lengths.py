# -----------------------------------------------------------------------------
# Jim McCleery
# August 3, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2021_71b8b2
# -----------------------------------------------------------------------------

from math import pi, sin, cos, sqrt
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------

def distance(x1, y1, x2, y2):
    """
    Calculates the Euclidean (straight-line) distance between two points (x1, y1) and (x2, y2).
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def plot_line(x1, y1, x2, y2):
    """
    Plots a line segment connecting point (x1, y1) to point (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2], color="blue")


# -----------------------------------------------------------------------------
# Main Program
# -----------------------------------------------------------------------------

# 'theta' represents angle C in radians, solved using the Law of Sines
theta = 0.7648297750183206778

# Define vertex coordinates for triangle ABC:
# Vertex A is placed at the origin (0, 0)
x_a, y_a = 0.0, 0.0

# Vertex C is placed at (6, 0) so that side AC = 6
x_c, y_c = 6.0, 0.0

# Vertex B is placed relative to C at distance BC = 8
x_b, y_b = 6.0 + 8.0 * cos(pi - theta), 8.0 * sin(pi - theta)

# Calculate the approximate length of side AB (distance from A to B)
AB_approx = distance(x_a, y_a, x_b, y_b)

# Plot the three side segments forming triangle ABC
plot_line(x_a, y_a, x_b, y_b)  # Side AB
plot_line(x_b, y_b, x_c, y_c)  # Side BC (length 8)
plot_line(x_c, y_c, x_a, y_a)  # Side CA (length 6)

# Label the coordinate vertices (A, B, C) on the plot
plt.text(x_a - 0.3, y_a - 0.3, "A", fontsize=12, fontweight="bold")
plt.text(x_b - 0.1, y_b + 0.2, "B", fontsize=12, fontweight="bold")
plt.text(x_c + 0.1, y_c - 0.3, "C", fontsize=12, fontweight="bold")

# Numerically solve for positive integers 'a' and 'b' such that AB = sqrt(a) - b
b = 0
while True:
    b += 1
    a = int(AB_approx**2 + 2 * b * AB_approx + b**2)
    if abs(sqrt(a) - b - AB_approx) < 0.0000000001:
        break

# Display the final computed result (100a + b = 7303)
plt.title(f"100a+b is {round(100 * a + b)}")
plt.axis("equal")
plt.axis("off")
plt.show()
