#  -----------------------------------------------------------------------------
#  Powers of Two 
#  Problem 686
#  https://projecteuler.net/problem=686
#  -----------------------------------------------------------------------------
from math import log10
from time import time
#  -----------------------------------------------------------------------------
def p(L,n):
    str_L = str(L)
    j = 1
    count = 0
    while True:
        res = 2**j
        if str_L == str(res)[:len(str_L)]:
            count += 1
            if count == n:
                return j
        j += 1
#  -----------------------------------------------------------------------------
def euler_686(limit):
    matLog2 = log10(2)
    count = 0
    i=0
    while True:
      i+=1
      val = 10**(i*matLog2-int(i*matLog2))
      if int(val*100) == 123:
        count+=1
        if count == limit:
          break
    return i
#  -----------------------------------------------------------------------------
print(p(12,1))
print(p(12,2))
print(euler_686(45))
start = time()
print(f'Solution: {euler_686(678910)}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 193060223
#  -----------------------------------------------------------------------------
