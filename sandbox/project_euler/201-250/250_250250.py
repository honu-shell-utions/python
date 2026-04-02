#-------------------------------------------------------------------------------
## 250250
## Problem 250
## Find the number of non-empty subsets of {1^1, 2^2, 3^3,..., 250250^250250},
## the sum of whose elements is divisible by 250.
## 
## Enter the rightmost 16 digits as your answer.
#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
def euler_250():
    MOD = 10**16
    subsets = [0] * 250  # subsets[i] is {the number of subsets with sum equal to i mod 250} mod 10^16
    subsets[0] = 1	
    for i in range(1, 250250 + 1):
        offset = pow(i, i, 250)
        subsets = [(val + subsets[(j - offset) % 250]) % MOD \
		for (j, val) in enumerate(subsets)]
        ans = (subsets[0] - 1) % MOD
    return str(ans)

start = time()
print(f'Solution: {euler_250()}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 1425480602091519
#-------------------------------------------------------------------------------
