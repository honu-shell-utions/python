# =============================================================================
# Jim McCleery
# June 23, 2026
# Kailua-Kona, HI
#
# Video Link: https://youtu.be/nbfNoMNEShI?si=Ca-Mt8XUQU73qhXp
# =============================================================================

# Import the square root function from Python's standard math library
from math import sqrt
# Import plotting functions, text styling, and random number generators
from matplotlib.pyplot import axis, title, show, plot, text
from random import uniform


def distance(x1, y1, x2, y2):
    """
    Calculate the straight-line (Euclidean) distance between two points.
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def plot_line(x1, y1, x2, y2, color='blue', linewidth=2):
    """
    Draw a single line segment between two coordinates with custom styling.
    """
    plot([x1, x2], [y1, y2], color=color, linewidth=linewidth)


# --- MAIN PROGRAM LOOP ---
while True:
    a = uniform(0, 1)
    b = sqrt(1 - a**2)
    side = b + sqrt(b**2 + 24)
    
    # Coordinates of the outer square vertices matching the diagram:
    # A (top-left), B (top-right), C (bottom-right), D (bottom-left)
    x3, y3 = 0, side       # Point A
    x2, y2 = side, side    # Point B
    x1, y1 = side, 0       # Point C
    x0, y0 = 0, 0          # Point D
    
    # Internal point E
    x4, y4 = b, side - a
    
    # Check the distance between B (x2, y2) and E (x4, y4) to see if it equals 5,
    # or check C (x1, y1) to E (x4, y4) to see if it equals 7.
    d = distance(x1, y1, x4, y4)
    if abs(d - 7) < 0.0001:
        break

# --- PLOTTING GEOMETRY ---
# Outer Square (Blue Frame)
plot_line(x3, y3, x2, y2, color='blue', linewidth=4)  # A to B
plot_line(x2, y2, x1, y1, color='blue', linewidth=4)  # B to C
plot_line(x1, y1, x0, y0, color='blue', linewidth=4)  # C to D
plot_line(x0, y0, x3, y3, color='blue', linewidth=4)  # D to A

# Inner Line Segments (Red Paths)
plot_line(x3, y3, x4, y4, color='red', linewidth=3)  # A to E (Length 1)
plot_line(x2, y2, x4, y4, color='red', linewidth=3)  # B to E (Length 5)
plot_line(x1, y1, x4, y4, color='red', linewidth=3)  # C to E (Length 7)

# Draw a black dot exactly at point E
plot(x4, y4, marker='o', color='black', markersize=8)

# --- ADDING TEXT LABELS ---
# Syntax: text(x, y, "string", fontsize, ha=horizontal_alignment, va=vertical_alignment)
# Offsets (like 'side * 0.03') keep labels cleanly separated from lines.

# Vertex Labels
text(x3 - side * 0.03, y3 + side * 0.02, 'A', fontsize=16, weight='bold', ha='right')
text(x2 + side * 0.03, y2 + side * 0.02, 'B', fontsize=16, weight='bold', ha='left')
text(x1 + side * 0.03, y1 - side * 0.02, 'C', fontsize=16, weight='bold', ha='left', va='top')
text(x0 - side * 0.03, y0 - side * 0.02, 'D', fontsize=16, weight='bold', ha='right', va='top')
text(x4, y4 + side * 0.04, 'E', fontsize=16, weight='bold', ha='center')

# Line Segment Length Labels (Placed close to the midpoint of each segment)
text(x4 - 0.4,y4 - 0.1, '1', fontsize=16, color='red', weight='bold')
text(x4 + 1.5,y4 + 0.4, '5', fontsize=16, color='red', weight='bold')
text(x4 + 2.4,y4 - 2.0, '7', fontsize=16, color='red', weight='bold')

# --- DISPLAY CONFIGURATION ---
axis('equal')
axis('off')
title(f'The area of the square is {side**2:0.3f}', fontsize=14)
show()
