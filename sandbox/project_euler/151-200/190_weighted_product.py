#-------------------------------------------------------------------------------
## Maximising a weighted product
## Problem 190
## Let Sm = (x1, x2, ... , xm) be the m-tuple of positive
## real numbers with x1 + x2 + ... + xm = m for which
## Pm = x1^1 * x2^2 * ... * xm^m is maximised.
## 
## For example, it can be verified that
## [P10] = 4112 ([ ] is the integer part function).
## 
## Find Σ[Pm] for 2 ≤ m ≤ 15.
#-------------------------------------------------------------------------------
def P(m):
   k = 2.0 / (m+1)
   pm = 1
   for i in range(1, m+1):
      pm *= (i*k)**i
   return int(pm)

summation = 0
for k in range(2,16):
    temp = P(k)
    summation += temp
    print(k,temp)
    
print('Solution:',summation)
#-------------------------------------------------------------------------------
#solution: 371048281
#-------------------------------------------------------------------------------
