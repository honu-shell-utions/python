"""
Jim McCleery
November 19, 2026
Kailua-Kona, HI

https://mathnet.mit.edu/explorer.html?p=usa_90b761
"""

from math import hypot
from random import uniform

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def circum_circle(a, b, c):
    """Return the center and radius of the circle through three points."""
    # Measure b and c relative to a to simplify the circle equations.
    bx, by = b[0] - a[0], b[1] - a[1]
    cx, cy = c[0] - a[0], c[1] - a[1]

    # The center is equally far from all three points. Solving those
    # equal-distance equations gives its coordinates relative to a.
    determinant = 2 * (bx * cy - by * cx)
    if determinant == 0:
        raise ValueError("Three noncollinear points are needed for a circle.")

    b_squared = bx**2 + by**2
    c_squared = cx**2 + cy**2
    x = (b_squared * cy - c_squared * by) / determinant
    y = (bx * c_squared - cx * b_squared) / determinant
    return (a[0] + x, a[1] + y), hypot(x, y)


def second_intersection(center1, center2, corner):
    """Find the other intersection when both circles pass through corner."""
    dx = center2[0] - center1[0]
    dy = center2[1] - center1[1]
    x = corner[0] - center1[0]
    y = corner[1] - center1[1]

    # The line through the centers is a mirror line for both circles.
    # Project the corner onto that line to find the midpoint of the two
    # intersections, then reflect the corner across the midpoint.
    fraction = (x * dx + y * dy) / (dx**2 + dy**2)
    midpoint_x = center1[0] + fraction * dx
    midpoint_y = center1[1] + fraction * dy
    return 2 * midpoint_x - corner[0], 2 * midpoint_y - corner[1]


def label_point(ax, name, point, offset, alignment):
    """Draw a dot and place its name and coordinates beside it."""
    x, y = point
    ax.plot(x, y, "o", color="#222222", markersize=4, zorder=4)
    # '.2f' rounds the displayed coordinates to two decimal places.
    ax.annotate(
        f"{name} ({x:.2f}, {y:.2f})",
        point,
        xytext=offset,
        textcoords="offset points",
        ha=alignment,
        va="center",
        fontsize=9,
        bbox={"facecolor": "white", "edgecolor": "none", "alpha": 0.9, "pad": 1.5},
    )


def draw_frame(ax, side):
    """Generate and draw one configuration of the four circles."""
    a, b = (0, 0), (side, 0)
    c, d = (side, side), (0, side)
    corners = (a, b, c, d)

    # Each third point sits inward from the midpoint of its side.
    # Keep the offsets below half the side so the centers stay outside.
    bottom, right, top, left = (
        uniform(side / 4, 0.49 * side) for _ in range(4)
    )
    half = side / 2
    circles = (
        circum_circle(a, b, (half, bottom)),
        circum_circle(b, c, (side - right, half)),
        circum_circle(c, d, (half, side - top)),
        circum_circle(d, a, (left, half)),
    )

    # At A, for example, k4 and k1 meet at A and again at L.
    inner_points = []
    for index, corner in enumerate(corners):
        previous_center = circles[index - 1][0]  # At index 0, -1 selects k4.
        current_center = circles[index][0]
        inner_points.append(second_intersection(previous_center, current_center, corner))

    l_point, m_point, n_point, _ = inner_points
    center, radius = circum_circle(l_point, m_point, n_point)

    # Unpack the corner pairs into a sequence of x-values and one of y-values.
    square_x, square_y = zip(*corners, a)
    ax.plot(square_x, square_y, color="#333333", linewidth=1.4)
    colors = ("#377eb8", "#ff7f00", "#4daf4a", "#984ea3")
    for index, ((center_i, radius_i), color) in enumerate(zip(circles, colors), start=1):
        ax.add_patch(
            Circle(center_i, radius_i, fill=False, edgecolor=color, label=f"$k_{index}$")
        )

    inner_x, inner_y = zip(*inner_points, inner_points[0])
    ax.plot(inner_x, inner_y, color="#555555", linewidth=1, alpha=0.7)
    ax.add_patch(
        Circle(center, radius, fill=False, edgecolor="#b2182b",
               linewidth=1.8, linestyle="--", label="Circle through L, M, N, P")
    )

    # Offsets are measured in screen points and follow the four square corners.
    offsets = ((-8, -8), (8, -8), (8, 8), (-8, 8))
    alignments = ("right", "left", "left", "right")
    for names, points in (("ABCD", corners), ("LMNP", inner_points)):
        for name, point, offset, alignment in zip(names, points, offsets, alignments):
            label_point(ax, name, point, offset, alignment)

    ax.set_aspect("equal")
    ax.set_xlim(-side, 2 * side)
    ax.set_ylim(-side, 2 * side)
    ax.set_axis_off()
    ax.legend(loc="upper right", frameon=False, fontsize=9)


def main():
    """Show ten random examples, one per second."""
    _, ax = plt.subplots(figsize=(8, 8))
    for _ in range(100):
        ax.clear()
        draw_frame(ax, side=10)
        plt.pause(1)
    plt.show()


# Run the animation when this file is launched as a script.
if __name__ == "__main__":
    main()
