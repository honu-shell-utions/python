#  -----------------------------------------------------------------------------
#  Square the Smallest 
#  Problem 822
#  https://projecteuler.net/problem=822
#  -----------------------------------------------------------------------------
from time import time
from math import sqrt
#  -----------------------------------------------------------------------------
def S(n, m):
    arr = list(range(2, n + 1))
    i = 0
    while (i < m):
        stop = True
        for x in arr:
            xsqrt = sqrt(x)
            if (abs(xsqrt - round(xsqrt)) < 1e-9):
                xsqrt = round(xsqrt)
                if (xsqrt in arr):
                    stop = False
                    break
        if (stop): break

        arr[0] *= arr[0]
        arr = sorted(arr)
        i += 1

    k = (m - i) // (n - 1)
    i += k * (n - 1)
    for j in range(len(arr)): arr[j] = pow(arr[j], pow(2, k, MOD-1), MOD)
    
    j = 0
    while i < m:
        arr[j] = (arr[j] * arr[j]) % MOD
        i += 1
        j += 1
    return sum(arr) % MOD
#  -----------------------------------------------------------------------------
MOD = 1234567891
for n,m in [(5,3),(10,100),(10**4,10**16)]:
    start = time()
    print(f'Solution for (n,m) = ({n:5},{m:17}): {S(n,m):10}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 950591530
#  -----------------------------------------------------------------------------
