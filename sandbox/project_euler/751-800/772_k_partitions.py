# ----------------------------------------------------------------------------
# Balanceable k-bounded partitions
# Problem 772
# https://projecteuler.net/problem=772
# ----------------------------------------------------------------------------
from time import time
# ----------------------------------------------------------------------------
def partitions(n):
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return		
    # modify partitions of n-1 to form partitions of n
    for p in partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]
# ----------------------------------------------------------------------------
def is_k_bounded(p,k):
    for v in p:
        if v > k:
            return False
    return True
# ----------------------------------------------------------------------------
def is_balanced(p,n):
    if n % 2 != 0 or len(p) == 1:
        return False
    test1 = set()
    test1.add(0)
    target = n//2
    for i in range(len(p)-1,-1,-1):
        test2 = set()
        for t in test1:
            if t + p[i] == target:
                return True
            test2.add(t+p[i])
            test2.add(t)
        test1 = test2
    return False
# ----------------------------------------------------------------------------
MOD = 10**9 + 7
for k in [3,4,5,6,7]:
    for n in range(2,10**6):
        k_bounded = 0
        balanced = 0
        for p in partitions(n):
            if is_k_bounded(p,k):
                k_bounded += 1
                if is_balanced(p,n):
                    balanced += 1
        if k_bounded == balanced:
            print(f'{n % MOD} has {k_bounded} {k}-bounded partitions and all are balanced')
            break
# ----------------------------------------------------------------------------
# solution = 83985379
# ----------------------------------------------------------------------------
