# 31-coinSum.py
#
# In the United Kingdom the currency is made up of pound (£) and pence (p).
# There are eight coins in general circulation:
# 1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
#
# It is possible to make £2 in the following way:
# 1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
#
# How many different ways can £2 be made using any number of coins?
#------------------------------------------------------------------------------
import itertools
import numpy as np

targetSum = 200

def solutions():
    numberOfSolutions = 0
    initialArray = np.array([1,2,5,10,20,50,100,200])
        
    for d0 in range(201):
        for d1 in range(101):
            for d2 in range(41):
                for d3 in range(21):
                    for d4 in range(11):
                        for d5 in range(5):
                            for d6 in range(3):
                                for d7 in range(2):
                                    testArray = np.array([d0,d1,d2,d3,d4,d5,d6,d7])
                                    if sum(initialArray*testArray) == targetSum:
                                        numberOfSolutions += 1
    return(numberOfSolutions)

print('Number of solutions:',solutions())
