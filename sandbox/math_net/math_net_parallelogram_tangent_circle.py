# =============================================================================
# Jim McCleery
# June 11, 2026
# Kailua-Kona, HI

##https://mathnet.mit.edu/explorer.html?p=usa_2022_9090d2

# =============================================================================

import matplotlib.pyplot as plt
import numpy as np


def plot_line(x1, y1, x2, y2, color="black", linestyle="-"):
    """Plots a straight line segment between two coordinates (x1, y1) and (x2, y2)."""
    plt.plot([x1, x2], [y1, y2], color=color, linestyle=linestyle)


def plot_circle(cx, cy, radius, color="blue"):
    """Plots a full circle given its center coordinates (cx, cy) and radius."""
    angles = np.linspace(0, 2 * np.pi, 200)
    x_values = cx + radius * np.cos(angles)
    y_values = cy + radius * np.sin(angles)
    plt.plot(x_values, y_values, color=color)


# --- 1. Exact Geometry Parameters ---
# Height of the parallelogram h = 6 * sqrt(3)
height = 6.0 * np.sqrt(3.0)
r = height / 2.0  # Radius is exactly half the height

side_AB = 10.5  # 6 + t (where t = 4.5)
side_BC = 24.5  # 20 + t

# Determine the slant projection of side AB onto the x-axis
# Using Pythagorean theorem on the slant right triangle: base = sqrt(hypotenuse^2 - height^2)
# base = sqrt(10.5^2 - (6*sqrt(3))^2) = sqrt(110.25 - 108) = sqrt(2.25) = 1.5
dx_AB = 1.5

# --- 2. Calculate Parallelogram Vertices ---
x0, y0 = 0.0, 0.0  # Vertex A at the origin
x1, y1 = dx_AB, height  # Vertex B
x2, y2 = x1 + side_BC, height  # Vertex C
x3, y3 = side_BC, 0.0  # Vertex D

# --- 3. Calculate Circle Center ---
# cy must equal the radius since it touches the bottom line y=0.
# cx is exactly 6 so that it remains perfectly tangent to the slanted line AB.
cx = 6.0
cy = r

# --- 4. Plotting the Elements ---
# Draw the four outer boundaries of the parallelogram
plot_line(x0, y0, x1, y1)  # Side AB
plot_line(x1, y1, x2, y2)  # Side BC
plot_line(x2, y2, x3, y3)  # Side CD
plot_line(x3, y3, x0, y0)  # Side DA

# Draw the AC diagonal line (Length is now exactly 28!)
plot_line(x0, y0, x2, y2, color="gray", linestyle="--")

# Draw the inscribed circle (Perfect triple tangency)
plot_circle(cx, cy, r, color="red")

# Label the vertices
plt.text(x0 - 1, y0 - 1, "A", fontsize=12, fontweight="bold")
plt.text(x1 - 1, y1 + 0.5, "B", fontsize=12, fontweight="bold")
plt.text(x2 + 0.5, y2 + 0.5, "C", fontsize=12, fontweight="bold")
plt.text(x3 + 0.5, y3 - 1, "D", fontsize=12, fontweight="bold")

# --- 5. Configure the Graph Layout ---
plt.axis("equal")
plt.title("Perfect Geometry Diagram: Area = 147√3")
plt.grid(True, linestyle=":", alpha=0.5)

# Display the final verified figure
plt.show()
