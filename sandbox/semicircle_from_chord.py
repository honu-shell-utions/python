# Python solution to Andy's math problem
# https://youtu.be/vRjydDx-t5E?si=6aejba5jqfwdO3vA
#
# This is a fun alternative solution using Python.
# Exploring problems like this with code is a good way
# to learn Python and also gain insight into the math.
#
# Jim McCleery
# March 27, 2026
# Kona, HI
# -----------------------------------------------------------------------------

from math import atan, cos, pi, sin, sqrt
from matplotlib.pyplot import *
import numpy as np
from random import uniform

# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    plot([x1, x2], [y1, y2])

# -----------------------------------------------------------------------------
def plot_partial_circle(x, y, radius, start, stop):
    angle = np.linspace(start, stop, 1500)

    # np.cos and np.sin operate elementwise on arrays.
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    plot(x_arr, y_arr)

# -----------------------------------------------------------------------------
# Set this to any positive integer.
loops = 20

for k in range(loops):
    # Randomly choose a value for a with a < b.
    # Keeping a > 3 is mainly for visual appearance.
    a = uniform(3, 10 / sqrt(2))

    # Compute b from a^2 + b^2 = 100.
    b = sqrt(100 - a**2)

    # Label the key points and segment lengths.
    text(0, -0.5, '(0,0)')
    text(b, a + 0.3, '(b,a)')
    text(b / 2, a / 2 + 0.5, '10')
    text(b + 10, a + 0.3, '(b+10,a)')
    text(b + 5, a + 0.5, '10')

    # Compute the perpendicular bisector of the segment
    # from (0,0) to (b+10,a). This line passes through
    # the center of the semicircle.
    m = a / (b + 10)
    m = -1 / m  # slope of the perpendicular bisector
    r = (m * b - a) / m

    plot(r, 0, 'o')
    text(r, -0.5, '(' + str(round(r, 3)) + ',0)')

    # Draw the semicircle and the relevant line segments.
    plot_partial_circle(r, 0, r, 0, pi)
    plot_line(0, 0, 2 * r, 0)
    plot_line(0, 0, b + 10, a)
    plot_line(b, a, r, 0)
    plot_line(0, 0, b, a)
    plot_line(b, a, b + 10, a)

    title('Radius = ' + str(round(r, 3)) +
          ', Area of semicircle = ' + str(round(pi * r**2 / 2, 2)))
    axis('equal')
    pause(2)

    if k < loops - 1:
        cla()

title('Radius = ' + str(round(r, 3)) +
      ', Area of semicircle = ' + str(round(pi * r**2 / 2, 2)) +
      ' (Finished)')
show()
