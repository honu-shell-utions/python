"""
Jim McCleery
September 1, 2026
Kailua-Kona, HI

https://mathnet.mit.edu/explorer.html?p=usa_2004_4ff424

Draw trapezoid ABCD and calculate the angle formed at E when sides AB and
CD are extended until they meet.
"""

from math import acos, degrees

import matplotlib.pyplot as plt


def angle_from_three_sides(side_1, side_2, opposite_side):
    """Return the angle between side_1 and side_2, measured in degrees.

    This is the Law of Cosines rearranged to solve for an angle.  The angle
    returned is opposite ``opposite_side``.
    """
    cosine_of_angle = (
        side_1**2 + side_2**2 - opposite_side**2
    ) / (2 * side_1 * side_2)

    # acos() returns radians, so degrees() converts the result to degrees.
    return degrees(acos(cosine_of_angle))


def draw_segment(point_1, point_2, **style):
    """Draw a line segment joining two points such as (x, y)."""
    x_values = [point_1[0], point_2[0]]
    y_values = [point_1[1], point_2[1]]
    plt.plot(x_values, y_values, **style)


# The parallel sides have lengths BC = 7 and AD = 17, so the small triangle
# EBC is 7/17 the size of the large triangle EAD.  Therefore:
#
#     EB / EA = EC / ED = 7 / 17
#
# Since AB = EA - EB = 6, EA = 6 * 17 / (17 - 7) = 10.2.
# Since CD = ED - EC = 8, ED = 8 * 17 / (17 - 7) = 13.6.
EA = 10.2
EB = 4.2
EC = 5.6
ED = 13.6
AD = 17

# Convenient coordinates put E at the origin, AB on the x-axis, and CD on
# the y-axis.  The calculated angle below confirms that these axes meet at
# the correct 90-degree angle.
E = (0, 0)
B = (EB, 0)
A = (EA, 0)
C = (0, EC)
D = (0, ED)

# In triangle EAD, angle E lies between sides EA and ED and is opposite AD.
angle_E = angle_from_three_sides(EA, ED, AD)

# Draw the four sides of the trapezoid.
for start, end in [(A, B), (B, C), (C, D), (D, A)]:
    draw_segment(start, end, color="navy", linewidth=2)

# Draw the extensions of AB and CD to their meeting point E as dashed lines.
draw_segment(E, B, color="gray", linestyle="--", linewidth=1.5)
draw_segment(E, C, color="gray", linestyle="--", linewidth=1.5)

# Mark and label each point.  The small offsets keep labels away from lines.
label_offsets = {
    "A": (0.25, -0.55),
    "B": (0.25, -0.55),
    "C": (-1.55, 0.15),
    "D": (-1.65, 0.15),
    "E": (-1.25, -0.55),
}

for name, point in {"A": A, "B": B, "C": C, "D": D, "E": E}.items():
    plt.scatter(*point, color="black", zorder=3)
    dx, dy = label_offsets[name]
    plt.text(
        point[0] + dx,
        point[1] + dy,
        f"{name} {point}",
        fontsize=10,
    )

plt.title(f"Angle E = {angle_E:.1f}°")
plt.axis("equal")  # Use the same scale on both axes so angles look correct.
plt.axis("off")
plt.tight_layout()
plt.show()

