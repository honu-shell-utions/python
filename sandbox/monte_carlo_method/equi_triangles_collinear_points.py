# -----------------------------------------------------------------------------
# Jim McCleery
# August 19, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2024_ff338f
# -----------------------------------------------------------------------------

from math import sqrt
from random import uniform
import matplotlib.pyplot as plt


# =============================================================================
# Helper Functions
# =============================================================================

def distance(P, Q):
    """Euclidean distance between two points."""
    return sqrt((P[0] - Q[0])**2 + (P[1] - Q[1])**2)


def cross(P, Q):
    """2-D cross product."""
    return P[0] * Q[1] - P[1] * Q[0]


def line_intersection(P, Q, R, S):
    """
    Intersection of the lines PQ and RS.

    Returns:
        (point, True) if the lines intersect,
        (None, False) if they are parallel.
    """

    v = (Q[0] - P[0], Q[1] - P[1])
    w = (S[0] - R[0], S[1] - R[1])

    denominator = cross(v, w)

    if abs(denominator) < 1e-12:
        return None, False

    RP = (R[0] - P[0], R[1] - P[1])

    t = cross(RP, w) / denominator

    intersection = (
        P[0] + t * v[0],
        P[1] + t * v[1]
    )

    return intersection, True


def circumcircle(P, Q, R):
    """
    Circumcenter and circumradius of triangle PQR.
    """

    x1, y1 = P
    x2, y2 = Q
    x3, y3 = R

    denominator = 2 * (
        x1 * (y2 - y3)
        + x2 * (y3 - y1)
        + x3 * (y1 - y2)
    )

    if abs(denominator) < 1e-12:
        return None, None

    ux = (
        (x1**2 + y1**2) * (y2 - y3)
        + (x2**2 + y2**2) * (y3 - y1)
        + (x3**2 + y3**2) * (y1 - y2)
    ) / denominator

    uy = (
        (x1**2 + y1**2) * (x3 - x2)
        + (x2**2 + y2**2) * (x1 - x3)
        + (x3**2 + y3**2) * (x2 - x1)
    ) / denominator

    center = (ux, uy)
    radius = distance(center, P)

    return center, radius


def point_line_distance(P, A, B):
    """Distance from P to line AB."""
    numerator = abs(
        (B[0] - A[0]) * (A[1] - P[1])
        - (A[0] - P[0]) * (B[1] - A[1])
    )

    denominator = distance(A, B)

    return numerator / denominator


def plot_line(P, Q):
    plt.plot([P[0], Q[0]], [P[1], Q[1]])


# =============================================================================
# Fixed Outer Equilateral Triangle
# =============================================================================

A = (0.0, 0.0)
B = (1.0, 0.0)
C = (0.5, sqrt(3) / 2)


# =============================================================================
# Monte Carlo Search
# =============================================================================

N = 10**9

best_score = float("inf")
best_data = None


