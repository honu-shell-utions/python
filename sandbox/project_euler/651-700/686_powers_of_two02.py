#  -----------------------------------------------------------------------------
#  Powers of Two 
#  Problem 686
#  https://projecteuler.net/problem=686
#  -----------------------------------------------------------------------------
from math import log2, floor
from time import time
#  -----------------------------------------------------------------------------
def euler_686(target,limit):
  log210 = log2(10)
  solutions = 0
  low_log = log2(target)
  high_log = log2(target+1)
  x = 1
  
  while solutions < limit:
    low = low_log + x*log210
    high = high_log + x*log210
    if floor(low) != floor(high):
      solutions += 1
    x += 1

  return int(high)
#  -----------------------------------------------------------------------------
for target,limit in [(12,1),(12,2),(123,45),(123,678910)]:
    start = time()
    print(f'For ({target:3},{limit:6}), solution: {euler_686(target,limit):10}, Run-Time: {time()-start:7.3f}')
#  -----------------------------------------------------------------------------
#  solution: 193060223
#  -----------------------------------------------------------------------------
