#  -----------------------------------------------------------------------------
#  Triangle Triples
#  Problem 378
#  https://projecteuler.net/problem=378
#  -----------------------------------------------------------------------------
from sympy import divisor_count
from time import time
from itertools import combinations
#  -----------------------------------------------------------------------------
def tri_gen():
  n = 1
  while True:
    yield n*(n+1)//2
    n += 1
#  -----------------------------------------------------------------------------
def make_combos(n):
  combo_list = []
  tg = tri_gen()
  num_tri = 0
  for t in tg:
    combo_list.append(t)
    num_tri += 1
    if num_tri >= n:
      break
  combos = combinations(combo_list,3)
  return combos
#  -----------------------------------------------------------------------------
def Tr(n):
  combos = make_combos(n)
  num_triples = 0
  for a,b,c in combos:
      if divisor_count(a) > divisor_count(b) > divisor_count(c):
          #print(a,b,c)
          num_triples += 1
  return num_triples
#  -----------------------------------------------------------------------------
for limit in [20,10**2,10**3]:
    start = time()
    print(f'Solution: {Tr(limit)}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
# 20 -------> 14
# 100 ------> 5772
# 1000 -----> 11174776
# 6*10**7 --> 147534623725724718
#  -----------------------------------------------------------------------------
