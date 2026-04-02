#  -----------------------------------------------------------------------------
#  Bitwise-OR operations on random integers 
#  Problem 323
#  https://projecteuler.net/problem=323
#  -----------------------------------------------------------------------------
from random import randint
from time import time
#  -----------------------------------------------------------------------------
def next_x(current_x):
    return current_x | randint(0,2**32)
#  -----------------------------------------------------------------------------
def run_trial():
    x = 0
    ndx = 1
    while True:
        x = next_x(x)
        if x == 2**32 - 1:
            break
        ndx += 1
    return ndx
#  -----------------------------------------------------------------------------
MAXIMUM = 2**32
EXP = 0
while True:
    start = time()
    EXP += 1
    NUM_TRIALS = 10**EXP
    sum_iterations = 0
    for _ in range(NUM_TRIALS):
        sum_iterations += run_trial()
    print(f'Average value for 10^{EXP} trials: {round(sum_iterations/NUM_TRIALS,10):10}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 6.3551758451
#  -----------------------------------------------------------------------------
