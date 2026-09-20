# Jim McCleery
# September 20, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2004_65438f
#
# Trapezoid ABCD
#
# Given:
#     AD is parallel to BC
#     angle A = angle D = 45 degrees
#     angle B = angle C = 135 degrees
#     AB = 6
#     area = 30
#
# Find the length of BC.


from math import sqrt
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
def plot_line(A, B):
    """
    Draw a line segment between two points.

    Each point is stored as a tuple:

        A = (x, y)
        B = (x, y)
    """

    x1, y1 = A
    x2, y2 = B

    plt.plot([x1, x2], [y1, y2], color="black")


# -----------------------------------------------------------------------------
# Because AB = 6 and angle A = 45 degrees, the horizontal and vertical
# components of AB are both:
#
#       6 / sqrt(2) = 3 * sqrt(2)
#
# Therefore the height of the trapezoid is 3*sqrt(2).

height = 3 * sqrt(2)


# The area of a trapezoid is:
#
#       area = height * (AD + BC) / 2
#
# Since the area is 30:
#
#       30 = 3*sqrt(2) * (AD + BC) / 2
#
# which gives:
#
#       AD + BC = 10*sqrt(2)
#
# The two 45-degree sides each extend horizontally by 3*sqrt(2), so:
#
#       AD - BC = 6*sqrt(2)
#
# Solving these two equations gives:
#
#       AD = 8*sqrt(2)
#       BC = 2*sqrt(2)

AD = 8 * sqrt(2)
BC = 2 * sqrt(2)


# -----------------------------------------------------------------------------
# Define the four vertices of the trapezoid.

A = (0, 0)
B = (3 * sqrt(2), 3 * sqrt(2))
C = (5 * sqrt(2), 3 * sqrt(2))
D = (8 * sqrt(2), 0)


# -----------------------------------------------------------------------------
# Draw the four sides of the trapezoid.

plot_line(A, B)
plot_line(B, C)
plot_line(C, D)
plot_line(D, A)


# Draw a dot at each vertex.
for point in [A, B, C, D]:
    plt.plot(point[0], point[1], "ko")


# -----------------------------------------------------------------------------
# Add the vertex names and their exact coordinates.

plt.text(
    A[0] - 0.3,
    A[1] - 0.45,
    r"$A(0,0)$",
    ha="right"
)

plt.text(
    B[0],
    B[1] + 0.35,
    r"$B(3\sqrt{2},\,3\sqrt{2})$",
    ha="right"
)

plt.text(
    C[0],
    C[1] + 0.35,
    r"$C(5\sqrt{2},\,3\sqrt{2})$",
    ha="left"
)

plt.text(
    D[0] + 0.3,
    D[1] - 0.45,
    r"$D(8\sqrt{2},\,0)$",
    ha="left"
)


# -----------------------------------------------------------------------------
# Add labels for the two parallel bases.

plt.text(
    (B[0] + C[0]) / 2,
    B[1] - 0.4,
    r"$BC=2\sqrt{2}$",
    ha="center"
)

plt.text(
    (A[0] + D[0]) / 2,
    -0.4,
    r"$AD=8\sqrt{2}$",
    ha="center"
)


# -----------------------------------------------------------------------------
# Finish the graph.

plt.title(
    rf"The length of $BC$ is $2\sqrt{{2}} \approx {BC:.3f}$"
)

# Use the same scale on both axes so the trapezoid has the correct shape.
plt.axis("equal")

# Hide the ordinary x- and y-axes.
plt.axis("off")

plt.show()
