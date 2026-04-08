"""
Jim McCleery
April 8, 2026
Kailua-Kona, HI

Python solution to the geometric area-coloring problem
Video: https://youtu.be/cbetoOAMtTw?si=9CXMwVHxSxYuvJhj

This program searches numerically for a configuration in which the total
blue area is approximately 140. Once such a configuration is found, the
figure is drawn.

The picture consists of a large triangle subdivided into alternating
colored bands.  The band boundaries are created by marking equally spaced
points on the two slanted sides and then joining corresponding points.
"""

from math import pi, sin, cos, tan
from random import uniform
import matplotlib.pyplot as plt


def polygon_area(vertices):
    """
    Compute the area of a polygon using the shoelace formula.

    Parameters
    ----------
    vertices : list of (x, y) tuples
        The vertices listed in order around the polygon.

    Returns
    -------
    float
        The area of the polygon.
    """
    area = 0.0
    n = len(vertices)

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2

    return abs(area) / 2.0


def polygon_fill_coordinates(vertices):
    """
    Convert polygon vertices into x- and y-coordinate lists suitable
    for matplotlib's fill() function.
    """
    x_coords, y_coords = zip(*vertices)
    return list(x_coords) + [x_coords[0]], list(y_coords) + [y_coords[0]]


def plot_line(ax, p, q, **kwargs):
    """
    Plot the line segment joining points p and q.
    """
    ax.plot([p[0], q[0]], [p[1], q[1]], **kwargs)


def build_band_vertices(k, lower_left, lower_right, s1, s2, alpha, beta, x_c):
    """
    Build the quadrilateral corresponding to level k.

    The lower edge is determined by the previous level.
    The upper edge is determined by the new points at level k.
    """
    upper_left = (k * s1 * cos(alpha), k * s1 * sin(alpha))
    upper_right = (x_c + k * s2 * cos(pi - beta), k * s2 * sin(pi - beta))
    vertices = [lower_left, upper_left, upper_right, lower_right]
    return vertices, upper_left, upper_right


def compute_colored_areas(alpha, beta, h):
    """
    Construct the geometry for a given alpha, beta, and h,
    then compute the total blue and red areas.
    """
    a = h / tan(alpha)
    b = h / tan(beta)

    # Equal step lengths along the slanted sides.
    s1 = h / sin(alpha)
    s2 = h / sin(beta)

    # Main triangle vertices.
    A = (0.0, 0.0)
    B = (8 * a, 8 * h)
    C = (8 * a + 8 * b, 0.0)

    blue_area = 0.0
    red_area = 0.0

    lower_left = A
    lower_right = C

    for k in range(9):
        vertices, upper_left, upper_right = build_band_vertices(
            k, lower_left, lower_right, s1, s2, alpha, beta, C[0]
        )

        area = polygon_area(vertices)

        if k % 2 == 0:
            blue_area += area
        else:
            red_area += area

        lower_left = upper_left
        lower_right = upper_right

    return {
        "alpha": alpha,
        "beta": beta,
        "h": h,
        "a": a,
        "b": b,
        "s1": s1,
        "s2": s2,
        "A": A,
        "B": B,
        "C": C,
        "blue_area": blue_area,
        "red_area": red_area,
    }


def find_configuration(target_blue_area=140.0, tolerance=1e-3):
    """
    Use random search to find a configuration whose blue area
    is approximately the desired target.
    """
    while True:
        alpha = uniform(0, pi / 2)
        beta = uniform(0, pi / 2)
        h = uniform(0, 10)

        data = compute_colored_areas(alpha, beta, h)

        if abs(data["blue_area"] - target_blue_area) < tolerance:
            return data


