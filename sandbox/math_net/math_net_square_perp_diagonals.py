"""
For the following Python code do the following: 
1) tidy up the code
2) remove unused functions 
3) add explanatory comments appropriate for beginning Python programmers
4) add this header/comment
Jim McCleery
Today's date
Kailua-Kona, HI

https://mathnet.mit.edu/explorer.html?p=usa_2021_839e71

"""
# -----------------------------------------------------------------------------
from math import pi, radians, sqrt, atan, sin, cos, tan, acos, asin, degrees, hypot, atan2
from matplotlib.pyplot import *
from random import uniform, choice
from itertools import permutations
import numpy as np


# -----------------------------------------------------------------------------
def circle_circle_intersections(x0, y0, r0, x1, y1, r1):
    """
    Return the intersection points of two circles.

    Returns:
        (x3, y3, x4, y4, True) if intersections exist
        (0, 0, 0, 0, False) otherwise
    """
    try:
        d = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
        a = (r0**2 - r1**2 + d**2) / (2 * d)
        h = sqrt(r0**2 - a**2)
        x2 = x0 + a * (x1 - x0) / d
        y2 = y0 + a * (y1 - y0) / d
        x3 = x2 + h * (y1 - y0) / d
        y3 = y2 - h * (x1 - x0) / d
        x4 = x2 - h * (y1 - y0) / d
        y4 = y2 + h * (x1 - x0) / d
        return x3, y3, x4, y4, True
    except:
        return 0, 0, 0, 0, False


# -----------------------------------------------------------------------------
def circle_sector_plus_triangles(chord1, chord2, radius):
    """
    Return the area formed by a circle sector together with two isosceles triangles.

    The inputs chord1 and chord2 are treated as side lengths subtending angles
    in the same circle of radius 'radius'. The result is:
        sector area + area of triangle(chord1, radius, radius)
                    + area of triangle(chord2, radius, radius)
    """
    alpha, _ = law_of_cosines(radius, radius, chord1)
    beta, _ = law_of_cosines(radius, radius, chord2)
    theta = 2 * pi - alpha - beta
    sector = theta / 2 * radius**2
    tri01, _ = heron_area(chord1, radius, radius)
    tri02, _ = heron_area(chord2, radius, radius)
    return sector + tri01 + tri02


# -----------------------------------------------------------------------------
def circle_through_points(x1, y1, x2, y2, x3, y3):
    """
    Return the unique circle through three points.

    Returns:
        (center_x, center_y, radius, True) if successful
        (0, 0, 0, False) if the circle cannot be determined
    """
    try:
        s1 = x1**2 + y1**2
        s2 = x2**2 + y2**2
        s3 = x3**2 + y3**2
        M11 = x1 * y2 + x2 * y3 + x3 * y1 - (x2 * y1 + x3 * y2 + x1 * y3)
        M12 = s1 * y2 + s2 * y3 + s3 * y1 - (s2 * y1 + s3 * y2 + s1 * y3)
        M13 = s1 * x2 + s2 * x3 + s3 * x1 - (s2 * x1 + s3 * x2 + s1 * x3)
        x0 = 0.5 * M12 / M11
        y0 = -0.5 * M13 / M11
        r0 = sqrt((x1 - x0) ** 2 + (y1 - y0) ** 2)
        return x0, y0, r0, True
    except:
        return 0, 0, 0, False


# -----------------------------------------------------------------------------
def define_circle_from_points(x1, y1, x2, y2, x3, y3):
    """
    Return the circle determined by three non-collinear points.

    Returns:
        (center_x, center_y, radius)

    Note:
        Unlike circle_through_points(), this version does not return a success flag.
    """
    temp = x2 * x2 + y2 * y2
    bc = (x1 * x1 + y1 * y1 - temp) / 2
    cd = (temp - x3 * x3 - y3 * y3) / 2
    det = (x1 - x2) * (y2 - y3) - (x2 - x3) * (y1 - y2)

    cx = (bc * (y2 - y3) - cd * (y1 - y2)) / det
    cy = ((x1 - x2) * cd - (x2 - x3) * bc) / det
    radius = sqrt((cx - x1) ** 2 + (cy - y1) ** 2)
    return cx, cy, radius


