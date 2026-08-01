# =============================================================================
# Jim McCleery
# August 1, 2026
# Kailua-Kona, HI
#
# Geometry Demonstration: Sum of the Tip Angles of a 5-Pointed Star (Pentagram)
# Link: https://mathnet.mit.edu/explorer.html?p=usa_602c2e
# =============================================================================

from math import pi, sqrt, acos, sin, cos, degrees
from matplotlib.pyplot import clf, plot, text, title, axis, pause, show
from random import uniform


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def distance(x1, y1, x2, y2):
    """
    Calculates the straight-line (Euclidean) distance between two points (x1, y1) and (x2, y2).
    Formula: sqrt((x1 - x2)^2 + (y1 - y2)^2)
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y0) ** 2) if 'y0' in locals() else sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def line_intersection_from_points(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Finds the intersection point (x, y) of two lines.
    Line 1 passes through (x1, y1) and (x2, y2).
    Line 2 passes through (x3, y3) and (x4, y4).
    
    Returns: (x, y, True) if an intersection is found, or (0, 0, False) if parallel.
    """
    try:
        # Calculate slope (m = rise / run) for both lines
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)
        
        # Solve for x where both line equations y = m*x + b intersect
        x = (y1 - m1 * x1 - y3 + m2 * x3) / (m2 - m1)
        y = y1 + m1 * x - m1 * x1
        return x, y, True
    except ZeroDivisionError:
        # Occurs if one line is perfectly vertical or lines are parallel
        return 0, 0, False


def law_of_cosines(d1, d2, side):
    """
    Calculates the angle opposite to 'side' in a triangle with side lengths d1, d2, and side.
    Uses the Law of Cosines: cos(angle) = (d1^2 + d2^2 - side^2) / (2 * d1 * d2)
    """
    try:
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        # acos converts the ratio back into an angle in radians
        return acos(temp), True
    except ValueError:
        return 0, False


def plot_line(x1, y1, x2, y2):
    """
    Draws a straight line segment between point (x1, y1) and point (x2, y2).
    """
    plot([x1, x2], [y1, y2], color='black', linewidth=1.5)


# -----------------------------------------------------------------------------
# MAIN ANIMATION LOOP
# -----------------------------------------------------------------------------

