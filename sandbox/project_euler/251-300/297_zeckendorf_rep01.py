#  -----------------------------------------------------------------------------
#  Zeckendorf Representation
#  Problem 297
#  https://projecteuler.net/problem=297
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def make_fibs():
    fibs = [1, 2]
    while fibs[-1] < limit:
      fibs.append(fibs[-1]+fibs[-2])
    return fibs
#  -----------------------------------------------------------------------------
def z(n):
    count = 1
    for i,v in enumerate(fibs):
        if v > n:
            break
    sub_fibs = fibs[:i]
    total = sub_fibs[-1]
    if total == n:
        return count, total
    for f in reversed(sub_fibs[:-1]):
        if total + f <= n:
            total += f
            count += 1      
    return count, total
#  -----------------------------------------------------------------------------
start = time()
solution = 0
limit = 10**6
fibs = make_fibs()
for n in range(1,limit):
    c,t = z(n)
    solution += c

print(f'Solution: {solution}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution for 10**6  = 7894453
#  solution for 10**10 = 92359637
#  solution for 10**17 = 2252639041804718029
#  -----------------------------------------------------------------------------