# -----------------------------------------------------------------------------
def distance(x1, y1, x2, y2):
    """
    Return the Euclidean distance between two points.
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# -----------------------------------------------------------------------------
def distance_from_point_to_circle(x, y, cx, cy, r):
    """
    Return the signed distance from a point to a circle.

    Positive if the point is outside the circle, negative if inside,
    and zero if on the circle.
    """
    dist_to_center = sqrt((x - cx) ** 2 + (y - cy) ** 2)
    return dist_to_center - r


# -----------------------------------------------------------------------------
def distance_point_to_circle(center_x, center_y, radius, point_x, point_y):
    """
    Return the absolute distance from a point to the circumference of a circle.
    """
    dist_to_center = sqrt((point_x - center_x) ** 2 + (point_y - center_y) ** 2)
    return abs(dist_to_center - radius)


# -----------------------------------------------------------------------------
def evaluate_f(x):
    """
    Evaluate the function:
        sqrt(sin(x)) / (sqrt(sin(x)) + sqrt(cos(x)))

    The caller is responsible for providing x values where sin(x) and cos(x)
    are nonnegative if real-valued output is desired.
    """
    top = sqrt(sin(x))
    bot = sqrt(sin(x)) + sqrt(cos(x))
    return top / bot


# -----------------------------------------------------------------------------
def fill_circle(x, y, r, c='skyblue', start=0, stop=2 * pi):
    """
    Draw and fill a circle or circular arc sector boundary using matplotlib.

    Args:
        x, y: center of the circle
        r: radius
        c: fill color
        start, stop: angular interval in radians
    """
    theta = np.linspace(start, stop, 300)
    x_vals = x + r * np.cos(theta)
    y_vals = y + r * np.sin(theta)
    fill(x_vals, y_vals, color=c, alpha=0.6)


# -----------------------------------------------------------------------------
def incircle_of_triangle(x1, y1, x2, y2, x3, y3):
    """
    Return the incenter and inradius of a triangle.

    Returns:
        (incenter_x, incenter_y, inradius)
    """
    a = distance(x2, y2, x3, y3)
    b = distance(x1, y1, x3, y3)
    c = distance(x1, y1, x2, y2)

    s = (a + b + c) / 2
    area = sqrt(s * (s - a) * (s - b) * (s - c))
    inradius = area / s

    incenter_x = (a * x1 + b * x2 + c * x3) / (a + b + c)
    incenter_y = (a * y1 + b * y2 + c * y3) / (a + b + c)

    return incenter_x, incenter_y, inradius


# -----------------------------------------------------------------------------
def intersection_of_lines(m1, b1, m2, b2):
    """
    Return the intersection point of two non-parallel lines in slope-intercept form.

    Each line is given by y = m*x + b.

    Returns:
        (x, y, True) if the lines intersect
        (0, 0, False) if the lines are parallel
    """
    if m1 == m2:
        return 0, 0, False
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y, True


# -----------------------------------------------------------------------------
def is_point_in_polygon(point, polygon):
    """
    Return True if a point lies inside a polygon, otherwise False.

    Uses the ray-casting algorithm.
    """
    x, y = point
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        x_intersect = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= x_intersect:
                            inside = not inside
        p1x, p1y = p2x, p2y

    return inside


# -----------------------------------------------------------------------------
def is_point_well_separated(x, y, centers, min_distance=2):
    """
    Return True if point (x, y) is at least min_distance away from every point in centers.
    """
    for (a, b) in centers:
        if distance(a, b, x, y) < min_distance:
            return False
    return True


# -----------------------------------------------------------------------------
def law_of_cosines(d1, d2, side):
    """
    Return the angle opposite 'side' in a triangle with side lengths d1, d2, side.

    Returns:
        (angle_in_radians, True) if successful
        (0, False) otherwise
    """
    try:
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except:
        return 0, False


# -----------------------------------------------------------------------------
def line_circle_intersection(x1, y1, r, m, b):
    """
    Return the intersection points of a circle and a line.

    Circle:
        center = (x1, y1), radius = r
    Line:
        y = m*x + b

    Returns:
        (x2, y2, x3, y3, True) if intersections exist
        (0, 0, 0, 0, False) otherwise
    """
    A = 1 + m**2
    B = -2 * x1 + 2 * m * b - 2 * m * y1
    C = x1**2 + b**2 - 2 * b * y1 + y1**2 - r**2
    x2, x3, OK = quadratic_equation(A, B, C)
    if OK:
        y2 = m * x2 + b
        y3 = m * x3 + b
        return x2, y2, x3, y3, OK
    else:
        return 0, 0, 0, 0, False


# -----------------------------------------------------------------------------
def line_intersection_from_points_v1(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Return the intersection of two lines, each defined by two points.

    This version computes slopes directly and then solves for the intersection.

    Returns:
        (x, y, True) if successful
        (0, 0, False) otherwise
    """
    try:
        m1 = (y2 - y1) / (x2 - x1)
        m2 = (y4 - y3) / (x4 - x3)
        x = (y1 - m1 * x1 - y3 + m2 * x3) / (m2 - m1)
        y = y1 + m1 * x - m1 * x1
        return x, y, True
    except:
        return 0, 0, False


# -----------------------------------------------------------------------------
def line_intersection_from_points_v2(x1, y1, x2, y2, x3, y3, x4, y4):
    """
    Return the intersection of two lines, each defined by two points.

    This version converts each line to slope-intercept form and then calls
    intersection_of_lines().

    Returns:
        (x, y, True) if successful
        (0, 0, False) otherwise
    """
    try:
        m1 = (y2 - y1) / (x2 - x1)
        b1 = y1 - m1 * x1
        m2 = (y4 - y3) / (x4 - x3)
        b2 = y3 - m2 * x3
        x, y, OK = intersection_of_lines(m1, b1, m2, b2)
        if not OK:
            return 0, 0, False
        return x, y, True
    except:
        return 0, 0, False