# Run the simulation 1,000,000 times with different randomly generated star shapes
for _ in range(10**6):

    clf()  # Clear the current figure before drawing a new frame
    
    # 1. Randomly choose angles along the unit circle for the 5 outer tips of the star.
    # We restrict each angle to a specific quadrant so the points remain in star-order (A, B, C, D, E).
    theta_A = uniform(pi, 3 * pi / 2)       # Bottom-left quadrant
    theta_B = uniform(3 * pi / 2, 2 * pi)   # Bottom-right quadrant
    theta_C = uniform(0, pi / 2)            # Top-right quadrant
    theta_D = uniform(pi / 2, 3 * pi / 4)   # Upper-top region
    theta_E = uniform(theta_D, pi)          # Top-left region
    
    # 2. Convert polar coordinates (angle theta) to Cartesian coordinates (x, y)
    xA, yA = cos(theta_A), sin(theta_A)  # Point A
    xB, yB = cos(theta_B), sin(theta_B)  # Point B
    xC, yC = cos(theta_C), sin(theta_C)  # Point C
    xD, yD = cos(theta_D), sin(theta_D)  # Point D
    xE, yE = cos(theta_E), sin(theta_E)  # Point E

    # 3. Find the 5 inner intersection points formed where the line segments cross:
    # M is the intersection of line (A-C) and line (B-E)
    xM, yM, _ = line_intersection_from_points(xA, yA, xC, yC, xB, yB, xE, yE)
    
    # N is the intersection of line (A-C) and line (B-D)
    xN, yN, _ = line_intersection_from_points(xA, yA, xC, yC, xB, yB, xD, yD)
    
    # P is the intersection of line (C-E) and line (B-D)
    xP, yP, _ = line_intersection_from_points(xC, yC, xE, yE, xB, yB, xD, yD)
    
    # Q is the intersection of line (A-D) and line (C-E)
    xQ, yQ, _ = line_intersection_from_points(xA, yA, xD, yD, xC, yC, xE, yE)
    
    # R is the intersection of line (A-D) and line (B-E)
    xR, yR, _ = line_intersection_from_points(xA, yA, xD, yD, xB, yB, xE, yE)

    # 4. Calculate the 5 tip angles (alpha, beta, gamma, delta, epsilon) using the Law of Cosines
    
    # Angle alpha at Vertex A (Triangle A-M-R)
    alpha, _ = law_of_cosines(distance(xA, yA, xM, yM), distance(xA, yA, xR, yR), distance(xM, yM, xR, yR))

    # Angle beta at Vertex B (Triangle B-M-N)
    beta, _ = law_of_cosines(distance(xB, yB, xM, yM), distance(xB, yB, xN, yN), distance(xM, yM, xN, yN))

    # Angle gamma at Vertex C (Triangle C-N-P)
    gamma, _ = law_of_cosines(distance(xC, yC, xN, yN), distance(xC, yC, xP, yP), distance(xN, yN, xP, yP))

    # Angle delta at Vertex D (Triangle D-Q-P)
    delta, _ = law_of_cosines(distance(xD, yD, xQ, yQ), distance(xD, yD, xP, yP), distance(xQ, yQ, xP, yP))

    # Angle epsilon at Vertex E (Triangle E-Q-R)
    epsilon, _ = law_of_cosines(distance(xE, yE, xQ, yQ), distance(xE, yE, xR, yR), distance(xQ, yQ, xR, yR))

    # 5. Draw the 5 main line segments that form the star
    plot_line(xC, yC, xA, yA)  # Segment C-A
    plot_line(xC, yC, xE, yE)  # Segment C-E
    plot_line(xE, yE, xB, yB)  # Segment E-B
    plot_line(xB, yB, xD, yD)  # Segment B-D
    plot_line(xA, yA, xD, yD)  # Segment A-D

    # 6. Plot the inner intersection points as dots
    for x, y in [(xM, yM), (xN, yN), (xP, yP), (xQ, yQ), (xR, yR)]:
        plot(x, y, 'ko', markersize=4)

    # 7. Add text labels matching the diagram (Vertices, Inner Points, and Greek Angles)
    # Outer Vertices
    text(xA * 1.08, yA * 1.08, '$A$', fontsize=12, ha='center')
    text(xB * 1.08, yB * 1.08, '$B$', fontsize=12, ha='center')
    text(xC * 1.08, yC * 1.08, '$C$', fontsize=12, ha='center')
    text(xD * 1.08, yD * 1.08, '$D$', fontsize=12, ha='center')
    text(xE * 1.08, yE * 1.08, '$E$', fontsize=12, ha='center')

    # Inner Intersections
    text(xM, yM - 0.08, '$M$', fontsize=11, ha='center')
    text(xN + 0.05, yN, '$N$', fontsize=11, ha='left')
    text(xP + 0.04, yP + 0.03, '$P$', fontsize=11, ha='left')
    text(xQ - 0.04, yQ + 0.03, '$Q$', fontsize=11, ha='right')
    text(xR - 0.05, yR, '$R$', fontsize=11, ha='right')

    # Greek Angle Labels inside the tips
    text(xA + 0.05, yA + 0.08, r'$\alpha$', fontsize=11)
    text(xB - 0.05, yB + 0.08, r'$\beta$', fontsize=11)
    text(xC - 0.12, yC - 0.05, r'$\gamma$', fontsize=11)
    text(xD - 0.02, yD - 0.12, r'$\delta$', fontsize=11)
    text(xE + 0.08, yE - 0.05, r'$\epsilon$', fontsize=11)

    # 8. Calculate total angle sum in degrees and show title
    total_degrees = degrees(alpha + beta + gamma + delta + epsilon)
    title(f'Sum of interior tip angles (α + β + γ + δ + ε) = {total_degrees:.3f}°')
    
    axis('equal')
    axis('off')
    pause(0.2)

show()
