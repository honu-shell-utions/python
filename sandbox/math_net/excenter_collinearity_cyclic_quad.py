# -----------------------------------------------------------------------------
# Jim McCleery
# November 13, 2026
# Kailua-Kona, HI
#
# MathNet Problem Visualization:
# https://mathnet.mit.edu/explorer.html?p=apm_2021_b4cc15
#
# Problem Statement:
# Let ABCD be a cyclic convex quadrilateral and Gamma be its circumcircle.
# Let E be the intersection of the diagonals AC and BD, let L be the center
# of the circle tangent to sides AB, BC, and CD, and let M be the midpoint of
# the arc BC of Gamma not containing A and D. Prove that the excenter of
# triangle BCE opposite E lies on the line LM.
#
# Note on Representing Points:
# Points are stored as Python tuples: A = (x, y). Passing a single tuple
# into functions like distance(A, B) keeps the code much cleaner and easier
# to read than passing four separate numbers: distance(x1, y1, x2, y2).
# -----------------------------------------------------------------------------

from math import pi, sqrt, sin, cos, tan, acos, hypot
from random import uniform
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Geometry Helper Functions
# -----------------------------------------------------------------------------

def distance(A, B):
    """
    Calculate the straight-line distance between two points A and B.
    """
    # Unpack the (x, y) tuples into individual variables
    x1, y1 = A
    x2, y2 = B

    # Apply the standard distance formula (Pythagorean theorem)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def mid_point(A, B):
    """
    Find the exact halfway point (midpoint) between two points A and B.
    """
    x1, y1 = A
    x2, y2 = B

    # Average the x-coordinates and average the y-coordinates
    return ((x1 + x2) / 2, (y1 + y2) / 2)


def law_of_cosines(d1, d2, side):
    """
    Find an angle (in radians) opposite 'side' in a triangle with side
    lengths d1, d2, and 'side'. Returns (angle, True) if valid.
    """
    try:
        cosine_value = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)

        # Clamp the value between -1 and 1 to prevent tiny computer rounding
        # errors from crashing the acos() function
        cosine_value = max(-1, min(1, cosine_value))

        angle = acos(cosine_value)
        return angle, True

    except (ValueError, ZeroDivisionError):
        return 0, False


def quadratic_equation(A, B, C):
    """
    Solve a quadratic equation of the form A*x^2 + B*x + C = 0.
    Returns (x1, x2, True) with x1 <= x2 if real solutions exist.
    """
    try:
        # Calculate the discriminant (the part inside the square root)
        discriminant = B**2 - 4 * A * C
        square_root = sqrt(discriminant)

        # Apply the quadratic formula
        x1 = (-B - square_root) / (2 * A)
        x2 = (-B + square_root) / (2 * A)

        # Ensure x1 is always the smaller root
        if x1 > x2:
            x1, x2 = x2, x1

        return x1, x2, True

    except (ValueError, ZeroDivisionError):
        return 0, 0, False


def line_intersection_from_points(A, B, C, D):
    """
    Find the intersection point of two lines: one passing through A and B,
    and another passing through C and D. Returns (point, True) if they cross.
    """
    x1, y1 = A
    x2, y2 = B
    x3, y3 = C
    x4, y4 = D

    try:
        # Calculate the slope (rise over run) of each line
        slope1 = (y2 - y1) / (x2 - x1)
        slope2 = (y4 - y3) / (x4 - x3)

        # Set the two line equations equal to each other and solve for x
        x = (y1 - slope1 * x1 - y3 + slope2 * x3) / (slope2 - slope1)

        # Plug x back into the first line equation to find y
        y = y1 + slope1 * (x - x1)

        return (x, y), True

    except ZeroDivisionError:
        # Happens if a line is vertical or if the two lines are parallel
        return (0, 0), False


