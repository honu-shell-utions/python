#-------------------------------------------------------------------------------
## Integer partition equations
## 
## Problem 207
## For some positive integers k, there exists an integer
## partition of the form   4^t = 2^t + k,
## where 4t, 2t, and k are all positive integers and
## t is a real number.
## 
## The first two such partitions are 4^1 = 2^1 + 2 and
## 4^1.5849625... = 2^1.5849625... + 6.
## 
## Partitions where t is also an integer are called perfect.
## For any m ≥ 1 let P(m) be the proportion of such partitions
## that are perfect with k ≤ m.
## 
## Thus P(6) = 1/2.
## 
## In the following table are listed some values of P(m)
## 
##    P(5) = 1/1
##    P(10) = 1/2
##    P(15) = 2/3
##    P(20) = 1/2
##    P(25) = 1/2
##    P(30) = 2/5
##    ...
##    P(180) = 1/4
##    P(185) = 3/13
## 
## Find the smallest m for which P(m) < 1/12345
#-------------------------------------------------------------------------------
from time import time
from math import log
from fractions import Fraction
#-------------------------------------------------------------------------------
start_time = time()
n=3
countint=1
total=2

while True:
   if log(n+1,2) == int(log(n+1,2)):
       countint += 1
   total += 1
   if Fraction(countint, total) < Fraction(1,12345):
       print(n**2+n, Fraction(countint,total))
       break
   n += 1

print(f'{time()-start_time}')
#-------------------------------------------------------------------------------
# solution: 44043947822
#-------------------------------------------------------------------------------
