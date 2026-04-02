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
def fibonacci_gen():
    c1 = '14159265358979323846264338327950288419716939937510 \
          58209749445923078164062862089986280348253421170679'
    c2 = '82148086513282306647093844609550582231725359408128 \
          48111745028410270193852110555964462294895493038196'
    yield c1
    yield c2
    while True:
        yield c1+c2
        c1,c2 = c2,c1+c2
#-------------------------------------------------------------------------------
def D(n,fib_string):
    return int(fib_string[n-1:n])
#-------------------------------------------------------------------------------
start = time()
fib = fibonacci_gen()
total = 0
for n in range(1,18):
    val = (127+19*n)*7**n
    f = next(fib)
    while len(f) < val:
        f = next(fib)
    total += 10*n*D(val,f)

print(f'Solution: {total}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 
#-------------------------------------------------------------------------------