def line_circle_intersection(C, radius, line):
    """
    Find the two intersection points of a circle (center C, radius) and a
    line in slope-intercept form y = m*x + b, passed as tuple (m, b).
    """
    center_x, center_y = C
    m, b = line

    # Substituting y = m*x + b into the circle equation (x - h)^2 + (y - k)^2 = r^2
    # creates a quadratic equation A*x^2 + B*x + C_value = 0
    A = 1 + m**2
    B = -2 * center_x + 2 * m * b - 2 * m * center_y
    C_value = center_x**2 + b**2 - 2 * b * center_y + center_y**2 - radius**2

    # Solve for the x-coordinates of the intersections
    x1, x2, ok = quadratic_equation(A, B, C_value)

    if not ok:
        return (0, 0), (0, 0), False

    # Plug x1 and x2 into the line equation to find their y-coordinates
    P1 = (x1, m * x1 + b)
    P2 = (x2, m * x2 + b)

    return P1, P2, True


def circle_circle_intersections(C0, r0, C1, r1):
    """
    Find the two intersection points P1 and P2 of two circles:
    Circle 0 with center C0 and radius r0, and Circle 1 with center C1 and radius r1.
    """
    x0, y0 = C0
    x1, y1 = C1

    try:
        # Distance between the two circle centers
        d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

        # Distance from C0 to the radical axis (line connecting intersections)
        a = (r0**2 - r1**2 + d**2) / (2 * d)

        # Height from the center line to either intersection point
        h = sqrt(r0**2 - a**2)

        # Midpoint between the two intersection points
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d

        # Calculate the two intersection points by offsetting perpendicular to C0-C1
        P1 = (x2 + h * (y1 - y0) / d, y2 - h * (x1 - x0) / d)
        P2 = (x2 - h * (y1 - y0) / d, y2 + h * (x1 - x0) / d)

        return P1, P2, True

    except (ValueError, ZeroDivisionError):
        return (0, 0), (0, 0), False


def excenter(B, C, E):
    """
    Find the center and radius of the excircle of triangle BCE opposite vertex E.
    This circle is tangent to segment BC and the extensions of sides EB and EC.
    """
    x_B, y_B = B
    x_C, y_C = C
    x_E, y_E = E

    # Calculate the three side lengths of triangle BCE using hypot()
    b = hypot(x_C - x_E, y_C - y_E)  # Length of side CE (opposite B)
    c = hypot(x_B - x_E, y_B - y_E)  # Length of side BE (opposite C)
    dx = x_C - x_B
    dy = y_C - y_B
    e = hypot(dx, dy)                # Length of side BC (opposite E)

    # Trilinear-to-Cartesian coordinate formula for the E-excenter
    denominator = b + c - e
    x = (b * x_B + c * x_C - e * x_E) / denominator
    y = (b * y_B + c * y_C - e * y_E) / denominator

    # The exradius is the perpendicular distance from the excenter to line BC
    radius = abs(dx * (y - y_B) - dy * (x - x_B)) / e

    return (x, y), radius


# -----------------------------------------------------------------------------
# Plotting Helper Functions
# -----------------------------------------------------------------------------

def plot_circle(C, radius, start=0, stop=2 * pi, linestyle="-", color=None):
    """
    Draw a circle or circular arc centered at C using 1,500 plotted points.
    """
    center_x, center_y = C

    # Generate 1,500 evenly spaced angles between start and stop
    angles = np.linspace(start, stop, 1500)

    # Convert polar coordinates (radius, angle) to Cartesian (x, y)
    x_values = radius * np.cos(angles) + center_x
    y_values = radius * np.sin(angles) + center_y

    plt.plot(x_values, y_values, linestyle=linestyle, color=color)


def plot_line(A, B, linestyle="-", color=None):
    """
    Draw a straight line segment connecting point A and point B.
    """
    x1, y1 = A
    x2, y2 = B
    plt.plot([x1, x2], [y1, y2], linestyle=linestyle, color=color)


def plot_point(A, label="", offset=(0.04, 0.04), color="black"):
    """
    Plot a dot at point A and place a text label slightly offset from the dot
    so the text doesn't overlap the point marker.
    """
    x, y = A
    plt.plot(x, y, "o", color=color, markersize=5)

    # Add a text label if one was provided
    if label:
        plt.text(
            x + offset[0],
            y + offset[1],
            label,
            fontsize=11,
            fontweight="bold",
            color=color
        )


# -----------------------------------------------------------------------------
# Main Simulation & Visualization Loop
# -----------------------------------------------------------------------------

# Define the circumcircle Gamma (centered at origin with radius 1)
gamma_center = (0, 0)
r1 = 1

