"""
https://mathnet.mit.edu/explorer.html?view=problems&mode=country&country=United+States
"""

from math import cos, sin, radians, hypot, atan2
import matplotlib.pyplot as plt
import sympy as sp
from sympy.geometry import Point as SPoint, Segment, Polygon


# -----------------------------------------------------------------------------
def rotate_point(point, angle_degrees, center=(0, 0)):
    """
    Rotate one point about center by angle_degrees.
    """
    x, y = point
    cx, cy = center

    theta = radians(angle_degrees)
    dx = x - cx
    dy = y - cy

    return (
        cx + dx * cos(theta) - dy * sin(theta),
        cy + dx * sin(theta) + dy * cos(theta)
    )


# -----------------------------------------------------------------------------
def rotate_polygon(points, angle_degrees, center=(0, 0)):
    """
    Rotate a polygon about a given center by angle_degrees.
    """
    return [rotate_point(p, angle_degrees, center) for p in points]


# -----------------------------------------------------------------------------
def polygon_edges(points):
    """
    Return the edges of a polygon as pairs of points.
    """
    return [
        (points[i], points[(i + 1) % len(points)])
        for i in range(len(points))
    ]


# -----------------------------------------------------------------------------
def plot_polygon(points, **kwargs):
    """
    Plot a closed polygon.
    """
    xs = [p[0] for p in points] + [points[0][0]]
    ys = [p[1] for p in points] + [points[0][1]]
    plt.plot(xs, ys, **kwargs)


# -----------------------------------------------------------------------------
def line_segment_intersection(p1, p2, p3, p4, tolerance=1e-9):
    """
    Return the intersection point of two line segments, if it exists.

    Each segment is given by two endpoints:
        segment 1: p1 to p2
        segment 2: p3 to p4

    Returns:
        (x, y) if the segments intersect
        None otherwise
    """
    x1, y1 = p1
    x2, y2 = p2
    x3, y3 = p3
    x4, y4 = p4

    denominator = (x1 - x2) * (y3 - y4) - (y1 - y2) * (x3 - x4)

    if abs(denominator) < tolerance:
        return None

    px = (
        (x1 * y2 - y1 * x2) * (x3 - x4)
        - (x1 - x2) * (x3 * y4 - y3 * x4)
    ) / denominator

    py = (
        (x1 * y2 - y1 * x2) * (y3 - y4)
        - (y1 - y2) * (x3 * y4 - y3 * x4)
    ) / denominator

    if (
        min(x1, x2) - tolerance <= px <= max(x1, x2) + tolerance
        and min(y1, y2) - tolerance <= py <= max(y1, y2) + tolerance
        and min(x3, x4) - tolerance <= px <= max(x3, x4) + tolerance
        and min(y3, y4) - tolerance <= py <= max(y3, y4) + tolerance
    ):
        return px, py

    return None


# -----------------------------------------------------------------------------
def unique_points(points, tolerance=1e-7):
    """
    Remove duplicate or nearly duplicate points.
    """
    unique = []

    for x, y in points:
        already_found = False

        for a, b in unique:
            if hypot(x - a, y - b) < tolerance:
                already_found = True
                break

        if not already_found:
            unique.append((x, y))

    return unique


# -----------------------------------------------------------------------------
def nearest_intersections(polygons, center=(0, 0), count=12):
    """
    Find the count intersection points nearest the center.

    The input polygons should be a list of polygons, where each polygon
    is a list of vertices.
    """
    intersections = []

    for i in range(len(polygons)):
        edges1 = polygon_edges(polygons[i])

        for j in range(i + 1, len(polygons)):
            edges2 = polygon_edges(polygons[j])

            for edge1 in edges1:
                for edge2 in edges2:
                    point = line_segment_intersection(*edge1, *edge2)

                    if point is not None:
                        intersections.append(point)

    intersections = unique_points(intersections)

    cx, cy = center

    intersections.sort(
        key=lambda p: hypot(p[0] - cx, p[1] - cy)
    )

    return intersections[:count]


# -----------------------------------------------------------------------------
def polygon_area(vertices):
    """
    Return the area of a polygon using the shoelace formula.

    The polygon is given as an ordered list of (x, y) vertices.
    """
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2


# -----------------------------------------------------------------------------
def polygon_fill_coordinates(vertices):
    """
    Return x and y coordinate lists suitable for filling or shading a polygon.

    The first vertex is appended to the end so the polygon is closed.
    """
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords


