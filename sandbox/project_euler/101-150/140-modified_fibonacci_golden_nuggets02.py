################################################################################
##Modified Fibonacci golden nuggets
##Problem 140
################################################################################
from time import time
from math import sqrt
################################################################################
def test_k(k):
    b_squared = 5*k**2 + 14*k + 1
    b_root = sqrt(b_squared)
    if b_squared == int(b_root + 0.5)**2:
        return True
    else:
        return False
################################################################################
start = time()
limit = 10**10
count = 1
total = 0
for k in range(1,limit):
    if test_k(k):
        print(count,'\t',k)
        count += 1
        total += k
        if count > 30:
            break
#NOTE: this program will run until the heat death of the universe        
print('The solution:',total,'Run Time:',time()-start)
################################################################################
#solution: 5673835352990
################################################################################
