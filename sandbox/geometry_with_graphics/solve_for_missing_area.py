# =============================================================================
# Jim McCleery
# November 4, 2026
# Kailua-Kona, HI
#
# Reference: https://youtu.be/Brgb73qzi5o?si=JGVghKDkiwlvT7lt
# =============================================================================

from math import sqrt
from random import uniform
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Essential Geometry Helper Functions
# -----------------------------------------------------------------------------


def line_intersection_from_points(A, B, C, D):
    """Find the intersection point (x, y) of two lines.

    The first line passes through points A and B.
    The second line passes through points C and D.
    Points are represented as (x, y) tuples.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D

    # Compute the slopes of each line (rise over run)
    slope1 = (y2 - y1) / (x2 - x1)
    slope2 = (y4 - y3) / (x4 - x3)

    # Solve for the x-coordinate where the two line equations meet
    x = (y1 - slope1 * x1 - y3 + slope2 * x3) / (slope2 - slope1)

    # Calculate y using the point-slope formula on the first line
    y = y1 + slope1 * (x - x1)

    return (x, y), True


def polygon_area(vertices):
    """Calculate the area of a 2D polygon using the Shoelace formula.

    'vertices' is an ordered list of (x, y) coordinate tuples.
    """
    n = len(vertices)
    area = 0.0

    # Cross-multiply coordinates in cyclic order around the boundary
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # Wraps around from last point to first
        area += x1 * y2 - y1 * x2

    return abs(area) / 2.0


def polygon_fill_coordinates(vertices):
    """Format polygon vertices for matplotlib's plt.fill() function.

    Repeats the initial point at the end to form a closed shape.
    """
    x_coords = [p[0] for p in vertices] + [vertices[0][0]]
    y_coords = [p[1] for p in vertices] + [vertices[0][1]]
    return x_coords, y_coords


def plot_line(A, B, color="black", linewidth=1.5):
    """Draw a straight line segment between points A and B."""
    plt.plot([A[0], B[0]], [A[1], B[1]], color=color, linewidth=linewidth)


# -----------------------------------------------------------------------------
# Coordinate Solver
# -----------------------------------------------------------------------------
# Based on the problem diagram:
# - Square ABCD has side length s: D=(0,0), C=(s,0), B=(s,s), A=(0,s).
# - E lies on top edge AB at (m, s). Line DE goes from (0,0) to (m,s).
# - FG is perpendicular to DE, intersecting at H with right triangle FHD (area=4).
# - Trapezoid AFHE has area 5, and triangle DHG has area 11.
# - A randomized search finds the side length s satisfying all geometric constraints.

while True:
    s = uniform(5.5, 6.5)  # Guess a plausible square side length
    m = 18.0 / s  # Derived from area(ADE) = area(AFHE) + area(FHD) = 5 + 4 = 9 = (m * s)/2
    if m > s:
        continue

    p = sqrt(8.0 * 18.0 / (m**2))  # Length along the perpendicular line
    q = 8.0 / p  # Associated height for right triangle FHD
    r = sqrt(q**2 + p**2)  # y-coordinate of point F on the left edge AD
    t = (30.0 - r * s) / s  # y-coordinate of point G on the right edge BC

    # Assign square corners and boundary points
    D = (0, 0)
    C = (s, 0)
    B = (s, s)
    A = (0, s)
    E = (m, s)
    F = (0, r)
    G = (s, t)

    # Slopes of lines DE and FG
    slope_DE = (E[1] - D[1]) / (E[0] - D[0])
    slope_FG = (F[1] - G[1]) / (F[0] - G[0])

    # Check for perpendicularity: slope_DE * slope_FG == -1
    if abs(slope_DE * slope_FG + 1.0) < 1e-5:
        break

# Compute the perpendicular intersection point H
H, _ = line_intersection_from_points(D, E, F, G)

# -----------------------------------------------------------------------------
# Plotting and Visual Labels
# -----------------------------------------------------------------------------
plt.figure(figsize=(7, 7))

# Draw the perimeter of square ABCD
plot_line(A, B)
plot_line(B, C)
plot_line(C, D)
plot_line(D, A)

# Draw interior segments DE and FG
plot_line(D, E)
plot_line(F, G)

# Fill the unknown region (polygon E-B-C-G-H)
unknown_polygon = [H, G, C, B, E]
area_unknown = polygon_area(unknown_polygon)
plt.fill(
    *polygon_fill_coordinates(unknown_polygon),
    color="chocolate",
    alpha=0.85,
    edgecolor="darkred",
    linewidth=2,
)

# Plot and label all key points with their calculated coordinates
points = {
    "A": (A, (-0.45, 0.15)),
    "B": (B, (0.15, 0.15)),
    "C": (C, (0.15, -0.35)),
    "D": (D, (-0.45, -0.35)),
    "E": (E, (0.0, 0.2)),
    "F": (F, (-0.45, 0.0)),
    "G": (G, (0.15, 0.0)),
    "H": (H, (0.15, -0.15)),
}

for label, (pt, offset) in points.items():
    # Draw point marker
    plt.plot(pt[0], pt[1], "o", color="navy", markersize=5)
    # Add point name and formatted coordinates (x, y)
    plt.text(
        pt[0] + offset[0],
        pt[1] + offset[1],
        f"{label} ({pt[0]:.2f}, {pt[1]:.2f})",
        fontsize=9,
        weight="bold",
        color="darkblue",
    )

plt.title(f"Area of Unknown Region (EBCGH) = {area_unknown:.2f}", fontsize=12)
plt.axis("equal")
plt.axis("off")
plt.tight_layout()
plt.show()
