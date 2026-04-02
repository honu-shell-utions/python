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
def k1():
    for a in range(1,int(sqrt(limit))+1):
        for b in range(1,int(sqrt(limit - a*a))+1):
            n = a*a + b*b
            if n > limit:
                break
            set1.add(n)
#-------------------------------------------------------------------------------
def k2():
    for a in range(1,int(sqrt(limit))+1):
        for b in range(1,int(sqrt(limit - a*a))+1):
            n = a*a + 2*b*b
            if n > limit:
                break
            set2.add(n)
#-------------------------------------------------------------------------------
def k3():
    for a in range(1,int(sqrt(limit))+1):
        for b in range(1,int(sqrt(limit - a*a))+1):
            n = a*a + 3*b*b
            if n > limit:
                break
            set3.add(n)
#-------------------------------------------------------------------------------
def k7():
    for a in range(1,int(sqrt(limit))+1):
        for b in range(1,int(sqrt(limit - a*a))+1):
            n = a*a + 7*b*b
            if n > limit:
                break
            set7.add(n)
#-------------------------------------------------------------------------------    
def euler_229():
    k1()
    k2()
    k3()
    k7()
#-------------------------------------------------------------------------------
start = time()
limit = 10**7
set1 = set()
set2 = set()
set3 = set()
set7 = set()
euler_229()
solution = len(set1 & set2 & set3 & set7)
print(f'Solution: {solution}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 11325263
#-------------------------------------------------------------------------------
