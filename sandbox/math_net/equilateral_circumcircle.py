# Jim McCleery
# October 31, 2026
# Kailua-Kona, HI
# https://mathnet.mit.edu/explorer.html?p=ibe_1994_85323d

"""Find P so that rays AP, BP, CP meet the circumcircle at an equilateral DEF.

Install the three required packages once:
    python -m pip install numpy matplotlib scipy
Then run:
    python equilateral_circumcircle.py

Points are (x, y) tuples. NumPy arrays let us subtract or scale whole points.
This is a numerical construction, not a geometric proof or an exhaustive search.
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from scipy.optimize import least_squares


def circumcircle(A, B, C):
    """Return the center and radius through three noncollinear points."""
    # Subtracting two circle equations eliminates the squared unknowns.
    # The remaining two linear equations determine the center.
    vertices = np.array([A, B, C], dtype=float)
    if vertices.shape != (3, 2) or not np.all(np.isfinite(vertices)):
        raise ValueError("Supply three finite (x, y) points.")
    a, b, c = vertices
    matrix = 2 * np.array([b - a, c - a])
    rhs = np.array([np.dot(b - a, b - a), np.dot(c - a, c - a)])
    if np.linalg.matrix_rank(matrix) < 2:
        raise ValueError("The vertices must form a nondegenerate triangle.")
    center = a + np.linalg.solve(matrix, rhs)
    return center, float(np.linalg.norm(a - center))


def equilateral_vertices(angle):
    """Place three points 120 degrees apart on the unit circle."""
    angles = angle + np.arange(3) * (2 * np.pi / 3)
    # Each row of the result is one (x, y) point.
    return np.column_stack((np.cos(angles), np.sin(angles)))


def find_point(A, B, C):
    """Return P, D/E/F, circle center, and radius for an acute triangle.

    Rotate an equilateral triangle on the circle until AD, BE, and CF
    meet at P. Try both orders of D/E/F and several starting rotations.
    A failed numerical search raises an error instead of looping forever.
    """
    center, radius = circumcircle(A, B, C)
    vertices = np.array([A, B, C], dtype=float)
    # At each vertex, a positive dot product means an angle below 90 degrees.
    for i in range(3):
        u = vertices[(i + 1) % 3] - vertices[i]
        v = vertices[(i + 2) % 3] - vertices[i]
        if np.dot(u, v) <= 0:
            raise ValueError("ABC must be an acute-angled triangle.")

    # Work on a circle of radius 1 centered at (0, 0). This makes the
    # solver's tolerance independent of the triangle's size and position.
    normalized = (vertices - center) / radius
    tolerance = 1e-9

    for order in ((0, 1, 2), (0, 2, 1)):
        def residuals(unknowns):
            """Three zero cross products mean three pairs are collinear."""
            p = unknowns[:2]
            targets = equilateral_vertices(unknowns[2])[list(order)]
            directions = targets - normalized
            offsets = p - normalized
            # In two dimensions, u_x*v_y - u_y*v_x is zero for
            # parallel vectors. Divide by length for a distance residual.
            lengths = np.linalg.norm(directions, axis=1)
            return (directions[:, 0] * offsets[:, 1]
                    - directions[:, 1] * offsets[:, 0]) / np.maximum(lengths, 1e-12)

        for angle in np.linspace(0, 2 * np.pi, 24, endpoint=False):
            result = least_squares(
                residuals, [0.0, 0.0, angle],
                xtol=1e-12, ftol=1e-12, gtol=1e-12, max_nfev=1000,
            )
            p = result.x[:2]
            targets = equilateral_vertices(result.x[2])[list(order)]
            directions = targets - normalized
            squared_lengths = np.sum(directions**2, axis=1)
            if np.min(squared_lengths) < tolerance:
                continue  # A second intersection must differ from its vertex.
            # P = vertex + t*(target - vertex). 0 < t < 1 puts P
            # between the original vertex and the second circle intersection.
            t = np.sum((p - normalized) * directions, axis=1) / squared_lengths
            if (result.success
                    and np.max(np.abs(residuals(result.x))) < tolerance
                    and np.linalg.norm(p) < 1 - tolerance
                    and np.all((t > tolerance) & (t < 1 - tolerance))):
                return center + radius * p, center + radius * targets, center, radius

    raise RuntimeError("No verified solution found. Try more starting rotations.")


def draw_diagram(A, B, C, P, targets, center, radius):
    """Draw the construction and label all seven points with coordinates."""
    fig, ax = plt.subplots(figsize=(11, 9), layout="constrained")
    ax.add_patch(Circle(center, radius, fill=False, color="slategray", lw=1.7))
    # Repeating the first vertex closes each triangle.
    for points, color, label in (
        ([A, B, C], "#2463a0", "Original triangle ABC"),
        (targets, "#c65b16", "Equilateral triangle DEF"),
    ):
        closed = np.vstack([points, points[0]])
        ax.plot(closed[:, 0], closed[:, 1], color=color, lw=2, label=label)

    # These segments show where the three rays meet the circle again.
    for vertex, target in zip([A, B, C], targets):
        ax.plot([vertex[0], target[0]], [vertex[1], target[1]],
                "--", color="gray", lw=1, alpha=0.65)

    points = dict(zip("ABCDEF", [A, B, C, *targets]))
    for name, point in points.items():
        x, y = point
        # Move each label outward from the circle to keep it off the edges.
        direction = (point - center) / radius
        offset = 14 * direction
        ax.scatter(x, y, color="#2463a0" if name in "ABC" else "#c65b16", zorder=4)
        ax.annotate(f"{name} ({x:.3f}, {y:.3f})", (x, y),
                    xytext=tuple(offset), textcoords="offset points",
                    ha="left" if direction[0] >= 0 else "right",
                    va="bottom" if direction[1] >= 0 else "top", fontsize=10)
    ax.scatter(*P, color="purple", s=55, zorder=5, label="Point P")
    ax.annotate(f"P ({P[0]:.3f}, {P[1]:.3f})", P, xytext=(10, 10),
                textcoords="offset points", color="purple", fontsize=10)
    ax.set(xlim=(center[0] - 1.5 * radius, center[0] + 1.5 * radius),
           ylim=(center[1] - 1.4 * radius, center[1] + 1.4 * radius),
           xlabel="x-coordinate", ylabel="y-coordinate",
           title="Find P so that DEF is equilateral\nD, E, F are on the circumcircle")
    # Equal scales prevent a circle from appearing oval.
    ax.set_aspect("equal")
    ax.grid(alpha=0.18)
    ax.legend(loc="upper right")
    return fig


def main():
    """Choose the triangle, solve the problem, and display the result."""
    # Change these three tuples to explore other acute triangles.
    A = (0, 0)
    B = (14, 0)
    C = (5, 11)
    P, targets, center, radius = find_point(A, B, C)
    print("Coordinates (rounded for display):")
    for name, point in zip("ABCPDEF", [A, B, C, P, *targets]):
        print(f"  {name} = ({point[0]:.6f}, {point[1]:.6f})")
    D, E, F = targets
    lengths = [np.linalg.norm(D - E), np.linalg.norm(E - F), np.linalg.norm(F - D)]
    print("DE, EF, FD:", ", ".join(f"{length:.10f}" for length in lengths))
    print(f"Largest side-length difference: {max(lengths) - min(lengths):.3e}")
    draw_diagram(A, B, C, P, targets, center, radius)
    plt.show()


# Run main() only when this file is executed, not when it is imported.
if __name__ == "__main__":
    main()
