# -----------------------------------------------------------------------------
# Jim McCleery
# September 26, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=btw_1997_483abb
#
# Infinite Angle Sum on Two Parallel Lines
# -----------------------------------------------------------------------------

from math import pi, sqrt, acos
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def distance(A, B):
    """
    Return the straight-line distance between two points.

    Each point is stored as a tuple:

        A = (x, y)
        B = (x, y)
    """

    x1, y1 = A
    x2, y2 = B

    return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# -----------------------------------------------------------------------------
def law_of_cosines(a, b, c):
    """
    Return the angle opposite side c.

    The Law of Cosines says:

        c^2 = a^2 + b^2 - 2ab cos(theta)

    Solving for theta gives:

        theta = acos((a^2 + b^2 - c^2) / (2ab))

    The returned angle is in radians.
    """

    cosine_value = (a**2 + b**2 - c**2) / (2 * a * b)

    # Floating-point calculations can sometimes produce a number
    # very slightly outside the legal range [-1, 1] for acos().
    cosine_value = max(-1, min(1, cosine_value))

    return acos(cosine_value)


# -----------------------------------------------------------------------------
def plot_line(A, B):
    """Draw a line segment from point A to point B."""

    x1, y1 = A
    x2, y2 = B

    plt.plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# Problem setup
#
# Put the A points on y = 0, one unit apart.
# Put the B points on y = height, two units apart.
#
# The value 0.5 determines the horizontal position of B1.
# -----------------------------------------------------------------------------

height = 5

A1 = (0, 0)
A2 = (1, 0)
B1 = (0.5, height)


# -----------------------------------------------------------------------------
# Find alpha = angle A1-A2-B1.
#
# In triangle A1-A2-B1:
#
#     A1A2 = 1
#     A1B1 = d1
#     A2B1 = d2
#
# alpha is the angle at A2, opposite side A1B1.
# -----------------------------------------------------------------------------

d1 = distance(A1, B1)
d2 = distance(A2, B1)

alpha = law_of_cosines(1, d2, d1)


# -----------------------------------------------------------------------------
# Approximate the infinite angle sum.
#
# 10,000 terms are more than enough to make the numerical result
# very close to its limiting value.
#
# We calculate all 10,000 terms, but we do NOT draw all of them.
# -----------------------------------------------------------------------------

number_of_terms = 10_000
total_angles = 0

for i in range(number_of_terms):

    # A_i and A_(i+1)
    A_i = (i, 0)
    A_next = (i + 1, 0)

    # B_i
    B_i = (0.5 + 2 * i, height)

    # Lengths from B_i to the two neighboring A points.
    d1 = distance(A_i, B_i)
    d2 = distance(A_next, B_i)

    # Since A_i and A_(i+1) are one unit apart,
    # the angle at B_i is opposite the side of length 1.
    angle = law_of_cosines(d1, d2, 1)

    total_angles += angle


# -----------------------------------------------------------------------------
# Draw the geometric picture.
#
# Only the first few points are drawn so the diagram remains readable.
# -----------------------------------------------------------------------------

number_to_plot = 6

plt.figure(figsize=(11, 6))

# Draw the two parallel lines.
plt.axhline(0)
plt.axhline(height)


# Draw and label the A points.
for i in range(number_to_plot + 1):

    A = (i, 0)

    plt.plot(*A, "o")

    # Label each point with both its name and coordinates.
    plt.text(
        A[0],
        A[1] - 0.35,
        rf"$A_{{{i + 1}}}$ = ({A[0]}, {A[1]})",
        ha="center",
        va="top"
    )


# Draw and label the B points.
for i in range(number_to_plot):

    B = (0.5 + 2 * i, height)

    plt.plot(*B, "o")

    plt.text(
        B[0],
        B[1] + 0.30,
        rf"$B_{{{i + 1}}}$ = ({B[0]:g}, {B[1]})",
        ha="center",
        va="bottom"
    )

    # Draw the two sides that form the angle at B_i.
    A_i = (i, 0)
    A_next = (i + 1, 0)

    plot_line(A_i, B)
    plot_line(A_next, B)


# -----------------------------------------------------------------------------
# Display the numerical result.
# -----------------------------------------------------------------------------

plt.title(
    f"Angle sum ≈ {total_angles:.6f} radians\n"
    f"π − α ≈ {pi - alpha:.6f} radians"
)

plt.xlim(-1, 12)
plt.ylim(-1, height + 1)

# Equal scaling keeps the geometry from being distorted.
plt.gca().set_aspect("equal", adjustable="box")

# Hide the ordinary x- and y-axis markings because the point
# coordinates are written directly on the diagram.
plt.axis("off")

plt.show()


# Print the important numerical values.
print(f"alpha             = {alpha:.10f}")
print(f"angle sum         = {total_angles:.10f}")
print(f"pi - alpha        = {pi - alpha:.10f}")
print(f"difference        = {abs(total_angles - (pi - alpha)):.10e}")
