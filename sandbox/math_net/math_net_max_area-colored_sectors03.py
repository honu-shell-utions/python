import numpy as np

def simulate_shaded_area(num_darts=10**7):
    # 1. Choose a random interior point inside the unit circle
    # Using rejection sampling to ensure uniform distribution inside the circle
    while True:
        px, py = np.random.uniform(-1, 1, 2)
        if px**2 + py**2 < 1:
            break
            
    # 2. Generate random "darts" uniformly distributed inside the unit circle
    # We generate a bit extra to account for corners outside the circle, then filter
    raw_darts = np.random.uniform(-1, 1, (int(num_darts * 1.3), 2))
    inside_circle = raw_darts[np.sum(raw_darts**2, axis=1) <= 1]
    darts = inside_circle[:num_darts] # Keep exactly num_darts
    
    # 3. Calculate the angle of each dart relative to our random interior point
    dx = darts[:, 0] - px
    dy = darts[:, 1] - py
    angles = np.arctan2(dy, dx) # Returns values from -pi to pi
    
    # Map angles to a [0, 2*pi) range
    angles = np.mod(angles, 2 * np.pi)
    
    # 4. Divide into 8 sectors (each sector is pi/4 radians wide)
    # sector_indices will be 0, 1, 2, 3, 4, 5, 6, 7
    sector_indices = np.floor(angles / (np.pi / 4)).astype(int)
    
    # 5. Shaded areas are alternating sectors (e.g., sectors 1, 3, 5, 7)
    # Check if the sector index is odd
    is_shaded = (sector_indices % 2 == 1)
    
    # 6. Calculate area: (fraction of darts in shaded regions) * (total circle area)
    total_circle_area = np.pi
    shaded_area_est = (np.sum(is_shaded) / num_darts) * total_circle_area
    
    print(f"Empirical Shaded Area (Monte Carlo): {shaded_area_est:.6f}")

# Run the simulation
simulate_shaded_area()