for trial in range(N):

    # -------------------------------------------------------------------------
    # d1 = AZ
    # -------------------------------------------------------------------------

    d1 = uniform(0.01, 0.99)

    Z = (
        d1 / 2,
        d1 * sqrt(3) / 2
    )

    Y = (
        1 - d1,
        0
    )

    X = (
        (1 + d1) / 2,
        (1 - d1) * sqrt(3) / 2
    )


    # -------------------------------------------------------------------------
    # Choose D randomly on XZ
    # -------------------------------------------------------------------------

    t = uniform(0, 1)

    D = (
        Z[0] + t * (X[0] - Z[0]),
        Z[1] + t * (X[1] - Z[1])
    )


    # -------------------------------------------------------------------------
    # E = CD intersection YZ
    # -------------------------------------------------------------------------

    E, ok = line_intersection(C, D, Y, Z)

    if not ok:
        continue


    # -------------------------------------------------------------------------
    # F = BD intersection XY
    # -------------------------------------------------------------------------

    F, ok = line_intersection(B, D, X, Y)

    if not ok:
        continue


    # -------------------------------------------------------------------------
    # Make sure E and F are actually on the required sides.
    # -------------------------------------------------------------------------

    def between(P, Q, R):
        """
        True if R lies between P and Q.
        """
        return (
            min(P[0], Q[0]) - 1e-10 <= R[0] <= max(P[0], Q[0]) + 1e-10
            and
            min(P[1], Q[1]) - 1e-10 <= R[1] <= max(P[1], Q[1]) + 1e-10
        )

    if not between(Y, Z, E):
        continue

    if not between(X, Y, F):
        continue


    # =========================================================================
    # TEST 1: DEF must be equilateral
    # =========================================================================

    DE = distance(D, E)
    EF = distance(E, F)
    FD = distance(F, D)

    equilateral_error = (
        abs(DE - EF)
        + abs(EF - FD)
        + abs(FD - DE)
    )


    # =========================================================================
    # TEST 2: A, E, F must be collinear
    #
    # Since A = (0,0), this is simply
    #
    #       E x F = 0
    # =========================================================================

    collinear_error = abs(cross(E, F))


    # =========================================================================
    # TEST 3: UNIQUE XYZ
    #
    # Let O be the center of equilateral DEF.
    #
    # X lies on the circumcircle of D,O,F.
    #
    # For X to be unique on BC, that circle must be tangent to BC.
    # =========================================================================

    O = (
        (D[0] + E[0] + F[0]) / 3,
        (D[1] + E[1] + F[1]) / 3
    )

    circle_center, circle_radius = circumcircle(D, O, F)

    if circle_center is None:
        continue

    distance_to_BC = point_line_distance(circle_center, B, C)

    tangency_error = abs(distance_to_BC - circle_radius)


    # =========================================================================
    # TOTAL ERROR
    # =========================================================================

    score = (
        equilateral_error
        + collinear_error
        + tangency_error
    )


    # -------------------------------------------------------------------------
    # Keep the best configuration found so far.
    # -------------------------------------------------------------------------

    if score < best_score:

        best_score = score

        best_data = (
            d1,
            X, Y, Z,
            D, E, F,
            DE, EF, FD,
            equilateral_error,
            collinear_error,
            tangency_error
        )


# =============================================================================
# Display Result
# =============================================================================

(
    d1,
    X, Y, Z,
    D, E, F,
    DE, EF, FD,
    equilateral_error,
    collinear_error,
    tangency_error
) = best_data


# =============================================================================
# Plotting the Geometry with Coordinate Labels
# =============================================================================

# Draw the outer triangle ABC
plot_line(A, B)
plot_line(B, C)
plot_line(C, A)

# Draw the inner equilateral triangle XYZ
plot_line(X, Z)
plot_line(Z, Y)
plot_line(Y, X)

# Draw the three important cevians/lines
plot_line(C, E)     # C-D-E
plot_line(B, D)     # B-D-F
plot_line(A, E)     # A-E-F
plot_line(A, F)     # A-E-F

# Plot all points
points = {
    "A": A,
    "B": B,
    "C": C,
    "D": D,
    "E": E,
    "F": F,
    "X": X,
    "Y": Y,
    "Z": Z
}

for label, P in points.items():
    plt.scatter(P[0], P[1], s=35)

# -------------------------------------------------------------------------
# Coordinate labels
# -------------------------------------------------------------------------

# Offsets are chosen individually so labels don't overlap the geometry.

offsets = {
    "A": (-0.035, -0.055),
    "B": ( 0.015, -0.055),
    "C": ( 0.015,  0.015),

    "D": ( 0.015,  0.015),
    "E": ( 0.015,  0.015),
    "F": ( 0.015,  0.015),

    "X": ( 0.015,  0.015),
    "Y": (-0.045, -0.055),
    "Z": (-0.045,  0.015),
}

for label, P in points.items():
    dx, dy = offsets[label]

    plt.text(
        P[0] + dx,
        P[1] + dy,
        label,
        fontsize=14,
        fontweight="bold"
    )

# -------------------------------------------------------------------------
# Title
# -------------------------------------------------------------------------

plt.title(
    f"Monte Carlo: AZ = {d1:.8f}."
)

plt.axis("equal")
plt.axis("off")
plt.show()
