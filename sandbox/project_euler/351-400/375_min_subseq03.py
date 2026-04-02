#  -----------------------------------------------------------------------------
#  Minimum of subsequences
#  Problem 375
#  https://projecteuler.net/problem=375
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def M(N):
    """Compute the sum of A(i,j) over all 1 <= i <= j <= N"""
    val = 290797**2 % 50515093
    # We store previous minimums ans there positions the stored minimums
    # will be strictly increasing
    mins = [(val,1)]
    res = val   # the desired val
    partial = val  # accounts for the contributions of all minimums in mins
    for j in range(2,N+1):
        val = val**2 % 50515093
        # We remove minimums from mins as long as they are larger than val
        if val < mins[-1][0]:
            while val <= mins[-1][0]:
                if len(mins) > 1:
                    partial -= mins[-1][0]*(mins[-1][1]-mins[-2][1])
                    mins.pop()
                else:
                    partial = 0
                    mins = []
                    break
        # Add the new value
        mins.append((val,j))
        if len(mins) > 1:
            partial += val*(j-mins[-2][1])
        else:
            # if the current value is the smallest value that has been seen
            partial = val*j
        # add A(i,j) for all 1<= i <= j
        res += partial
    return res
#  -----------------------------------------------------------------------------
for n in [2,3,5,10,20,10**2,10**3,10**4,2*10**9]:
    start = time()
    print(f'n = {n:12}: {M(n):20}, Run-Time: {time()-start:8.3f}')
#  -----------------------------------------------------------------------------
# 14598198  for M(2)
# 44119381  for M(3)
# 104348007 for M(5)
# 432256955 for M(10)
# 1264201746 for M(20)
# 27022904418 for M(10**2)
# 322833621931 for M(10**3)
# 3264567774119 for M(10**4)
# 7435327983715286168 for M(2*10**9)
#  -----------------------------------------------------------------------------
