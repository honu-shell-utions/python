# -----------------------------------------------------------------------------
# Jim McCleery
# July 2, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_2024_32690c
# -----------------------------------------------------------------------------

# Import only the necessary mathematical tools we need for our calculations
from math import sqrt, acos, degrees
from random import uniform


def distance(x1, y1, x2, y2):
    """
    Calculate the straight-line (Euclidean) distance between two points:
    (x1, y1) and (x2, y2).
    """
    # Uses the Pythagorean theorem: distance = sqrt((change in x)^2 + (change in y)^2)
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def law_of_cosines(d1, d2, side):
    """
    Find the angle (in radians) opposite to 'side' in a triangle 
    where the other two side lengths are d1 and d2.
    """
    try:
        # The algebraic formula for the Law of Cosines rearranged to solve for the angle:
        # cos(Angle) = (d1^2 + d2^2 - side^2) / (2 * d1 * d2)
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        
        # acos is the inverse of cosine, which gives us the angle in radians
        return acos(temp), True
    except ValueError:
        # If the side lengths cannot physically form a triangle, return 0 and False
        return 0, False


# -----------------------------------------------------------------------------
# Main Simulation Code
# -----------------------------------------------------------------------------

# Define the boundaries of a 1x1 unit square (though not explicitly used, 
# it sets the context for our points chosen between 0 and 1)
x0, y0 = 0, 0  # Bottom-left corner
x1, y1 = 1, 0  # Bottom-right corner
x2, y2 = 1, 1  # Top-right corner
x3, y3 = 0, 1  # Top-left corner

# Variables to keep track of our simulation statistics
total_degrees = 0.0
total_trials = 10**6  # Run the experiment 1,000,000 times

# Loop through our random trials
for k in range(1, total_trials + 1):
    # Pick 3 random points inside our 1x1 square
    # uniform(0, 1) picks a random decimal number between 0.0 and 1.0
    x4, y4 = uniform(0, 1), uniform(0, 1)  # Point A
    x5, y5 = uniform(0, 1), uniform(0, 1)  # Point B (the vertex of our angle)
    x6, y6 = uniform(0, 1), uniform(0, 1)  # Point C

    # Calculate the three side lengths of the triangle formed by these 3 points
    d1 = distance(x4, y4, x5, y5)  # Distance from A to B
    d2 = distance(x5, y5, x6, y6)  # Distance from B to C
    d3 = distance(x6, y6, x4, y4)  # Distance from C to A (opposite to angle B)

    # Calculate angle ABC (the angle at vertex B) using the Law of Cosines.
    # d1 and d3 are the sides touching the vertex, d2 is the side opposite the vertex.
    theta, success = law_of_cosines(d1, d3, d2)
    
    # Convert the angle from radians to degrees and add it to our running total
    total_degrees += degrees(theta)
    
current_average = total_degrees / total_trials
print(f"The expected value for angle ABC is {current_average:0.2f} degrees.")
