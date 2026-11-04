# Jim McCleery
# November 3, 2026
# Kailua-Kona, HI
# https://mathnet.mit.edu/explorer.html?p=nmo_1991_bd8ca4
"""Explore the overlap of triangles ABF and CDE in a trapezium.

AB and CD are parallel. E stays fixed on AB while F moves along CD.
The shaded quadrilateral E-H-F-G is the intersection of the triangles.
This program estimates the maximum by sampling positions; it is not a proof.

Requires NumPy and Matplotlib:
    python -m pip install numpy matplotlib
Run with:
    python trapezium_overlap.py
"""

from random import uniform

import matplotlib.pyplot as plt
import numpy as np

# Change these settings to control the animation.
NUMBER_OF_POSITIONS = 2001   # Includes both ends of CD.
PAUSE_SECONDS = 0.03
ANIMATE = True             # False calculates and displays only the best position.


def line_intersection(A, B, C, D):
    """Return the intersection of lines AB and CD, including vertical lines."""
    # Points are (x, y) tuples. Unpacking gives each coordinate its own name.
    ax, ay = A
    bx, by = B
    cx, cy = C
    dx, dy = D

    # Write the first line as A + t*(B - A). Solve for the number t.
    ux, uy = bx - ax, by - ay
    vx, vy = dx - cx, dy - cy
    denominator = ux * vy - uy * vx
    if abs(denominator) < 1e-12:
        raise ValueError("The lines are parallel or have coincident points.")
    t = ((cx - ax) * vy - (cy - ay) * vx) / denominator
    return ax + t * ux, ay + t * uy


def polygon_area(vertices):
    """Return the area using the shoelace formula; vertices go around the edge."""
    twice_area = 0
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        # % wraps the last index back to zero, closing the polygon.
        x2, y2 = vertices[(i + 1) % len(vertices)]
        twice_area += x1 * y2 - y1 * x2
    return abs(twice_area) / 2


def overlap_points(A, B, C, D, E, F):
    """Find G = AF intersect ED and H = BF intersect EC."""
    G = line_intersection(A, F, E, D)
    H = line_intersection(B, F, E, C)
    return G, H


def draw_diagram(ax, A, B, C, D, E, F, G, H, fraction, best, final=False):
    """Draw the construction and label every point with its coordinates."""
    ax.clear()

    # Repeat A to close the trapezium. Lists hold the coordinates to plot.
    outline = [A, B, C, D, A]
    ax.plot([p[0] for p in outline], [p[1] for p in outline],
            color="0.25", linewidth=2)
    for start, end in [(A, F), (B, F), (E, D), (E, C)]:
        ax.plot([start[0], end[0]], [start[1], end[1]],
                color="steelblue", linewidth=1.5)

    overlap = [E, H, F, G]
    ax.fill([p[0] for p in overlap], [p[1] for p in overlap],
            color="lightblue", edgecolor="tab:blue", alpha=0.65)

    points = {"A": A, "B": B, "C": C, "D": D,
              "E": E, "F": F, "G": G, "H": H}
    # Offsets are in display points, so labels stay readable at different scales.
    offsets = {"A": (-8, -25), "B": (8, -25), "C": (8, 12),
               "D": (-8, 12), "E": (0, -42), "F": (0, 32),
               "G": (-12, 0), "H": (12, 0)}
    for name, point in points.items():
        x, y = point
        offset = offsets[name]
        ax.plot(x, y, "o", color="black", markersize=4)
        ax.annotate(f"{name} ({x:.2f}, {y:.2f})", xy=point,
                    xytext=offset, textcoords="offset points",
                    ha="right" if offset[0] < 0 else
                       "left" if offset[0] > 0 else "center",
                    va="center", fontsize=9,
                    bbox=dict(facecolor="white", edgecolor="none", alpha=0.8))

    heading = "Best sampled position" if final else "Moving F along CD"
    ax.set_title(f"{heading}\nCurrent overlap: {100 * fraction:.3f}%"
                 f"   |   Largest sampled: {100 * best:.3f}%", pad=42)
    # Equal scales prevent the geometry from being stretched.
    ax.set_aspect("equal", adjustable="box")
    ax.set_xlim(A[0] - 0.18 * (B[0] - A[0]), B[0] + 0.18 * (B[0] - A[0]))
    ax.set_ylim(-0.4 * C[1], 1.5 * C[1])
    ax.set_axis_off()


def main():
    """Create a trapezium, explore F, then display the best sampled overlap."""
    A = (0.0, 0.0)
    B = (uniform(20, 100), 0.0)
    C = (B[0] - uniform(5, 19), uniform(10, 30))
    D = (uniform(A[0], C[0]), C[1])
    E = (uniform(A[0], B[0]), 0.0)
    total_area = polygon_area([A, B, C, D])

    fig, ax = plt.subplots(figsize=(12, 7), layout="constrained")
    best_fraction = -1.0
    best_points = None

    # linspace gives evenly spaced positions, covering CD systematically.
    # Unlike random sampling, this also includes both endpoints.
    for x in np.linspace(D[0], C[0], NUMBER_OF_POSITIONS):
        if not plt.fignum_exists(fig.number):
            return  # Stop if the user closes the animation window.
        F = (float(x), C[1])
        G, H = overlap_points(A, B, C, D, E, F)
        fraction = polygon_area([E, H, F, G]) / total_area
        if fraction > best_fraction:
            best_fraction = fraction
            best_points = (F, G, H)
        if ANIMATE:
            draw_diagram(ax, A, B, C, D, E, F, G, H, fraction, best_fraction)
            plt.pause(PAUSE_SECONDS)

    # Restore the best position so the last frame matches the reported maximum.
    F, G, H = best_points
    draw_diagram(ax, A, B, C, D, E, F, G, H,
                 best_fraction, best_fraction, final=True)
    print(f"Best sampled F: ({F[0]:.6f}, {F[1]:.6f})")
    print(f"Largest sampled overlap: {100 * best_fraction:.3f}% of the trapezium")
    plt.show()


# Run main only when this file is executed, not when another file imports it.
if __name__ == "__main__":
    main()