# -----------------------------------------------------------------------------
def sort_points_by_angle(points, center=(0, 0), clockwise=False):
    """
    Sort points in circular order around center.

    clockwise=False gives counterclockwise order.
    clockwise=True gives clockwise order.
    """
    cx, cy = center

    return sorted(
        points,
        key=lambda p: atan2(p[1] - cy, p[0] - cx),
        reverse=clockwise
    )


# =============================================================================
# Exact SymPy versions for exact area
# =============================================================================

# -----------------------------------------------------------------------------
def rotate_point_exact(point, angle_degrees, center=(0, 0)):
    """
    Rotate one point about center by angle_degrees, exactly.
    """
    x, y = point
    cx, cy = center
    theta = sp.pi * angle_degrees / 180

    dx = x - cx
    dy = y - cy

    return SPoint(
        sp.simplify(cx + dx * sp.cos(theta) - dy * sp.sin(theta)),
        sp.simplify(cy + dx * sp.sin(theta) + dy * sp.cos(theta))
    )


# -----------------------------------------------------------------------------
def rotate_polygon_exact(points, angle_degrees, center=(0, 0)):
    """
    Rotate a polygon exactly.
    """
    return [rotate_point_exact(p, angle_degrees, center) for p in points]


# -----------------------------------------------------------------------------
def polygon_edges_exact(points):
    """
    Return exact edges as SymPy segments.
    """
    return [
        Segment(points[i], points[(i + 1) % len(points)])
        for i in range(len(points))
    ]


# -----------------------------------------------------------------------------
def nearest_intersections_exact(polygons, count=12):
    """
    Find the count exact intersection points nearest the origin.
    """
    intersections = []

    for i in range(len(polygons)):
        edges1 = polygon_edges_exact(polygons[i])

        for j in range(i + 1, len(polygons)):
            edges2 = polygon_edges_exact(polygons[j])

            for e1 in edges1:
                for e2 in edges2:
                    result = e1.intersection(e2)

                    for obj in result:
                        if isinstance(obj, SPoint) and obj not in intersections:
                            intersections.append(obj)

    intersections.sort(key=lambda p: sp.simplify(p.x**2 + p.y**2))
    return intersections[:count]


# -----------------------------------------------------------------------------
def sort_points_by_angle_exact(points, center=(0, 0), clockwise=False):
    """
    Sort exact points by angle around center.
    """
    cx, cy = center

    return sorted(
        points,
        key=lambda p: atan2(float(p.y - cy), float(p.x - cx)),
        reverse=clockwise
    )


# -----------------------------------------------------------------------------
def extract_abc(expr):
    """
    Given expr of the form a - b*sqrt(c), return a, b, c.
    """
    expr = sp.expand(sp.nsimplify(expr))

    const, terms = expr.as_coeff_add()
    a = int(const)

    surd_term = -sum(terms)          # make it positive: b*sqrt(c)
    b, radical = surd_term.as_coeff_Mul()
    b = int(b)

    # radical should be sqrt(c), represented as c**(1/2)
    c = int(radical.base)

    return a, b, c


# -----------------------------------------------------------------------------
# Main program
# -----------------------------------------------------------------------------

base_square = [(3, 3), (-3, 3), (-3, -3), (3, -3)]
angles = [0, 30, 60]

# ----- floating-point version for graphics -----
squares = [
    rotate_polygon(base_square, angle)
    for angle in angles
]

for square in squares:
    plot_polygon(square, color='black')

inner_points = sort_points_by_angle(
    nearest_intersections(squares, center=(0, 0), count=12)
)

for x, y in inner_points:
    plt.plot(x, y, "o", color='blue')

area_numeric = polygon_area(inner_points)

plt.fill(
    *polygon_fill_coordinates(inner_points),
    color='red',
    edgecolor='red',
    alpha=0.35,
    linewidth=2
)

# ----- exact version for the algebra -----
squares_exact = [
    rotate_polygon_exact(base_square, angle)
    for angle in angles
]

inner_points_exact = sort_points_by_angle_exact(
    nearest_intersections_exact(squares_exact, count=12)
)

area_exact = sp.simplify(Polygon(*inner_points_exact).area)
a, b, c = extract_abc(area_exact)

plt.title(f"Area = {area_exact}    a+b+c = {a+b+c}")
plt.axis("equal")
plt.show()
