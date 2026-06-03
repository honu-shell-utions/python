from random import uniform
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------------------------------------------------------
# Configuration
# -----------------------------------------------------------------------------
num_birds = 3
total_distance = 0
simulations = 10**2   # Smooth for animation; increase for absolute precision

# Setup the matplotlib figure
plt.figure(figsize=(10, 4))

# -----------------------------------------------------------------------------
# Simulation Loop
# -----------------------------------------------------------------------------
for k in range(1, simulations + 1):
    # Generate and sort random bird positions on a wire from 0 to 1
    birds = sorted([uniform(0, 1) for _ in range(num_birds)])
    
    # FIX: Calculate the actual distance between adjacent birds
    # Interval 1: birds[1] - birds[0]
    # Interval 2: birds[2] - birds[1]
    # Summed up, this is exactly the span from the first bird to the last bird: birds[2] - birds[0]
    frame_distance = birds[2] - birds[0]
    total_distance += frame_distance
    
    # Average distance over all simulation runs so far
    avg_dist = total_distance / k
    
    # Reset canvas for animation frame
    plt.cla()
    
    # Draw the wire
    plt.plot([0, 1], [0, 0], color='dimgray', linewidth=2, zorder=1)
    
    # Draw custom birds
    for x_pos in birds:
        # 1. Bird Body (Circle)
        body = plt.Circle((x_pos, 0.08), radius=0.04, color='skyblue', zorder=3)
        plt.gca().add_patch(body)
        
        # 2. Bird Beak (Triangle pointing right)
        beak_x = [x_pos + 0.035, x_pos + 0.06, x_pos + 0.035]
        beak_y = [0.09, 0.08, 0.07]
        plt.fill(beak_x, beak_y, color='orange', zorder=4)
        
        # 3. Bird Tail (Triangle pointing left-down)
        tail_x = [x_pos - 0.035, x_pos - 0.06, x_pos - 0.025]
        tail_y = [0.07, 0.05, 0.09]
        plt.fill(tail_x, tail_y, color='steelblue', zorder=2)
        
        # 4. Bird Eye (Small Dot)
        plt.plot(x_pos + 0.02, 0.09, 'ko', markersize=3, zorder=5)
        
        # 5. Bird Legs (Tiny lines connecting body to wire)
        plt.plot([x_pos - 0.01, x_pos - 0.01], [0.04, 0], color='black', linewidth=1.5, zorder=2)
        plt.plot([x_pos + 0.01, x_pos + 0.01], [0.04, 0], color='black', linewidth=1.5, zorder=2)

    # Window adjustments
    plt.xlim(-0.1, 1.1)
    plt.ylim(-0.1, 0.3)
    plt.gca().set_aspect('equal')
    plt.axis('off')  # Hides grid axes for a cleaner look
    
    # Display statistics
    plt.title(f'Simulation: {k} | Avg Painted Interval: {avg_dist:.3f}', fontsize=12, fontweight='bold')
    
    # Pause slightly to create animation effect
    plt.pause(0.2)

plt.show()
