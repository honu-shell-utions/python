#  -----------------------------------------------------------------------------
#  Friend numbers
#  Problem 612
#  https://projecteuler.net/problem=612
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def are_friends(a,b):
    set_a = set(str(a))
    set_b = set(str(b))
    if set_a.intersection(set_b):
        return True
    else:
        return False
#  -----------------------------------------------------------------------------
def f(n):
    num_friends = 0
    for p in range(1,n-1):
        for q in range(p+1,n):
            if are_friends(p,q):
                num_friends += 1
    return num_friends           
#  -----------------------------------------------------------------------------
for exp in range(2,11):
    start = time()
    solution = f(10**exp)
    print(f'Solution for 10^{exp:2}: {solution:10}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 819963842
#  -----------------------------------------------------------------------------
