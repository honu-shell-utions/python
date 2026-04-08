"""
Jim McCleery
April 8, 2026
Kailua-Kona, HI

Python solution to the geometric area-coloring problem
Video: https://youtu.be/cbetoOAMtTw?si=9CXMwVHxSxYuvJhj

This program searches numerically for a configuration in which the total
blue area is approximately 140. Once such a configuration is found, the
figure is drawn.

The picture consists only of the large triangle and the alternating
red and blue stripes.
"""

from math import pi, sin, cos, tan
from random import uniform
import matplotlib.pyplot as plt


def polygon_area(vertices):
    """
    Compute the area of a polygon using the shoelace formula.
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
    Convert polygon vertices into x- and y-coordinate lists for fill().
    """
    x_coords, y_coords = zip(*vertices)
    return list(x_coords) + [x_coords[0]], list(y_coords) + [y_coords[0]]


def build_band_vertices(k, lower_left, lower_right, s1, s2, alpha, beta, x_c):
    """
    Build the quadrilateral for stripe level k.
    """
    upper_left = (k * s1 * cos(alpha), k * s1 * sin(alpha))
    upper_right = (x_c + k * s2 * cos(pi - beta), k * s2 * sin(pi - beta))
    vertices = [lower_left, upper_left, upper_right, lower_right]
    return vertices, upper_left, upper_right


def compute_colored_areas(alpha, beta, h):
    """
    Build the striped triangle and compute the total blue and red areas.
    """
    a = h / tan(alpha)
    b = h / tan(beta)

    s1 = h / sin(alpha)
    s2 = h / sin(beta)

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


def draw_configuration(data):
    """
    Draw only the large triangle and the alternating red/blue stripes.
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

        lower_left = upper_left
        lower_right = upper_right

    ax.plot([A[0], B[0]], [A[1], B[1]], color="black", linewidth=2)
    ax.plot([B[0], C[0]], [B[1], C[1]], color="black", linewidth=2)
    ax.plot([A[0], C[0]], [A[1], C[1]], color="black", linewidth=2)

    ax.set_title(f"Striped Triangle Figure   (Red Area = {red_area:.1f})")
    ax.set_aspect("equal")
    ax.axis("off")

    return fig
def main():
    """
    Main driver for the program.
    """
    for _ in range(10):
        data = find_configuration(target_blue_area=140.0, tolerance=1e-2)
        fig = draw_configuration(data)
        plt.show(block=False)
        plt.pause(0.5)
        plt.close(fig)

if __name__ == "__main__":
    main()
