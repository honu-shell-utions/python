# ----------------------------------------------------------------------------
# 171_sum_squares.py
# finding numbers for which the sum of the squares of the digits is a square
#
# For a positive integer n, let f(n) be the sum of the squares of the digits
# (in base 10) of n, e.g.
#      f(3) = 3^2 = 9,
#      f(25) = 2^2 + 5^2 = 4 + 25 = 29,
#      f(442) = 4^2 + 4^2 + 2^2 = 16 + 16 + 4 = 36
#
# Find the last nine digits of the sum of all n, 0 < n < 10^20, such that
# f(n) is a perfect square.
# ----------------------------------------------------------------------------
def euler_171(d,l):
    res = {}
    for k in d.keys():
        for i in range(10):
            x = k+i**2
            val = res.get(x,[0,0])
            val[0] += d[k][0]+i*10**l*d[k][1]
            val[1] += d[k][1]
            res[x] = val
    return res
# ----------------------------------------------------------------------------
from time import time
start = time()

DS = {i**2:[i,1] for i in range(10)}

for i in range(1,20):
    DS = euler_171(DS,i)
    
res = 0
for j in [i**2 for i in range(41)]:
    res += (DS.get(j,[0,0])[0]%(10**9))
    
res %= (10**9)

print (f'Solution: {res}, Run-Time: {time()-start}')
# ----------------------------------------------------------------------------
# solution: 142989277
# ----------------------------------------------------------------------------
