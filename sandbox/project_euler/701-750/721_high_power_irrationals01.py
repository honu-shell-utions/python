#  -----------------------------------------------------------------------------
#  High powers of irrational numbers
#  Problem 721
#  https://projecteuler.net/problem=721
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def f(a,n):
    global next_square, next_ix   
    if a == next_square:
        next_ix += 1
        next_square = next_ix**2
        return pow(2*(next_ix-1), n, MOD)
    c = next_ix
    rxp = 1
    ryp = 0
    bxp = c
    byp = 1
    while n != 0:
        if n % 2 == 1:
            rxp, ryp = (rxp*bxp+a*ryp*byp) % MOD, (ryp*bxp + rxp*byp) % MOD       
        n >>= 1
        bxp, byp = (bxp*bxp+a*byp*byp) % MOD, (byp*bxp + bxp*byp) % MOD
        
    return (2*rxp) - 1
#  -----------------------------------------------------------------------------
start = time()
target = 5_000_000
MOD = 999_999_937
next_ix = 1
next_square = 1
total = 0

for a in range(1,target+1):
    total += f(a,a**2)
    total %= MOD

print("Answer: ", total)
print("Time: ", time() - start)
#  -----------------------------------------------------------------------------
#  solution: 700792959
#  -----------------------------------------------------------------------------
