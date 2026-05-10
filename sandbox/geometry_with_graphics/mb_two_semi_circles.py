"""
Jim McCleery
May 10, 2026
Kailua-Kona, HI

Reference:
https://youtu.be/GuyiAQXrigw?si=UJkA7S0Y0r2UCnSN
"""

from dataclasses import dataclass
from math import atan2, hypot, pi, sqrt

import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# Basic geometry data structure
# -----------------------------------------------------------------------------

@dataclass(frozen=True)
class Point:
    """A point in the plane."""
    x: float
    y: float


# -----------------------------------------------------------------------------
# Geometry helper functions
# -----------------------------------------------------------------------------

def circle_circle_intersections(
    center1: Point,
    radius1: float,
    center2: Point,
    radius2: float,
) -> tuple[Point, Point]:
    """
    Return the two intersection points of two circles.

    Raises:
        ValueError: if the circles do not intersect in two distinct points.
    """
    dx = center2.x - center1.x
    dy = center2.y - center1.y
    d = hypot(dx, dy)

    if d == 0:
        raise ValueError("The circles have the same center.")

    if d > radius1 + radius2:
        raise ValueError("The circles are separate and do not intersect.")

    if d < abs(radius1 - radius2):
        raise ValueError("One circle lies inside the other without intersection.")

    # Distance from center1 to the midpoint of the common chord
    a = (radius1**2 - radius2**2 + d**2) / (2 * d)

    # Half-length of the common chord
    h = sqrt(radius1**2 - a**2)

    # Midpoint of the common chord
    xm = center1.x + a * dx / d
    ym = center1.y + a * dy / d

    # Offset from the midpoint to each intersection point
    rx = -dy * h / d
    ry = dx * h / d

    p1 = Point(xm + rx, ym + ry)
    p2 = Point(xm - rx, ym - ry)

    return p1, p2


# -----------------------------------------------------------------------------
# Plotting helper functions
# -----------------------------------------------------------------------------

def plot_segment(ax: plt.Axes, p1: Point, p2: Point) -> None:
    """Plot a line segment between two points."""
    ax.plot([p1.x, p2.x], [p1.y, p2.y], color="black")


def plot_circle_arc(
    ax: plt.Axes,
    center: Point,
    radius: float,
    start_angle: float,
    stop_angle: float,
    num_points: int = 1000,
) -> None:
    """Plot a circular arc."""
    angles = np.linspace(start_angle, stop_angle, num_points)
    x_vals = center.x + radius * np.cos(angles)
    y_vals = center.y + radius * np.sin(angles)
    ax.plot(x_vals, y_vals, color="black")


def fill_sector(
    ax: plt.Axes,
    center: Point,
    radius: float,
    start_angle: float,
    stop_angle: float,
    color: str = "red",
    alpha: float = 0.6,
    num_points: int = 1000,
) -> None:
    """Fill a sector of a circle."""
    angles = np.linspace(start_angle, stop_angle, num_points)
    x_vals = center.x + radius * np.cos(angles)
    y_vals = center.y + radius * np.sin(angles)
    ax.fill(x_vals, y_vals, color=color, alpha=alpha)


def plot_labeled_point(
    ax: plt.Axes,
    point: Point,
    label: str,
    dx: float = 0.08,
    dy: float = 0.08,
) -> None:
    """Plot a point and place a label nearby."""
    ax.plot(point.x, point.y, "o", color="black")
    ax.text(point.x + dx, point.y + dy, label, fontsize=12, fontweight="bold")


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------

def main() -> None:
    """
    Draw the figure and shade the correct half of the small circle.
    """

    # Large semicircle centered at O with radius 4
    R = 4
    O = Point(0, 0)
    left_end = Point(-R, 0)
    right_end = Point(R, 0)

    # Two given points on the x-axis
    A = Point(-1, 0)
    B = Point(2, 0)

    # Small circle:
    # It passes through A and B and has radius 3.
    # Since AB = 3, the center lies on the perpendicular bisector of AB.
    r = 3
    C = Point(0.5, 3 * sqrt(3) / 2)

    # Intersections of the two circles
    P, Q = circle_circle_intersections(C, r, O, R)

    # Put the rightmost point into P and the leftmost into Q for consistency
    if P.x < Q.x:
        P, Q = Q, P

    # The segment PQ is the diameter of the red semicircle.
    # We want to shade the OTHER half of the small circle.
    diameter_angle = atan2(Q.y - P.y, Q.x - P.x)
    start_angle = diameter_angle
    stop_angle = diameter_angle + pi

    # Area of the red semicircle
    red_area = pi * r**2 / 2

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 6))

    # Draw the large diameter and large upper semicircle
    plot_segment(ax, left_end, right_end)
    plot_circle_arc(ax, O, R, 0, pi)

    # Draw the diameter PQ of the small semicircle
    plot_segment(ax, P, Q)

    # Shade and draw the correct half of the small circle
    fill_sector(ax, C, r, start_angle, stop_angle, color="red", alpha=0.6)
    plot_circle_arc(ax, C, r, start_angle, stop_angle)

    # Label the main points
    plot_labeled_point(ax, O, "O", dx=-0.20, dy=-0.30)
    plot_labeled_point(ax, C, "C", dx=0.10, dy=0.10)
    plot_labeled_point(ax, A, "A", dx=-0.05, dy=-0.35)
    plot_labeled_point(ax, B, "B", dx=-0.05, dy=-0.35)
    plot_labeled_point(ax, P, "P", dx=0.08, dy=0.08)
    plot_labeled_point(ax, Q, "Q", dx=-0.30, dy=0.08)

    # Final formatting
    ax.set_title(f"Area of red semicircle = {red_area:.5f}")
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    plt.show()


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
