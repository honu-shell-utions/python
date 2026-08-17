# -----------------------------------------------------------------------------
# Jim McCleery
# August 17, 2026
# Kailua-Kona, HI
#
# Problem source: https://mathnet.mit.edu/explorer.html?p=usa_2023_6e821b
#
# Problem Statement:
# Let ABCD be a convex quadrilateral such that ∠ABD = ∠BCD = 90°, and let M
# be the midpoint of segment BD. Suppose that CM = 2 and AM = 3. Compute AD.
# -----------------------------------------------------------------------------

from math import sqrt
import matplotlib.pyplot as plt


def distance(x1, y1, x2, y2):
    """Calculate the straight-line (Euclidean) distance between two points."""
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def plot_line(x1, y1, x2, y2, style="b-", linewidth=1.5):
    """Draw a line segment between (x1, y1) and (x2, y2)."""
    plt.plot([x1, x2], [y1, y2], style, linewidth=linewidth)


# -----------------------------------------------------------------------------
# Coordinate Setup:
# 1. In right triangle BCD (∠BCD = 90°), M is the midpoint of hypotenuse BD.
#    The median to the hypotenuse equals half the hypotenuse: BM = MD = CM = 2.
#    Therefore, the length of BD = 4.
# 2. Place B at the origin (0, 0) and D along the y-axis at (0, 4).
#    Midpoint M is at (0, 2).
# 3. Choose C at (2, 2) so that CM = 2 and ∠BCD = 90°.
# 4. Since ∠ABD = 90° and BD lies on the y-axis, segment AB lies on the x-axis.
#    With M = (0, 2) and AM = 3, we solve: x_A^2 + 2^2 = 3^2 -> x_A = sqrt(5).
# -----------------------------------------------------------------------------

# Define the coordinates of each point
points = {
    "B": (0, 0),
    "A": (sqrt(5), 0),
    "D": (0, 4),
    "M": (0, 2),
    "C": (2, 2),
}

# Unpack points into individual variables for plotting
xB, yB = points["B"]
xA, yA = points["A"]
xD, yD = points["D"]
xM, yM = points["M"]
xC, yC = points["C"]

# Set up the plot figure
plt.figure(figsize=(7, 7))

# Draw the quadrilateral sides ABCD
plot_line(xA, yA, xB, yB, style="b-")  # Side AB
plot_line(xB, yB, xC, yC, style="b-")  # Side BC
plot_line(xC, yC, xD, yD, style="b-")  # Side CD
plot_line(xA, yA, xD, yD, style="r--")  # Side AD (hypotenuse to solve for)

# Draw interior segments BD, CM, and AM
plot_line(xB, yB, xD, yD, style="gray", linewidth=1)  # Diagonal BD
plot_line(xM, yM, xC, yC, style="g--", linewidth=1.2)  # Median CM = 2
plot_line(xM, yM, xA, yA, style="m--", linewidth=1.2)  # Segment AM = 3

# Add point markers and text labels with coordinates
offsets = {
    "A": (0.1, -0.2),
    "B": (-0.4, -0.2),
    "C": (0.1, 0.1),
    "D": (-0.4, 0.1),
    "M": (-0.5, 0.0),
}

for name, (x, y) in points.items():
    plt.plot(x, y, "ko")  # Plot point marker
    dx, dy = offsets[name]
    plt.text(
        x + dx,
        y + dy,
        f"{name} ({x:.2f}, {y:.2f})",
        fontsize=10,
        fontweight="bold",
    )

# Calculate target distance AD
d_AD = distance(xA, yA, xD, yD)

# Finalize plot formatting
plt.title(f"Quadrilateral ABCD — Length AD = $\\sqrt{{21}} \\approx$ {d_AD:.5f}")
plt.axis("equal")
plt.axis("off")
plt.grid(True, linestyle=":", alpha=0.6)
plt.show()
