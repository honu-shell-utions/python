# -----------------------------------------------------------------------------
# Jim McCleery
# June 6, 2026
# Kailua-Kona, HI
# 
# https://mathnet.mit.edu/explorer.html?p=usa_ca9c60
# -----------------------------------------------------------------------------

from math import sqrt
import matplotlib.pyplot as plt
from random import uniform

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS USED IN THE SIMULATION
# -----------------------------------------------------------------------------

def intersection_of_lines(m1, b1, m2, b2):
    """
    Finds where two lines cross (intersect) using their slope-intercept forms.
    Each line is defined by the equation: y = m * x + b
    """
    if m1 == m2:
        return 0, 0, False
        
    x = (b2 - b1) / (m1 - m2)
    y = m1 * x + b1
    return x, y, True


def distance(x1, y1, x2, y2):
    """
    Calculates the straight-line distance between two points using the Pythagorean theorem.
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def plot_line(x1, y1, x2, y2):
    """
    Draws a straight line segment on the screen between two points.
    """
    plt.plot([x1, x2], [y1, y2], color='black', linewidth=1.5)


# -----------------------------------------------------------------------------
# MAIN SIMULATION SCRIPT
# -----------------------------------------------------------------------------

# Step 1: Define the dimensions of the main triangle
base = uniform(5,20)
height = uniform(5,20)

# Step 2: Define the three corners (vertices) of the triangle
x0, y0 = 0, 0              # Vertex B (Bottom-left)
x1, y1 = base, 0           # Vertex C (Bottom-right)
x2, y2 = base / 2, height  # Vertex A (Top peak)

# Step 3: Run the simulation loop 1,000 times
for _ in range(10**3):
    plt.cla()  # Clear the screen for the next animation frame
    
    # Pick a random point 'P' along the bottom edge BC
    x4, y4 = uniform(0, base), 0

    # Draw the main triangle edges
    plot_line(x0, y0, x1, y1)  # Side BC
    plot_line(x1, y1, x2, y2)  # Side CA
    plot_line(x2, y2, x0, y0)  # Side AB

    # --- LEFT SIDE CALCULATIONS (Side AB & Point X) ---
    m1 = 2 * height / base
    b1 = 0
    m2 = -1 / m1
    b2 = y4 - m2 * x4
    
    x5, y5, _ = intersection_of_lines(m1, b1, m2, b2)
    d1 = distance(x4, y4, x5, y5)
    
    # Draw line PX and its endpoints
    plt.plot(x4, y4, 'ro')        # Point P (drawn in red)
    plt.plot(x5, y5, 'bo')        # Point X (drawn in blue)
    plt.plot([x4, x5], [y4, y5], 'g--') # Green dashed line for PX
    
    # --- RIGHT SIDE CALCULATIONS (Side CA & Point Y) ---
    m1 = -2 * height / base
    b1 = y1 - m1 * x1
    m2 = -1 / m1
    b2 = y4 - m2 * x4
    
    x6, y6, _ = intersection_of_lines(m1, b1, m2, b2)
    d2 = distance(x4, y4, x6, y6)

    # Draw line PY and its endpoint
    plt.plot(x6, y6, 'bo')        # Point Y (drawn in blue)
    plt.plot([x4, x6], [y4, y6], 'g--') # Green dashed line for PY

    # --- ADD LABELS PER THE GRAPHIC ---
    plt.text(x2 - 0.2, y2 + 0.3, 'A', fontsize=12, fontweight='bold')
    plt.text(x0 - 0.5, y0 - 0.5, 'B', fontsize=12, fontweight='bold')
    plt.text(x1 + 0.2, y1 - 0.5, 'C', fontsize=12, fontweight='bold')
    plt.text(x4 - 0.1, y4 - 0.6, 'P', fontsize=12, fontweight='bold', color='red')
    plt.text(x5 - 0.6, y5, 'X', fontsize=12, fontweight='bold', color='blue')
    plt.text(x6 + 0.2, y6, 'Y', fontsize=12, fontweight='bold', color='blue')

    # --- DISPLAY THE RESULTS ---
    plt.title(f'Theorem Demo: PX + PY = {d1 + d2:0.6f}')
    
    # Set plot boundaries slightly wider than the triangle so labels don't get cut off
    plt.xlim(-1, base + 1)
    plt.ylim(-1, height + 1)
    
    # Fix: Set aspect ratio to 'equal' using 'adjustable=box' to avoid the terminal warning loop
    plt.gca().set_aspect('equal', adjustable='box')
    
    plt.pause(0.5)

plt.show()
