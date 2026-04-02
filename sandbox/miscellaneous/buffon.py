"""
jim.mccleery
April 2, 2026
Kailua-Kona, HI 

Buffon's Needle simulation

We draw equally spaced horizontal lines and repeatedly "drop" a unit-length
needle at random. By counting how often the needle crosses a line, we can
estimate pi.

In this version:
- line spacing D = 2
- needle length L = 1

For Buffon's Needle, when L <= D,

    P(crossing) = 2L / (pi D)

With L = 1 and D = 2, this becomes

    P(crossing) = 1 / pi

so

    pi ≈ number_of_drops / number_of_hits
"""

import matplotlib.pyplot as plt
from random import uniform
from math import cos, sin, pi


def draw_segment(x1, y1, x2, y2, **kwargs):
    """Draw a line segment between two points."""
    plt.plot([x1, x2], [y1, y2], **kwargs)


# ---------------------------------------------------------------------
# Parameters for the simulation and display
# ---------------------------------------------------------------------
dt = 0.05              # pause between drawing updates
drops = 10**3          # number of needles to drop
needle_length = 1.0    # L
line_spacing = 2.0     # D

# ---------------------------------------------------------------------
# Set up the figure
# ---------------------------------------------------------------------
fig, ax = plt.subplots()
ax.set_aspect("equal")
ax.set_xlim(0, 20)
ax.set_ylim(0, 22)

# Remove tick labels and tick marks for a cleaner picture
ax.set_xticklabels([])
ax.set_yticklabels([])
ax.tick_params(left=False, bottom=False)

# Draw the horizontal floor cracks at y = 2, 4, 6, ..., 20
for y in range(2, 21, 2):
    draw_segment(0, y, 20, y, color="black")
    plt.pause(dt)

# ---------------------------------------------------------------------
# Run the simulation
# ---------------------------------------------------------------------
hits = 0

for k in range(drops):
    # Choose one endpoint of the needle uniformly in the viewing window.
    # We stay away from the left/right edges so the full needle remains visible.
    x1 = uniform(1, 19)
    y1 = uniform(1, 21)

    # Choose a random orientation uniformly from 0 to 2*pi.
    theta = uniform(0, 2 * pi)

    # Compute the other endpoint using the needle length and angle.
    x2 = x1 + needle_length * cos(theta)
    y2 = y1 + needle_length * sin(theta)

    # Since the floor lines are horizontal and spaced 2 units apart,
    # a crossing occurs when the endpoints lie in different strips.
    #
    # Example:
    #   y in [0,2)   -> strip 0
    #   y in [2,4)   -> strip 1
    #   y in [4,6)   -> strip 2
    #
    # If the strip numbers differ, the segment must cross a line.
    strip1 = int(y1 // line_spacing)
    strip2 = int(y2 // line_spacing)
    crosses = (strip1 != strip2)

    if crosses:
        hits += 1

        # Draw only the needles that cross a line
        plt.plot(x1, y1, ".", color="black")
        plt.plot(x2, y2, ".", color="black")
        draw_segment(x1, y1, x2, y2, color="black")

        # Estimate pi from the experimental crossing probability.
        # After (k + 1) drops, estimated P = hits / (k + 1),
        # so estimated pi = 1 / P = (k + 1) / hits.
        pi_est = (k + 1) / hits
        ax.set_title(f"Estimated pi = {pi_est:.4f}")

        plt.pause(dt)

plt.show()

