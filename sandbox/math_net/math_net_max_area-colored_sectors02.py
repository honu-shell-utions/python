# -----------------------------------------------------------------------------
# Jim McCleery
# June 4, 2026
# Kailua-Kona, HI
#
# https://mathnet.mit.edu/explorer.html?p=usa_bcb7be
# -----------------------------------------------------------------------------

# Import necessary functions from built-in Python modules
from random import uniform  # Used to generate random floating-point numbers
from math import sqrt       # Used to calculate the square root of a number

# -----------------------------------------------------------------------------
# Configuration and Initialization
# -----------------------------------------------------------------------------
r = 1            # Radius of the main circle
throws = 10**4   # Number of random points (darts) thrown to estimate the area
counter = 0
total_area = 0
# x0, y0 represent the origin/center of the circle at (0, 0)
x0, y0 = 0, 0

# -----------------------------------------------------------------------------
# Main Simulation Loop
# -----------------------------------------------------------------------------
# We run the outer simulation 1,000,000 times to test different random shapes/regions
for k in range(10**6):
    
    # Pick a random point (xa, ya) inside a bounding box from -1 to 1
    xa, ya = uniform(-1, 1), uniform(-1, 1)
    
    # Check if the point lies OUTSIDE the unit circle using the circle equation: x^2 + y^2 > r^2
    # If it is outside, skip the rest of this loop and try a new point.
    if xa**2 + ya**2 > 1:
        continue
    else:
        counter += 1

    # Calculate coordinates on the boundary of the circle based on our random point
    x1, y1 = sqrt(1 - ya**2), ya
    x2, y2 = -sqrt(1 - ya**2), ya
    x3, y3 = xa, sqrt(1 - xa**2)
    x4, y4 = xa, -sqrt(1 - xa**2)

    # -------------------------------------------------------------------------
    # Inner Monte Carlo Loop: Estimating the Geometric Area
    # -------------------------------------------------------------------------
    hits = 0  # Counter for how many random "throws" land inside our target region
    
    for _ in range(throws):
        # Generate a random test point (x, y) within the square bounding box [-1, 1]
        x, y = uniform(-1, 1), uniform(-1, 1)
        
        # If the test point is outside the circle, it doesn't count. Move to next throw.
        if x**2 + y**2 > 1:
            continue
            
        # Define the geometric boundaries of the specific sub-areas we are tracking.
        # These boolean checks test if the point (x, y) is bounded by lines relative to (xa, ya).
        in_area01 = (y > ya) and (y < ya + x - xa)
        in_area02 = (x < xa) and (y > ya - x + xa)
        in_area03 = (y < ya) and (y > ya + x - xa)
        in_area04 = (x > xa) and (y < ya - x + xa)
        
        # If the point lands in any of these 4 defined target regions, count it as a hit
        if in_area01 or in_area02 or in_area03 or in_area04:
            hits += 1
            
    # Calculate the estimated area of the region.
    # (hits / throws) gives the ratio. Multiplying by 4 scales it to the area of the bounding square (2x2).
    total_area += (hits / throws) * 4
    
    # Every 1,000 iterations, print out the current average area
    if k % 10**3 == 0:  
        print(total_area/counter)
