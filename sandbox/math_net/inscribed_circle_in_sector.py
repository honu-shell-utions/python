# =============================================================================
# Jim McCleery
# June 6, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_935c46
# =============================================================================

from math import cos, pi, sin, sqrt
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------
# Reusable Helper Functions
# -----------------------------------------------------------------------------
def plot_circle(x, y, radius, start=0, stop=2 * pi):
    """
    Plots a full circle or a specific arc segment using Matplotlib.
    """
    angle = np.linspace(start, stop, 1500)
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    plt.plot(x_arr, y_arr, color="black", linewidth=1.5)


def plot_line(x1, y1, x2, y2):
    """
    Plots a straight line segment between two coordinates.
    """
    plt.plot([x1, x2], [y1, y2], color="black", linewidth=1.5)


def add_label(text, x, y, offset_x=0.15, offset_y=0.15):
    """
    Adds text labels next to the geometric points for clarity.
    
    Parameters:
        text     : The label name (e.g., 'A', 'B', 'O')
        x, y     : Position of the geometric point
        offset_x : Horizontal shift so text doesn't sit directly on the point
        offset_y : Vertical shift so text doesn't sit directly on the point
    """
    plt.text(x + offset_x, y + offset_y, text, fontsize=12, fontstyle="italic", weight="bold")


# -----------------------------------------------------------------------------
# Main Script / Geometric Definitions
# -----------------------------------------------------------------------------

# Set base radius dimensions for the geometry
R = 6  # Large outer arc radius (Sector AC-B)
r = 2  # Small inner inscribed circle radius

# Define key coordinate points matching the graphic layout
# Point A acts as our local origin (0,0) on the graph
x0, y0 = 0, 0
x1, y1 = R, 0                               # Point B
x2, y2 = R * cos(pi / 3), R * sin(pi / 3)   # Point C
x3, y3 = R * cos(pi / 6), R * sin(pi / 6)   # Point T (Arc intersection)

# Inner circle center and line intersections
x4, y4 = r * sqrt(3), r                     # Center Point O
x5, y5 = r * sqrt(3), 0                     # Point D (Base intersection)
x6, y6 = r * sqrt(3) * cos(pi / 3), r * sqrt(3) * sin(pi / 3) # Point E

# -----------------------------------------------------------------------------
# Drawing the Visualization
# -----------------------------------------------------------------------------

# 1. Draw the outer circle arc from B to C
plot_circle(x0, y0, R, 0, pi / 3)

# 2. Draw the inner circle centered at O
plot_circle(x4, y4, r)

# 3. Draw the structural boundary and divider lines
plot_line(x0, y0, x1, y1)  # Line A to B
plot_line(x0, y0, x2, y2)  # Line A to C
plot_line(x0, y0, x3, y3)  # Line A through O to T

# 4. Draw perpendicular radius lines from center O
plot_line(x5, y5, x4, y4)  # Line D to O
plot_line(x6, y6, x4, y4)  # Line E to O

# -----------------------------------------------------------------------------
# Coordinate Labeling (Matching the Graphic)
# -----------------------------------------------------------------------------
add_label("A", x0, y0, offset_x=-0.3, offset_y=-0.1)
add_label("B", x1, y1, offset_x=0.1,  offset_y=-0.1)
add_label("C", x2, y2, offset_x=-0.1, offset_y=0.1)
add_label("D", x5, y5, offset_x=-0.1, offset_y=-0.4)
add_label("E", x6, y6, offset_x=-0.4, offset_y=0.1)
add_label("T", x3, y3, offset_x=0.15, offset_y=0.1)
add_label("O", x4, y4, offset_x=-0.1, offset_y=0.2)

# -----------------------------------------------------------------------------
# Plot Formatting and Display
# -----------------------------------------------------------------------------

# Clean up axes display to hide graph grid lines for a textbook look
plt.gca().set_aspect('equal')
plt.axis('off')
plt.title(f'Radius of the small circle is {r}.')
# Render the window with labeled drawing
plt.show()
