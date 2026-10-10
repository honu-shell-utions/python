# Jim McCleery
# October 9, 2026
# Kailua-Kona, HI
# https://mathnet.mit.edu/explorer.html?p=imo_2024_7db46b

"""Illustrate the geometry in the supplied problem using random triangles.

Install Matplotlib if needed: python -m pip install matplotlib
Run this file: python geometry_angles.py
The numerical angle sums illustrate the result; they are not a proof.
"""

from math import acos, cos, degrees, hypot, pi, sin, sqrt
from random import uniform

import matplotlib.pyplot as plt
from matplotlib.patches import Circle

# Change these settings to control the number and speed of the drawings.
NUMBER_OF_TRIALS = 100
PAUSE_SECONDS = 2

# A point is a tuple (x, y). For example, A = (0, 0).
# Tuple unpacking, such as x, y = A, gives names to its two coordinates.


def distance(a, b):
    """Return the straight-line distance between two points."""
    return hypot(b[0] - a[0], b[1] - a[1])


def midpoint(a, b):
    """Average the coordinates to find the midpoint of a segment."""
    return ((a[0] + b[0]) / 2, (a[1] + b[1]) / 2)


def angle_from_sides(a, b, opposite):
    """Return the angle between sides a and b, in radians."""
    if min(a, b, opposite) <= 0 or not abs(a - b) < opposite < a + b:
        raise ValueError("The side lengths must form a nondegenerate triangle.")
    cosine = (a * a + b * b - opposite * opposite) / (2 * a * b)
    # Rounding can put the cosine just outside the allowed interval [-1, 1].
    return acos(max(-1.0, min(1.0, cosine)))


def angle_at(a, vertex, b):
    """Return angle a-vertex-b, with the middle point as its vertex."""
    return angle_from_sides(
        distance(a, vertex), distance(vertex, b), distance(a, b)
    )


def incircle(a, b, c):
    """Return the incenter and radius of the triangle's incircle."""
    side_a = distance(b, c)  # The side opposite A.
    side_b = distance(a, c)
    side_c = distance(a, b)
    perimeter = side_a + side_b + side_c
    center = (
        (side_a * a[0] + side_b * b[0] + side_c * c[0]) / perimeter,
        (side_a * a[1] + side_b * b[1] + side_c * c[1]) / perimeter,
    )
    # The cross product gives twice the triangle's area.
    twice_area = abs(
        (b[0] - a[0]) * (c[1] - a[1])
        - (b[1] - a[1]) * (c[0] - a[0])
    )
    return center, twice_area / perimeter


def circumcircle(a, b, c):
    """Return the center and radius of the circle through A, B, and C.

    This drawing places A at (0, 0) and B on the positive x-axis.
    The perpendicular bisector of AB therefore has x = B.x / 2.
    """
    center_x = b[0] / 2
    center_y = (c[0] ** 2 + c[1] ** 2 - 2 * center_x * c[0]) / (2 * c[1])
    center = (center_x, center_y)
    return center, distance(center, a)


def line_intersection(a, direction, b, other_direction):
    """Intersect the lines a + t*direction and b + u*other_direction.

    A direction is a tuple (dx, dy), so vertical lines need no special case.
    These are infinite lines, rather than just the segments between points.
    """
    dx, dy = direction
    ex, ey = other_direction
    determinant = dx * ey - dy * ex
    if abs(determinant) < 1e-12:
        raise ValueError("The lines are parallel or coincident.")
    t = ((b[0] - a[0]) * ey - (b[1] - a[1]) * ex) / determinant
    return (a[0] + t * dx, a[1] + t * dy)


def draw_segment(ax, a, b, **style):
    """Draw a segment; **style passes color and other options to Matplotlib."""
    ax.plot([a[0], b[0]], [a[1], b[1]], **style)


