import numpy
from time import time
# ---------------------------------------------------------------
def euler_378(n_max):
    start = time()
    # load the divisors of 1 to n into an array
    n = n_max + 1
    num_divisors = (n + 1)*[1]
    for k in range(2, n//2 + 1):
        num_divisors[k::k] = [i + 1 for i in num_divisors[k::k]]
    for k in range(n//2 + 1, n + 1):
        num_divisors[k] += 1
    # ---------------------------------------------------------------
    # load the divisors for the triangular numbers
    dT = [0]*(n_max + 1)
    for j in range(n_max+1):
        if j % 2 == 0:
            dT[j] = num_divisors[j//2]*num_divisors[j + 1]
        else:
            dT[j] = num_divisors[j]*num_divisors[(j + 1)//2]
    # ---------------------------------------------------------------
    # -- Valeurs des dT[j] avec leur ordre de multiplicite ----------
    vdT, wdT = [], []
    for v in list(set(dT)):
        vdT.append(v)
        wdT.append(0)
    vdT.sort()
    # ---------------------------------------------------------------
    # -- adT[j] : nombre de i < j tels que dT[i] > dT[j] ------------
    adT = numpy.array([0]*(n_max + 1))
    for j in range(1,n_max+1):
        i = vdT.index(dT[j])
        adT[j] = sum(wdT[i + 1:])
        wdT[i] += 1
    # ---------------------------------------------------------------
    # -- Valeurs des dT[k] avec leur ordre de multiplicite ----------
    vdT, wdT = [], []
    for v in list(set(dT)):
        vdT.append(v)
        wdT.append(0)
    vdT.sort()
    # ---------------------------------------------------------------
    # -- bdT[j] : nombre de k > j tels que dT[j] > dT[k] ------------
    bdT = numpy.array([0]*(n_max + 1))
    for j in range(n_max,0,-1):
        i = vdT.index(dT[j])
        bdT[n_max - j] = sum(wdT[:i])
        wdT[i] += 1
    # ---------------------------------------------------------------
    solution = 0
    MOD = 10**18
    for j in range(1,n_max+1):
        solution += int(adT[j])*int(bdT[n_max - j])  
    print (f'Solution: {solution % MOD:18}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
for limit in [20,10**2,10**3,6*10**7]:
    euler_378(limit)
#  -----------------------------------------------------------------------------
# https://projecteuler.net/problem=378
# 20 -------> 14
# 100 ------> 5772
# 1000 -----> 11174776
# 6*10**7 --> 147534623725724718
#  -----------------------------------------------------------------------------

