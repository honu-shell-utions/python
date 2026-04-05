#  -----------------------------------------------------------------------------
#  Pythagorean Ant
#  Problem 613
#  Dave is doing his homework on the balcony and, preparing a presentation
#  about Pythagorean triangles, has just cut out a triangle with side
#  lengths 30cm, 40cm and 50cm from some cardboard, when a gust of wind
#  blows the triangle down into the garden.  Another gust blows a small
#  ant straight onto this triangle. The poor ant is completely disoriented
#  and starts to crawl straight ahead in random direction in order to get
#  back into the grass.
#  
#  Assuming that all possible positions of the ant within the triangle and
#  all possible directions of moving on are equiprobable, what is the
#  probability that the ant leaves the triangle along its longest side?
#  Give your answer rounded to 10 digits after the decimal point.
#  
#  https://projecteuler.net/problem=613
#  -----------------------------------------------------------------------------
from time import time
from random import uniform
from math import atan, pi
#  -----------------------------------------------------------------------------
def get_xy():
    x = uniform(0,3)
    y = uniform(0,4*x/3)
    return x,y
#  -----------------------------------------------------------------------------
def prob_hypot(x,y):
    alpha = atan((4-y)/(3-x))
    beta = atan(x/y)
    gamma = 3*pi/2 - alpha - beta
    return gamma/(2*pi)               
#  -----------------------------------------------------------------------------
num_ants = 1
total_p = 0
for _ in range(10**8):
    num_ants += 1
    x,y = get_xy()
    total_p += prob_hypot(x,y)
    print(round(total_p/num_ants,10))
#  -----------------------------------------------------------------------------
#  solution:  0.3916721504
#  -----------------------------------------------------------------------------
