#-------------------------------------------------------------------------------
## Sums of Digit Factorials
## Problem 254
## Define f(n) as the sum of the factorials of the digits of n.
## For example, f(342) = 3! + 4! + 2! = 32.
## 
## Define sf(n) as the sum of the digits of f(n).
## So sf(342) = 3 + 2 = 5.
## 
## Define g(i) to be the smallest positive integer n such
## that sf(n) = i. Though sf(342) is 5, sf(25) is also 5,
## and it can be verified that g(5) is 25.
## 
## Define sg(i) as the sum of the digits of g(i).
## So sg(5) = 2 + 5 = 7.
## 
## Further, it can be verified that g(20) is 267
## and ∑ sg(i) for 1 ≤ i ≤ 20 is 156.
## 
## What is ∑ sg(i) for 1 ≤ i ≤ 150?
#-------------------------------------------------------------------------------
from math import factorial
from time import time
#-------------------------------------------------------------------------------
def f(n):
    total = 0
    for d in str(n):
        total += factorial(int(d))
    return total
#-------------------------------------------------------------------------------
def sf(n):
    n = f(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total
#-------------------------------------------------------------------------------
def g(i):
    k = 1
    while True:
        if sf(k) == i:
            return k
        else:
            k += 1
#-------------------------------------------------------------------------------
def sg(i):
    total = 0
    n = g(i)
    while n > 0:
        total += n % 10
        n //= 10
    return total
#-------------------------------------------------------------------------------
start = time()
print('f(342) =',f(342))
print('sf(342) =',sf(342))
print('g(sf(342)) =',g(sf(342)))
print('sg(5) =',sg(5))
N = 63
total = 0
for i in range(1,N+1):
    temp = sg(i)
    total += temp
    
print(f'Sum of sg(n) for n = 1..{N} = {total}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 8184523820510
#N = 20  # Answer: 156
#N = 63  # Answer: 3398
#N = 150  # Answer: 8184523820510
#-------------------------------------------------------------------------------
