#-------------------------------------------------------------------------------
from math import isqrt
from sympy import isprime, primerange, factorint
from time import time
#-------------------------------------------------------------------------------
def sigma(prime, power):
  res = 0
  m = 1
  for x in range(0, power + 1):
    res += m
    m *= prime
  return factorint(res)
#-------------------------------------------------------------------------------
def walk(current, factors, balance, number):
  # check end  
  if balance.count(0) == len(balance):
    print("found: ", number, factors)
    global total
    total += number
    return
  
  if len(factors) > 30:
    return

  if current == len(balance):
    return

  # try powers
  start = balance[current]
  if start < 1:
    walk(current + 1, factors, balance, number) # for zero
    start = 1

  p = factors[current]

  for power in range(start, 30):

    f = sigma(p, power)   

    number_new = number * p ** power

    #check if applicable
    if number_new > MAX:
      break

    apply = True
    for v in f:           
      if v in factors:
        i = factors.index(v)
        if i < current and balance[i] + f[v] > 0:
          apply = False
        break    

    # apply
    if apply:
      balance_new = balance[:]
      factors_new = factors[:]

      balance_new[current] -= power

      for v in f:           
        if not v in factors_new:
          factors_new.append(v)
          balance_new.append(f[v])
        else:
          i = factors.index(v)        
          balance_new[i] += f[v]

      walk(current + 1, factors_new, balance_new, number_new)
#-------------------------------------------------------------------------------
start = time()
MAX_PRIME = 10 ** 3
p = list(primerange(2,MAX_PRIME + 1))
MAX =  10 ** 18 
total = 0

for x in range(3, 15, 2):
  print("Checking: ", x / 2.0)
  if x == 9:
    balance = [1, -2]
    factors = [2, 3]
  else:
    balance = [1, -1]
    factors = [2, x]
  walk(0, factors, balance, 1)

print(f'Solution: {total}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# 482316491800641154
#-------------------------------------------------------------------------------
