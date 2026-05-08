"""
Jim McCleery
May 8, 2026
Kailua-Kona, HI

Source:
https://youtu.be/FsLKCCx8hoc?si=BaLsQ6vod9ivFyfD
"""

from math import acos, cos, hypot, pi, sin
import matplotlib.pyplot as plt


# ----------------------------------------------------------------------------- 
# Geometry helper functions
# -----------------------------------------------------------------------------

def distance(point_a, point_b):
    """Return the Euclidean distance between two points."""
    x1, y1 = point_a
    x2, y2 = point_b
    return hypot(x2 - x1, y2 - y1)


def angle_opposite_side(side_a, side_b, opposite_side):
    """
    Return the angle opposite 'opposite_side' using the Law of Cosines.

    The triangle has side lengths:
        side_a, side_b, opposite_side
    """
    cosine_value = (
        side_a**2 + side_b**2 - opposite_side**2
    ) / (2 * side_a * side_b)

    # Protect against tiny floating-point roundoff errors.
    cosine_value = max(-1.0, min(1.0, cosine_value))

    return acos(cosine_value)


def line_intersection(m1, b1, m2, b2):
    """
    Return the intersection point of two non-parallel lines.

    Each line is written in slope-intercept form:
        y = m*x + b
    """
    if abs(m1 - m2) < 1e-12:
        raise ValueError("The two lines are parallel or nearly parallel.")

    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1

    return x, y


# ----------------------------------------------------------------------------- 
# Main geometry construction
# -----------------------------------------------------------------------------

def build_figure(theta):
    """
    Build the points in the diagram for a given angle theta.

    Returns:
        points: dictionary containing vertices A, B, C, D, E
        alpha: angle used in the condition alpha = 2*beta
        beta:  angle used in the condition alpha = 2*beta
    """

    # Fixed base points.
    point_a = (0.0, 0.0)
    point_b = (40.0, 0.0)

    # Construct point C using the chosen angle theta.
    point_c = (
        25 * cos(pi - 3 * theta),
        25 * sin(pi - 3 * theta)
    )

    # Point D is 25 units horizontally to the right of C.
    point_d = (
        point_c[0] + 25,
        point_c[1]
    )

    # Line BC.
    m_bc = (point_c[1] - point_b[1]) / (point_c[0] - point_b[0])
    b_bc = point_b[1] - m_bc * point_b[0]

    # Line through D perpendicular to BC.
    m_de = -1 / m_bc
    b_de = point_d[1] - m_de * point_d[0]

    # Point E is the intersection of BC and the perpendicular line through D.
    point_e = line_intersection(m_bc, b_bc, m_de, b_de)

    # Compute alpha.
    length_bc = distance(point_b, point_c)
    alpha = angle_opposite_side(25, length_bc, 40)

    # Compute beta.
    length_ce = distance(point_c, point_e)
    length_de = distance(point_d, point_e)
    beta = angle_opposite_side(25, length_ce, length_de)

    points = {
        "A": point_a,
        "B": point_b,
        "C": point_c,
        "D": point_d,
        "E": point_e,
    }

    return points, alpha, beta


def angle_error(theta):
    """
    Return alpha - 2*beta.

    The desired diagram occurs when this value is zero.
    """
    _, alpha, beta = build_figure(theta)
    return alpha - 2 * beta


def solve_for_theta(tolerance=1e-12):
    """
    Find theta such that alpha = 2*beta.
    Uses bisection.
    """
    low = pi / 6
    high = pi / 3 - 1e-9

    error_low = angle_error(low)
    error_high = angle_error(high)

    if error_low * error_high > 0:
        raise ValueError("Bisection failed: no sign change found.")

    while high - low > tolerance:
        mid = (low + high) / 2
        error_mid = angle_error(mid)

        if error_low * error_mid <= 0:
            high = mid
            error_high = error_mid
        else:
            low = mid
            error_low = error_mid

    return (low + high) / 2


# ----------------------------------------------------------------------------- 
# Plotting functions
# -----------------------------------------------------------------------------

def plot_segment(ax, point_a, point_b, label=None):
    """Draw a line segment between two points."""
    ax.plot(
        [point_a[0], point_b[0]],
        [point_a[1], point_b[1]],
        linewidth=2,
        label=label
    )


def label_point(ax, name, point, dx=0.6, dy=0.6):
    """Place a vertex label near a point."""
    ax.text(
        point[0] + dx,
        point[1] + dy,
        name,
        fontsize=12,
        fontweight="bold"
    )


def draw_diagram(points):
    """Draw the final geometric diagram."""

    point_a = points["A"]
    point_b = points["B"]
    point_c = points["C"]
    point_d = points["D"]
    point_e = points["E"]

    x_length = distance(point_b, point_e)

    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw the diagram segments.
    plot_segment(ax, point_a, point_b)
    plot_segment(ax, point_a, point_c)
    plot_segment(ax, point_b, point_c)
    plot_segment(ax, point_b, point_d)
    plot_segment(ax, point_c, point_d)
    plot_segment(ax, point_d, point_e)

    # Mark and label the vertices.
    for name, point in points.items():
        ax.scatter(point[0], point[1], s=35)
        label_point(ax, name, point)

    # Label the requested line segment.
    midpoint_x = (point_b[0] + point_e[0]) / 2
    midpoint_y = (point_b[1] + point_e[1]) / 2
    ax.text(
        midpoint_x,
        midpoint_y - 1.2,
        f"x = {x_length:.2f}",
        fontsize=12,
        fontweight="bold"
    )

    ax.set_title(f"Length of line segment x = {x_length:.2f}")
    ax.set_aspect("equal", adjustable="box")
    ax.grid(True, alpha=0.3)

    plt.show()


# ----------------------------------------------------------------------------- 
# Program entry point
# -----------------------------------------------------------------------------

def main():
    """Solve the geometry condition and draw the resulting diagram."""
    theta = solve_for_theta()
    points, _, _ = build_figure(theta)
    draw_diagram(points)


if __name__ == "__main__":
    main()
