"""
Jim McCleery
April 7, 2026
Kailua-Kona, HI

# Python solution to
# Video: https://youtu.be/aKiOyRzSy94?si=ghxTc4WVMdFk2CHj
#
# This program explores an alternative solution numerically.
# It uses Python both to investigate the geometry and to draw the figure.
#
# The goal is to find the side length s of the square for which a certain
# triangle in the figure has area 30.
#
# Rather than scanning millions of values of s, we use binary search.
# That is much faster and also illustrates a very useful numerical method.
#
# This version also labels the figure, shades the target triangle,
# and displays triangle areas in boxed text.
"""

import matplotlib.pyplot as plt


# ---------------------------------------------------------------------
# 1. A general-purpose geometry helper
# ---------------------------------------------------------------------
def polygon_area(vertices):
    """
    Compute the area of a polygon by the shoelace formula.
    """
    total = 0.0
    n = len(vertices)

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        total += x1 * y2 - y1 * x2

    return abs(total) / 2.0


def triangle_area(P, Q, R):
    """
    Return the area of triangle PQR.
    """
    return polygon_area([P, Q, R])


def midpoint(P, Q):
    """
    Return the midpoint of segment PQ.
    """
    return ((P[0] + Q[0]) / 2.0, (P[1] + Q[1]) / 2.0)


def centroid(P, Q, R):
    """
    Return the centroid of triangle PQR.
    """
    return ((P[0] + Q[0] + R[0]) / 3.0, (P[1] + Q[1] + R[1]) / 3.0)


# ---------------------------------------------------------------------
# 2. Build the geometry for a given square side length s
# ---------------------------------------------------------------------
def construct_figure(s):
    """
    Construct the key points in the diagram for a given square side length s.
    """
    if s <= 4:
        return None

    # Corners of the square
    A = (0.0, 0.0)
    B = (s, 0.0)
    D = (s, s)
    E = (0.0, s)

    # Point on the right side of the square
    C = (s, 4.0)

    # Point Q = (x5, y5)
    x5 = s - 20.0 / (s - 4.0)

    # Q lies on line CE
    slope_CE = (E[1] - C[1]) / (E[0] - C[0])
    y5 = C[1] + slope_CE * (x5 - C[0])
    Q = (x5, y5)

    # Same validity check as in the original code
    if y5 > x5:
        return None

    # Point R = where line QD meets the x-axis
    slope_QD = (Q[1] - D[1]) / (Q[0] - D[0])
    if slope_QD == 0:
        return None

    x6 = D[0] - D[1] / slope_QD
    R = (x6, 0.0)

    return {
        "A": A,
        "B": B,
        "C": C,
        "D": D,
        "E": E,
        "Q": Q,
        "R": R,
    }


# ---------------------------------------------------------------------
# 3. The quantity we want to control
# ---------------------------------------------------------------------
def target_triangle_area(s):
    """
    Return the area of triangle RQE for a given value of s.
    """
    figure = construct_figure(s)
    if figure is None:
        return None

    R = figure["R"]
    Q = figure["Q"]
    E = figure["E"]

    return triangle_area(R, Q, E)


# ---------------------------------------------------------------------
# 4. Binary search
# ---------------------------------------------------------------------
def find_s_for_area(target_area, tol=1e-12, max_iter=100):
    """
    Find the value of s for which the target triangle has area = target_area.
    """
    low = 10.0
    high = 20.0

    area_low = target_triangle_area(low)
    area_high = target_triangle_area(high)

    if area_low is None or area_high is None:
        raise ValueError("Initial interval produced invalid geometry.")

    if abs(area_low - target_area) < tol:
        return low
    if abs(area_high - target_area) < tol:
        return high

    if not (area_low <= target_area <= area_high):
        raise ValueError("The target area is not bracketed by the chosen interval.")

    for _ in range(max_iter):
        mid = (low + high) / 2.0
        area_mid = target_triangle_area(mid)

        if area_mid is None:
            raise ValueError("Invalid geometry encountered during binary search.")

        if abs(area_mid - target_area) < tol:
            return mid

        if area_mid < target_area:
            low = mid
        else:
            high = mid

        if high - low < tol:
            break

    return (low + high) / 2.0


# ---------------------------------------------------------------------
# 5. Plotting helpers
# ---------------------------------------------------------------------
def plot_segment(P, Q, **kwargs):
    """
    Plot the line segment joining two points P and Q.
    """
    plt.plot([P[0], Q[0]], [P[1], Q[1]], **kwargs)


