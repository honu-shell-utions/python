"""
Jim McCleery
April 18, 2026
Kailua-Kona, HI

https://youtu.be/LlVaguCF1xE?si=x8hu5yB0zQWGVhlO
"""

# -----------------------------------------------------------------------------
# Pipe-through-corridor simulation
#
# This program simulates a straight pipe being placed through a right-angled
# corridor. It repeatedly generates a candidate pipe position, draws the
# corridor and the pipe, and keeps track of the shortest pipe length found.
#
# The geometry is:
#   - A vertical corridor of width 18
#   - A horizontal corridor of width 12
#   - Variable corridor heights/lengths are chosen randomly
#
# Coordinate labels are added to help visualize the construction.
# -----------------------------------------------------------------------------

from math import sqrt
from random import uniform

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Geometry helper functions
# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """Return the Euclidean distance between two points."""
    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


def plot_segment(ax, p1, p2, **kwargs):
    """Plot a line segment between points p1 and p2."""
    ax.plot([p1[0], p2[0]], [p1[1], p2[1]], **kwargs)


def label_point(ax, name, point, dx=0.4, dy=0.4):
    """
    Label a point on the plot.

    Parameters:
        ax: matplotlib axes
        name: point label such as 'P0'
        point: (x, y)
        dx, dy: small offsets so the text does not sit directly on the point
    """
    x, y = point
    ax.plot(x, y, marker="o", markersize=4)
    ax.text(x + dx, y + dy, f"{name} ({x:.2f}, {y:.2f})", fontsize=9)


# -----------------------------------------------------------------------------
# Main simulation
# -----------------------------------------------------------------------------
def main():
    """Run the pipe-through-corridor simulation."""
    # Fixed corridor widths
    vertical_width = 18
    horizontal_width = 12

    # Random corridor dimensions
    h = uniform(12, 50)
    w = uniform(18, 50)

    # Best (smallest) pipe length found so far
    min_length = float("inf")

    # Interactive plotting
    plt.ion()
    fig, ax = plt.subplots()

    for _ in range(1000):
        ax.clear()

        # ---------------------------------------------------------------------
        # Define corridor boundary points
        #
        # P0 ---- P1
        # |       |
        # |       P2 ---- P3
        # |               |
        # P5 ----------- P4
        #
        # with the "corner corridor" shape determined by h and w.
        # ---------------------------------------------------------------------
        p0 = (0, 0)
        p1 = (vertical_width, 0)
        p2 = (vertical_width, h)
        p3 = (vertical_width + w, h)
        p4 = (vertical_width + w, h + horizontal_width)
        p5 = (0, h + horizontal_width)

        # Random point P6 on the left wall of the vertical corridor
        p6 = (0, uniform(0, h))

        # ---------------------------------------------------------------------
        # Construct the candidate pipe.
        #
        # The pipe starts at P6 and passes through P2. It continues until it
        # meets the top horizontal boundary y = p4[1]. That intersection is P7.
        # ---------------------------------------------------------------------
        slope = (p2[1] - p6[1]) / (p2[0] - p6[0])
        x7 = (p5[1] - p2[1] + slope * p2[0]) / slope
        p7 = (x7, p4[1])

        # If the pipe exits beyond the right boundary, reject this trial
        if p7[0] > p3[0]:
            continue

        # Compute pipe length
        pipe_length = distance(p6[0], p6[1], p7[0], p7[1])
        min_length = min(min_length, pipe_length)

        # ---------------------------------------------------------------------
        # Draw corridor
        # ---------------------------------------------------------------------
        plot_segment(ax, p0, p1, color="black")
        plot_segment(ax, p1, p2, color="black")
        plot_segment(ax, p2, p3, color="black")
        plot_segment(ax, p3, p4, color="black")
        plot_segment(ax, p4, p5, color="black")
        plot_segment(ax, p5, p0, color="black")

        # Draw candidate pipe
        plot_segment(ax, p6, p7, color="blue", linewidth=2)

        # ---------------------------------------------------------------------
        # Label points
        # ---------------------------------------------------------------------
        label_point(ax, "P0", p0)
        label_point(ax, "P1", p1)
        label_point(ax, "P2", p2)
        label_point(ax, "P3", p3)
        label_point(ax, "P4", p4)
        label_point(ax, "P5", p5)
        label_point(ax, "P6", p6)
        label_point(ax, "P7", p7)

        # Plot formatting
        ax.set_aspect("equal")
        ax.set_title(
            f"Pipe length: {pipe_length:.2f}    "
            f"Shortest found so far: {min_length:.2f}"
        )
        ax.set_xlabel("x")
        ax.set_ylabel("y")
        ax.grid(True, alpha=0.3)

        plt.pause(0.5)

    plt.ioff()
    plt.show()


# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()
