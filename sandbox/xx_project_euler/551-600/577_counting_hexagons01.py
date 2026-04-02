#  -----------------------------------------------------------------------------
#  Counting Hexagons
#  Problem 577
#  https://projecteuler.net/problem=577
#  -----------------------------------------------------------------------------
from matplotlib.pyplot import *
from math import sqrt
#  -----------------------------------------------------------------------------
def plot_triangle(left_x,bottom_y):
    x_vals = [left_x, left_x+1,left_x+1/2,left_x]
    y_vals = [bottom_y,bottom_y,bottom_y+sqrt(3)/2,bottom_y]
    plot(x_vals,y_vals)
#  -----------------------------------------------------------------------------

#  -----------------------------------------------------------------------------
fig, ax = subplots()
for limit in [3,6,10,20]:
    axis('off')
    for row in range(limit):
        for col in range(row,limit):
            plot_triangle(col-1/2*row,row*sqrt(3)/2)
    plot()
    show() 
close(fig)
#  -----------------------------------------------------------------------------
#  solution:
#  -----------------------------------------------------------------------------
