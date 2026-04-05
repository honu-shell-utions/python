from sympy import primerange
from time import time

def S(k, n, p):
  total = 0   
  for i in range(n % p + 1, p):
      y = (n + 1 - i) % p
      z = pow(i, k, p)
      total += y*z
      total %= p
  return p - total 
    
def main():
  start = time()
  P_MIN = 2*10**9
  K = 10**4
  N = 10**12
  print("Calculating all primes between %d to %d" % (P_MIN, P_MIN + 2000))
  primes = primerange(P_MIN, P_MIN + 2001)
  print("Calculating result...")
  sum = 0
  for p in primes:
      sum += S(K, N, p)
  print(f'Solution: {sum}, Run-Time: {time()-start}')

main()
#  solution: 106650212746
