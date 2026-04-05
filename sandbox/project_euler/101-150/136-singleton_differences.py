################################################################################
##Singleton difference 
##Problem 136
##The positive integers, x, y, and z, are consecutive terms of
##an arithmetic progression. Given that n is a positive integer,
##the equation, x^2 − y^2 − z^2 = n, has exactly one solution when n = 20:
##
##13^2 − 10^2 − 7^2 = 20
##
##In fact there are twenty-five values of n below one hundred
##for which the equation has a unique solution.
##
##How many values of n less than fifty million have exactly one solution?
################################################################################
from time import time
################################################################################
def euler_136():
    max = 50*10**6
    keepers = [0]*(max+1)
    for u in range(1,max+1):
        for v in range(1,max+1):
            if u*v > max+1:
                break
            if (u + v) % 4 == 0 and 3 * v  > u and (3 * v - u) % 4 == 0:
                keepers[u * v] += 1              
    return keepers             
################################################################################
start = time()
results = euler_136()
total = results.count(1)
print('Solution:',total,'Run Time:',time()-start)
################################################################################
#solution: 2544559
################################################################################
