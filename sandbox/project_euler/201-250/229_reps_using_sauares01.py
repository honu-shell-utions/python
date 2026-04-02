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
        for b in range(1, int(sqrt(limit/k)) + 1):
            bvalue = k*b*b
            if k == 1:
                t = b
            else:
                t = 1
            for a in range(t, int(sqrt(limit - bvalue)) + 1):
                key = a*a + bvalue
                if key < limit:
                    if k == 1:
                        set1.add(key)
                    elif k == 2:
                        set2.add(key)
                    elif k == 3:
                        set3.add(key)
                    elif k == 7:
                        set7.add(key)
                else:
                    break
    return len(set1 & set2 & set3 & set7)

start = time()
print(f'Solution: {euler_229(2*10**9)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 11325263
#-------------------------------------------------------------------------------