def draw_example(ax, ab, ac, bc):
    """Construct and label one triangle; return the angle sum in degrees."""
    theta = angle_from_sides(ab, ac, bc)
    A = (0.0, 0.0)
    B = (ab, 0.0)
    C = (ac * cos(theta), ac * sin(theta))
    K = midpoint(A, B)
    L = midpoint(A, C)
    I, radius = incircle(A, B, C)
    O, circumradius = circumcircle(A, B, C)

    # AC's unit direction has length 1. Its right-hand perpendicular points
    # into the triangle. Moving 2*r in that direction gives the other
    # tangent parallel to AC (AC itself is already one tangent).
    direction_ac = (cos(theta), sin(theta))
    tangent_start = (2 * radius * sin(theta), -2 * radius * cos(theta))
    direction_bc = (C[0] - B[0], C[1] - B[1])
    X = line_intersection(tangent_start, direction_ac, B, direction_bc)
    M = line_intersection(tangent_start, direction_ac, A, (1.0, 0.0))

    # AB is horizontal at y = 0; its other parallel tangent is y = 2*r.
    Y = line_intersection((0.0, 2 * radius), (1.0, 0.0), B, direction_bc)
    horizontal_start = (0.0, 2 * radius)

    # A is the origin and lies on the circumcircle. Substituting P = t*I
    # into |P-O|^2 = R^2 gives roots t=0 (A) and the value below (P).
    t = 2 * (I[0] * O[0] + I[1] * O[1]) / (I[0] ** 2 + I[1] ** 2)
    P = (t * I[0], t * I[1])
    angle_sum = degrees(angle_at(K, I, L) + angle_at(Y, P, X))

    ax.clear()  # Replace the previous drawing with the current one.
    ax.add_patch(Circle(I, radius, fill=False, color="tab:orange"))
    ax.add_patch(Circle(O, circumradius, fill=False, color="tab:blue"))
    for first, second in [(A, B), (B, C), (C, A)]:
        draw_segment(ax, first, second, color="black", linewidth=1.2)
    draw_segment(ax, M, X, color="tab:green")
    draw_segment(ax, horizontal_start, Y, color="tab:green")
    draw_segment(ax, A, P, color="gray", linestyle="--", linewidth=1)

    # Fill the two triangles whose angles we are comparing.
    for vertices in [(K, I, L), (Y, P, X)]:
        ax.fill(
            [point[0] for point in vertices],
            [point[1] for point in vertices],
            color="lightblue", edgecolor="blue", linewidth=1.5, alpha=0.5,
        )

    # The image supplies these point names. Show each name and its computed
    # (x, y) coordinates, rounded to two decimal places for readability.
    points = {"A": A, "B": B, "C": C, "I": I, "K": K, "L": L,
              "X": X, "Y": Y, "P": P}
    offsets = {"A": (-12, -26), "B": (8, -24), "C": (8, 12),
               "I": (8, -24), "K": (0, -26), "L": (-80, 10),
               "X": (18, -6), "Y": (10, 16), "P": (8, 12)}
    for name, point in points.items():
        ax.plot(*point, "o", color="black", markersize=4)
        ax.annotate(
            f"{name} ({point[0]:.2f}, {point[1]:.2f})", point,
            xytext=offsets[name], textcoords="offset points", fontsize=9,
            bbox={"facecolor": "white", "alpha": 0.8, "edgecolor": "none"},
        )

    ax.set_title(f"∠KIL + ∠YPX = {angle_sum:.3f}°")
    # Equal scale keeps circles round and angles visually accurate.
    ax.set_aspect("equal", adjustable="box")
    ax.autoscale_view()
    ax.margins(0.22)
    ax.axis("off")
    return angle_sum


def main():
    """Try random side lengths and display the valid examples."""
    fig, ax = plt.subplots(figsize=(12, 9))
    for _ in range(NUMBER_OF_TRIALS):
        if not plt.fignum_exists(fig.number):
            break  # Stop the animation if the user closes the window.
        ab = uniform(2, 20)
        ac = uniform(ab, 25)
        bc = uniform(ac, 30)
        # Enforce AB < AC < BC and the triangle inequality before using acos.
        if not 0 < ab < ac < bc < ab + ac:
            continue
        theta = angle_from_sides(ab, ac, bc)
        if not pi / 6 < theta < 5 * pi / 6:
            continue  # Avoid extremely narrow or wide triangles.
        draw_example(ax, ab, ac, bc)
        plt.pause(PAUSE_SECONDS)
    plt.show()


# Run the animation only when this file is executed directly.
# Importing it from another Python file leaves its functions available.
if __name__ == "__main__":
    main()
