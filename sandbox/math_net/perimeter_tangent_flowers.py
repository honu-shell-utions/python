# -----------------------------------------------------------------------------
# Jim McCleery
# August 11, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2024_3a2120
# -----------------------------------------------------------------------------

import matplotlib.pyplot as plt
import numpy as np
from math import pi, radians, sin, cos, sqrt

# -----------------------------------------------------------------------------
# HELPER FUNCTIONS
# -----------------------------------------------------------------------------

def plot_circle(x, y, radius, start=0, stop=2 * pi):
    """
    Plots a circle or circular arc centered at (x, y) with a given radius.
    
    Parameters:
        x, y (float): Center coordinates of the circle/arc.
        radius (float): Radius of the circle.
        start (float): Starting angle in radians (default: 0).
        stop (float): Ending angle in radians (default: 2*pi for full circle).
    """
    # Generate 1500 points smoothly along the arc angle
    angles = np.linspace(start, stop, 1500)
    
    # Convert polar coordinates to Cartesian coordinates (X, Y)
    x_coords = x + radius * np.cos(angles)
    y_coords = y + radius * np.sin(angles)
    
    # Plot the arc line
    plt.plot(x_coords, y_coords, color="black", linewidth=1.2)


# -----------------------------------------------------------------------------
# MAIN SCRIPT
# -----------------------------------------------------------------------------

# Calculate radii for the figure geometry
r1 = 4 * sin(radians(67.5)) / sqrt(2)  # Distance from origin to centers of outer arcs
r2 = sqrt(r1**2 - 1)                   # Radius of the central inner circle

plt.figure(figsize=(7, 7))

# 1. Draw the central inner circle
plot_circle(0, 0, r2)

# 2. Draw the 8 outer petal arcs
theta = pi / 2   # Start angle for the top petal center
bump = 0         # Angular offset for the arc sweep

while theta < 5 * pi / 2:
    # Petal center coordinates
    x = r1 * cos(theta)
    y = r1 * sin(theta)
    
    # Draw arc centered at (x, y) with radius 1
    plot_circle(x, y, 1, bump - pi / 8, bump + pi + pi / 8)
    
    # Advance by 45 degrees (pi/4) for the next petal
    theta += pi / 4
    bump += pi / 4

# 3. Add vertex dots and labels (A1 through A8)
# The 8 vertices on the inner circle are located at angles pi/8, 3*pi/8, ..., 15*pi/8
vertex_angles = [
    (pi / 8, "$A_1$"),       # Top right (~22.5°)
    (3 * pi / 8, "$A_2$"),   # Top right-center (~67.5°)
    (5 * pi / 8, "$A_3$"),   # Top left-center (~112.5°)
    (7 * pi / 8, "$A_4$"),   # Top left (~157.5°)
    (9 * pi / 8, "$A_5$"),   # Bottom left (~202.5°)
    (11 * pi / 8, "$A_6$"),  # Bottom left-center (~247.5°)
    (13 * pi / 8, "$A_7$"),  # Bottom right-center (~292.5°)
    (15 * pi / 8, "$A_8$"),  # Bottom right (~337.5°)
]

for angle, label in vertex_angles:
    # Calculate vertex position on the inner circle
    vx = r2 * cos(angle)
    vy = r2 * sin(angle)
    
    # Draw a black dot at the vertex
    plt.plot(vx, vy, "ko", markersize=5)
    
    # Position label text slightly inside the inner circle (0.83 scale factor)
    tx = vx * 0.83
    ty = vy * 0.83
    
    plt.text(tx, ty, label, fontsize=13, ha="center", va="center")

# Formatting plot appearance
plt.title("The perimeter of the flower is 10*pi.", fontsize=14, pad=15)
plt.axis("equal")  # Maintain 1:1 aspect ratio so circles remain round
plt.axis("off")    # Turn off axes frame and ticks

# Display figure
plt.show()
