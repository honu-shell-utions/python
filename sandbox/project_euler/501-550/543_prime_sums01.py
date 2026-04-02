#  -----------------------------------------------------------------------------
#  Prime-Sum Numbers
#  Problem 543
#  Define function P(n,k) = 1 if n can be written as the sum of k prime
#  numbers (with repetitions allowed), and P(n,k) = 0 otherwise.
#  
#  For example, P(10,2) = 1 because 10 can be written as either 3 + 7 or 5 + 5,
#  but P(11,2) = 0 because no two primes can sum to 11.
#  
#  Let S(n) be the sum of all P(i,k) over 1 ≤ i,k ≤ n.
#  
#  For example, S(10) = 20, S(100) = 2402, and S(1000) = 248838.
#  
#  Let F(k) be the kth Fibonacci number (with F(0) = 0 and F(1) = 1).
#  
#  Find the sum of all S(F(k)) over 3 ≤ k ≤ 44
#  
#  https://projecteuler.net/problem=543
#  -----------------------------------------------------------------------------
from time import time
from sympy import primepi
#  -----------------------------------------------------------------------------
def fibonacci_gen():
    T1 = 0
    T2 = 1
    yield T1
    yield T2
    while True:
        yield T1+T2
        T1,T2 = T2,T1+T2
#  -----------------------------------------------------------------------------
def S(n):
  ans = primepi(n)  # k = 1

  if n >= 4:        # k = 2 and odd i
    ans += primepi(n - 2) - 1
    
  ans += n // 2 - 1 # k = 2 and even i

  if n >= 5:        # k >= 3
    beg, end = n - 5, (n - 1) % 2
    ans += (beg + end) * ((beg - end) // 2 + 1) // 2
    
  return ans
#  -----------------------------------------------------------------------------
start = time()
fg = fibonacci_gen()
fibonacci = []
for _ in range(45):
    fibonacci.append(next(fg))

print('S(10) =',S(10),'\nS(100) =', S(100),'\nS(1000) =', S(1000))

ans = 0
for i in range(3, 45):
  n = fibonacci[i]
  ans += S(n)

print(f'Solution: {ans}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 199007746081234640
#  -----------------------------------------------------------------------------
