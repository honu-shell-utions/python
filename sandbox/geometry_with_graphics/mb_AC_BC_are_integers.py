# -----------------------------------------------------------------------------
# Jim McCleery
# 2026-06-05
# Kailua-Kona, HI
#
# Geometry visualizer based on: https://youtu.be/KdsNouDPH0U?si=gZsuWEqzH5OzqlhX
# -----------------------------------------------------------------------------

from math import atan, cos, pi, sin, sqrt
import matplotlib.pyplot as plt

# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------

def plot_line(x1, y1, x2, y2):
    """
    Plots a straight line segment between two coordinates (x1, y1) and (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2], color="blue", linewidth=1.5)
# -----------------------------------------------------------------------------
def find_b_c_d(side_a):
    """
    Searches for valid geometric dimensions based on the problem criteria.
    Iterates through possible values for side 'b' to compute corresponding
    values for hypotenuse 'c', segment 'd', and angle 'theta'.
    """
    solutions = []
    
    # Loop through a reasonable range of integer values for side b
    for b in range(1, 100):
        c = sqrt(side_a**2 + b**2)
        
        # Check if the hypotenuse is a whole number (integer) and greater than 8
        if c == int(c) and c > 8:
            # Calculate angles and distances using trigonometry rules
            theta = atan(side_a / b)
            alpha = pi - 2 * theta
            d = sqrt(32 / (1 - cos(alpha)))
            
            # Keep the solution if distance d is structurally valid (less than b)
            if d < b:
                solutions.append((b, c, d, theta))
                
    return solutions
# -----------------------------------------------------------------------------
# Main Execution Script
# -----------------------------------------------------------------------------

# Define side 'a' using the video's mathematical constant: 4 * sqrt(6)
side_a = 4 * sqrt(6)

# Find all valid geometric configurations matching our constraints
found_solutions = find_b_c_d(side_a)

# Loop through and render each valid geometric configuration found
for b, c, d, theta in found_solutions:
    # Set up the (x, y) coordinates for each geometric vertex
    x0, y0 = 0, 0                          # Outer Triangle Vertex 1 (Origin)
    x1, y1 = b, 0                          # Outer Triangle Vertex 2 (Bottom Right)
    x2, y2 = 0, side_a                     # Outer Triangle Vertex 3 (Top Left)
    
    # The segment points requested as Point A and Point B
    x3, y3 = b - d, 0                      # Point A (on the base line)
    x4, y4 = x1 + 8 * cos(pi - theta), 8 * sin(pi - theta)  # Point B (on the hypotenuse)
    
    # Create the plot figure window
    plt.figure(figsize=(8,6))
    
    # Draw the outer triangle boundaries
    plot_line(x0, y0, x1, y1)   # Base line
    plot_line(x2, y2, x1, y1)   # Hypotenuse line
    plot_line(x0, y0, x2, y2)   # Vertical height line
    
    # Draw the intersecting transversal line segment AB inside the triangle
    plot_line(x3, y3, x4, y4)
    
    # Add scatter dots on key vertices to highlight them clearly
    points_x = [x0, x1, x2, x3, x4]
    points_y = [y0, y1, y2, y3, y4]
    plt.scatter(points_x, points_y, color="red", zorder=5)
    
    # Add text labels right next to each coordinate point with a slight visual offset
    # Points A and B are highlighted in dark red per your specifications
    plt.text(x3, y3 + 0.3, f"A ({x3:.2f}, {y3:.2f})", fontsize=11, weight="bold", color="darkred")
    plt.text(x4 + 0.5, y4, f"B ({x4:.2f}, {y4:.2f})", fontsize=11, weight="bold", color="darkred")
    
    # Background layout labels
    plt.text(x0 - 1.5, y0 - 1.5, f"V1 (0, 0)", fontsize=10, weight="bold")
    plt.text(x1 + 1.0, y1 - 1.5, f"V2 ({b}, 0)", fontsize=10, weight="bold")
    plt.text(x2 - 1.5, y2 + 1.5, f"V3 (0, {side_a:.2f})", fontsize=10, weight="bold")
    
    # Configure graph styling layout
    plt.axis('equal')  # Keeps aspect ratio 1:1 so angles don't look stretched or distorted
    plt.title(f'Geometric Solution Configuration\nDistance from A to B = {d:0.4f}', fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.xlabel("X Coordinate Space")
    plt.ylabel("Y Coordinate Space")
    
    # Display the final rendered graph window to the user
    plt.show()
