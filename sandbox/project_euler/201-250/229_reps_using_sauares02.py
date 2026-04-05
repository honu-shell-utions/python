#-------------------------------------------------------------------------------
## Four Representations using Squares
## Problem 229
## Consider the number 3600. It is very special, because
## 
## 3600 = 48^2 + 36^2
## 3600 = 20^2 + 2×40^2
## 3600 = 30^2 + 3×30^2
## 3600 = 45^2 + 7×15^2
## 
## Similarly, we find that:
##     
## 88201 = 99^2 + 280^2
## 88201 = 287^2 + 2×54^2
## 88201 = 283^2 + 3×52^2
## 88201 = 197^2 + 7×84^2.
## 
## In 1747, Euler proved which numbers are representable as a sum
## of two squares. We are interested in the numbers n which admit
## representations of all of the following four types:
## 
## n = a1^2 + 1*b1^2
## n = a2^2 + 2*b2^2
## n = a3^2 + 3*b3^2
## n = a7^2 + 7*b7^2
## 
## where the ak and bk are positive integers.
## 
## There are 75373 such numbers that do not exceed 10^7.
## How many such numbers are there that do not exceed 2×10^9?
#-------------------------------------------------------------------------------
from time import time
from math import sqrt
#-------------------------------------------------------------------------------
def euler_229(limit):
    set1 = set()
    set2 = set()
    set3 = set()
    set7 = set()
    
    for k in [1,2,3,7]:
        for a in range(1,limit):
            for b in range(1,limit):
                second_term = k*b*b
                n = a*a + second_term
                if n > limit:
                    break
                if k == 1:
                    set1.add(n)
                elif k == 2:
                    set2.add(n)
                elif k == 3:
                    set3.add(n)
                elif k == 7:
                    set7.add(n)
                    
    return len(set1 & set2 & set3 & set7)

start = time()
print(f'Solution: {euler_229(10**7)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 11325263
#-------------------------------------------------------------------------------