# Generate 10 random geometric configurations to visually verify the theorem
for _ in range(10):
    plt.cla()
    plt.figure(figsize=(8, 8))

    # 1. Place vertices A, B, C, and D in counter-clockwise order on Gamma
    A = (-r1, 0)  # Fixed on the far left of the circle

    theta_B = uniform(pi / 2, pi)           # Top-left quadrant
    B = (r1 * cos(theta_B), r1 * sin(theta_B))

    theta_C = uniform(0, pi / 2)            # Top-right quadrant
    C = (r1 * cos(theta_C), r1 * sin(theta_C))

    theta_D = uniform(3 * pi / 2, 2 * pi)   # Bottom-right quadrant
    D = (r1 * cos(theta_D), r1 * sin(theta_D))

    # 2. Calculate side and diagonal lengths of quadrilateral ABCD
    AB = distance(A, B)
    BC = distance(B, C)
    CD = distance(C, D)
    AC = distance(A, C)
    BD = distance(B, D)

    # 3. Find circle centered at L tangent to sides AB, BC, and CD
    # Find interior angles at B (beta) and C (gamma)
    beta, _ = law_of_cosines(BC, AB, AC)
    gamma, _ = law_of_cosines(BC, CD, BD)

    # Use angle bisector properties to find the radius (r2) of the tangent circle
    a = (BC * tan(gamma / 2)) / (tan(beta / 2) + tan(gamma / 2))
    b = BC - a
    r2 = a * tan(beta / 2)

    # Distance from vertices A and D to center L
    d1 = sqrt((AB - a) ** 2 + r2**2)
    d2 = sqrt((CD - b) ** 2 + r2**2)

    # Locate center L by intersecting circles around A and D
    _, L, _ = circle_circle_intersections(A, d1, D, d2)

    # 4. Find M, the midpoint of arc BC not containing A and D
    MP = mid_point(B, C)
    m = (MP[1] - gamma_center[1]) / (MP[0] - gamma_center[0])
    b_int = MP[1] - m * MP[0]
    M1, M2, _ = line_circle_intersection(gamma_center, r1, (m, b_int))

    # Since B and C are in the upper half-plane, pick the upper intersection
    M = M1 if M1[1] > M2[1] else M2

    # 5. Find E, the intersection of diagonals AC and BD
    E, _ = line_intersection_from_points(A, C, B, D)

    # 6. Find XC (excenter) and xr (exradius) of triangle BCE opposite E
    XC, xr = excenter(B, C, E)

    # 7. Draw the geometric shapes
    # Quadrilateral ABCD
    plot_line(A, B, color="black")
    plot_line(B, C, color="black")
    plot_line(C, D, color="black")
    plot_line(A, D, color="black")

    # Diagonals AC and BD (dashed so they don't clutter the main sides)
    plot_line(A, C, linestyle="--", color="gray")
    plot_line(B, D, linestyle="--", color="gray")

    # Line connecting L, Excenter (XC), and M (demonstrating collinearity)
    plot_line(L, XC, color="crimson")

    # Circles: Circumcircle Gamma, circle tangent to AB/BC/CD, and excircle
    plot_circle(gamma_center, r1, color="steelblue")
    plot_circle(L, r2, color="seagreen")
    plot_circle(XC, xr, color="darkorange")

    # 8. Plot and label all key points from the problem statement
    plot_point(A, "A", offset=(-0.11, -0.03))
    plot_point(B, "B", offset=(-0.09, 0.05))
    plot_point(C, "C", offset=(0.05, 0.05))
    plot_point(D, "D", offset=(0.05, -0.08))
    plot_point(E, "E", offset=(0.04, -0.07))
    plot_point(L, "L", offset=(-0.10, -0.04), color="seagreen")
    plot_point(M, "M", offset=(0.03, 0.05), color="steelblue")
    plot_point(XC, "Excenter", offset=(0.05, 0.03), color="darkorange")

    # Label the circumcircle Gamma near the bottom-left arc
    plt.text(-0.82, -0.78, r"$\Gamma$", fontsize=14, fontweight="bold", color="steelblue")

    # Format and display the final plot
    plt.axis("equal")
    plt.axis("off")
    plt.title("APM 2021: Collinearity of L, Excenter of △BCE, and M")
    plt.pause(1)
plt.show()
