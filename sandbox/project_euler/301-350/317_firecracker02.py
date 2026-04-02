#  -----------------------------------------------------------------------------
#  Firecracker
#  Problem 317
#  https://projecteuler.net/problem=317
#  https://euler.stephan-brumme.com/317/
#  -----------------------------------------------------------------------------
from math import pi, radians, sin, cos, tan
from matplotlib.pyplot import *
from numpy import linspace
from random import uniform
#  -----------------------------------------------------------------------------
# Projectile Function
def projectile_plot(velocity,theta):
    global max_height
    # gravity
    g = 9.8
    # Evaluating Range
    range = velocity**2*sin(2*theta)/g
    # Evaluating max height
    height = velocity**2*(sin(theta))**2/(2*g)
    if height > max_height:
        max_height = height
    x = linspace(0, range, 100)
    # Solving for y
    y = x*tan(theta)-(1/2)*(g*x**2)/(velocity**2*(cos(theta))**2 )
    # Plot orderd pairs
    plot(x,y,'-')
#  -----------------------------------------------------------------------------
max_height = -10**2
num_parabolas = 100
for _ in range(num_parabolas):
    velocity = 100
    theta = uniform(0,pi)
    projectile_plot(velocity,theta)
title(f'Maximum Height: {round(max_height,2)} meters.')
show()
#  -----------------------------------------------------------------------------
#  -----------------------------------------------------------------------------
#  solution: 1856532.8455
#  -----------------------------------------------------------------------------
