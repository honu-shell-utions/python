# -----------------------------------------------------------------------------
# Jim McCleery
# May 1, 2026
# Kailua-Kona, HI
# -----------------------------------------------------------------------------
"""
Geometry drawing inspired by:
https://youtu.be/hCznRtWwhZM?si=BzC1UdmQR12M5muE

The construction produces seven congruent red squares.
Each square has side length sqrt(2), so the total red area is:

    7 * (sqrt(2))^2 = 14
"""
# -----------------------------------------------------------------------------

from math import cos, sin, radians, sqrt
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Basic drawing helpers
# -----------------------------------------------------------------------------

def plot_segment(ax, p1, p2, **style):
    """Draw a line segment from p1 to p2."""
    x_values = [p1[0], p2[0]]
    y_values = [p1[1], p2[1]]
    ax.plot(x_values, y_values, **style)


def polygon_fill_coordinates(vertices):
    """
    Return x- and y-coordinate lists for a closed polygon.

    Matplotlib's fill() function expects separate x and y lists.
    The first vertex is repeated at the end so the polygon closes cleanly.
    """
    x_values = [point[0] for point in vertices]
    y_values = [point[1] for point in vertices]

    x_values.append(vertices[0][0])
    y_values.append(vertices[0][1])

    return x_values, y_values


def rotate_point(point, angle):
    """Rotate a point counterclockwise about the origin."""
    x, y = point

    rotated_x = x * cos(angle) - y * sin(angle)
    rotated_y = x * sin(angle) + y * cos(angle)

    return rotated_x, rotated_y


def rotate_points(points, angle):
    """Rotate a list of points counterclockwise about the origin."""
    return [rotate_point(point, angle) for point in points]


def draw_filled_square(ax, lower_left, side_length, angle):
    """
    Draw a square whose first side makes angle 'angle' with the positive x-axis.

    The square is constructed from one starting vertex and two perpendicular
    edge directions.
    """
    x, y = lower_left

    edge_x = side_length * cos(angle)
    edge_y = side_length * sin(angle)

    perp_x = -side_length * sin(angle)
    perp_y = side_length * cos(angle)

    p0 = (x, y)
    p1 = (x + edge_x, y + edge_y)
    p2 = (x + edge_x + perp_x, y + edge_y + perp_y)
    p3 = (x + perp_x, y + perp_y)

    square_vertices = [p0, p1, p2, p3]

    ax.fill(
        *polygon_fill_coordinates(square_vertices),
        color="red",
        edgecolor="black",
        linewidth=2,
        alpha=0.85
    )


def label_point(ax, point, label, dx=0.08, dy=0.08):
    """Add a text label near a point."""
    x, y = point
    ax.text(
        x + dx,
        y + dy,
        label,
        fontsize=12,
        fontweight="bold",
        ha="center",
        va="center"
    )


# -----------------------------------------------------------------------------
# Main construction
# -----------------------------------------------------------------------------

def main():
    fig, ax = plt.subplots(figsize=(8, 8))

    # Exact values found from the geometry.
    # The original program searched randomly for these values.
    s = 2 + 2 * sqrt(3)
    square_side = sqrt(2)
    theta = radians(15)

    # Main outer vertices.
    A = (0, 0)
    B = (0, s)
    C = (-s, s)
    D = (-s, 0)
    E = (4 - s, s)

    # These are the lower-left starting vertices for the 4-by-5 tilted grid
    # from which the seven red squares are selected.
    grid_points = [
        (0, 0),      (0, square_side),      (0, 2 * square_side),      (0, 3 * square_side),
        (-square_side, 0), (-square_side, square_side), (-square_side, 2 * square_side), (-square_side, 3 * square_side),
        (-2 * square_side, 0), (-2 * square_side, square_side), (-2 * square_side, 2 * square_side), (-2 * square_side, 3 * square_side),
        (-3 * square_side, 0), (-3 * square_side, square_side), (-3 * square_side, 2 * square_side), (-3 * square_side, 3 * square_side),
        (-4 * square_side, 0), (-4 * square_side, square_side), (-4 * square_side, 2 * square_side), (-4 * square_side, 3 * square_side),
    ]

    # Rotate the grid so the small squares match the slant of the construction.
    rotated_grid_points = rotate_points(grid_points, theta)

    # These are the seven selected grid positions.
    selected_square_numbers = {1, 2, 7, 8, 10, 15, 18}

    for square_number, point in enumerate(rotated_grid_points, start=1):
        if square_number in selected_square_numbers:
            draw_filled_square(ax, point, square_side, theta)

    # Draw the outside construction lines.
    line_style = {"color": "black", "linewidth": 2}

    plot_segment(ax, A, B, **line_style)
    plot_segment(ax, B, C, **line_style)
    plot_segment(ax, C, D, **line_style)
    plot_segment(ax, D, A, **line_style)
    plot_segment(ax, A, E, **line_style)

    # Label the main vertices.
    label_point(ax, A, "A", dx=0.15, dy=-0.15)
    label_point(ax, B, "B", dx=0.15, dy=0.15)
    label_point(ax, C, "C", dx=-0.15, dy=0.15)
    label_point(ax, D, "D", dx=-0.15, dy=-0.15)
    label_point(ax, E, "E", dx=0.15, dy=0.15)

    # Compute and display the total red area.
    red_area = 7 * square_side**2

    ax.set_title(f"Red Area = {red_area:.0f}", fontsize=16)
    ax.set_aspect("equal", adjustable="box")
    ax.axis("off")

    plt.show()


# -----------------------------------------------------------------------------

if __name__ == "__main__":
    main()
