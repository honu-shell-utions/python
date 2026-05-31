# -----------------------------------------------------------------------------
# Jim McCleery
# May 31, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_6dbc98
# -----------------------------------------------------------------------------

# Import math functions for geometry calculations
from math import pi, sqrt, sin, cos, asin

# Import plotting tools from matplotlib
from matplotlib.pyplot import cla, fill, title, axis, pause, show, plot, text
from random import uniform


# -----------------------------------------------------------------------------
def circle_circle_intersections(x0, y0, r0, x1, y1, r1):
    """
    Calculates where two circles overlap and cross each other.

    Parameters:
        x0, y0: Center coordinates of the first circle
        r0:     Radius of the first circle
        x1, y1: Center coordinates of the second circle
        r1:     Radius of the second circle

    Returns:
        (x3, y3, x4, y4, True)  if the circles cross (returns both points)
        (0, 0, 0, 0, False)     if they don't cross or there is an error
    """
    try:
        # Distance between the two circle centers
        d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

        # Distance from center 0 to the chord line connecting the intersections
        a = (r0**2 - r1**2 + d**2) / (2 * d)

        # Half the length of the chord line connecting the intersections
        h = sqrt(r0**2 - a**2)

        # Midpoint on the line between the two circle centers
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d

        # Calculate the first intersection point
        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d

        # Calculate the second intersection point
        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d

        return x3, y3, x4, y4, True
    except (ZeroDivisionError, ValueError):
        # Handles cases where circles don't intersect or overlap identically
        return 0, 0, 0, 0, False


# -----------------------------------------------------------------------------
def plot_circle(x, y, radius):
    """
    Plots a complete circle by breaking it into a sequence of small segments.
    """
    import numpy as np

    # Create an array of 300 steps between 0 and 2*pi radians (a full circle)
    angle = np.linspace(0, 2 * pi, 300)

    # Use trigonometry to get the perimeter x and y coordinates
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y

    # Draw the circle boundary line
    plot(x_arr, y_arr, color="black", linestyle="--", alpha=0.5)


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2, color="gray"):
    """
    Plots a straight line connecting point (x1, y1) to point (x2, y2).
    """
    plot([x1, x2], [y1, y2], color=color)


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Calculates the area of any polygon using the Shoelace formula.
    """
    n = len(vertices)
    area = 0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2

    return abs(area) / 2


# -----------------------------------------------------------------------------
def polygon_fill_coordinates(vertices):
    """
    Prepares coordinate lists to shade inside a polygon layout.
    """
    x_coords, y_coords = zip(*vertices)

    # Close the shape loop by returning to the first point
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]

    return x_coords, y_coords


# -----------------------------------------------------------------------------
# Main Visual Loop
# -----------------------------------------------------------------------------
for _ in range(20):
    cla()

    # Generate random sizes for the two circles
    r = uniform(1, 2)  # Left circle radius (kept minimum size 1 for text readability)
    R = uniform(r, 4)  # Right circle radius

    # Anchor center points for both circles
    x0, y0 = 0, 0
    x1, y1 = r + R + 2, 0  # Spaced out extra to make text readable

    # Determine intersection geometries for the construction lines
    d_left = sqrt((r + R + 2) ** 2 - R**2)
    x2, y2, x3, y3, _ = circle_circle_intersections(x0, y0, d_left, x1, y1, R)

    d_right = sqrt((r + R + 2) ** 2 - r**2)
    x4, y4, x5, y5, _ = circle_circle_intersections(x1, y1, d_right, x0, y0, r)

    # Use basic trig relationships to find matching tangent contact points
    alpha = asin(R / (r + R + 2))
    beta = asin(r / (r + R + 2))

    # Identify the precise 4 corners of the common tangent belt
    x6, y6 = r * cos(alpha), r * sin(alpha)
    x7, y7 = x1 + R * cos(pi - beta), y1 + R * sin(pi - beta)
    x8, y8 = x1 + R * cos(pi + beta), y1 + R * sin(pi + beta)
    x9, y9 = r * cos(-alpha), r * sin(-alpha)

    # Gather points, fill the inner tangent section red, and find its area
    vertices = [(x6, y6), (x7, y7), (x8, y8), (x9, y9)]
    fill(
        *polygon_fill_coordinates(vertices),
        color="red",
        edgecolor="darkred",
        linewidth=2,
        alpha=0.4,
    )
    area = polygon_area(vertices)

    # Draw structural reference shapes (Circles and Baseline)
    plot_circle(x0, y0, r)
    plot_circle(x1, y1, R)
    plot_line(x0, y0, x1, y1, color="blue")

    # Draw triangular projection lines for the left intersection points
    plot_line(x0, y0, x2, y2)
    plot_line(x0, y0, x3, y3)
    plot_line(x2, y2, x1, y1)
    plot_line(x3, y3, x1, y1)
    plot_line(x3, y3, x2, y2)

    # Draw triangular projection lines for the right intersection points
    plot_line(x4, y4, x1, y1)
    plot_line(x5, y5, x1, y1)
    plot_line(x0, y0, x4, y4)
    plot_line(x0, y0, x5, y5)
    plot_line(x4, y4, x5, y5)

    # -------------------------------------------------------------------------
    # ADD DYNAMIC COORDINATE LABELS TO THE GRAPHIC
    # -------------------------------------------------------------------------
    # Circle Centers
    text(x0, y0, f" C0\n ({x0},{y0})", verticalalignment="bottom", color="blue")
    text(
        x1,
        y1,
        f" C1\n ({x1:.1f},{y1})",
        verticalalignment="bottom",
        color="blue",
    )

    # Outer Red Shaded Corners (Tangent points)
    text(x6, y6, f"  (x6,y6)\n  ({x6:.1f},{y6:.1f})", color="darkred")
    text(
        x7,
        y7,
        f" (x7,y7)\n ({x7:.1f},{y7:.1f})",
        horizontalalignment="right",
        color="darkred",
    )
    text(
        x8,
        y8,
        f" ({x8:.1f},{y8:.1f})\n (x8,y8)",
        horizontalalignment="right",
        verticalalignment="top",
        color="darkred",
    )
    text(
        x9,
        y9,
        f"  ({x9:.1f},{y9:.1f})\n  (x9,y9)",
        verticalalignment="top",
        color="darkred",
    )

    # Geometric Construction Intersections
    text(
        x2,
        y2,
        f" (x2,y2)\n ({x2:.1f},{y2:.1f})",
        color="purple",
        fontsize=9,
        verticalalignment="bottom",
    )
    text(
        x4,
        y4,
        f" (x4,y4)\n ({x4:.1f},{y4:.1f})",
        color="darkgreen",
        fontsize=9,
        verticalalignment="bottom",
    )

    # Window configuration
    title(f"The area of the red region is {area:0.3f}")
    axis("equal")

    # Pause 1.5 seconds so you can analyze the labels before it refreshes
    pause(1.5)

show()
