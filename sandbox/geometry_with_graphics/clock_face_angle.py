"""
Jim McCleery
November 16, 2026
Kailua-Kona, HI

Solves and plots the 12-hour clock secant angle geometry problem from:
http://www.youtube.com/watch?v=dVKG5h8sxBw
"""

# Import standard math functions needed for trigonometry and geometry
from math import pi, sqrt, sin, cos, acos, radians, degrees

# Import NumPy (aliased as 'np') for generating smooth arrays of angles
import numpy as np

# Import Matplotlib's pyplot module (aliased as 'plt') for drawing the diagram
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def distance(A, B):
    """
    Return the straight-line distance between two points A and B.

    Parameters:
        A, B: points written as (x, y) tuples
    """
    # Unpack each (x, y) tuple into separate variables
    x1, y1 = A
    x2, y2 = B

    # Apply the Pythagorean theorem: sqrt((dx)^2 + (dy)^2)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# -----------------------------------------------------------------------------
def law_of_cosines(d1, d2, side):
    """
    Find an angle of a triangle using the Law of Cosines:
        c^2 = a^2 + b^2 - 2ab * cos(C)
    The returned angle (in radians) is opposite 'side'.

    Returns:
        (angle, True) if successful
        (0, False) if the side lengths cannot form a valid triangle
    """
    try:
        # Rearrange the Law of Cosines to isolate cos(angle)
        cosine_value = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)

        # Clamp the value strictly between -1 and 1 to prevent floating-point
        # rounding errors (like 1.0000000000000002) from crashing acos()
        cosine_value = max(-1, min(1, cosine_value))

        # Inverse cosine converts the ratio into an angle in radians
        angle = acos(cosine_value)

        return angle, True

    except (ValueError, ZeroDivisionError):
        return 0, False


# -----------------------------------------------------------------------------
def line_intersection_from_points(A, B, C, D):
    """
    Find the intersection point of two lines defined by pairs of points.
    Line 1 passes through A and B; Line 2 passes through C and D.

    Returns:
        (P, True) where P is an (x, y) tuple if the lines intersect
        ((0, 0), False) if the lines are parallel or vertical
    """
    # Unpack all four (x, y) point tuples
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D

    try:
        # Calculate rise-over-run slope for each line
        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y4 - y3) / (x4 - x3)

        # Solve for the x-coordinate where both point-slope equations meet
        x = (y1 - slope1 * x1 - y3 + slope2 * x3) / (slope2 - slope1)

        # Plug x back into the first line's equation to find y
        y = y1 + slope1 * (x - x1)

        return (x, y), True

    except ZeroDivisionError:
        return (0, 0), False


# -----------------------------------------------------------------------------
def plot_circle(C, radius, start=0, stop=2 * pi):
    """
    Plot the outline of a circle using Matplotlib.

    Parameters:
        C: center written as (x, y)
        radius: radius of the circle
        start: starting angle in radians (defaults to 0)
        stop: ending angle in radians (defaults to 2*pi, a full circle)
    """
    center_x, center_y = C

    # Create 1,500 evenly spaced angles so the circle looks completely smooth
    angles = np.linspace(start, stop, 1500)

    # Convert polar coordinates (radius, angle) to Cartesian (x, y) coordinates
    x_values = radius * np.cos(angles) + center_x
    y_values = radius * np.sin(angles) + center_y

    plt.plot(x_values, y_values, color="black", linewidth=1.5)


# -----------------------------------------------------------------------------
def plot_line(A, B):
    """
    Plot a straight line segment between two points A and B.
    """
    x1, y1 = A
    x2, y2 = B

    # plt.plot expects a list of x-values first, followed by a list of y-values
    plt.plot([x1, x2], [y1, y2], color="steelblue", linewidth=1.5)


# -----------------------------------------------------------------------------
def plot_point(A):
    """
    Plot a single point as a circular dot on the graph.
    """
    x, y = A
    plt.plot(x, y, "o", color="black", markersize=5)


# -----------------------------------------------------------------------------
def label_point(P, text, offset_scale=1.15):
    """
    Place a text label slightly outside a point relative to the origin (0, 0).

    Parameters:
        P: (x, y) coordinate of the point
        text: string label to display
        offset_scale: multiplier pushing the text outward from the center
    """
    x, y = P
    plt.text(
        x * offset_scale,
        y * offset_scale,
        text,
        fontsize=10,
        ha="center",
        va="center",
    )


# =============================================================================
# Main Script: Build and Solve the Clock Secant Problem
# =============================================================================

# Define the circle center at the origin (0, 0) and create an empty list for points
O = (0, 0)
points = []

# Generate 12 equally spaced points around the unit circle (every 30 degrees),
# starting at 0 degrees (3 o'clock) and moving counter-clockwise:
# index 0 = 3:00, index 1 = 2:00, ..., index 4 = 11:00, ..., index 9 = 6:00, index 11 = 4:00
for angle in range(0, 360, 30):
    theta = radians(angle)
    points.append((cos(theta), sin(theta)))

# Roman numeral clock labels matching the indices of 'points' (0° = III, 30° = II, etc.)
clock_labels = [
    "III", "II", "I", "XII", "XI", "X",
    "IX", "VIII", "VII", "VI", "V", "IV"
]

# Create a clean square figure
plt.figure(figsize=(7, 7))

# Draw the unit circle
plot_circle(O, 1)

# Plot each of the 12 clock points and add its Roman numeral label
for pt, label in zip(points, clock_labels):
    plot_point(pt)
    label_point(pt, label, offset_scale=1.14)

# Find intersection point A (called "XIII" in the video) where the secant through
# 2:00 (points[1]) & 11:00 (points[4]) meets the secant through 6:00 (points[9]) & 4:00 (points[11])
A, found = line_intersection_from_points(points[1], points[4], points[9], points[11])

# Plot and label the external intersection point A / XIII
plot_point(A)
plt.text(A[0] + 0.08, A[1], "A (XIII)", fontsize=10, va="center")

# Calculate the three side lengths of triangle (A, 11 o'clock, 6 o'clock)
d1 = distance(A, points[4])
d2 = distance(A, points[9])
d3 = distance(points[4], points[9])

# Use the Law of Cosines to find angle alpha at vertex A and convert to degrees
alpha_rad, _ = law_of_cosines(d1, d2, d3)
alpha = degrees(alpha_rad)

# Draw the two secant segments from vertex A through the circle
plot_line(A, points[4])
plot_line(A, points[9])

# Place the Greek letter alpha inside the vertex angle
plt.text(A[0] - 0.35, A[1] - 0.03, r"$\alpha$", fontsize=12, color="steelblue")

# Format and display the final plot
plt.title(f"Angle $\\alpha$ = {alpha:0.3f} degrees")
plt.axis("equal")
plt.axis("off")
plt.tight_layout()
plt.show()
