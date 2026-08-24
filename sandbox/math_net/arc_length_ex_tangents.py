"""
Jim McCleery
August 24, 2026
Kailua-Kona, HI

https://mathnet.mit.edu/explorer.html?p=usa_3bad72
"""

from math import pi, radians, sin, cos
import matplotlib.pyplot as plt
import numpy as np


# -----------------------------------------------------------------------------
# HELPER FUNCTIONS FOR PLOTTING
# -----------------------------------------------------------------------------

def plot_circle(x, y, radius, start=0, stop=2 * pi):
    """
    Draws a circle (or arc) centered at (x, y) with the given radius.
    """
    angles = np.linspace(start, stop, 1500)
    x_coords = radius * np.cos(angles) + x
    y_coords = radius * np.sin(angles) + y
    plt.plot(x_coords, y_coords, color='black', linewidth=1.5)


def plot_line(x1, y1, x2, y2, color='blue', linestyle='-'):
    """
    Draws a line segment between (x1, y1) and (x2, y2).
    """
    plt.plot([x1, x2], [y1, y2], color=color, linestyle=linestyle)


def label_point(x, y, label, offset=(0.08, 0.08)):
    """
    Plots a point marker and displays its text label with an offset.
    """
    plt.plot(x, y, 'ko', markersize=4)
    plt.text(x + offset[0], y + offset[1], label, fontsize=11, fontweight='bold')


# -----------------------------------------------------------------------------
# GEOMETRY & TRIGONOMETRY CALCULATIONS
# -----------------------------------------------------------------------------

# Distance from center O to external points Q and P along the 75° centerline ray:
# Right triangle hypotenuse = radius / cos(half-angle)
d1 = 1 / cos(radians(75))    # Distance OQ (half-angle at Q = 15°, central half-angle = 75°)
d2 = 1 / cos(radians(67.5))  # Distance OP (half-angle at P = 22.5°, central half-angle = 67.5°)

# Minimum central angle between closest tangency points P2 and Q2 on the same side
arc_length = (7.5 / 360) * (2 * pi)

# Coordinates for geometric points:
x0, y0 = 0, 0                                    # Center O (origin)
x1, y1 = 1, 0                                    # Q1: Tangency point on unit circle at 0°
x2, y2 = cos(radians(7.5)), sin(radians(7.5))    # P1: Tangency point on unit circle at 7.5°
x3, y3 = d1 * cos(radians(75)), d1 * sin(radians(75))  # External point Q (along 75° ray)
x4, y4 = d2 * cos(radians(75)), d2 * sin(radians(75))  # External point P (along 75° ray)
x5, y5 = cos(radians(142.5)), sin(radians(142.5))      # P2: Tangency point on unit circle at 142.5°
x6, y6 = cos(radians(150)), sin(radians(150))          # Q2: Tangency point on unit circle at 150°


# -----------------------------------------------------------------------------
# PLOTTING THE GEOMETRY
# -----------------------------------------------------------------------------

# Draw the unit circle centered at O
plot_circle(x0, y0, radius=1)

# Draw radial reference lines from O to the tangency points and external points
plot_line(x0, y0, x1, y1, color='gray', linestyle='--')
plot_line(x0, y0, x2, y2, color='gray', linestyle='--')
plot_line(x0, y0, x3, y3, color='black', linestyle='-')   # Ray OPQ through origin
plot_line(x0, y0, x5, y5, color='gray', linestyle='--')
plot_line(x0, y0, x6, y6, color='gray', linestyle='--')

# Draw tangent lines from Q to its tangency points (Q1, Q2)
plot_line(x3, y3, x1, y1, color='tab:blue')
plot_line(x3, y3, x6, y6, color='tab:blue')

# Draw tangent lines from P to its tangency points (P1, P2)
plot_line(x4, y4, x2, y2, color='tab:red')
plot_line(x4, y4, x5, y5, color='tab:red')

# Add coordinate point markers and geometric labels
label_point(x0, y0, r'$O$', offset=(-0.15, -0.15))
label_point(x1, y1, r'$Q_1$', offset=(0.08, -0.05))
label_point(x2, y2, r'$P_1$', offset=(0.08, 0.05))
label_point(x3, y3, r'$Q$', offset=(0.10, 0.05))
label_point(x4, y4, r'$P$', offset=(-0.25, 0.10))
label_point(x5, y5, r'$P_2$', offset=(-0.25, 0.05))
label_point(x6, y6, r'$Q_2$', offset=(-0.25, -0.15))

# Title and display settings
plt.title(f'The arc length from $P_2$ to $Q_2$ is {arc_length:0.6f}', fontsize=12)
plt.axis('equal')
plt.axis('off')

# Display the diagram
plt.show()
