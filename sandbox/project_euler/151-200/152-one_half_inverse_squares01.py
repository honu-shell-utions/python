################################################################################
##Writing 1/2 as a sum of inverse squares 
##Problem 152
##There are several ways to write the number 1/2 as a sum of
##inverse squares using distinct integers.
##
##For instance, the numbers {2,3,4,5,7,12,15,20,28,35} can be used:
##                  
##In fact, only using integers between 2 and 45 inclusive, there are
##exactly three ways to do it, the remaining two being:
##{2,3,4,6,7,9,10,20,28,35,36,45} and {2,3,4,6,7,9,12,15,28,30,35,36,45}.
##
##How many ways are there to write the number 1/2 as a sum of inverse
##squares using distinct integers between 2 and 80 inclusive?
################################################################################
from time import time
from math import lcm
from itertools import chain, combinations
################################################################################
candidates = [2,3,4,5,6,7,8,9,10,12,13,14,15,16,18,20,\
              21,24,27,28,30,32,35,36,39,40,42,45,48,\
              52,54,56,60,63,64,65,70,72,80]

##candidates = [2,3,4,5,6,7,8,9,10,12,13,14,15,16,18,20,\
##               21,24,27,28,30,32,35,36,39,40,42,45]

l_c_m = lcm(*candidates)**2
half_lcm = l_c_m // 2
################################################################################
#create the power set for the current set
def powerset():
    return chain.from_iterable(combinations(candidates, r) \
                               for r in range(10,len(candidates)+1))
################################################################################
def euler_152():
    counter = 0
    combos = powerset()
    for com in combos:
        total =  sum(list(map(lambda x: l_c_m / (x*x),com)))
        if total == half_lcm:
            counter += 1
    return counter
################################################################################
start_time = time()
solution = euler_152()
run_time = time()-start_time
print(f'Solution: {solution}, Run-Time: {run_time} seconds.')
################################################################################
#solution: 301
################################################################################
