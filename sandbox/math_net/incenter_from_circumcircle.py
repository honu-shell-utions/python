"""
Jim McCleery
November 11, 2026
Kailua-Kona, HI

https://mathnet.mit.edu/explorer.html?p=egm_2020_9202c0
"""

from math import dist, sqrt

import matplotlib.pyplot as plt
from matplotlib.patches import Circle


def incircle_of_triangle(A, B, C):
    """Return the center and radius of the circle tangent to the three sides."""
    # Each lowercase letter is the length of the side opposite that vertex.
    a = dist(B, C)
    b = dist(A, C)
    c = dist(A, B)
    perimeter = a + b + c

    # Use the opposite side lengths as weights in a coordinate average.
    center_x = (a * A[0] + b * B[0] + c * C[0]) / perimeter
    center_y = (a * A[1] + b * B[1] + c * C[1]) / perimeter

    # Heron's formula gives the area from the three side lengths.
    s = perimeter / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    return (center_x, center_y), area / s


def plot_line(ax, A, B, **style):
    """Draw one segment by giving Matplotlib its x-values and y-values."""
    x1, y1 = A
    x2, y2 = B
    ax.plot([x1, x2], [y1, y2], **style)


def label_point(ax, name, point, offset, color):
    """Mark a point and place its coordinate label nearby."""
    x, y = point  # Unpack the two values stored in the tuple.
    ax.plot(x, y, "o", color=color, markersize=4, zorder=4)
    ax.annotate(
        f"{name} ({x:.2f}, {y:.2f})",
        xy=point,
        xytext=offset,
        textcoords="offset points",
        ha="center",
        color=color,
        fontsize=10,
        zorder=5,
        bbox={"facecolor": "white", "edgecolor": "none", "pad": 1.3},
    )


def main():
    # A point is an (x, y) tuple. Keep AB horizontal and 20 units long.
    A = (0, 0)
    B = (20, 0)
    radius = 12
    P = (radius, 0)  # Starting with AP = radius builds in this given.
    pb = dist(P, B)

    # The center is above the midpoint of AB. Use the right triangle
    # formed by A, that midpoint, and O to find the center's height.
    center_x = (A[0] + B[0]) / 2
    center_y = sqrt(radius**2 - (B[0] - center_x)**2)
    O = (center_x, center_y)

    # C is the other intersection of the circumcircle and the circle
    # centered at P with radius PB. Both circles already pass through B.
    # Subtracting their equations gives the slope of the common chord BC.
    slope = (P[0] - center_x) / center_y

    # Write a point on BC as (B[0] + dx, slope * dx). Substitution into
    # the circle centered at P gives dx = 0 at B and this second root at C.
    dx = -2 * pb / (1 + slope**2)
    C = (B[0] + dx, slope * dx)

    # The perpendicular bisector of horizontal PB is a vertical line.
    # D and E share its x-coordinate and sit equally far above and below O.
    bisector_x = (P[0] + B[0]) / 2
    half_chord = sqrt(radius**2 - (bisector_x - center_x)**2)
    D = (bisector_x, center_y + half_chord)
    E = (bisector_x, center_y - half_chord)

    # Calculate the incircle from the three vertices, as in the original script.
    I, inradius = incircle_of_triangle(C, D, E)

    fig, ax = plt.subplots(figsize=(8, 7.5), layout="constrained")
    blue, teal, gold, gray = "#264f91", "#007a72", "#9d531b", "#697b91"

    # Circle patches use a center and a radius in plot coordinates.
    ax.add_patch(Circle(O, radius, fill=False, edgecolor=gray, linewidth=1.5))
    ax.add_patch(Circle(I, inradius, fill=False, edgecolor=gold, linestyle=":"))

    for start, end in [(A, B), (B, C), (C, A)]:
        plot_line(ax, start, end, color=blue, linewidth=1.8)
    for start, end in [(C, D), (C, E)]:
        plot_line(ax, start, end, color=teal, linewidth=1.8)
    plot_line(ax, D, E, color=teal, linestyle="--")
    plot_line(ax, P, C, color=gold, linestyle="--")

    # Draw the right-angle marker in the upper-left corner of the crossing.
    square_size = 0.55
    ax.plot(
        [bisector_x - square_size, bisector_x - square_size, bisector_x],
        [0, square_size, square_size],
        color=teal,
    )
    ax.text(P[0] / 2, 0.55, r"$R$", color=blue, ha="center")
    ax.text(2, 16.2, r"$\Gamma$", color=gray, fontsize=16)

    # The offsets are in screen points so the labels sit clear of the dots.
    for name, point, offset, color in [
        ("A", A, (-20, 8), blue),
        ("B", B, (17, 9), blue),
        ("C", C, (-18, -17), blue),
        ("D", D, (24, 12), teal),
        ("E", E, (29, -15), teal),
        ("P / I", P, (9, 15), gold),
        ("O", O, (-48, 7), gray),
    ]:
        label_point(ax, name, point, offset, color)

    # Equal axis scaling keeps circles round. The point labels supply coordinates.
    ax.set_aspect("equal")
    ax.set(xlim=(-4, 25), ylim=(-7.5, 21))
    ax.axis("off")
    plt.show()


# Run main() when this file is executed directly.
if __name__ == "__main__":
    main()
