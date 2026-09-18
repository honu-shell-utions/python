# -----------------------------------------------------------------------------
# Jim McCleery
# May 26, 2026
# Kailua-Kona, HI
#
# Problem link:
# https://mathnet.mit.edu/explorer.html?p=usa_2025_1bed77
# -----------------------------------------------------------------------------

import sympy as sp
import numpy as np
import matplotlib.pyplot as plt


# -----------------------------------------------------------------------------
# Geometry helpers
# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Return the area of a polygon using the shoelace formula.

    Parameters
    ----------
    vertices : list[tuple[float, float]]
        Ordered list of polygon vertices.

    Returns
    -------
    float
        Area of the polygon.
    """
    area = 0.0
    n = len(vertices)

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2

    return abs(area) / 2.0


def closed_xy(vertices):
    """
    Return x- and y-coordinate lists for plotting/filling a closed polygon.
    """
    xs = [p[0] for p in vertices] + [vertices[0][0]]
    ys = [p[1] for p in vertices] + [vertices[0][1]]
    return xs, ys


def draw_circle(ax, center, radius, start=0, stop=2 * np.pi, **kwargs):
    """
    Draw a full circle or circular arc.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Axes on which to draw.
    center : tuple[float, float]
        Circle center.
    radius : float
        Circle radius.
    start, stop : float
        Start and stop angles in radians.
    """
    t = np.linspace(start, stop, 1000)
    x0, y0 = center
    x = x0 + radius * np.cos(t)
    y = y0 + radius * np.sin(t)
    ax.plot(x, y, **kwargs)


def draw_segment(ax, p, q, **kwargs):
    """
    Draw the line segment from point p to point q.
    """
    ax.plot([p[0], q[0]], [p[1], q[1]], **kwargs)


def mark_point(ax, name, point, dx=0.2, dy=0.2):
    """
    Plot and label a point.
    """
    ax.scatter(point[0], point[1], color="black", s=45, zorder=5)
    ax.text(point[0] + dx, point[1] + dy, name, fontsize=14)


def to_float_pair(point):
    """
    Convert a SymPy point (x, y) to a float pair.
    """
    return float(sp.N(point[0])), float(sp.N(point[1]))


# -----------------------------------------------------------------------------
# Solve for the upper-left corner G = (x, y)
# -----------------------------------------------------------------------------
def solve_for_G():
    """
    Solve the system

        (9 - x)(sqrt(15^2 - 9^2) - y) = y(15 + x)
        (x - 9)^2 + y^2 = 36
        x > 0, y > 0

    and return the positive solution as exact SymPy expressions.
    """
    x, y = sp.symbols("x y", real=True)

    eq1 = sp.Eq((9 - x) * (sp.sqrt(15**2 - 9**2) - y), y * (15 + x))
    eq2 = sp.Eq((x - 9)**2 + y**2, 36)

    solutions = sp.solve((eq1, eq2), (x, y), dict=True)

    for sol in solutions:
        if sol[x].is_real and sol[y].is_real:
            if sp.N(sol[x]) > 0 and sp.N(sol[y]) > 0:
                return sp.simplify(sol[x]), sp.simplify(sol[y])

    raise ValueError("No positive solution found.")


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------
def main():
    # -------------------------------------------------------------------------
    # Circle data
    # -------------------------------------------------------------------------
    R_big = 15
    R_small = 6

    # The large circle is centered at O = (0, 0).
    # (O is not labeled in the original graphic, but it is useful in the code.)
    O = (0, 0)

    # The small circle center is A = (9, 0).
    A_exact = (sp.Integer(9), sp.Integer(0))

    # -------------------------------------------------------------------------
    # Coordinates from the graphic
    #
    # Large circle:   x^2 + y^2 = 15^2
    # Small circle:   (x - 9)^2 + y^2 = 6^2
    #
    # Labeled points:
    #
    #   C = (-15, 0)
    #   A = (9, 0)
    #   B = (15, 0)
    #   D = (9, sqrt(15^2 - 9^2)) = (9, 12)
    #
    # Let G = (x, y) be the upper-left corner of rectangle GFEH.
    # Then by symmetry about x = 9:
    #
    #   H = (x, -y)
    #   F = (18 - x, y)
    #   E = (18 - x, -y)
    # -------------------------------------------------------------------------
    xG, yG = solve_for_G()

    points_exact = {
        "O": (sp.Integer(0), sp.Integer(0)),                  # center of large circle
        "C": (-sp.Integer(15), sp.Integer(0)),
        "A": A_exact,                                         # center of small circle
        "B": (sp.Integer(15), sp.Integer(0)),
        "D": (sp.Integer(9), sp.Integer(12)),
        "G": (xG, yG),
        "H": (xG, -yG),
        "F": (sp.Integer(18) - xG, yG),
        "E": (sp.Integer(18) - xG, -yG),
    }

    # Convert all points to floats for plotting
    points = {name: to_float_pair(pt) for name, pt in points_exact.items()}

    # Rectangle GFEH
    rectangle_vertices = [
        points["G"],
        points["F"],
        points["E"],
        points["H"],
    ]

    area = polygon_area(rectangle_vertices)

    # Exact area, for the m+n calculation
    width_exact = sp.simplify(points_exact["F"][0] - points_exact["G"][0])
    height_exact = sp.simplify(points_exact["G"][1] - points_exact["H"][1])
    area_exact = sp.simplify(width_exact * height_exact)

    m, n = area_exact.as_numer_denom()

    # -------------------------------------------------------------------------
    # Print coordinates
    # -------------------------------------------------------------------------
    print("Exact coordinates:")
    for name in ["C", "A", "B", "D", "G", "H", "F", "E"]:
        print(f"{name} = {points_exact[name]}")

    print("\nDecimal coordinates:")
    for name in ["C", "A", "B", "D", "G", "H", "F", "E"]:
        px, py = points[name]
        print(f"{name} = ({px:.6f}, {py:.6f})")

    print(f"\nRectangle area (exact)   = {area_exact}")
    print(f"Rectangle area (decimal) = {float(area_exact):.6f}")
    print(f"m + n = {m} + {n} = {m + n}")

    # -------------------------------------------------------------------------
    # Plot
    # -------------------------------------------------------------------------
    fig, ax = plt.subplots(figsize=(10, 7))

    # Circles
    draw_circle(ax, points["O"], R_big, color="black", linewidth=1.8)
    draw_circle(ax, points["A"], R_small, color="black", linewidth=1.5)

    # Main horizontal line C---B
    draw_segment(ax, points["C"], points["B"], color="black", linewidth=1.6)

    # Triangle/segment structure from the figure
    draw_segment(ax, points["C"], points["G"], color="black", linewidth=1.6)
    draw_segment(ax, points["C"], points["H"], color="black", linewidth=1.6)
    draw_segment(ax, points["G"], points["D"], color="black", linewidth=1.6)
    draw_segment(ax, points["D"], points["F"], color="black", linewidth=1.6)

    # Rectangle GFEH
    draw_segment(ax, points["G"], points["F"], color="black", linewidth=1.6)
    draw_segment(ax, points["F"], points["E"], color="black", linewidth=1.6)
    draw_segment(ax, points["E"], points["H"], color="black", linewidth=1.6)
    draw_segment(ax, points["H"], points["G"], color="black", linewidth=1.6)

    # Vertical segment D to A
    draw_segment(ax, points["D"], points["A"], color="black", linewidth=1.6)

    # Fill the rectangle
    ax.fill(
        *closed_xy(rectangle_vertices),
        color="red",
        alpha=0.35,
        edgecolor="darkred",
        linewidth=2,
        zorder=1,
    )

    # Mark and label points
    label_offsets = {
        "C": (-1.6, 0.35),
        "A": (0.35, -0.9),
        "B": (0.35, 0.15),
        "D": (0.15, 0.8),
        "G": (-1.35, 0.7),
        "H": (-1.35, -1.5),
        "F": (0.35, 0.35),
        "E": (0.35, -0.7),
    }

    for name in ["C", "A", "B", "D", "G", "H", "F", "E"]:
        dx, dy = label_offsets[name]
        mark_point(ax, name, points[name], dx=dx, dy=dy)

    # Optional: label the circles
    ax.text(2.5, -12.3, r"$\omega_2$", fontsize=18)
    ax.text(7.5, -5.3, r"$\omega_1$", fontsize=18)

    # Title
    ax.set_title(
        f"Rectangle GFEH area = {float(area_exact):.1f} = {area_exact}    "
        f"(m+n = {m+n})",
        fontsize=14,
    )

    ax.set_aspect("equal")
    ax.axis("off")
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    main()
