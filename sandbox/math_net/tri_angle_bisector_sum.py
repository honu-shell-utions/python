# -----------------------------------------------------------------------------
# Jim McCleery
# September 30, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=btw_1999_ed0c12
# -----------------------------------------------------------------------------

from math import pi, sqrt, sin, cos, degrees
from random import uniform
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Core Geometric Functions
# -----------------------------------------------------------------------------


def distance(A, B):
    """Calculate the straight-line distance between two points A and B.

    A and B are tuples formatted as (x, y).
    """
    x1, y1 = A
    x2, y2 = B
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def line_intersection_from_points(A, B, C, D):
    """Find the intersection point of two lines.

    Line 1 passes through points A and B.
    Line 2 passes through points C and D.
    Returns ((x, y), True) if an intersection exists, or ((0, 0), False) if
    parallel.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D

    try:
        # Calculate the slopes of both lines (rise / run)
        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y4 - y3) / (x4 - x3)

        # Solve for the x-coordinate where both line equations meet
        x = (y1 - slope1 * x1 - y3 + slope2 * x3) / (slope2 - slope1)
        # Substitute x back into the equation of the first line to get y
        y = y1 + slope1 * (x - x1)

        return (x, y), True

    except ZeroDivisionError:
        # Occurs if either line is vertical or if the two lines are parallel
        return (0, 0), False


def plot_line(A, B, color="black", linestyle="-", linewidth=1.5):
    """Draw a line segment between points A and B."""
    x1, y1 = A
    x2, y2 = B
    plt.plot([x1, x2], [y1, y2], color=color, linestyle=linestyle, linewidth=linewidth)


# -----------------------------------------------------------------------------
# Main Simulation Loop
# -----------------------------------------------------------------------------

# Search for triangle parameters where |AE| + |BD| == |AB|
while True:
    # 1. Randomly choose base side length AB and two interior base angles
    AB = uniform(5, 20)
    alpha = uniform(0.2, pi / 2)  # Angle at vertex A
    beta = uniform(0.2, pi / 2)  # Angle at vertex B
    gamma = pi - alpha - beta  # Angle at vertex C

    if gamma <= 0:
        continue

    # 2. Use the Law of Sines to determine the length of side AC:
    #    AC / sin(beta) = AB / sin(gamma)  -->  AC = AB * sin(beta) / sin(gamma)
    AC = AB * sin(beta) / sin(gamma)

    # 3. Define the Cartesian coordinates of vertices A, B, and C:
    A = (0.0, 0.0)  # Place vertex A at the origin
    B = (AB, 0.0)  # Place vertex B along the x-axis
    C = (AC * cos(alpha), AC * sin(alpha))  # Vertex C from polar coordinates

    # 4. Define directional helper points for angle bisectors:
    #    - Ray AF splits angle alpha in half at vertex A
    #    - Ray BG splits angle beta in half pointing inward from vertex B
    F = (cos(alpha / 2), sin(alpha / 2))
    G = (AB + cos(pi - beta / 2), sin(pi - beta / 2))

    # 5. Compute the intersection points:
    #    - D is where the bisector from A meets side BC
    #    - E is where the bisector from B meets side AC
    D, ok1 = line_intersection_from_points(A, F, B, C)
    E, ok2 = line_intersection_from_points(A, C, B, G)

    if not (ok1 and ok2):
        continue

    # 6. Check the condition: |AE| + |BD| == |AB|
    d = distance(A, E) + distance(B, D)
    if abs(d - AB) < 0.001:
        break

# -----------------------------------------------------------------------------
# Visualization
# -----------------------------------------------------------------------------

# Plot the triangle sides
plot_line(A, B, color="black", linewidth=2)
plot_line(B, C, color="black", linewidth=2)
plot_line(A, C, color="black", linewidth=2)

# Plot the internal angle bisectors
plot_line(A, D, color="crimson", linestyle="--", linewidth=1.5)
plot_line(B, E, color="navy", linestyle="--", linewidth=1.5)

# Coordinate labels and points
points = {"A": A, "B": B, "C": C, "D": D, "E": E}
offsets = {
    "A": (-0.6, -0.6),
    "B": (0.3, -0.6),
    "C": (0.0, 0.5),
    "D": (0.4, 0.2),
    "E": (-0.6, 0.2),
}

for label, pt in points.items():
    # Draw point marker
    plt.plot(pt[0], pt[1], "o", color="black", markersize=5)
    # Add coordinate label
    dx, dy = offsets[label]
    plt.text(
        pt[0] + dx,
        pt[1] + dy,
        f"{label} ({pt[0]:.2f}, {pt[1]:.2f})",
        fontsize=10,
        weight="bold",
    )

plt.title(f"Angle ACB = {degrees(gamma):0.1f} degrees.")
plt.axis("equal")
plt.axis("off")
plt.tight_layout()
plt.show()
