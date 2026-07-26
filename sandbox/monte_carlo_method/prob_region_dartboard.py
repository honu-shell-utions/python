# -----------------------------------------------------------------------------
# Jim McCleery
# July 26, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_1999_234b16
# -----------------------------------------------------------------------------

from math import sqrt
from random import uniform
from matplotlib.pyplot import axis, plot, show, title


def distance(x1, y1, x2, y2):
    """
    Calculate the straight-line (Euclidean) distance between two points (x1, y1) and (x2, y2).
    
    Formula: sqrt((x1 - x2)^2 + (y1 - y2)^2)
    """
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


# Track the number of darts that satisfy the target condition
hits = 0

# Total number of random dart throws for the Monte Carlo simulation
throws = 10**6

# Define the 4 corner coordinates of the 2x2 square dartboard
x0, y0 = 0, 0  # Bottom-Left corner
x1, y1 = 2, 0  # Bottom-Right corner
x2, y2 = 2, 2  # Top-Right corner
x3, y3 = 0, 2  # Top-Left corner

# Draw the boundary lines of the 2x2 square dartboard
plot([x0, x1], [y0, y1], color="black")  # Bottom edge
plot([x1, x2], [y1, y2], color="black")  # Right edge
plot([x2, x3], [y2, y3], color="black")  # Top edge
plot([x3, x0], [y3, y0], color="black")  # Left edge

# Add labels for the corners and center of the square based on the graphic problem
plot(x0, y0, "ro")
plot(x1, y1, "ro")
plot(x2, y2, "ro")
plot(x3, y3, "ro")

# Coordinate annotations offset slightly for readability
title("Monte Carlo Simulation: Dartboard Problem")
axis("equal")
axis("off")

# Run the simulation by throwing darts randomly across the 2x2 square
for k in range(1, throws):
    # Generate random (x, y) coordinates within the square boundary [0, 2] x [0, 2]
    x = uniform(0, 2)
    y = uniform(0, 2)

    # Calculate distance from the dart point to each of the 4 corners
    d0 = distance(x, y, x0, y0)
    d1 = distance(x, y, x1, y1)
    d2 = distance(x, y, x2, y2)
    d3 = distance(x, y, x3, y3)

    # Condition 1: Must be within a distance 1 of AT LEAST ONE corner
    if d0 > 1 and d1 > 1 and d2 > 1 and d3 > 1:
        continue

    # Calculate distance from the dart point to the center point (1, 1)
    d_center = distance(x, y, 1, 1)

    # Condition 2: Must be closer to the center than to ANY corner
    if (
        d_center < d0
        and d_center < d1
        and d_center < d2
        and d_center < d3
    ):
        hits += 1
        # Plot valid dart hits
        plot(x, y, "o", color="blue", markersize=1)

# Display final estimated probability title after simulation finishes
title(f"Final Estimated Probability: {hits / throws:0.4f}")
show()