def label_point(name, P, dx=0.15, dy=0.15):
    """
    Place a label near point P.
    """
    plt.text(P[0] + dx, P[1] + dy, name, fontsize=11, weight="bold")


def boxed_text(x, y, text, fontsize=10):
    """
    Draw text inside a small white box so it is easy to read on the figure.
    """
    plt.text(
        x,
        y,
        text,
        fontsize=fontsize,
        ha="center",
        va="center",
        bbox=dict(boxstyle="round,pad=0.25", facecolor="white", edgecolor="black")
    )


def label_triangle_area(name, P, Q, R, dx=0.0, dy=0.0):
    """
    Place a boxed triangle-area label near the centroid of triangle PQR.
    """
    cx, cy = centroid(P, Q, R)
    area = triangle_area(P, Q, R)
    boxed_text(cx + dx, cy + dy, f"{name}\nArea = {area:.3f}", fontsize=10)


def fill_triangle(P, Q, R, alpha=0.25):
    """
    Shade a triangle.
    """
    xs = [P[0], Q[0], R[0], P[0]]
    ys = [P[1], Q[1], R[1], P[1]]
    plt.fill(xs, ys, alpha=alpha)


def draw_figure(s):
    """
    Draw the geometric figure corresponding to the value of s,
    add labels for important points, and shade the target triangle.
    """
    figure = construct_figure(s)
    if figure is None:
        raise ValueError("Cannot draw the figure because the geometry is invalid.")

    A = figure["A"]
    B = figure["B"]
    C = figure["C"]
    D = figure["D"]
    E = figure["E"]
    Q = figure["Q"]
    R = figure["R"]

    plt.figure(figsize=(8, 8))

    # Shade triangles first so the lines appear on top of it.
    fill_triangle(R, Q, E, alpha=0.25)
    fill_triangle(Q, D, C, alpha=0.25)

    # Draw the segments
    plot_segment(E, R, color="black")
    plot_segment(D, R, color="black")
    plot_segment(A, B, color="black")
    plot_segment(B, D, color="black")
    plot_segment(E, D, color="black")
    plot_segment(A, E, color="black")
    plot_segment(E, C, color="black")

    # Emphasize the target triangle boundary
    plot_segment(R, Q, color="black", linewidth=2)
    plot_segment(Q, E, color="black", linewidth=2)
    plot_segment(E, R, color="black", linewidth=2)

    # Plot the points
    points = {"A": A, "B": B, "C": C, "D": D, "E": E, "Q": Q, "R": R}
    xs = [P[0] for P in points.values()]
    ys = [P[1] for P in points.values()]
    plt.scatter(xs, ys, s=30)

    # Label the points
    label_point("A", A, dx=0.18, dy=-0.45)
    label_point("B", B, dx=0.18, dy=-0.45)
    label_point("C", C, dx=0.18, dy=0.12)
    label_point("D", D, dx=0.18, dy=0.12)
    label_point("E", E, dx=-0.55, dy=0.12)
    label_point("Q", Q, dx=0.18, dy=0.12)
    label_point("R", R, dx=0.18, dy=-0.45)

    # Label some side lengths
    mid_AB = midpoint(A, B)
    mid_AE = midpoint(A, E)
    mid_BC = midpoint(B, C)

    boxed_text(mid_AB[0], mid_AB[1] - 0.65, f"s = {s:.3f}", fontsize=10)
    boxed_text(mid_AE[0] - 0.75, mid_AE[1], f"s = {s:.3f}", fontsize=10)
    boxed_text(mid_BC[0] + 0.50, mid_BC[1], "4", fontsize=10)

    # Triangle area labels
    label_triangle_area("△RQE", R, Q, E, dx=0.0, dy=0.55)
    label_triangle_area("△DEQ", D, E, Q, dx=0.25, dy=0.25)
    label_triangle_area("△DQC", D, Q, C, dx=0.65, dy=0.05)

    # Numerical summary on the figure
    boxed_text(
        s / 2.0,
        s + 1.1,
        f"Square area = {s**2:.3f}",
        fontsize=11
    )

    plt.axis("equal")
    plt.show()


# ---------------------------------------------------------------------
# 6. Main program
# ---------------------------------------------------------------------
def main():
    """
    Main driver for the program.
    """

    s = find_s_for_area(30.0)
    area = target_triangle_area(s)
    square_area = s**2

    print(f"Computed side length s      = {s:.12f}")
    print(f"Target triangle area        = {area:.12f}")
    print(f"Area of the square          = {square_area:.12f}")

    draw_figure(s)


if __name__ == "__main__":
    main()
