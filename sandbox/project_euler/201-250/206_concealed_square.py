#-------------------------------------------------------------------------------
## Concealed Square
## Problem 206
## Find the unique positive integer whose square
## has the form 1_2_3_4_5_6_7_8_9_0,
## where each “_” is a single digit.
#-------------------------------------------------------------------------------
from random import randint
from math import sqrt, isqrt
from time import time
#-------------------------------------------------------------------------------
def test_the_guess(current_guess):
    if current_guess[0::2] == '1234567890':
        return True
    return False

start = time()
guess = 10**9
while True:
    if test_the_guess(str(guess**2)):
        break
    guess += 10
  
print(f'Solution: {guess}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 1389019170
#-------------------------------------------------------------------------------
