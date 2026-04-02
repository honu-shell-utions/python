#  -----------------------------------------------------------------------------
#  Nim
#  Problem 301
#  https://projecteuler.net/problem=301
#  -----------------------------------------------------------------------------
import matplotlib.pyplot as plt
from random import randint, choice
import numpy as np
#  -----------------------------------------------------------------------------
def make_move(heap01,heap02,heap03):
    h01 = heap01
    h02 = heap02
    h03 = heap03
    total = h01+h02+h03
    while total == h01+h02+h03:
        heap = randint(1,3)
        if heap == 1 and h01 > 0:
            h01 -= randint(1,h01)
        elif heap == 2 and h02 > 0:
            h02 -= randint(1,h02)
        elif heap == 3 and h03 > 0:
            h03 -= randint(1,h03)
    return(h01,h02,h03)
#  -----------------------------------------------------------------------------
def make_stone(clump_center_x,clump_center_y):
    colors = ['blue','red','green','purple','orange','cyan','magenta','black']
    x = clump_center_x + randint(-10,10)
    y = clump_center_y + randint(-10,10)
    return plt.Circle((x,y),2,color=choice(colors))
#  -----------------------------------------------------------------------------
def make_circle(x,y,r):
    return plt.Circle((x,y),r,fill=False)
#  -----------------------------------------------------------------------------
limit = 10
heap01 = randint(1,limit+1)
heap02 = randint(1,limit+1)
heap03 = randint(1,limit+1)
    
while heap01 + heap02 + heap03 > 0:
    fig, ax = plt.subplots()
    plt.axis('off')
    ax.set_aspect('equal', adjustable='datalim')
    ax.add_patch(make_circle(-20,20,18))
    ax.add_patch(make_circle(20,20,18))
    ax.add_patch(make_circle(0,-20,18))
    for _ in range(heap01):
        ax.add_patch(make_stone(-20,20))
    for _ in range(heap02):
        ax.add_patch(make_stone(20,20))
    for _ in range(heap03):
        ax.add_patch(make_stone(0,-20))
    plt.title(f'Heap 1: {heap01}, Heap 2: {heap02}, Heap 3: {heap03}')
    heap01,heap02,heap03 = make_move(heap01,heap02,heap03)
    ax.plot()
    plt.show() 
plt.close(fig)
#  -----------------------------------------------------------------------------
#  solution: 2178309
#  -----------------------------------------------------------------------------
