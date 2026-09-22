# Jim McCleery
# September 22, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2007_dc7628
#
# Problem:
# A convex quadrilateral is determined by the points of intersection
# of the curves
#
#       x^4 + y^4 = 100
#
# and
#
#       xy = 4.
#
# Determine its area.


import numpy as np
import matplotlib.pyplot as plt
import sympy as sp


# -----------------------------------------------------------------------------
def get_solutions():
    """
    Find the real points of intersection of

        x^4 + y^4 = 100
        xy = 4

    Returns:
        A list of (x, y) tuples containing floating-point numbers.
    """

    # Create the symbolic variables x and y.
    x, y = sp.symbols("x y", real=True)

    # Write the two equations.
    equation1 = sp.Eq(x**4 + y**4, 100)
    equation2 = sp.Eq(x * y, 4)

    # Ask SymPy to solve the two equations simultaneously.
    solutions = sp.solve(
        (equation1, equation2),
        (x, y)
    )

    # Convert the SymPy values to ordinary Python floating-point numbers.
    real_solutions = []

    for x_value, y_value in solutions:

        if x_value.is_real and y_value.is_real:
            real_solutions.append(
                (float(x_value), float(y_value))
            )

    return real_solutions


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Find the area of a polygon using the shoelace formula.

    Parameters:
        vertices:
            A list of polygon vertices in order around the polygon.

    Returns:
        The area of the polygon.
    """

    area = 0

    number_of_vertices = len(vertices)

    for i in range(number_of_vertices):

        x1, y1 = vertices[i]

        # The % operator makes the last vertex connect back
        # to the first vertex.
        x2, y2 = vertices[(i + 1) % number_of_vertices]

        area += x1 * y2 - y1 * x2

    return abs(area) / 2


# -----------------------------------------------------------------------------
def sort_vertices(vertices):
    """
    Put the vertices in order around the center of the polygon.

    This is necessary before drawing or finding the area of the
    quadrilateral.

    Parameters:
        vertices:
            A list of (x, y) points.

    Returns:
        The vertices arranged counterclockwise around their center.
    """

    # Find the center of the four points.
    center_x = sum(x for x, y in vertices) / len(vertices)
    center_y = sum(y for x, y in vertices) / len(vertices)

    # np.arctan2() gives the angle from the center of the polygon
    # to each vertex.
    #
    # Sorting by this angle puts the points in order around
    # the quadrilateral.
    return sorted(
        vertices,
        key=lambda point: np.arctan2(
            point[1] - center_y,
            point[0] - center_x
        )
    )


# -----------------------------------------------------------------------------
# Find the four intersection points.
vertices = get_solutions()

# SymPy does not necessarily return the points in polygon order,
# so arrange them in counterclockwise order.
vertices = sort_vertices(vertices)

# Find the area of the quadrilateral.
area = polygon_area(vertices)


# -----------------------------------------------------------------------------
# Create a grid of x- and y-values for drawing the curves.

x_values = np.linspace(-4, 4, 1000)
y_values = np.linspace(-4, 4, 1000)

# meshgrid() creates a rectangular grid of coordinate pairs.
X, Y = np.meshgrid(x_values, y_values)


# Rewrite each equation so that its right-hand side is zero.
#
# The contour where F1 = 0 is:
#
#       x^4 + y^4 = 100
#
# and the contour where F2 = 0 is:
#
#       xy = 4

F1 = X**4 + Y**4 - 100
F2 = X * Y - 4


# -----------------------------------------------------------------------------
# Create the graph.

plt.figure(figsize=(8, 8))


# Draw the two curves.
plt.contour(
    X,
    Y,
    F1,
    levels=[0],
    linewidths=2
)

plt.contour(
    X,
    Y,
    F2,
    levels=[0],
    linewidths=2
)


# -----------------------------------------------------------------------------
# Draw and fill the quadrilateral.

# Separate the vertices into their x- and y-coordinates.
polygon_x = [point[0] for point in vertices]
polygon_y = [point[1] for point in vertices]

plt.fill(
    polygon_x,
    polygon_y,
    alpha=0.35,
    edgecolor="red",
    linewidth=2
)


# -----------------------------------------------------------------------------
# Plot and label each intersection point.

for x, y in vertices:

    # Draw the point.
    plt.plot(x, y, "o")

    # Create a label such as:
    #
    #       (3.13, 1.28)
    #
    coordinate_label = f"({x:.3f}, {y:.3f})"

    # Place the label slightly away from the point.
    plt.annotate(
        coordinate_label,
        xy=(x, y),
        xytext=(8, 8),
        textcoords="offset points",
        fontsize=10
    )


# -----------------------------------------------------------------------------
# Draw the coordinate axes.

plt.axhline(0, linewidth=0.8)
plt.axvline(0, linewidth=0.8)


# Add coordinate labels and a grid.
plt.xlabel("x")
plt.ylabel("y")

plt.xticks(np.arange(-4, 5, 1))
plt.yticks(np.arange(-4, 5, 1))

plt.grid(True, alpha=0.4)


# Keep the same scale on both axes.
plt.axis("equal")

plt.xlim(-4, 4)
plt.ylim(-4, 4)


# Add a title.
plt.title(
    r"$x^4+y^4=100$ and $xy=4$"
    "\n"
    f"Area of the quadrilateral = {area:.3f}"
)


# Display the numerical results in the console.
print("Intersection points:")

for point in vertices:
    print(f"    ({point[0]:.6f}, {point[1]:.6f})")

print()
print(f"Area = {area:.6f}")


# Display the graph.
plt.show()
