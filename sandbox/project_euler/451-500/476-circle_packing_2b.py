from math import pi, radians, sqrt, atan, sin, cos, tan, acos, asin, degrees, hypot, atan2
from matplotlib.pyplot import *
from random import uniform, choice
from itertools import permutations
import numpy as np


"""
https://projecteuler.net/problem=476

Let R(a,b,c) be the maximum area covered by three non-overlapping circles
inside a triangle with edge lengths a, b and c.

Let S(n) be the average value of R(a,b,c) over all integer triplets (a,b,c)
such that 1 <= a <= b <= c < a+b <= n.

You are given S(2) = R(1,1,1) = 0.31998, S(5) = 1.25899.

Find S(1803) rounded to 5 decimal places behind the decimal point.
"""
# -----------------------------------------------------------------------------
def law_of_cosines(d1, d2, side):
    """
    Return the angle opposite 'side' in a triangle with side lengths d1, d2, side.
    Returns:
        (angle_in_radians, True) if successful
        (0, False) otherwise
    """
    try:
        temp = (d1**2 + d2**2 - side**2) / (2 * d1 * d2)
        return acos(temp), True
    except:
        return 0, False
# -----------------------------------------------------------------------------
def packed_circles_data(a, b, c):
    """
    Return optimal radii and area for three packed circles.
    """
    a, b, c = sorted((a, b, c))

    r0 = inradius(a, b, c)
    sA, sB, _ = half_angle_sines(a, b, c)

    kA = corner_scale(sA)
    kB = corner_scale(sB)

    # Correct decision rule
    if sB <= (2 * sA) / (1 + sA * sA):
        radii = [r0, kA * r0, kB * r0]
        mode = "A+B"
    else:
        radii = [r0, kA * r0, (kA * kA) * r0]
        mode = "A+A"

    area = pi * sum(r * r for r in radii)
    return {
        "radii": radii,
        "mode": mode,
        "area": area,
        "sA": sA,
        "sB": sB,
    }
# -----------------------------------------------------------------------------
def semiperimeter(a, b, c):
    return 0.5 * (a + b + c)
# -----------------------------------------------------------------------------
def half_angle_sines(a, b, c):
    """
    For sorted sides a <= b <= c, let A,B,C be the opposite angles.
    Return sin(A/2), sin(B/2), sin(C/2).
    """
    s = semiperimeter(a, b, c)
    sA = sqrt((s - b) * (s - c) / (b * c))
    sB = sqrt((s - a) * (s - c) / (a * c))
    sC = sqrt((s - a) * (s - b) / (a * b))
    return sA, sB, sC
# -----------------------------------------------------------------------------
def plot_circle(x, y, radius, start=0, stop=2*pi):
    """
    Plot part of a circle from angle 'start' to angle 'stop' in radians.
    """
    angle = np.linspace(start, stop, 1500)
    x_arr = radius * np.cos(angle) + x
    y_arr = radius * np.sin(angle) + y
    plot(x_arr, y_arr)
# -----------------------------------------------------------------------------
def plot_line(x1, y1, x2, y2):
    """
    Plot a line segment between two points using matplotlib.
    """
    plot([x1, x2], [y1, y2])
# -----------------------------------------------------------------------------
def corner_scale(sh):
    """
    If a circle of radius r is tangent to both sides of an angle,
    then the next smaller tangent circle in the same corner has
    radius k*r where k = (1 - sin(theta/2)) / (1 + sin(theta/2)).
    """
    return (1 - sh) / (1 + sh)
# -----------------------------------------------------------------------------
def R(a, b, c):
    return packed_circles_data(a, b, c)["area"]
# -----------------------------------------------------------------------------
def inradius(a, b, c):
    s = semiperimeter(a, b, c)
    return sqrt(((s - a) * (s - b) * (s - c)) / s)
# -----------------------------------------------------------------------------
def valid_triples(n):
    for a in range(1, n // 2 + 1):
        for b in range(a, n - a + 1):
            for c in range(b, a + b):
                yield a, b, c
# -----------------------------------------------------------------------------
for n in [2,5]:
    total = 0.0
    count = 0
    for a, b, c in valid_triples(n):
        cla()
        r,ra,rb = packed_circles_data(a,b,c)['radii']
        x0,y0 = 0,0
        A,_ = law_of_cosines(b,c,a)
        x1,y1 = b*cos(A),b*sin(A)
        x2,y2 = c,0
        x3,y3 = ra/tan(A/2),ra
        x4,y4 = r/tan(A/2),r
        if packed_circles_data(a,b,c)['mode'] == 'A+B':
            B,_ = law_of_cosines(a,c,b)
            x5,y5 = c-rb/tan(B/2),rb
        else:
            x5,y5 = rb/tan(A/2),rb
        plot_line(x0,y0,x1,y1)
        plot_line(x1,y1,x2,y2)
        plot_line(x2,y2,x0,y0)
        plot_circle(x4,y4,r)
        plot_circle(x3,y3,ra)
        plot_circle(x5,y5,rb)
        total += R(a, b, c)
        count += 1
        title('n = '+str(n)+', average area = '+str(round(total / count, 5)))
        axis('equal')
        pause(0.5)
    pause(5)
show()
# -----------------------------------------------------------------------------
