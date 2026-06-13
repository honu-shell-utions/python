# Jim McCleery
# June 13, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2021_c9c535

from math import radians, sin, cos
from matplotlib.pyplot import plot, title, axis, show, text, fill, cla, pause
from random import uniform
import numpy as np


def plot_line(x1, y1, x2, y2):
    """
    Plots a straight line segment between two points: (x1, y1) and (x2, y2).
    """
    plot([x1, x2], [y1, y2], color="black", zorder=2)


def draw_angle_arc(cx, cy, start_deg, end_deg, radius, color="gainsboro"):
    """
    Draws a shaded geometric arc to represent an angle at a vertex.
    """
    angles = np.linspace(radians(start_deg), radians(end_deg), 50)
    x_coords = [cx] + [cx + radius * cos(a) for a in angles] + [cx]
    y_coords = [cy] + [cy + radius * sin(a) for a in angles] + [cy]
    fill(x_coords, y_coords, color=color, edgecolor="black", zorder=1)


# --- Main Simulation Loop ---
for _ in range(10):
    # 0. clear the graph
    cla()
    
    # 1. Define random lengths for our geometry
    AB = uniform(10, 20)  # Total square side length
    FD = uniform(3, AB / 2)  # Segment length for FD (keeps F well spaced from A)

    # 2. Match coordinates to the graphic layout:
    # A (top-left), B (bottom-left), C (bottom-right), D (top-right)
    x_a, y_a = 0, AB
    x_b, y_b = 0, 0
    x_c, y_c = AB, 0
    x_d, y_d = AB, AB

    # Point F sits on the top segment (AD), a distance of FD to the left of D
    x_f, y_f = AB - FD, AB

    # Point E extends out from D at an angle
    # The external angle CDE is 110 degrees. Downward vector DC is at 270 degrees.
    # 270 degrees - 110 degrees = 160 degrees (or -20 degrees from the horizontal)
    x_e = x_d + FD * cos(radians(20))
    y_e = y_d + FD * sin(radians(20))

    # Calculate target angle AFE
    angle_afe = 180 - 0.5 * (180 - (270 - 110))

    # 3. Draw the Outer Square Edges
    plot_line(x_a, y_a, x_b, y_b)  # Left (AB)
    plot_line(x_b, y_b, x_c, y_c)  # Bottom (BC)
    plot_line(x_c, y_c, x_d, y_d)  # Right (CD)
    plot_line(x_d, y_d, x_a, y_a)  # Top (DA)

    # 4. Draw the Triangle Lines
    plot_line(x_f, y_f, x_e, y_e)  # Line FE
    plot_line(x_d, y_d, x_e, y_e)  # Line DE

    # 5. Draw the Black Marker Dots at Vertices
    pts_x = [x_a, x_b, x_c, x_d, x_f, x_e]
    pts_y = [y_a, y_b, y_c, y_d, y_f, y_e]
    plot(pts_x, pts_y, "ko", zorder=3)  # 'ko' plots black circles

    # 6. Add Text Labels for Vertices (with slight padding offsets)
    offset = AB * 0.04
    text(x_a - offset, y_a + offset, "A", fontsize=12, style="italic")
    text(x_b - offset, y_b - 2 * offset * 1.5, "B", fontsize=12, style="italic")
    text(x_c + offset, y_b - 2 * offset * 1.5, "C", fontsize=12, style="italic")
    text(x_d - offset, y_d + .3 * offset * 1.5, "D", fontsize=12, style="italic")
    text(x_f - offset, y_f + offset, "F", fontsize=12, style="italic")
    text(x_e + offset, y_e + offset, "E", fontsize=12, style="italic")
    
    # 7. Draw the Shaded 110-Degree Angle Arc at Vertex D
    # Arc swings from -90 degrees (straight down) to 20 degrees (direction of E)
    arc_radius = AB * 0.15
    draw_angle_arc(x_d, y_d, -90, 20, arc_radius)
    text(
        x_d + arc_radius * 0.5,
        y_d - arc_radius * 1.2,
        r"$110^\circ$",
        fontsize=11,
    )

    # 8. Render Plot Properties
    title(f"The angle AFE = {angle_afe} degrees")
    axis("equal")
    axis("off")
    pause(2.0)
show()
