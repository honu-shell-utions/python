"""
Jim McCleery
April 29, 2026
Kailua-Kona, HI

Problem:
Circumcircle intersections in a parallelogram

Let ABCD be a parallelogram, and let O be a point inside ABCD.
Suppose the circumcircles of triangles OAB and OCD intersect at P != O,
and the circumcircles of triangles OBC and OAD intersect at Q != O.

The program draws the configuration and displays angle POQ.
"""

from math import acos, cos, degrees, hypot, radians, sin, sqrt
from random import uniform

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Geometry helpers
# -----------------------------------------------------------------------------

def distance(p, q):
    """Return the Euclidean distance between two points."""
    return hypot(p[0] - q[0], p[1] - q[1])


def angle_opposite_side(side1, side2, opposite):
    """
    Return the angle opposite the side named 'opposite',
    using the Law of Cosines.
    """
    try:
        value = (side1**2 + side2**2 - opposite**2) / (2 * side1 * side2)

        # Guard against tiny floating-point errors.
        value = max(-1, min(1, value))

        return acos(value)

    except (ValueError, ZeroDivisionError):
        return None


def circle_through_three_points(p1, p2, p3):
    """
    Return the circle through three non-collinear points.

    The circle is returned as:

        (center_x, center_y, radius)

    Returns None if the points are collinear or nearly collinear.
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    temp = x2**2 + y2**2

    bc = (x1**2 + y1**2 - temp) / 2
    cd = (temp - x3**2 - y3**2) / 2

    det = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    if abs(det) < 1e-9:
        return None

    cx = (bc * (y2 - y3) - cd * (y1 - y2)) / det
    cy = ((x1 - x2) * cd - (x2 - x3) * bc) / det
    radius = distance((cx, cy), p1)

    return cx, cy, radius


def circle_circle_intersections(circle1, circle2):
    """
    Return the intersection points of two circles.

    Each circle is represented as:

        (center_x, center_y, radius)

    Returns an empty list if there are not two real intersection points.
    """
    x0, y0, r0 = circle1
    x1, y1, r1 = circle2

    d = distance((x0, y0), (x1, y1))

    if d == 0:
        return []

    if d > r0 + r1:
        return []

    if d < abs(r0 - r1):
        return []

    a = (r0**2 - r1**2 + d**2) / (2 * d)
    h_squared = r0**2 - a**2

    if h_squared < 0:
        return []

    h = sqrt(h_squared)

    x2 = x0 + a * (x1 - x0) / d
    y2 = y0 + a * (y1 - y0) / d

    rx = -(y1 - y0) * h / d
    ry = (x1 - x0) * h / d

    return [
        (x2 + rx, y2 + ry),
        (x2 - rx, y2 - ry),
    ]


def other_intersection(circle1, circle2, known_point):
    """
    Return the circle-intersection point that is not the known shared point.

    In this problem, each relevant pair of circles already shares O.
    The other intersection is either P or Q.
    """
    points = circle_circle_intersections(circle1, circle2)

    if len(points) != 2:
        return None

    points.sort(key=lambda point: distance(point, known_point))
    return points[1]


def polygon_fill_coordinates(vertices):
    """Return x- and y-coordinate lists for filling a closed polygon."""
    x_coords, y_coords = zip(*vertices)
    return list(x_coords) + [x_coords[0]], list(y_coords) + [y_coords[0]]


# -----------------------------------------------------------------------------
# Plotting helpers
# -----------------------------------------------------------------------------

def plot_segment(ax, p, q, **kwargs):
    """Plot the segment joining p and q."""
    ax.plot([p[0], q[0]], [p[1], q[1]], **kwargs)


def plot_circle(ax, circle, **kwargs):
    """Plot a circle."""
    cx, cy, radius = circle

    theta = np.linspace(0, 2 * np.pi, 800)

    x_values = cx + radius * np.cos(theta)
    y_values = cy + radius * np.sin(theta)

    ax.plot(x_values, y_values, **kwargs)


def label_point(ax, point, label, dx=0.12, dy=0.12):
    """Plot and label a point."""
    ax.plot(point[0], point[1], "o", markersize=5, color="black")
    ax.text(point[0] + dx, point[1] + dy, label, fontsize=13, weight="bold")


# -----------------------------------------------------------------------------
# Example generation
# -----------------------------------------------------------------------------

def generate_example():
    """
    Generate one visually clean instance of the problem.

    The constraints are chosen to avoid:
        - very flat parallelograms
        - O too close to the boundary
        - P and Q too close to O
        - diagrams where angle POQ is hard to see
    """
    # Build a reasonably shaped parallelogram.
    base = uniform(9, 13)
    side = uniform(0.55 * base, 0.85 * base)
    alpha = radians(uniform(40, 65))

    A = (0, 0)
    B = (base, 0)
    D = (side * cos(alpha), side * sin(alpha))
    C = (B[0] + D[0], B[1] + D[1])

    # Choose O safely inside ABCD.
    #
    # Since ABCD is a parallelogram, every interior point can be written as
    #
    #     O = uB + vD
    #
    # with 0 < u < 1 and 0 < v < 1.
    #
    # Keeping u and v away from 0 and 1 keeps O away from the edges.
    u = uniform(0.30, 0.70)
    v = uniform(0.30, 0.70)

    O = (
        u * B[0] + v * D[0],
        u * B[1] + v * D[1],
    )

    # Circumcircles from the problem statement.
    circle_OAB = circle_through_three_points(O, A, B)
    circle_OCD = circle_through_three_points(O, C, D)

    circle_OBC = circle_through_three_points(O, B, C)
    circle_OAD = circle_through_three_points(O, A, D)

    if None in [circle_OAB, circle_OCD, circle_OBC, circle_OAD]:
        return None

    # P is the second intersection of circles OAB and OCD.
    P = other_intersection(circle_OAB, circle_OCD, O)

    # Q is the second intersection of circles OBC and OAD.
    Q = other_intersection(circle_OBC, circle_OAD, O)

    if P is None or Q is None:
        return None

    # Reject cramped cases.
    if min(distance(O, P), distance(O, Q), distance(P, Q)) < 1.5:
        return None

    # Compute angle POQ, the angle at O.
    angle_POQ = angle_opposite_side(
        distance(O, P),
        distance(O, Q),
        distance(P, Q),
    )

    if angle_POQ is None:
        return None

    return {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "O": O,
        "P": P,
        "Q": Q,
        "circle_OAB": circle_OAB,
        "circle_OCD": circle_OCD,
        "circle_OBC": circle_OBC,
        "circle_OAD": circle_OAD,
        "angle_A": degrees(alpha),
        "angle_POQ": degrees(angle_POQ),
    }


# -----------------------------------------------------------------------------
# Drawing
# -----------------------------------------------------------------------------

def draw_example(example):
    """Draw one example of the configuration."""
    fig, ax = plt.subplots(figsize=(10, 7))

    A = example["A"]
    B = example["B"]
    C = example["C"]
    D = example["D"]
    O = example["O"]
    P = example["P"]
    Q = example["Q"]

    circles = [
        example["circle_OAB"],
        example["circle_OCD"],
        example["circle_OBC"],
        example["circle_OAD"],
    ]

    # Draw the four circumcircles.
    for circle in circles:
        plot_circle(ax, circle, color="blue", linewidth=1.2, alpha=0.65)

    # Draw the parallelogram ABCD.
    for start, end in [(A, B), (B, C), (C, D), (D, A)]:
        plot_segment(ax, start, end, color="black", linewidth=2)

    # Lightly shade the parallelogram.
    ax.fill(
        *polygon_fill_coordinates([A, B, C, D]),
        color="lightcyan",
        alpha=0.45,
    )

    # Draw the important angle POQ.
    plot_segment(ax, O, P, color="red", linewidth=2.5)
    plot_segment(ax, O, Q, color="red", linewidth=2.5)

    # Draw segment PQ faintly, just to make triangle POQ visible.
    plot_segment(ax, P, Q, color="red", linewidth=1.5, alpha=0.55)

    # Mark the midpoint of PQ, as in the sample diagram.
    M = ((P[0] + Q[0]) / 2, (P[1] + Q[1]) / 2)
    label_point(ax, M, "M", dx=0.12, dy=-0.35)

    # Label the main points.
    label_point(ax, A, "A", dx=-0.35, dy=0.15)
    label_point(ax, B, "B", dx=0.15, dy=0.15)
    label_point(ax, C, "C", dx=0.15, dy=-0.35)
    label_point(ax, D, "D", dx=-0.35, dy=-0.35)

    label_point(ax, O, "O", dx=0.15, dy=0.15)
    label_point(ax, P, "P", dx=0.15, dy=0.15)
    label_point(ax, Q, "Q", dx=-0.40, dy=-0.10)

    angle_A = example["angle_A"]
    angle_B = 180 - angle_A
    angle_POQ = example["angle_POQ"]

    ax.set_title(
        f"Angle A = {angle_A:.2f}°    "
        f"Angle B = {angle_B:.2f}°    "
        f"Angle POQ = {angle_POQ:.2f}°",
        fontsize=13,
    )

    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.25)

    plt.show()


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------

def main():
    """Find and draw ten clean examples."""
    examples_wanted = 20
    max_trials = 10_000

    examples_found = 0

    for _ in range(max_trials):
        example = generate_example()

        if example is not None:
            examples_found += 1
            draw_example(example)
            if examples_found == examples_wanted:
                return

    raise RuntimeError(
        f"Only found {examples_found} clean examples "
        f"after {max_trials} trials. Try relaxing the constraints."
    )

if __name__ == "__main__":
    main()
