"""
# =============================================================================
# Jim McCleery
# October 5, 2026
# Kailua-Kona, HI
#
# Reference Problem:
# https://mathnet.mit.edu/explorer.html?p=btw_1991_fb0a1f
#
# Problem Statement:
# Two points A(x1, y1) and B(x2, y2) lie on y = 1/x with 0 < x1 < x2.
# |AB| = 2 * |OA|, and C is the midpoint of segment AB.
# Show that: angle(x-axis, OA) = 3 * angle(x-axis, OC).
# =============================================================================
"""

from math import atan, degrees, sqrt
from random import uniform
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------
# Helper Functions
# -----------------------------------------------------------------------------
def distance(point_a, point_b):
    """Calculate the Euclidean (straight-line) distance between two (x, y) points.

    Formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    """
    # Unpack the (x, y) coordinate tuples into separate variables
    x1, y1 = point_a
    x2, y2 = point_b

    # Use the Pythagorean theorem to find the distance
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def mid_point(point_a, point_b):
    """Find the midpoint between two (x, y) points by averaging their coordinates."""
    x1, y1 = point_a
    x2, y2 = point_b

    # Add coordinates together and divide by 2
    return ((x1 + x2) / 2, (y1 + y2) / 2)

def plot_point(point):
    """Plot a single point (x, y) as a small circle ('o') on the current graph."""
    x, y = point
    plt.plot(x, y, "o")

def plot_line(point_a, point_b):
    """Draw a line segment connecting point_a and point_b."""
    x1, y1 = point_a
    x2, y2 = point_b

    # plt.plot takes a list of x-values: [x1, x2] and a list of y-values: [y1, y2]
    plt.plot([x1, x2], [y1, y2])

# -----------------------------------------------------------------------------
# Simulation Setup (Monte Carlo / Random Search)
# -----------------------------------------------------------------------------

# Origin point (0, 0)
origin = (0, 0)

# Initialize tracking variables for the best match found:
# Start with a very large error value so the first test will beat it.
best_error = 10**6
best_A = (0, 0)
best_B = (0, 0)

# Run a Monte Carlo simulation (1,000,000 random trials)
# Using '_' as the loop variable signals that we do not need the loop counter itself.
for _ in range(10**6):
    # 1. Pick a random x-coordinate for point A between 0.1 and 10.0
    x1 = uniform(0.1, 10.0)
    y1 = 1 / x1
    A = (x1, y1)

    # Calculate distance from origin O(0,0) to point A
    dist_oa = distance(origin, A)

    # 2. Pick a random x-coordinate for B that is to the right of A (x2 >= x1)
    x2 = uniform(x1, 10.0)
    y2 = 1 / x2
    B = (x2, y2)

    # Calculate distance from point A to point B
    dist_ab = distance(A, B)

    # 3. Check condition: We want AB to equal 2 * OA, so the difference (error)
    # should be as close to 0 as possible.
    error = abs(dist_ab - 2 * dist_oa)

    # If this trial is closer than any previous trial, save these points
    if error < best_error:
        best_error = error
        best_A = A
        best_B = B


# -----------------------------------------------------------------------------
# Midpoint and Angle Calculations
# -----------------------------------------------------------------------------

# Find the midpoint C between best_A and best_B
C = mid_point(best_A, best_B)

# Calculate the angle of segment OA relative to the x-axis:
# atan(y / x) returns the angle in radians
angle_oa_rad = atan(best_A[1] / best_A[0])

# Calculate the angle of segment OC relative to the x-axis:
angle_oc_rad = atan(C[1] / C[0])


# -----------------------------------------------------------------------------
# Visualization
# -----------------------------------------------------------------------------

# Plot the smooth curve y = 1/x using 100 points between 0.1 and 10
x_vals = np.linspace(0.1, 10, 100)
y_vals = 1 / x_vals
plt.plot(x_vals, y_vals, label="y = 1/x")

# Draw horizontal and vertical axes passing through (0, 0)
plt.axhline(0, linewidth=1, color="gray")
plt.axvline(0, linewidth=1, color="gray")

# --- Plot and label Point C (Midpoint of AB) ---
plt.text(C[0] + 0.1, C[1] + 0.1, "C")
plot_point(C)
plot_line(origin, C)

# --- Plot and label Point A ---
plt.text(best_A[0] + 0.1, best_A[1] + 0.1, "A")
plot_point(best_A)
plot_line(origin, best_A)

# --- Plot and label Point B ---
plt.text(best_B[0] + 0.1, best_B[1] + 0.1, "B")
plot_point(best_B)
plot_line(best_A, best_B)  # Segment AB
plot_line(origin, best_B)  # Segment OB

# --- Plot and label the Origin (O) ---
plt.text(origin[0] - 0.2, origin[1] + 0.1, "O")
plot_point(origin)

# Set the title showing the angles converted from radians to degrees
# '0.1f' formats the float to 1 decimal place
plt.title(
    f"The angle between the x-axis and OA is {degrees(angle_oa_rad):0.1f}°, "
    f"3 times the angle between the x-axis and OC is {3*degrees(angle_oc_rad):0.1f}°."
)

# Keep the scale of x and y axes equal so geometric angles display correctly
plt.axis("equal")

# Turn off the default outer box ticks for a clean geometric diagram
plt.axis("off")

# Render the plot window
plt.show()
