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
#
#  see: Robert_OConnor's post on the Euler forum
#  -----------------------------------------------------------------------------
from time import time
from sympy import primepi as pi
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
    # k = 1                                                                     
    res = pi(n) # number of primes p <= n                                       
    if n < 4:
        return res
    
    # k = 2                                                                     
    # count even numbers greater than 2 and odd numbers of the form p+2 for     
    # all odd primes p                                                           
    res += pi(n-2)-1+(n-2)//2

    # k > 2                                                                     
    # all numbers greater than 2k-1 can be represented as the sum of k primes   
    res += ((n-4)*(n-4))//4
    return res
#  -----------------------------------------------------------------------------
start = time()
# Compute the Fibonacci numbers
fg = fibonacci_gen()
fibonacci = []
while len(fibonacci) < 45:
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
