# -----------------------------------------------------------------------------
# Jim McCleery
# September 25, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=btw_1995_44d191
#
# Geometry problem:
#
# In triangle ABC, l is the bisector of the external angle at C.
# The line through the midpoint O of AB, parallel to l, meets AC at E.
#
# Given:
#       AC = 7
#       CB = 4
#
# Determine CE.
#
# This program draws several different triangles satisfying AC = 7 and
# BC = 4.  In every case, CE should have the same length.
# -----------------------------------------------------------------------------


from math import sqrt
from random import uniform

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def distance(P, Q):
    """Return the distance between two points P and Q."""

    x1, y1 = P
    x2, y2 = Q

    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


# -----------------------------------------------------------------------------
def midpoint(P, Q):
    """Return the midpoint of the segment joining P and Q."""

    x1, y1 = P
    x2, y2 = Q

    return ((x1 + x2) / 2, (y1 + y2) / 2)


# -----------------------------------------------------------------------------
def cross(v, w):
    """
    Return the 2-dimensional cross product of vectors v and w.

    For vectors

        v = (vx, vy)
        w = (wx, wy)

    the cross product is

        vx*wy - vy*wx

    We use this to find the intersection of two lines.
    """

    vx, vy = v
    wx, wy = w

    return vx * wy - vy * wx


# -----------------------------------------------------------------------------
def line_intersection(P1, P2, Q1, Q2):
    """
    Find the intersection of the infinite lines P1-P2 and Q1-Q2.

    This method works for vertical, horizontal, and sloping lines.
    """

    # Direction vector for the first line.
    r = (
        P2[0] - P1[0],
        P2[1] - P1[1]
    )

    # Direction vector for the second line.
    s = (
        Q2[0] - Q1[0],
        Q2[1] - Q1[1]
    )

    denominator = cross(r, s)

    # A zero denominator means the lines are parallel.
    if abs(denominator) < 1e-12:
        raise ValueError("The lines are parallel.")

    Q1_minus_P1 = (
        Q1[0] - P1[0],
        Q1[1] - P1[1]
    )

    # t tells us how far to travel from P1 in direction r.
    t = cross(Q1_minus_P1, s) / denominator

    return (
        P1[0] + t * r[0],
        P1[1] + t * r[1]
    )


# -----------------------------------------------------------------------------
def label_point(name, P):
    """Plot a point and label it with its name and coordinates."""

    x, y = P

    plt.plot(x, y, "o")

    plt.annotate(
        f"{name} ({x:.2f}, {y:.2f})",
        (x, y),
        xytext=(6, 6),
        textcoords="offset points"
    )


# -----------------------------------------------------------------------------
# Fixed side lengths from the problem.

AC = 7
BC = 4


# Draw 20 different triangles.

for _ in range(20):

    plt.cla()

    # -------------------------------------------------------------
    # Choose AB randomly.
    #
    # The triangle inequality requires:
    #
    #       |AC - BC| < AB < AC + BC
    #
    #       3 < AB < 11
    #
    # We stay slightly away from the endpoints so the triangle
    # does not become almost completely flat.
    # -------------------------------------------------------------

    AB = uniform(3.2, 10.8)


    # -------------------------------------------------------------
    # Place A and B on the x-axis.
    # -------------------------------------------------------------

    A = (0, 0)
    B = (AB, 0)


    # -------------------------------------------------------------
    # Find point C.
    #
    # We know:
    #
    #       distance(A, C) = 7
    #       distance(B, C) = 4
    #
    # From the two circle equations, the x-coordinate of C is:
    #
    #       x = (AC^2 - BC^2 + AB^2) / (2*AB)
    #
    # Then use
    #
    #       x^2 + y^2 = AC^2
    #
    # to find y.
    # -------------------------------------------------------------

    xC = (AC**2 - BC**2 + AB**2) / (2 * AB)
    yC = sqrt(AC**2 - xC**2)

    C = (xC, yC)


    # -------------------------------------------------------------
    # Find unit vectors pointing from C toward A and B.
    #
    # Since CA = 7 and CB = 4, dividing by those lengths
    # produces vectors of length 1.
    # -------------------------------------------------------------

    unit_CA = (
        (A[0] - C[0]) / AC,
        (A[1] - C[1]) / AC
    )

    unit_CB = (
        (B[0] - C[0]) / BC,
        (B[1] - C[1]) / BC
    )


    # -------------------------------------------------------------
    # The difference of these two unit vectors points along an
    # EXTERNAL angle bisector at C.
    # -------------------------------------------------------------

    external_direction = (
        unit_CA[0] - unit_CB[0],
        unit_CA[1] - unit_CB[1]
    )


    # Create another point on the external angle bisector.
    # The factor 5 merely makes the plotted line long enough
    # to see clearly.

    L = (
        C[0] + 5 * external_direction[0],
        C[1] + 5 * external_direction[1]
    )


    # -------------------------------------------------------------
    # O is the midpoint of AB.
    # -------------------------------------------------------------

    O = midpoint(A, B)


    # -------------------------------------------------------------
    # Construct a line through O parallel to the external
    # angle bisector.
    #
    # Since it uses exactly the same direction vector, the
    # two lines are parallel.
    # -------------------------------------------------------------

    P = (
        O[0] + 5 * external_direction[0],
        O[1] + 5 * external_direction[1]
    )


    # -------------------------------------------------------------
    # E is where the line through O meets line AC.
    # -------------------------------------------------------------

    E = line_intersection(A, C, O, P)


    # -------------------------------------------------------------
    # Calculate CE.
    # -------------------------------------------------------------

    CE = distance(C, E)


    # -------------------------------------------------------------
    # Plot triangle ABC.
    # -------------------------------------------------------------

    plt.plot(
        [A[0], B[0], C[0], A[0]],
        [A[1], B[1], C[1], A[1]]
    )


    # -------------------------------------------------------------
    # Plot the external angle bisector through C.
    #
    # Extend it in both directions to make it easier to see.
    # -------------------------------------------------------------

    L1 = (
        C[0] - 5 * external_direction[0],
        C[1] - 5 * external_direction[1]
    )

    L2 = (
        C[0] + 5 * external_direction[0],
        C[1] + 5 * external_direction[1]
    )

    plt.plot(
        [L1[0], L2[0]],
        [L1[1], L2[1]],
        "--",
        label="External angle bisector"
    )


    # -------------------------------------------------------------
    # Plot the parallel line through O.
    # -------------------------------------------------------------

    P1 = (
        O[0] - 5 * external_direction[0],
        O[1] - 5 * external_direction[1]
    )

    P2 = (
        O[0] + 5 * external_direction[0],
        O[1] + 5 * external_direction[1]
    )

    plt.plot(
        [P1[0], P2[0]],
        [P1[1], P2[1]],
        "--",
        label="Parallel through O"
    )


    # -------------------------------------------------------------
    # Plot and label the important points.
    # -------------------------------------------------------------

    label_point("A", A)
    label_point("B", B)
    label_point("C", C)
    label_point("O", O)
    label_point("E", E)


    # -------------------------------------------------------------
    # Finish the graph.
    # -------------------------------------------------------------

    plt.title(f"CE = {CE:.5f}")

    plt.grid()

    # Set the visible coordinate range.
    plt.xlim(-3, AB + 3)
    plt.ylim(-5, 10)

    # Make one unit on the x-axis the same size as one unit on the y-axis.
    # "adjustable='box'" avoids the warning about fixed limits.
    plt.gca().set_aspect("equal", adjustable="box")

    plt.pause(1)
    
plt.show()
