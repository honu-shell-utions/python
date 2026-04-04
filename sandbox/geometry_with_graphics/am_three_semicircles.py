# Python solution to Andy's math problem
# https://youtu.be/teFMm_QWuK4?si=2Q5XWW53eTgT4eQ3
#
# A simple Python sketch for visualizing the geometry.
#
# Jim McCleery
# March 28, 2026
# Kona, HI
# -----------------------------------------------------------------------
from math import sqrt, pi, sin, cos, acos
import numpy as np
from matplotlib.pyplot import plot, axis, show, title
# -----------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    plot([x1, x2], [y1, y2])

# -----------------------------------------------------------------------
def plot_partial_circle(x, y, radius, start, stop):
    angles = np.linspace(start, stop, 1500)
    x_vals = radius * np.cos(angles) + x
    y_vals = radius * np.sin(angles) + y
    plot(x_vals, y_vals)
# -----------------------------------------------------------------------
def law_of_cosines(d1, d2, side):
    value = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
    return acos(value)
# -----------------------------------------------------------------------
def lens_area(r, d):
    alpha = law_of_cosines(r, d, r)
    return 2 * (alpha * r**2 - r**2 * sin(alpha) * cos(alpha))

# -----------------------------------------------------------------------
r = 1
R = 1.5

x0, y0 = 0, 0
d = sqrt((r + R)**2 - R**2)

x1, y1 = x0 + d, R
x2, y2 = x0 - r, 0
x3, y3 = r, 0
x4, y4 = x1 - R, R
x5, y5 = x1 + R, R

diameter = 2 * r + 2 * R
x6, y6 = x2 + diameter / 2, 0
x3, y3 = x2 + diameter, 0

plot_partial_circle(x0, y0, r, 0, pi)
plot_partial_circle(x1, y1, R, pi, 2 * pi)
plot_partial_circle(x6, y6, diameter / 2, 0, pi)

plot_line(x3, y3, x2, y2)
plot_line(x4, y4, x5, y5)

title('Diameter of largest semicircle: '+str(diameter))
axis("equal")
show()
# -----------------------------------------------------------------------
