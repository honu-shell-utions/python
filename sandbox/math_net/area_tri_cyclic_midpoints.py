# Jim McCleery
# Today's date
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_bf340b

import random
import matplotlib.pyplot as plt
import numpy as np


def compute_polygon_area(vertices):
    """Calculate the area of a polygon using the Shoelace Formula."""
    x = [v[0] for v in vertices]
    y = [v[1] for v in vertices]

    # Shoelace formula via matrix dot products
    area = 0.5 * np.abs(np.dot(x, np.roll(y, 1)) - np.dot(y, np.roll(x, 1)))
    return area


def generate_random_triangle_area_1():
    """Generates three random (non-collinear) points and scales them

    so that Triangle ABC has an area of exactly 1.0.
    """
    while True:
        # Generate 3 random 2D points with coordinates between -5 and 5
        A = np.array([random.uniform(-5, 5), random.uniform(-5, 5)])
        B = np.array([random.uniform(-5, 5), random.uniform(-5, 5)])
        C = np.array([random.uniform(-5, 5), random.uniform(-5, 5)])

        # Measure the raw area of this random triangle
        raw_area = compute_polygon_area([A, B, C])

        # Ensure the points aren't flat/collinear (area > 0)
        if raw_area > 0.1:
            break

    # Scale coordinates by 1/sqrt(raw_area) so the new area equals 1
    scale_factor = 1.0 / np.sqrt(raw_area)
    A *= scale_factor
    B *= scale_factor
    C *= scale_factor

    return A, B, C

# -----------------------------------------------------------------------------
# 1. GENERATE RANDOM TRIANGLE ABC WITH AREA = 1
# -----------------------------------------------------------------------------
A, B, C = generate_random_triangle_area_1()

# -----------------------------------------------------------------------------
# 2. CALCULATE INTERIOR POINTS D, E, F EXACTLY
# -----------------------------------------------------------------------------
# System solution for midpoints:
# D is midpoint of AE, E is midpoint of BF, F is midpoint of CD
D = (4 * A + 2 * B + C) / 7.0
E = (A + 4 * B + 2 * C) / 7.0
F = (2 * A + B + 4 * C) / 7.0

# -----------------------------------------------------------------------------
# 3. VERIFY AREAS
# -----------------------------------------------------------------------------
area_ABC = compute_polygon_area([A, B, C])
area_DEF = compute_polygon_area([D, E, F])

# -----------------------------------------------------------------------------
# 4. PLOT THE RANDOMIZED GEOMETRY
# -----------------------------------------------------------------------------
fig, ax = plt.subplots(figsize=(8, 6))

# Close loop coordinates for drawing triangles
triangle_ABC = np.array([A, B, C, A])
triangle_DEF = np.array([D, E, F, D])

# Draw outer triangle (Blue) and inner triangle (Red)
ax.plot(
    triangle_ABC[:, 0], triangle_ABC[:, 1], "b-", linewidth=2, label="Outer ABC"
)
ax.plot(
    triangle_DEF[:, 0], triangle_DEF[:, 1], "r-", linewidth=2, label="Inner DEF"
)

# Fill inner triangle DEF
ax.fill(triangle_DEF[:, 0], triangle_DEF[:, 1], color="red", alpha=0.35)

# Draw midpoint construction line segments (A-D-E, B-E-F, C-F-D)
ax.plot([A[0], E[0]], [A[1], E[1]], "k--", alpha=0.4, label="Midpoint Lines")
ax.plot([B[0], F[0]], [B[1], F[1]], "k--", alpha=0.4)
ax.plot([C[0], D[0]], [C[1], D[1]], "k--", alpha=0.4)

# Label all 6 vertices on plot
for name, pt in [
    ("A", A),
    ("B", B),
    ("C", C),
    ("D", D),
    ("E", E),
    ("F", F),
]:
    ax.annotate(
        f" {name}",
        (pt[0], pt[1]),
        fontsize=12,
        fontweight="bold",
    )

# Formatting
ax.set_aspect("equal")
ax.axis("off")
ax.set_title(
    f"Randomized Triangle ABC (Area = {area_ABC:.4f})\n"
    f"Inner Triangle DEF Area = {area_DEF:.6f} (Always 1/7)",
    fontsize=13,
)
ax.legend(loc="upper right")
plt.pause(0.5)
plt.show()
