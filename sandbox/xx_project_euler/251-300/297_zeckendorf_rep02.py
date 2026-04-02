#  -----------------------------------------------------------------------------
#  Zeckendorf Representation
#  Problem 297
#  https://projecteuler.net/problem=297
#  -----------------------------------------------------------------------------
def Zeckendorf(n):
    fib = [1,1]
    while(fib[-1] < n):
        fib.append(fib[-1]+fib[-2])
    zeck = [0 for i in fib]
    for i in range(2,len(fib)):
        zeck[i] = zeck[i-1] + zeck[i-2] + fib[i-2]
    total = 0
    for i in range(len(fib)-1, -1, -1):
        if n >= fib[i]:
            total += zeck[i]
            n -= fib[i]
            total += n
    return total

for limit in [10**6,10**10,10**17]:
    print(f'for n = {limit}, Z(n) = {Zeckendorf(limit)}')
#  -----------------------------------------------------------------------------
#  solution for 10**6  = 7894453
#  solution for 10**10 = 92359637
#  solution for 10**17 = 2252639041804718029
#  -----------------------------------------------------------------------------
