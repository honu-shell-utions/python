"""
Jim McCleery
April 19, 2026
Kailua-Kona, HI

https://youtu.be/psW8LZW08Lg?si=wy6cQas_BAj_K6sE
"""

from math import pi, sqrt
import matplotlib.pyplot as plt


def law_of_cosines(side_a, side_b, opposite_side):
    """
    Return the angle opposite 'opposite_side' using the Law of Cosines.

    Parameters
    ----------
    side_a, side_b : float
        The two adjacent sides.
    opposite_side : float
        The side opposite the desired angle.

    Returns
    -------
    float
        Angle in radians.
    """
    cosine_value = (
        side_a**2 + side_b**2 - opposite_side**2
    ) / (2 * side_a * side_b)
    return acos_clamped(cosine_value)


def acos_clamped(x):
    """
    Return arccos(x), after clamping x into [-1, 1] to avoid
    floating-point roundoff issues.
    """
    x = max(-1.0, min(1.0, x))
    from math import acos
    return acos(x)


def polygon_fill_coordinates(vertices):
    """
    Convert a list of polygon vertices into x- and y-coordinate lists
    suitable for matplotlib fill().

    The first vertex is repeated at the end so the polygon closes.
    """
    x_coords, y_coords = zip(*vertices)
    return list(x_coords) + [x_coords[0]], list(y_coords) + [y_coords[0]]


def draw_segment(ax, p1, p2, **kwargs):
    """
    Draw a line segment between points p1 and p2.
    """
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], **kwargs)


def label_point(ax, point, name, dx=0.15, dy=0.15):
    """
    Plot and label a point with its coordinates.
    """
    x, y = point
    ax.plot(x, y, "ko", markersize=4)
    ax.text(
        x + dx,
        y + dy,
        f"{name} ({x:.3f}, {y:.3f})",
        fontsize=10
    )


def compute_geometry():
    """
    Compute the rectangle and triangle geometry exactly.

    Given what we know about the angle sizes these values
    can be solved exactly, giving

        h^2 = 10*sqrt(3)
        b = 20 / h
        w = h * sqrt(3)

    Returns
    -------
    dict
        Dictionary containing the named points and dimensions.
    """
    h = sqrt(10 * sqrt(3))
    b = 20 / h
    w = h * sqrt(3)

    points = {
        "A": (0.0, 0.0),
        "B": (w, 0.0),
        "C": (w, h),
        "D": (0.0, h),
        "E": (b, 0.0),
    }

    return {
        "h": h,
        "b": b,
        "w": w,
        "area_rectangle": w * h,
        "points": points,
    }


def main():
    """
    Draw the rectangle, diagonals, and shaded triangle.
    """
    data = compute_geometry()
    points = data["points"]

    A = points["A"]
    B = points["B"]
    C = points["C"]
    D = points["D"]
    E = points["E"]

    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw the outer rectangle.
    draw_segment(ax, A, B, color="black")
    draw_segment(ax, B, C, color="black")
    draw_segment(ax, C, D, color="black")
    draw_segment(ax, D, A, color="black")

    # Draw the two interior segments from the original figure.
    draw_segment(ax, E, C, color="black")
    draw_segment(ax, A, C, color="black")

    # Shade triangle AEC.
    triangle_vertices = [A, E, C]
    x_fill, y_fill = polygon_fill_coordinates(triangle_vertices)
    ax.fill(
        x_fill,
        y_fill,
        color="lightblue",
        edgecolor="blue",
        linewidth=2
    )

    # Label the points with coordinates.
    label_point(ax, A, "A")
    label_point(ax, B, "B")
    label_point(ax, C, "C")
    label_point(ax, D, "D")
    label_point(ax, E, "E")

    # Add a title and axis styling.
    ax.set_title(f"Area of rectangle = {data['area_rectangle']:.3f}")
    ax.set_aspect("equal")
    ax.grid(True, linestyle="--", alpha=0.4)

    # Add a little padding around the figure.
    x_values = [p[0] for p in points.values()]
    y_values = [p[1] for p in points.values()]
    x_margin = 0.8
    y_margin = 0.8

    ax.set_xlim(min(x_values) - x_margin, max(x_values) + x_margin)
    ax.set_ylim(min(y_values) - y_margin, max(y_values) + y_margin)

    plt.show()


if __name__ == "__main__":
    main()
