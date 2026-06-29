# -----------------------------------------------------------------------------
# Jim McCleery
# June 29, 2026
# Kailua-Kona, HI

# https://mathnet.mit.edu/explorer.html?p=usa_2021_319a8d
# -----------------------------------------------------------------------------

# Import specific tools we need from standard Python libraries
from math import cos, pi, sin, sqrt

# Import specific tools we need for plotting graphs
from matplotlib.pyplot import axis, plot, show, text, title


def plot_line(x1, y1, x2, y2):
    """Plot a straight line segment between two coordinate points (x1, y1) and

    (x2, y2).
    """
    plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------
# MAIN PROGRAM LOOP
# -----------------------------------------------------------------------------
"""
solving:  (18-d)^2 = (18-2d)^2 -3d(18-2d) + 9d^2 yields d = 0 or 5,
d cannot be 0 so we know d = 5
"""
d = 5
ab = 18
bc = 18 - d
ad = 18 - (2 * d)
cd = 18 - (3 * d)

# Define the (x, y) coordinates for 4 vertices of a shape
# pi/3 radians is equal to 60 degrees
x0, y0 = 0, 0
x1, y1 = ab, 0
x2, y2 = ad * cos(pi / 3) + cd, ad * sin(pi / 3)
x3, y3 = ad * cos(pi / 3), ad * sin(pi / 3)

# Draw the lines connecting the four points to close the shape
plot_line(x0, y0, x1, y1)  # Line from Point 0 to Point 1
plot_line(x2, y2, x1, y1)  # Line from Point 2 to Point 1
plot_line(x2, y2, x3, y3)  # Line from Point 2 to Point 3
plot_line(x0, y0, x3, y3)  # Line from Point 0 to Point 3

# Add labels to the coordinates (with slight offsets for readability)
text(x0 - 0.5, y0 - 0.5, f"A ({x0}, {y0})", fontsize=9, ha="right")
text(x1 + 0.5, y1 - 0.5, f"B ({x1}, {y1})", fontsize=9, ha="left")
text(
    x2 + 0.5,
    y2 + 0.5,
    f"C ({x2:.2f}, {y2:.2f})",
    fontsize=9,
    ha="left",
    va="bottom",
)
text(
    x3 - 0.5,
    y3 + 0.5,
    f"D ({x3:.2f}, {y3:.2f})",
    fontsize=9,
    ha="right",
    va="bottom",
)

# Format the plotting window scale and look
axis("equal")  # Keeps the aspect ratio 1:1 so shapes aren't stretched
axis("off")  # Hides the grid lines and axis numbers

# Set the text title at the top of the graph window using an f-string
title(f"side sum = {bc+cd+ad}")

# Display the final generated window to the screen
show()
