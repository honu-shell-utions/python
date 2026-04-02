#  -----------------------------------------------------------------------------
#  Bitwise-OR operations on random integers 
#  Problem 323
#  https://projecteuler.net/problem=323
#  -----------------------------------------------------------------------------
from random import choice
from time import time
#  -----------------------------------------------------------------------------
def run_trial():
    plays = 0
    #print(''.join(COIN_LIST))
    while 'H' in COIN_LIST:
        plays += 1
        for ndx in range(len(COIN_LIST)):
            if COIN_LIST[ndx] == 'H':
                COIN_LIST[ndx] = choice('HT')
        #print(''.join(COIN_LIST))
    return plays                        
#  -----------------------------------------------------------------------------
EXP = 0
while True:
    start = time()
    EXP += 1
    NUM_TRIALS = 10**EXP
    sum_iterations = 0
    for _ in range(NUM_TRIALS):
        COIN_LIST =['H' for i in range(32)]
        sum_iterations += run_trial()
    print(f'Average value for 10^{EXP} trials: {round(sum_iterations/NUM_TRIALS,10):10}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 6.3551758451
#  -----------------------------------------------------------------------------
