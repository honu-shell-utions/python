#  -----------------------------------------------------------------------------
#  Range flips
#  Problem 430
#  https://projecteuler.net/problem=430
#  -----------------------------------------------------------------------------
import matplotlib.pyplot as plt
from random import randint
#  -----------------------------------------------------------------------------
def make_square(x,y,s,status):
    return plt.Rectangle((x,y),s,s,fill=status)
#  -----------------------------------------------------------------------------
square_side = 10
num_squares = 10
status = [False]*num_squares
start = 0
end = num_squares - 1
for k in range(5):
    fig, ax = plt.subplots()
    plt.axis('off')
    ax.set_aspect('equal', adjustable='datalim')
    left = 0
    for i in range(num_squares):
        ax.add_patch(make_square(left,0,square_side,status[i]))
        left += square_side
    start = randint(0,num_squares-1)
    end = randint(start,num_squares-1)
    for j in range(start,end+1):
        status[j] = not status[j]
    left = 0
    for i in range(num_squares):
        ax.add_patch(make_square(left,-square_side,square_side,status[i]))
        left += square_side
    plt.title(f'Range reversed: from: {start} to: {end}')
    ax.plot()
    plt.show() 
    plt.close(fig)
#  -----------------------------------------------------------------------------
#  solution: 5000624921.38
#  -----------------------------------------------------------------------------
