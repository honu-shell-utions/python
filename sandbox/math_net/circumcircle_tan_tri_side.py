"""
Jim McCleery
November 27, 2026
Kailua-Kona, HI

https://mathnet.mit.edu/explorer.html?p=sau_2025_9a540f
"""

# -----------------------------------------------------------------------------
# Import standard math tools (pi for circles, sqrt for square roots)
from math import pi, sqrt
# Import uniform to pick random decimal numbers within a given range
from random import uniform

# Import Matplotlib's pyplot module (nicknamed 'plt') for drawing graphs
import matplotlib.pyplot as plt
# Import NumPy (nicknamed 'np') for fast math across lists/arrays of numbers
import numpy as np


# -----------------------------------------------------------------------------
def distance(A, B):
    """
    Calculate the straight-line distance between two points.

    Parameters:
        A, B: points written as (x, y) tuples

    Returns:
        The distance between A and B as a float.
    """
    # Unpack each (x, y) tuple into separate variables
    x1, y1 = A
    x2, y2 = B

    # Use the Pythagorean theorem: sqrt((dx)^2 + (dy)^2)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# -----------------------------------------------------------------------------
def circumcircle(A, B, C):
    """
    Find the unique circle that passes through three points A, B, and C.

    Parameters:
        A, B, C: three points written as (x, y) tuples

    Returns:
        (center, radius, True) if a valid circle exists.
        ((0, 0), 0, False) if the three points lie on a straight line.
    """
    # Unpack the x- and y-coordinates of all three points
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C

    # Use try/except to catch math errors (like dividing by zero) safely
    try:
        # Pre-calculate x^2 + y^2 for each point to keep the formulas readable
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2

        # Compute determinants to solve for the circle's center coordinates
        M11 = x1 * y2 + x2 * y3 + x3 * y1 - x2 * y1 - x3 * y2 - x1 * y3
        M12 = s1 * y2 + s2 * y3 + s3 * y1 - s2 * y1 - s3 * y2 - s1 * y3
        M13 = s1 * x2 + s2 * x3 + s3 * x1 - s2 * x1 - s3 * x2 - s1 * x3

        # Calculate the (x, y) center of the circle
        center_x = 0.5 * M12 / M11
        center_y = -0.5 * M13 / M11
        center = (center_x, center_y)

        # Since point A is on the circle, the distance from center to A is the radius
        radius = distance(A, center)

        return center, radius, True

    # Triggered if the three points are collinear (in a straight line), making M11 == 0
    except (ValueError, ZeroDivisionError):
        return (0, 0), 0, False


# -----------------------------------------------------------------------------
def quadratic_equation(A, B, C):
    """
    Solve the quadratic equation A*x^2 + B*x + C = 0 for real roots.

    Returns:
        (x1, x2, True) where x1 <= x2, if real solutions exist.
        (0, 0, False) if there are no real solutions.
    """
    try:
        # Calculate the discriminant (the expression inside the square root)
        discriminant = B**2 - 4 * A * C

        # Raises ValueError if discriminant is negative (no real roots)
        square_root = sqrt(discriminant)

        # Apply the quadratic formula to find both solutions
        x1 = (-B - square_root) / (2 * A)
        x2 = (-B + square_root) / (2 * A)

        # Swap values if needed so x1 is always the smaller root
        if x1 > x2:
            x1, x2 = x2, x1

        return x1, x2, True

    except (ValueError, ZeroDivisionError):
        return 0, 0, False


# -----------------------------------------------------------------------------
def line_circle_intersection(C, radius, line):
    """
    Find where a straight line (y = m*x + b) intersects a circle.

    Parameters:
        C: circle center written as (x, y)
        radius: radius of the circle
        line: tuple (m, b) where m is slope and b is y-intercept

    Returns:
        (P1, P2, True) with the two intersection points if they exist.
        ((0, 0), (0, 0), False) if the line misses the circle.
    """
    # Unpack the circle center and the line's slope and intercept
    center_x, center_y = C
    m, b = line

    # Substituting y = m*x + b into the circle equation gives A*x^2 + B*x + C = 0
    A = 1 + m**2
    B = -2 * center_x + 2 * m * b - 2 * m * center_y
    C_value = center_x**2 + b**2 - 2 * b * center_y + center_y**2 - radius**2

    # Solve the quadratic equation to get the two x-coordinates
    x1, x2, ok = quadratic_equation(A, B, C_value)

    # Stop early if no real intersection points were found
    if not ok:
        return (0, 0), (0, 0), False

    # Plug each x-coordinate back into y = m*x + b to get the matching y-coordinates
    P1 = (x1, m * x1 + b)
    P2 = (x2, m * x2 + b)

    return P1, P2, True