def add_labels(ax, data):
    """
    Add geometric labels to the finished figure.
    """
    alpha = data["alpha"]
    beta = data["beta"]
    s1 = data["s1"]
    s2 = data["s2"]
    A = data["A"]
    B = data["B"]
    C = data["C"]
    blue_area = data["blue_area"]
    red_area = data["red_area"]

    x0, y0 = A
    x1, y1 = B
    x2, y2 = C

    # ---- Label the main vertices ----
    ax.text(x0 - 0.35, y0 - 0.35, "A", fontsize=12)
    ax.text(x1, y1 + 0.35, "B", fontsize=12)
    ax.text(x2 + 0.20, y2 - 0.35, "C", fontsize=12)

    # ---- Foot of the altitude ----
    D = (x1, 0.0)
    ax.plot([x1, x1], [0.0, y1], "--", color="black", linewidth=1)
    ax.text(D[0] + 0.12, D[1] + 0.12, "D", fontsize=11)
    ax.text(x1 + 0.15, y1 / 2, r"$8h$", fontsize=11)

    # ---- Angle labels ----
    ax.text(
        x0 + 0.9 * cos(alpha / 2),
        y0 + 0.9 * sin(alpha / 2),
        r"$\alpha$",
        fontsize=12
    )

    ax.text(
        x2 + 0.9 * cos(pi - beta / 2),
        y2 + 0.9 * sin(pi - beta / 2),
        r"$\beta$",
        fontsize=12
    )

    # ---- Level labels along the slanted sides ----
    #
    # The point at level k on the left side is:
    #     L_k = (k s1 cos(alpha), k s1 sin(alpha))
    #
    # The corresponding point at level k on the right side is:
    #     R_k = (x2 + k s2 cos(pi-beta), k s2 sin(pi-beta))
    #
    # These labels help students see how the bands are built.
    for k in range(9):
        left_k = (k * s1 * cos(alpha), k * s1 * sin(alpha))
        right_k = (x2 + k * s2 * cos(pi - beta), k * s2 * sin(pi - beta))

        # Slight offsets so the labels do not sit directly on the boundary lines.
        ax.text(left_k[0] - 0.45, left_k[1] + 0.08, f"$k={k}$", fontsize=9)
        ax.text(right_k[0] + 0.12, right_k[1] + 0.08, f"$k={k}$", fontsize=9)

        # Mark the boundary points themselves.
        ax.plot(left_k[0], left_k[1], "ko", markersize=3)
        ax.plot(right_k[0], right_k[1], "ko", markersize=3)


def draw_configuration(data):
    """
    Draw the colored figure and add labels.
    """
    alpha = data["alpha"]
    beta = data["beta"]
    s1 = data["s1"]
    s2 = data["s2"]
    A = data["A"]
    B = data["B"]
    C = data["C"]
    red_area = data["red_area"]

    fig, ax = plt.subplots(figsize=(10, 6))

    # Reset the lower boundary before drawing the bands.
    lower_left = A
    lower_right = C

    for k in range(9):
        vertices, upper_left, upper_right = build_band_vertices(
            k, lower_left, lower_right, s1, s2, alpha, beta, C[0]
        )

        color = "blue" if k % 2 == 0 else "red"
        ax.fill(
            *polygon_fill_coordinates(vertices),
            color=color,
            edgecolor="black",
            linewidth=1,
            alpha=0.75
        )

        # Optional: draw the strip boundary segment between corresponding
        # level-k points so students can see the subdivision lines clearly.
        ax.plot(
            [upper_left[0], upper_right[0]],
            [upper_left[1], upper_right[1]],
            color="black",
            linewidth=0.8
        )

        lower_left = upper_left
        lower_right = upper_right

    # Draw the outer triangle.
    plot_line(ax, A, B, color="black", linewidth=2)
    plot_line(ax, B, C, color="black", linewidth=2)
    plot_line(ax, A, C, color="black", linewidth=2)

    add_labels(ax, data)

    ax.set_title(f"Striped Triangle Figure   (Red Area = {red_area:.1f})")
    ax.set_aspect("equal")
    plt.show()


def main():
    """
    Main driver for the program.
    """
    data = find_configuration(target_blue_area=140.0, tolerance=1e-3)
    draw_configuration(data)


if __name__ == "__main__":
    main()
