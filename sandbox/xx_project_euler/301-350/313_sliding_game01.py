#  -----------------------------------------------------------------------------
# Sliding game 
# Problem 313
# https://projecteuler.net/problem=313
#  -----------------------------------------------------------------------------
from matplotlib.pyplot import *
from random import randint
#  -----------------------------------------------------------------------------
def make_circles(rows,cols,rr,cc):
    for r in range(1,rows+1):
        for c in range(1,cols+1):
            if r == rr and c == cc:
                col = 'r'
            else:
                col = 'b'
            circ = Circle((c*interval,r*interval),radius,color=col)
            axes.add_artist(circ)
#  -----------------------------------------------------------------------------
interval = 100
radius = 40
rows = 5
cols = 8
for _ in range(10):
    figure, axes = subplots()
    axis('off')
    axes.set_xlim(0,(1+cols)*interval)
    axes.set_ylim(0,(1+rows)*interval)
    axes.set_aspect(1)
    rr = randint(1,rows)
    cc = randint(1,cols)
    make_circles(rows,cols,rr,cc) 
    show()
#  -----------------------------------------------------------------------------
#  solution: 2057774861813004
#  -----------------------------------------------------------------------------
