#-------------------------------------------------------------------------------
## Fibonacci Words 
## Problem 230
## For any two strings of digits, A and B, we define
## F(A,B) to be the sequence (A,B,AB,BAB,ABBAB,...) in
## which each term is the concatenation of the previous two.
## 
## Further, we define D(A,B)(n) to be the nth digit in the first
## term of F(A,B) that contains at least n digits.
## 
## Example:
## 
## Let A=1415926535, B=8979323846. We wish to find DA,B(35), say.
## 
## The first few terms of F(A,B) are:
## 1415926535
## 8979323846
## 14159265358979323846
## 897932384614159265358979323846
## 14159265358979323846897932384614159265358979323846
## 
## Then D(A,B)(35) is the 35th digit in the fifth term, which is 9.
## 
## Now we use for A the first 100 digits of π behind the decimal point:
## 
## 14159265358979323846264338327950288419716939937510 
## 58209749445923078164062862089986280348253421170679
## 
## and for B the next hundred digits:
## 
## 82148086513282306647093844609550582231725359408128 
## 48111745028410270193852110555964462294895493038196 .
## 
## Find ∑n = 0,1,...,17   10n× D(A,B)((127+19*n)×7^n) .
#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
start = time()
g = 1.6180339887498949 # golden ratio

t = (
    '14159265358979323846264338327950288419716939937510' +
    '58209749445923078164062862089986280348253421170679',
    '82148086513282306647093844609550582231725359408128' +
    '48111745028410270193852110555964462294895493038196'
)

l = len(t[0])

def D(n):
    i = (n-1) % l
    j =  (n-1) // l
    if j-1 <= j//g * g < j:
        k = 1
    else:
        k = 0 # magic
    return int(t[k][i])

total =  sum([10**i * D((127 + 19*i) * 7**i) for i in range(18)])
print(f'Solution: {total}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 850481152593119296
#-------------------------------------------------------------------------------
