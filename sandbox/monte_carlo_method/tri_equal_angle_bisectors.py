# Jim McCleery
# September 13, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2023_e269b2

from math import pi, sqrt, sin, cos, acos, hypot
from random import uniform

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """Return the distance between two points."""
    return hypot(x2 - x1, y2 - y1)


# -----------------------------------------------------------------------------
def law_of_cosines(side1, side2, opposite_side):
    """
    Return the angle opposite 'opposite_side'.

    The three arguments are the side lengths of a triangle.

    For example, if a triangle has sides a, b, and c, then

        law_of_cosines(a, b, c)

    returns the angle opposite side c.
    """

    value = (
        side1**2 + side2**2 - opposite_side**2
    ) / (2 * side1 * side2)

    # Rounding error can occasionally produce something like
    # 1.0000000001, which acos() cannot handle.
    if value < -1 or value > 1:
        return None

    return acos(value)


# -----------------------------------------------------------------------------
def point_line_distance(px, py, x1, y1, x2, y2):
    """
    Return the perpendicular distance from point P to the line through
    (x1, y1) and (x2, y2).
    """

    numerator = abs(
        (x2 - x1) * (y1 - py)
        - (x1 - px) * (y2 - y1)
    )

    denominator = hypot(x2 - x1, y2 - y1)

    return numerator / denominator


# -----------------------------------------------------------------------------
# We put B at the origin and C on the positive x-axis:
#
#       B = (0, 0)
#       C = (BC, 0)
#
# A is then determined from AB, BC, and AC = 2.
#
# We use a random search for values of AB and BC satisfying both
# conditions:
#
#       angle BAN = angle MAC
#
# and
#
#       AB * BC = AM
#
# This is not the most efficient numerical method, but it is simple
# and closely follows the geometry.

best_error = float("inf")
best_data = None

for trial in range(10**7):

    # Choose trial side lengths.
    AB = uniform(0.2, 1.0)
    BC = uniform(0.5, 4.0)

    AC = 2.0

    # -------------------------------------------------------------
    # Find angle ABC.
    #
    # At B, the adjacent sides are AB and BC and the opposite side
    # is AC.
    angle_B = law_of_cosines(AB, BC, AC)

    if angle_B is None:
        continue

    # Coordinates of the triangle.
    Bx, By = 0.0, 0.0
    Cx, Cy = BC, 0.0

    Ax = AB * cos(angle_B)
    Ay = AB * sin(angle_B)

    # -------------------------------------------------------------
    # Check that angle BAC is obtuse.
    angle_A = law_of_cosines(AB, AC, BC)

    if angle_A is None or angle_A <= pi / 2:
        continue

    # -------------------------------------------------------------
    # D is the foot of the perpendicular from A to BC.
    #
    # Since BC is the x-axis, D has the same x-coordinate as A.
    Dx, Dy = Ax, 0.0

    # M is the midpoint of BC.
    Mx, My = BC / 2, 0.0

    # N is the midpoint of BD.
    Nx, Ny = Dx / 2, 0.0

    # -------------------------------------------------------------
    # Compute the actual lengths AN and AM.
    AN = distance(Ax, Ay, Nx, Ny)
    AM_actual = distance(Ax, Ay, Mx, My)

    BN = distance(Bx, By, Nx, Ny)
    MC = distance(Mx, My, Cx, Cy)

    # -------------------------------------------------------------
    # angle BAN:
    #
    # In triangle ABN, the angle at A is opposite side BN.
    angle_BAN = law_of_cosines(AB, AN, BN)

    # angle MAC:
    #
    # In triangle AMC, the angle at A is opposite side MC.
    angle_MAC = law_of_cosines(AM_actual, AC, MC)

    if angle_BAN is None or angle_MAC is None:
        continue

    # -------------------------------------------------------------
    # CONDITION 1:
    # angle BAN = angle MAC
    angle_error = abs(angle_BAN - angle_MAC)

    # CONDITION 2:
    # AB * BC = AM
    length_error = abs(AB * BC - AM_actual)

    # Combine the two errors into one number.
    total_error = angle_error**2 + length_error**2

    # Keep the best trial found so far.
    if total_error < best_error:
        best_error = total_error
        best_data = (
            AB,
            BC,
            Ax,
            Ay,
            Dx,
            Dy,
            Mx,
            My,
            Nx,
            Ny,
            AM_actual,
        )


# -----------------------------------------------------------------------------
# Use the best approximation found.

AB, BC, Ax, Ay, Dx, Dy, Mx, My, Nx, Ny, AM = best_data

Bx, By = 0.0, 0.0
Cx, Cy = BC, 0.0

# Distance from B to line AM.
answer = point_line_distance(
    Bx, By,
    Ax, Ay,
    Mx, My
)

print(f"AB = {AB:.8f}")
print(f"BC = {BC:.8f}")
print(f"AM = {AM:.8f}")
print(f"AB * BC = {AB * BC:.8f}")
print(f"Distance from B to line AM = {answer:.8f}")
print(f"Search error = {best_error:.12g}")


# -----------------------------------------------------------------------------
# Draw the diagram.

plt.plot([Bx, Ax], [By, Ay])       # AB
plt.plot([Ax, Cx], [Ay, Cy])       # AC
plt.plot([Bx, Cx], [By, Cy])       # BC
plt.plot([Ax, Dx], [Ay, Dy])       # AD
plt.plot([Ax, Mx], [Ay, My])       # AM
plt.plot([Ax, Nx], [Ay, Ny])       # AN

# Plot and label the important points.
points = {
    "A": (Ax, Ay),
    "B": (Bx, By),
    "C": (Cx, Cy),
    "D": (Dx, Dy),
    "M": (Mx, My),
    "N": (Nx, Ny),
}

for name, (x, y) in points.items():
    plt.plot(x, y, "ko")
    plt.text(x, y, f"  {name}", fontsize=12)

plt.title(
    f"Distance from B to line AM = {answer:.5f}"
)

plt.axis("equal")
plt.axis("off")
plt.show()
