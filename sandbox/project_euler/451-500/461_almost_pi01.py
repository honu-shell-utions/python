#  -----------------------------------------------------------------------------
#  Almost Pi
#  Problem 461
#  Let fn(k) = e^(k/n)-1, for all non-negative integers k.
#  
#  Remarkably:
#  fsub(200)(6)+fsub(200)(75)+fsub(200)(89)+fsub(200)(226) = 3.141592644529… ≈ π.
#  
#  In fact, it is the best approximation of π of the form
#  fn(a) + fn(b) + fn(c) + fn(d) for n = 200.
#  
#  Let g(n) = a^2 + b^2 + c^2 + d^2 for a, b, c, d that minimize
#  the error: | fn(a) + fn(b) + fn(c) + fn(d) - π|
#  (where |x| denotes the absolute value of x).
#  
#  You are given g(200) = 6^2 + 75^2 + 89^2 + 226^2 = 64658.
#  
#  Find g(10_000).
#  -----------------------------------------------------------------------------
from math import pi, expm1
from time import time
#  -----------------------------------------------------------------------------
def f(k,n):
    return expm1(k/n)
#  -----------------------------------------------------------------------------
def abs_error(res):
    return abs(res-pi)
#  -----------------------------------------------------------------------------
def g(a,b,c,d):
    return a**2+b**2+c**2+d**2
#  -----------------------------------------------------------------------------
start = time()
min_error = 10**8
n = 200
limit = 300
for a in range(1,limit):
    for b in range(a+1,limit):
        for c in range(b+1,limit):
            for d in range(c+1,limit):
                approx = f(a,n)+f(b,n)+f(c,n)+f(d,n)
                error = abs_error(approx)
                if error < min_error:
                    min_error = error
                    solution = a**2 + b**2 + c**2 + d**2
                    print(a,b,c,d,'\t',g(a,b,c,d),'\t',min_error)

print(f'Min-Error: {solution}: Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution for n = 10**4: 159820276
#  solution for n = 200: 64658
#  -----------------------------------------------------------------------------
