"""
410_circle_tangent_line.py
https://projecteuler.net/problem=410

Circle and Tangent Line
Let C be the circle with radius r, x^2 + y^2 = r^2. We choose two points
P(a, b) and Q(-a, c) so that the line passing through P and Q is tangent to C.

For example, the quadruplet (r, a, b, c) = (2, 6, 2, -7) satisfies this
property.

Let F(R, X) be the number of the integer quadruplets (r, a, b, c) with this
property, and with 0 < r ≤ R and 0 < a ≤ X.

We can verify that F(1,5) = 10, F(2,10) = 52 and F(10,100) = 3384.

Find F(10^8, 10^9) + F(10^9, 10^8).

"""
#  -----------------------------------------------------------------------------
from matplotlib.pyplot import *
from random import randint
from math import sqrt,lcm,pi
import numpy as np
from fractions import Fraction
#  -----------------------------------------------------------------------------
def get_line(x1,y1,x2,y2):
    if x1 == x2:
        A = 1
        B = 0
        C = -x1
    else:
        m = Fraction(y2-y1,x2-x1)
        A = -m
        B = Fraction(1,1)
        C = m*Fraction(x1,1) - Fraction(y1,1)
        P = lcm(A.denominator,B.denominator,C.denominator)
        A *= P
        B *= P
        C *= P
    return A,B,C
#  -----------------------------------------------------------------------------
def get_distance(A,B,C,x,y):
    return abs(A*x+B*y+C)/sqrt(A**2+B**2)
#  -----------------------------------------------------------------------------
def plot_circle(radius):
    angle = np.linspace(0,2*pi,1500)
    x_arr = radius*np.cos(angle)
    y_arr = radius*np.sin(angle)
    plot(x_arr,y_arr)
#  -----------------------------------------------------------------------------
def graph_quadruplets(R, X):
    count = 0
    for r in range(1, R + 1):
        for a in range(1, X + 1):
            for b in range(1, X + 1):
                for c in range(1, X + 1):
                    A,B,C = get_line(a,b,-a,c)
                    dist = get_distance(A,B,C,0,0)
                    if dist == r:
                        count += 1
                        axis('equal')
                        plot_circle(r)
                        plot([a,-a],[b,c])
                        title(f'Current Count: {count}')
                        show()
    return count
#  -----------------------------------------------------------------------------
graph_quadruplets(3,20)
#  -----------------------------------------------------------------------------
#  solution: 799999783589946560
#  -----------------------------------------------------------------------------
