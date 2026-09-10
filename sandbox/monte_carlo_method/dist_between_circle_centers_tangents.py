# Jim McCleery
# September 9, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2023_ff8f78
#
# Two non-intersecting circles:
#     common internal tangent = 19
#     common external tangent = 37
#     expected value of XY^2 = 2023
#
# Goal:
#     Estimate the distance between the centers using Monte Carlo simulation.
#
# Coordinate labels used in the diagram:
#     O1 = center of circle 1
#     O2 = center of circle 2
#     A, B = endpoints of the common external tangent
#     C, D = endpoints of the common internal tangent

# -----------------------------------------------------------------------------

from math import pi, sqrt, sin, cos, acos
from random import uniform

import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def distance_squared(x1, y1, x2, y2):
    """Return the square of the distance between two points."""

    return (x2 - x1) ** 2 + (y2 - y1) ** 2


# -----------------------------------------------------------------------------
def monte_carlo_expected_xy_squared(r1, r2, d, samples):
    """
    Estimate E[XY^2] by Monte Carlo simulation.

    X is chosen uniformly at random on circle 1.
    Y is chosen uniformly at random on circle 2.

    Circle 1 has center O1 = (0, 0).
    Circle 2 has center O2 = (d, 0).
    """

    total = 0.0

    for _ in range(samples):

        # A random angle from 0 to 2*pi chooses a point uniformly
        # around the circumference of a circle.
        angle_x = uniform(0, 2 * pi)
        angle_y = uniform(0, 2 * pi)

        # Coordinates of random point X on circle 1.
        x_x = r1 * cos(angle_x)
        y_x = r1 * sin(angle_x)

        # Coordinates of random point Y on circle 2.
        # The second circle is shifted d units to the right.
        x_y = d + r2 * cos(angle_y)
        y_y = r2 * sin(angle_y)

        total += distance_squared(x_x, y_x, x_y, y_y)

    return total / samples


# -----------------------------------------------------------------------------
def plot_circle(center_x, center_y, radius):
    """Draw a circle."""

    circle = plt.Circle(
        (center_x, center_y),
        radius,
        fill=False,
        linewidth=2
    )

    plt.gca().add_patch(circle)


# -----------------------------------------------------------------------------
# Information given in the problem.

internal_tangent = 19
external_tangent = 37
target_expected_value = 2023


# -----------------------------------------------------------------------------
# The tangent-length formulas give
#
#     external_tangent^2 = d^2 - (r1 - r2)^2
#     internal_tangent^2 = d^2 - (r1 + r2)^2
#
# Subtracting the equations gives
#
#     4*r1*r2 = external_tangent^2 - internal_tangent^2
#
# Therefore, once r1 is chosen, r2 is determined.

radius_product = (
    external_tangent ** 2 - internal_tangent ** 2
) / 4


# -----------------------------------------------------------------------------
# Monte Carlo search.
#
# For each trial:
#     1. Choose a possible value for r1.
#     2. Compute r2 from r1*r2 = 252.
#     3. Compute d from the external tangent.
#     4. Randomly choose many X and Y points.
#     5. Estimate E[XY^2].
#     6. Keep the circle pair whose estimate is closest to 2023.
#
# Increasing either number below improves the estimate but takes longer.

radius_trials = 10**4
samples_per_radius = 10**4

best_difference = float("inf")

best_r1 = None
best_r2 = None
best_d = None
best_expected_value = None


for _ in range(radius_trials):

    # Try a possible radius for circle 1.
    r1 = uniform(10, 15)

    # The tangent lengths force the product r1*r2 to be 252.
    r2 = radius_product / r1

    # From the external tangent:
    #
    #     37^2 = d^2 - (r1-r2)^2
    #
    # so
    #
    #     d = sqrt(37^2 + (r1-r2)^2)
    d = sqrt(
        external_tangent ** 2
        + (r1 - r2) ** 2
    )

    # Estimate E[XY^2] for THESE circles only.
    expected_value = monte_carlo_expected_xy_squared(
        r1,
        r2,
        d,
        samples_per_radius
    )

    difference = abs(
        expected_value - target_expected_value
    )

    # Save the best result found so far.
    if difference < best_difference:

        best_difference = difference
        best_r1 = r1
        best_r2 = r2
        best_d = d
        best_expected_value = expected_value


# -----------------------------------------------------------------------------
# Display the numerical result.

print(f"radius 1 = {best_r1:.5f}")
print(f"radius 2 = {best_r2:.5f}")
print(f"estimated E[XY^2] = {best_expected_value:.5f}")
print(f"distance between centers = {best_d:.5f}")


# -----------------------------------------------------------------------------
# Construct coordinates for the picture.
#
# O1 and O2 are the two centers.

O1_x, O1_y = 0, 0
O2_x, O2_y = best_d, 0


# -----------------------------------------------------------------------------
# A and B are the tangent points of a common EXTERNAL tangent.
#
# For the right triangle formed by the centers and the tangent,
#
#     sin(theta) = (r1-r2) / d

sin_theta = (best_r1 - best_r2) / best_d
cos_theta = external_tangent / best_d

# A is on circle 1.
A_x = best_r1 * sin_theta
A_y = best_r1 * cos_theta

# B is on circle 2.
B_x = best_d + best_r2 * sin_theta
B_y = best_r2 * cos_theta


# -----------------------------------------------------------------------------
# C and D are the tangent points of a common INTERNAL tangent.
#
# Here
#
#     cos(phi) = (r1+r2) / d

phi = acos(
    (best_r1 + best_r2) / best_d
)

# C is on circle 1.
C_x = best_r1 * cos(phi)
C_y = best_r1 * sin(phi)

# D is on circle 2 and lies on the opposite side of its center.
D_x = best_d - best_r2 * cos(phi)
D_y = -best_r2 * sin(phi)


# -----------------------------------------------------------------------------
# Draw the two circles.

fig, ax = plt.subplots(figsize=(11, 6))

plot_circle(O1_x, O1_y, best_r1)
plot_circle(O2_x, O2_y, best_r2)


# Draw the line joining the centers.
plt.plot(
    [O1_x, O2_x],
    [O1_y, O2_y],
    linestyle="--"
)


# Draw the common external tangent AB.
plt.plot(
    [A_x, B_x],
    [A_y, B_y],
    linewidth=2
)


# Draw the common internal tangent CD.
plt.plot(
    [C_x, D_x],
    [C_y, D_y],
    linewidth=2
)


# -----------------------------------------------------------------------------
# Mark the important coordinates.

points = {
    "O1": (O1_x, O1_y),
    "O2": (O2_x, O2_y),
    "A": (A_x, A_y),
    "B": (B_x, B_y),
    "C": (C_x, C_y),
    "D": (D_x, D_y),
}


for label, (x, y) in points.items():

    plt.plot(x, y, "o")

    # Show both the point's name and its approximate coordinates.
    plt.annotate(
        f"{label} ({x:.1f}, {y:.1f})",
        (x, y),
        xytext=(7, 7),
        textcoords="offset points"
    )


# Label the two tangent lengths.
plt.text(
    (A_x + B_x) / 2,
    (A_y + B_y) / 2 + 1,
    "37",
    fontsize=12
)

plt.text(
    (C_x + D_x) / 2,
    (C_y + D_y) / 2 - 2,
    "19",
    fontsize=12
)


# -----------------------------------------------------------------------------
# Finish the graph.

plt.title(
    f"Monte Carlo estimate of center distance = {best_d:.5f}"
)

plt.axis("equal")
plt.axis("off")
plt.show()