# -----------------------------------------------------------------------------
def perpendicular_chord_radius(a, b, c, d):
    """
    Return a radius computed from four perpendicular chord-related quantities.

    Formula used:
        radius = sqrt(a^2 + b^2 + c^2 + d^2) / 2

    Returns:
        (radius, True) if successful
        (0, False) otherwise
    """
    try:
        temp = a**2 + b**2 + c**2 + d**2
        return sqrt(temp) / 2, True
    except:
        return 0, False


# -----------------------------------------------------------------------------
def plot_circle(x, y, radius, start=0, stop=2*pi):
    """
    Plot part of a circle from angle 'start' to angle 'stop' in radians.
    """
    angle = np.linspace(start, stop, 1500)
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    plot(x_arr, y_arr)


# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Plot a line segment between two points using matplotlib.
    """
    plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
def point_in_polygon(x, y, polygon):
    """
    Return True if point (x, y) lies inside the polygon, otherwise False.

    This is the same algorithm as is_point_in_polygon(), but with x and y
    passed separately.
    """
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if y > min(p1y, p2y):
            if y <= max(p1y, p2y):
                if x <= max(p1x, p2x):
                    if p1y != p2y:
                        x_intersect = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                        if p1x == p2x or x <= x_intersect:
                            inside = not inside
        p1x, p1y = p2x, p2y

    return inside


# -----------------------------------------------------------------------------
def point_line_distance(x, y, a, b, c):
    """
    Return the distance from point (x, y) to the line a*x + b*y + c = 0.
    """
    return abs(a * x + b * y + c) / sqrt(a**2 + b**2)


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
def polygon_draw(points):
    """
    Draw a polygon from a list of ordered pairs.

    Example:
        draw_polygon([(0, 0), (4, 0), (3, 2), (1, 3)])
    """
    if len(points) < 3:
        raise ValueError("A polygon needs at least 3 points.")

    x = [p[0] for p in points]
    y = [p[1] for p in points]

    x.append(points[0][0])
    y.append(points[0][1])

    plot(x, y, marker="o")


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


# fill(*polygon_fill_coordinates(vertices), color='lightblue', edgecolor='blue', linewidth=2)


# -----------------------------------------------------------------------------
def quadratic_equation(A, B, C):
    """
    Solve the quadratic equation A*x^2 + B*x + C = 0.

    Returns:
        (x1, x2, True) with x1 <= x2 if real roots exist
        (0, 0, False) otherwise
    """
    try:
        disc = B**2 - 4 * A * C
        disc = sqrt(disc)
        x1 = (-B - disc) / (2 * A)
        x2 = (-B + disc) / (2 * A)
        if x1 > x2:
            x1, x2 = x2, x1
        return x1, x2, True
    except:
        return 0, 0, False


# -----------------------------------------------------------------------------
def rotate_polygon(points, angle_degrees, center=(0, 0)):
    """
    Rotate a polygon about a given center by angle_degrees.

    Args:
        points: list of (x, y) points
        angle_degrees: rotation angle in degrees
        center: point about which to rotate

    Returns:
        A new list of rotated points.
    """
    points = np.array(points, dtype=float)
    center = np.array(center, dtype=float)

    theta = np.radians(angle_degrees)
    rotation_matrix = np.array([
        [np.cos(theta), -np.sin(theta)],
        [np.sin(theta),  np.cos(theta)]
    ])

    return ((points - center) @ rotation_matrix.T + center).tolist()


# -----------------------------------------------------------------------------
def triangle_area_from_heron(a, b, c):
    """
    Return the area of a triangle with side lengths a, b, c using Heron's formula.

    Returns:
        (area, True) if successful
        (0, False) otherwise
    """
    try:
        s = 0.5 * (a + b + c)
        area = sqrt(s * (s - a) * (s - b) * (s - c))
        return area, True
    except:
        return 0, False

# -----------------------------------------------------------------------------
while True:
    theta = uniform(0,pi/4)
    side = 13*cos(theta)

    x0,y0 = 0,0
    x1,y1 = -side,0
    x2,y2 = -side,side
    x3,y3 = 0,side
    x4,y4 = 6*cos(pi-theta),6*sin(pi-theta)
    x5,y5 = 13*cos(pi-theta),13*sin(pi-theta)
    m = 1/tan(theta)
    x6,y6 = (m*x3 -y3)/m,0
    x7,y7,_ = line_intersection_from_points_v2(x0,y0,x5,y5,x3,y3,x6,y6)

    d = distance(x4,y4,x7,y7)
    if d < 0.000001:
        break
    
plot_line(x0,y0,x1,y1)
plot_line(x2,y2,x1,y1)
plot_line(x2,y2,x3,y3)
plot_line(x0,y0,x3,y3)
plot_line(x0,y0,x5,y5)
plot_line(x6,y6,x3,y3)

title(f'The area of the square is {side**2:0.3f}')
axis('equal')
axis('off')
show()