# -----------------------------------------------------------------------------
def plot_circle(C, radius, label=None, start=0, stop=2 * pi):
    """
    Draw a circle (or circular arc) on the graph using Matplotlib.

    Parameters:
        C: center written as (x, y)
        radius: radius of the circle
        label: optional text label for the legend
        start: starting angle in radians (default is 0)
        stop: ending angle in radians (default is 2*pi, a full circle)
    """
    center_x, center_y = C

    # Create 1,500 evenly spaced angles around the circle so the curve looks smooth
    angles = np.linspace(start, stop, 1500)

    # Convert angles into x- and y-coordinates using NumPy
    x_values = radius * np.cos(angles) + center_x
    y_values = radius * np.sin(angles) + center_y

    # Plot the circle outline
    plt.plot(x_values, y_values, label=label)


# -----------------------------------------------------------------------------
def plot_line(A, B, color="black", linestyle="-"):
    """
    Draw a straight line segment between two points A and B.

    Parameters:
        A, B: endpoints written as (x, y) tuples
        color: line color (default is black)
        linestyle: line style such as '-' for solid or '--' for dashed
    """
    x1, y1 = A
    x2, y2 = B

    # Matplotlib expects a list of x-values first, then a list of y-values
    plt.plot([x1, x2], [y1, y2], color=color, linestyle=linestyle)


# -----------------------------------------------------------------------------
def plot_point(P, label, offset=(5, 5)):
    """
    Draw a dot at point P and place a text label next to it.

    Parameters:
        P: point written as (x, y)
        label: text string to display next to the dot
        offset: (dx, dy) shift in screen points so text doesn't sit on top of the dot
    """
    x, y = P

    # Plot a small black circular marker ('ko') at the point
    plt.plot(x, y, "ko", markersize=4)

    # Place the label slightly offset from the dot for readability
    plt.annotate(
        label,
        xy=(x, y),
        xytext=offset,
        textcoords="offset points",
        fontsize=11,
        fontweight="bold",
    )


# -----------------------------------------------------------------------------
# Main animation loop: test 100 random right triangles ABC
for _ in range(100):
    # Clear the previous frame before drawing the new triangle
    plt.cla()

    # Pick random lengths for segments BH and CH along the hypotenuse BC
    BH = uniform(1, 10)
    CH = uniform(1, BH)

    # In right triangle ABC, altitude AH satisfies AH^2 = BH * CH
    AH = sqrt(CH * BH)
    BC = BH + CH

    # Given DE = AH * sqrt(5) and power of a point DH * EH = BH * CH:
    # Solve for EH (below H) and DH (between A and H)
    discriminant_term = sqrt(5 * AH**2 - 4 * BH * CH)
    EH = (AH * sqrt(5) + discriminant_term) / 2
    DH = (AH * sqrt(5) - discriminant_term) / 2

    # Define the coordinates of the main points on the Cartesian plane
    B = (0, 0)
    H = (BH, 0)
    C = (BC, 0)
    A = (BH, AH)
    D = (BH, DH)
    E = (BH, -EH)

    # Construct circle (omega) passing through B, C, and E (and also D)
    omega_center, omega_radius, _ = circumcircle(B, C, E)

    # Find M where circle (omega) intersects segment AB (line through B and A)
    slope_AB = AH / BH
    intercept_AB = 0
    _, M, _ = line_circle_intersection(
        omega_center, omega_radius, (slope_AB, intercept_AB)
    )

    # Find N where circle (omega) intersects segment AC (line through C and A)
    slope_AC = -AH / CH
    intercept_AC = C[1] - slope_AC * C[0]
    N, _, _ = line_circle_intersection(
        omega_center, omega_radius, (slope_AC, intercept_AC)
    )

    # Construct the circumcircle of triangle HMN
    hmn_center, hmn_radius, _ = circumcircle(H, M, N)

    # Draw triangle ABC and altitude line AE
    plot_line(A, B)
    plot_line(B, C)
    plot_line(A, C)
    plot_line(A, E, color="gray", linestyle="--")

    # Draw circle (omega) and the circumcircle of triangle HMN
    plot_circle(omega_center, omega_radius, label="Circle (ω)")
    plot_circle(hmn_center, hmn_radius, label="Circumcircle of △HMN")

    # Add dots and coordinate labels for all key points from the problem
    plot_point(A, "A", offset=(0, 7))
    plot_point(B, "B", offset=(-14, -10))
    plot_point(C, "C", offset=(6, -10))
    plot_point(H, "H", offset=(5, -13))
    plot_point(D, "D", offset=(6, 2))
    plot_point(E, "E", offset=(6, -12))
    plot_point(M, "M", offset=(-15, 4))
    plot_point(N, "N", offset=(6, 4))

    # Measure the gap between line BC (y = 0) and the bottom of circle HMN
    # A distance of 0 proves the circle is tangent to BC
    distance_to_BC = abs(hmn_center[1] - hmn_radius)

    # Format the plot title, legend, and equal aspect ratio so circles aren't stretched
    plt.title(f"Distance from line BC to circumcircle of △HMN: {distance_to_BC:.6f}")
    plt.legend(loc="upper right")
    plt.axis("equal")
    plt.axis("off")

    # Pause 1 second so we can view each random configuration
    plt.pause(1)

# Keep the final plot window open when the loop finishes
plt.show()
