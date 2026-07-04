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
from sympy import symbols, sin, pi, nsolve

def get_sols():
    alpha, beta, BC = symbols('alpha beta BC')

    eq1 = 288 - 624*sin(alpha)
    eq2 = 91*sin(pi - alpha - beta) - 28*sin(beta)
    eq3 = 91*sin(alpha) - BC*sin(beta)

    sol = nsolve(
        [eq1, eq2, eq3],
        [alpha, beta, BC],
        [0.5, 1.0, 100.0]      # initial guess
    )

    return sol
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

alpha, beta, BC_len = get_sols()
gamma = pi - alpha - beta

# Establish the coordinate space mapped directly to the original graphic
B = (0.0, 0.0)
C = (BC_len, 0.0)
A = (28 * cos(beta), 28 * sin(beta))
F = (BC_len + 78 * cos(pi-gamma), 78 * sin(pi-gamma))
D = (24 * cos(beta), 24 * sin(beta))
G = (BC_len + 26 * cos(pi - gamma), 26 * sin(pi - gamma))
E = (8 * cos(beta), 8 * sin(beta))

# Derived coordinate points M and N
M = (2*F[0] - D[0], 2*F[1] - D[1])
N = (2*E[0] - G[0], 2*E[1] - G[1])

# --- GRAPH RENDERING AND VISUALIZATION ---

# Define the final layout points for our primary red shaded polygon
vertices = [A, M, E, C, B, N, F]
final_area = polygon_area(vertices)

# Fill the inside of the calculated polygon with transparent red
plt.fill(*polygon_fill_coordinates(vertices), color='red', alpha=0.3, edgecolor='red', linewidth=2)

# Draw lines based on the graphic layout
plot_line(B, C)
plot_line(A, C)
plot_line(B, A)

plot_line(D, M)
plot_line(G, N)

plot_line(N, F)
plot_line(B, N)
plot_line(E, M)
plot_line(A, M)
plot_line(E, C)

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
print(beta)
