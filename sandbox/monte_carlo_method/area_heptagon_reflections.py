# =============================================================================
# Jim McCleery
# July 3, 2026
# Kailua-Kona, HI
#
# Geometry Problem Link:
# https://mathnet.mit.edu/explorer.html?p=usa_2025_8a437a
# =============================================================================

from math import pi, sqrt, acos, sin, cos
import matplotlib.pyplot as plt
from random import uniform


# --- HELPER GEOMETRY FUNCTIONS ---

def law_of_cosines(d1, d2, side):
    """
    Finds the angle opposite to 'side' in a triangle where the other 
    two known side lengths are d1 and d2.
    """
    try:
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except ValueError:
        return 0, False


def distance(x1, y1, x2, y2):
    """
    Calculates the straight-line (Euclidean) distance between two points.
    """
    return sqrt((x1 - x2)**2 + (y1 - y2)**2)


def polygon_area(vertices):
    """
    Calculates the total area of any polygon using the "Shoelace Formula".
    """
    n = len(vertices)
    area = 0
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2


# --- PLOTTING HELPER FUNCTIONS ---

def plot_line(p1, p2):
    """
    Draws a line segment connecting Point 1 (x, y) to Point 2 (x, y).
    """
    plt.plot([p1[0], p2[0]], [p1[1], p2[1]], color='black', linewidth=1.5)


def polygon_fill_coordinates(vertices):
    """
    Prepares a list of coordinates for matplotlib to shade a shape.
    """
    x_coords, y_coords = zip(*vertices)
    x_coords = list(x_coords) + [x_coords[0]]
    y_coords = list(y_coords) + [y_coords[0]]
    return x_coords, y_coords


# --- MAIN ENGINE / COORDINATE SEARCH LOOP ---

while True:
    BC_len = uniform(115, 117)
    
    alpha, _ = law_of_cosines(BC_len, 28, 91)
    if alpha > pi / 2:
        continue
        
    beta, _ = law_of_cosines(BC_len, 91, 28)
    
    # Establish the coordinate space mapped directly to the original graphic
    B = (0.0, 0.0)
    C = (BC_len, 0.0)
    A = (28 * cos(alpha), 28 * sin(alpha))
    F = (24 * cos(alpha), 24 * sin(alpha))
    D = (8 * cos(alpha), 8 * sin(alpha))
    G = (BC_len + 78 * cos(pi - beta), 78 * sin(pi - beta))
    E = (BC_len + 26 * cos(pi - beta), 26 * sin(pi - beta))
    
    # Derived coordinate points M and N
    d1 = distance(F[0], F[1], G[0], G[1])
    M = (F[0] + 2 * d1, F[1])
    
    d2 = distance(D[0], D[1], E[0], E[1])
    N = (D[0] - d2, D[1])

    # Target polygon for checking loop termination condition (DFGE)
    check_vertices = [D, E, G, F]
    area = polygon_area(check_vertices)
    
    if abs(area - 288) < 0.0001:
        break


# --- GRAPH RENDERING AND VISUALIZATION ---

# Define the final layout points for our primary red shaded polygon (D M A G N B C)
vertices = [D, M, A, G, N, B, C]
final_area = polygon_area(vertices)

# Fill the inside of the calculated polygon with transparent red
plt.fill(*polygon_fill_coordinates(vertices), color='red', alpha=0.3, edgecolor='red', linewidth=2)

# Draw lines based on the graphic layout
plot_line(B, C)
plot_line(A, C)
plot_line(B, A)
plot_line(F, M)
plot_line(D, M)
plot_line(E, N)
plot_line(G, N)
plot_line(B, N)
plot_line(E, N)

# Label the points
plt.text(*A,'A')
plt.text(*B,'B')
plt.text(*C,'C')
plt.text(*D,'D')
plt.text(*E,'E')
plt.text(*F,'F')
plt.text(*G,'G')
plt.text(*M,'M')
plt.text(*N,'N')

# Hide chart grid/axes
plt.axis('off')

# Display target calculation summary
plt.title(f'Red polygon has an area of {final_area:0.3f}.', fontsize=14)
plt.show()
