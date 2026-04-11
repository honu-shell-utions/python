# Jim McCleery
# April 11, 2026
# Kailua-Kona, HI
#
# Python solution to
# Video: https://youtu.be/Fq-4VDJuMUE?si=tc2HzAgOPbDajePt
#
# This program explores an alternative strategy for solving
# this problem posted by Math Booster.

from math import pi, sqrt
from random import uniform
import numpy as np
import matplotlib.pyplot as plt


def plot_line(x1, y1, x2, y2):
    """Draw a line segment from (x1, y1) to (x2, y2)."""
    plt.plot([x1, x2], [y1, y2], "k")


def plot_circle(cx, cy, radius, start=0, stop=2 * pi):
    """Draw part of a circle centered at (cx, cy)."""
    t = np.linspace(start, stop, 400)
    x = cx + radius * np.cos(t)
    y = cy + radius * np.sin(t)
    plt.plot(x, y, "k")


def label_point(x, y, name, dx=0.15, dy=0.15):
    """Plot a point and label it."""
    plt.plot(x, y, "ko")
    plt.text(x + dx, y + dy, f"{name} ({x:.2f}, {y:.2f})", fontsize=10)


# ------------------------------------------------------------------
# Fixed points in the diagram
# ------------------------------------------------------------------
x0, y0 = 0, 0        # O
x1, y1 = 0, 5        # A
x2, y2 = 0, 10       # B
x3, y3 = -10, 0      # C

# ------------------------------------------------------------------
# Search for the radius r of the small quarter-circle.
#
# Idea:
# 1. Guess r.
# 2. Compute s from the right triangle relation:
#       s^2 = r^2 + 10r
# 3. This gives the center of the small circle at (-s, 0).
# 4. The top point of that small circle is (-s, r).
# 5. We want that top point to lie on the large circle x^2 + y^2 = 100.
# ------------------------------------------------------------------
counter = 0

while True:
    counter += 1

    # Random guess for the small radius
    r = uniform(0, 10)

    # From the geometry in the figure
    s = sqrt(r**2 + 10 * r)

    # The center must stay inside the large quarter-circle picture
    if s > 10:
        continue

    # Important points determined by r
    x4, y4 = -s, 0    # D = center of the small circle
    x5, y5 = -s, r    # E = top point of the small circle

    # Show every 1000th guess so we can watch the search
    if counter % 1000 == 0:
        plot_line(x0, y0, x2, y2)
        plot_line(x0, y0, x3, y3)
        plot_line(x4, y4, x5, y5)

        plot_circle(x1, y1, 5, pi / 2, 3 * pi / 2)   # semicircle
        plot_circle(x0, y0, 10, pi / 2, pi)          # large quarter-circle
        plot_circle(x4, y4, r, 0, pi / 2)            # small quarter-circle

        plt.axis("equal")
        plt.axis("off")
        plt.title("Guessing the radius of the small quarter circle...")
        plt.pause(0.15)
        plt.cla()
        
    # Stop when E is on the large circle x^2 + y^2 = 100
    if abs(x5**2 + y5**2 - 100) < 0.001:
        break

# ------------------------------------------------------------------
# Shade the desired region using random points.
#
# Keep points that are:
# - inside the large quarter-circle
# - outside the circle centered at A with radius 5
# - outside the small quarter-circle
# ------------------------------------------------------------------
for _ in range(10000):
    x = uniform(-10, 0)
    y = uniform(0, 10)

    # Outside the large quarter-circle
    if x**2 + y**2 > 100:
        continue

    # Inside the circle centered at A = (0, 5) with radius 5
    if x**2 + (y1 - y)**2 < 25:
        continue

    # Inside the small quarter-circle
    if (x4 - x)**2 + y**2 < r**2 and x > -s:
        continue

    plt.plot(x, y, ".", color="gray", markersize=2)

# ------------------------------------------------------------------
# Draw the final picture
# ------------------------------------------------------------------
plot_line(x0, y0, x2, y2)
plot_line(x0, y0, x3, y3)
plot_line(x4, y4, x5, y5)

plot_circle(x1, y1, 5, pi / 2, 3 * pi / 2)
plot_circle(x0, y0, 10, pi / 2, pi)
plot_circle(x4, y4, r, 0, pi / 2)

# Label the key coordinates
label_point(x0, y0, "O")
label_point(x1, y1, "A")
label_point(x2, y2, "B")
label_point(x3, y3, "C", dx=-1.5, dy=-0.6)
label_point(x4, y4, "D", dx= 0.2, dy=-0.6)
label_point(x5, y5, "E", dx=-2.5, dy=0.2)

# Area of the small quarter-circle
area = pi * r**2 / 4

plt.title(f"The shaded area = {area:.2f}, The small radius = {r:.2f}")
plt.axis("equal")
plt.axis("off")
plt.show()
