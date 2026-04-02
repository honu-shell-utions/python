#  -----------------------------------------------------------------------------
#  Prime connection
#  Problem 425
#  Two positive numbers A and B are said to be connected (denoted by "A ↔ B")
#  if one of these conditions holds:
#  (1) A and B have the same length and differ in exactly one digit;
#  for example, 123 ↔ 173.
#  (2) Adding one digit to the left of A (or B) makes B (or A); for example,
#  23 ↔ 223 and 123 ↔ 23.
#  
#  We call a prime P a 2's relative if there exists a chain of connected
#  primes between 2 and P and no prime in the chain exceeds P.
#  
#  For example, 127 is a 2's relative. One of the possible chains is shown below:
#  2 ↔ 3 ↔ 13 ↔ 113 ↔ 103 ↔ 107 ↔ 127
#  However, 11 and 103 are not 2's relatives.
#  
#  Let F(N) be the sum of the primes ≤ N which are not 2's relatives.
#  We can verify that F(10^3) = 431 and F(10^4) = 78728.
#  
#  Find F(10^7).
#  
#  https://projecteuler.net/problem=425
#  -----------------------------------------------------------------------------
from time import time
import heapq
from sympy import isprime
#  -----------------------------------------------------------------------------
class euler_425:
    def __init__(self,limit):
        self.LIMIT = limit
        self.is_prime = [isprime(x) for x in range(self.LIMIT)]
        self.solution = self.compute_solution()
    #  ------------------------------------------------------------------------
    def compute_solution(self):	
        pathmax = [None] * len(self.is_prime)
        queue = [(2, 2)]
        while len(queue) > 0:
            pmax, n = heapq.heappop(queue)
            if pathmax[n] is not None and pmax >= pathmax[n]:
                continue
            pathmax[n] = pmax
            digits = self.to_digits(n)
            tempdigits = list(digits)
            for i in range(len(tempdigits)):  # For each digit position
                for j in range(10):  # For each digit value
                    tempdigits[i] = j
                    m = self.to_number(tempdigits)
                    nextpmax = max(m, pmax)
                    if m < len(self.is_prime) and self.is_prime[m] and (pathmax[m]\
                            is None or nextpmax < pathmax[m]):
                        heapq.heappush(queue, (nextpmax, m))
                tempdigits[i] = digits[i]  # Restore the digit
            
        ans = sum(i for i in range(len(self.is_prime))\
                      if self.is_prime[i] and (pathmax[i] is None or pathmax[i] > i))
        return str(ans)
    #  ------------------------------------------------------------------------
    def to_digits(self,n):
        if n < 0:
            raise ValueError()
        temp = []
        while True:
            temp.append(n % 10)
            n //= 10
            if n == 0:
                break	
        temp.append(0)
        temp.reverse()
        return temp
    #  ------------------------------------------------------------------------
    def to_number(self,digits):
        result = 0
        for x in digits:
            result = result * 10 + x
        return result
    #  ------------------------------------------------------------------------
    def get_solution(self):
        return self.solution
    #  ------------------------------------------------------------------------
#  -----------------------------------------------------------------------------
for exp in range(2,8):
    start = time()
    limit = 10**exp
    instance = euler_425(limit)
    sol = instance.get_solution()
    print(f'Solution for n = 10^{exp}: {sol:>20}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 46479497324
#  -----------------------------------------------------------------------------
