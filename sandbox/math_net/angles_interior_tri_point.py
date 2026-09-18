# -----------------------------------------------------------------------------
# Jim McCleery
# September 18, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2015_b948ee
# -----------------------------------------------------------------------------

from math import acos, cos, degrees, radians, sin, sqrt
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def law_of_cosines(side1, side2, opposite_side):
    """
    Find an angle of a triangle using the Law of Cosines.

    side1 and side2 are the sides next to the angle.
    opposite_side is the side opposite the angle.

    The function returns the angle in radians.
    """
    cosine_value = (
        side1**2 + side2**2 - opposite_side**2
    ) / (2 * side1 * side2)

    return acos(cosine_value)


# -----------------------------------------------------------------------------
def plot_line(point1, point2, style="-", linewidth=2):
    """
    Draw a line segment between two points.

    Each point is stored as an (x, y) coordinate pair.
    """
    x1, y1 = point1
    x2, y2 = point2

    plt.plot(
        [x1, x2],
        [y1, y2],
        style,
        linewidth=linewidth,
    )


# -----------------------------------------------------------------------------
# GEOMETRY CALCULATIONS
# -----------------------------------------------------------------------------

# Length AM.
#
# This comes from the small triangle containing the 40°, 30°, and 110°
# angles.  The side of length 5 is opposite the 110° angle.
AM = 5 / sin(radians(110))


# Length BM.
#
# Apply the Law of Sines to a triangle containing AM.
BM = AM * sin(radians(10)) / sin(radians(20))


# Length CM.
CM = 10 * sin(radians(40)) / sin(radians(110))


# Length AB.
AB = BM * sin(radians(150)) / sin(radians(10))


# Length BC.
#
# Triangle ABC has:
#     AC = 10
#     AB = calculated above
#     angle BAC = 50°
#
# Use the Law of Cosines to find BC.
AC = 10

BC = sqrt(
    AB**2
    + AC**2
    - 2 * AB * AC * cos(radians(50))
)


# -----------------------------------------------------------------------------
# POINT COORDINATES
# -----------------------------------------------------------------------------

# Put A at the origin and AC along the x-axis.
A = (0, 0)

# AB makes a 50° angle with the positive x-axis.
B = (
    AB * cos(radians(50)),
    AB * sin(radians(50)),
)

# AC has length 10 and lies on the x-axis.
C = (10, 0)

# AM makes a 40° angle with the positive x-axis.
M = (
    AM * cos(radians(40)),
    AM * sin(radians(40)),
)


# -----------------------------------------------------------------------------
# FIND THE UNKNOWN ANGLE MBC
# -----------------------------------------------------------------------------

# In triangle BMC:
#     BM = BM
#     BC = BC
#     CM = CM
#
# Angle MBC is between BM and BC, so CM is the side opposite the angle.
angle_MBC = law_of_cosines(BM, BC, CM)

# Convert the answer from radians to degrees.
angle_MBC = degrees(angle_MBC)


# -----------------------------------------------------------------------------
# DRAW THE FIGURE
# -----------------------------------------------------------------------------

# Draw the three outside sides of triangle ABC.
plot_line(A, B)
plot_line(B, C)
plot_line(C, A)

# Draw the three lines connecting M to the vertices.
# Dashed lines make them easier to distinguish from the main triangle.
plot_line(A, M, "--", linewidth=1.5)
plot_line(B, M, "--", linewidth=1.5)
plot_line(C, M, "--", linewidth=1.5)


# Draw a dot at each important point.
for point in [A, B, C, M]:
    plt.plot(point[0], point[1], "ko")


# -----------------------------------------------------------------------------
# ADD POINT AND COORDINATE LABELS
# -----------------------------------------------------------------------------

# The offsets move each label slightly away from its point so that the
# text does not sit directly on top of the dot.
point_labels = {
    "A": (A, (-0.55, -0.25)),
    "B": (B, (-0.15, 0.35)),
    "C": (C, (0.15, -0.25)),
    "M": (M, (0.15, 0.20)),
}

for name, (point, offset) in point_labels.items():
    x, y = point
    dx, dy = offset

    # Show both the point name and its calculated coordinates.
    plt.text(
        x + dx,
        y + dy,
        f"{name} ({x:.2f}, {y:.2f})",
        fontsize=11,
    )


# -----------------------------------------------------------------------------
# FINISH THE GRAPH
# -----------------------------------------------------------------------------

plt.title(f"The angle MBC is {angle_MBC:.1f}°\n\n")

# Make one unit on the x-axis the same physical size as one unit on the y-axis.
# This prevents the triangle from being visually distorted.
plt.axis("equal")

# Hide the normal x- and y-axis markings because this is a geometry diagram.
plt.axis("off")

plt.show()
