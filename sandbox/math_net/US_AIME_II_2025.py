"""
Jim McCleery
April 21, 2026
Kailua-Kona, HI

Six points A, B, C, D, E, and F lie in a straight line in that order.
Suppose that G is a point not on the line and that
AC = 26, BD = 22, CE = 31, DF = 33, AF = 73, CG = 40, and DG = 30.
Find the area of triangle BGE.
"""

from math import sqrt
import matplotlib.pyplot as plt


def circle_circle_intersections(x0, y0, r0, x1, y1, r1):
    """
    Return the intersection points of two circles.

    Parameters
    ----------
    (x0, y0), r0 : center and radius of the first circle
    (x1, y1), r1 : center and radius of the second circle

    Returns
    -------
    ((x3, y3), (x4, y4))
        The two intersection points.

    Raises
    ------
    ValueError
        If the circles do not intersect.
    """
    d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)

    if d > r0 + r1 or d < abs(r0 - r1) or d == 0:
        raise ValueError("The circles do not have two distinct intersection points.")

    a = (r0**2 - r1**2 + d**2) / (2 * d)
    h = sqrt(r0**2 - a**2)

    x2 = x0 + a * (x1 - x0) / d
    y2 = y0 + a * (y1 - y0) / d

    x3 = x2 + h * (y1 - y0) / d
    y3 = y2 - h * (x1 - x0) / d

    x4 = x2 - h * (y1 - y0) / d
    y4 = y2 + h * (x1 - x0) / d

    return (x3, y3), (x4, y4)


def triangle_area(p1, p2, p3):
    """
    Return the area of a triangle given three points.

    Uses the coordinate-area formula.
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3

    return abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2


def draw_labeled_point(ax, point, label, dx=0.0, dy=0.0):
    """
    Plot a point and place its label nearby.
    """
    x, y = point
    ax.plot(x, y, "o", color="black")
    ax.text(x + dx, y + dy, f"{label}{point}", fontsize=10)


def main():
    # Since the six points lie on a line in order, place them on the x-axis.
    # Let A = (0, 0). Then the given segment lengths determine all coordinates.
    A = (0, 0)
    C = (26, 0)
    F = (73, 0)

    # From AC = 26 and AF = 73:
    # B and E are determined by BD = 22, CE = 31, and DF = 33.
    B = (18, 0)   # because D = 40, so B = 40 - 22 = 18
    D = (40, 0)   # because F = 73 and DF = 33, so D = 73 - 33 = 40
    E = (57, 0)   # because C = 26 and CE = 31, so E = 26 + 31 = 57

    points = {"A": A, "B": B, "C": C, "D": D, "E": E, "F": F}

    # Point G is the intersection of:
    #   circle centered at C with radius CG = 40
    #   circle centered at D with radius DG = 30
    g1, g2 = circle_circle_intersections(C[0], C[1], 40, D[0], D[1], 30)

    # Choose the point above the x-axis.
    G = g1 if g1[1] > 0 else g2

    # Compute the area of triangle BGE.
    area = triangle_area(B, G, E)

    # ---- Plotting ----
    fig, ax = plt.subplots(figsize=(10, 5))

    # Draw the baseline containing A, B, C, D, E, F.
    ax.plot([A[0], F[0]], [0, 0], color="black", linewidth=1.5)

    # Draw triangle BGE.
    ax.plot([B[0], G[0]], [B[1], G[1]], color="blue", linewidth=2)
    ax.plot([E[0], G[0]], [E[1], G[1]], color="blue", linewidth=2)
    ax.fill([B[0], E[0], G[0]], [B[1], E[1], G[1]], color="red", alpha=0.35)

    # Label all points with their coordinates.
    for label, point in points.items():
        draw_labeled_point(ax, point, label, dx=-1.8, dy=-2.5)

    draw_labeled_point(ax, G, "G", dx=1.0, dy=1.0)

    # Cosmetic settings.
    ax.set_aspect("equal")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title(f"Area of triangle BGE = {area:.0f}")
    ax.grid(True, alpha=0.3)

    plt.show()

    print(f"G = ({G[0]:.0f}, {G[1]:.0f})")
    print(f"Area of triangle BGE = {area:.0f}")


if __name__ == "__main__":
    main()
