import numpy as np
from time import time

start = time()
limit = 10**7
arr = np.ones(limit+1,int)

for n in range(2,limit):
  for m in range (1,limit//n+1):
    arr[n*m] += 1

count = 0
for i in range(2,limit-1):
  if arr[i] == arr[i+1]:
    count += 1

print(f'Solution: {count}, Run-Time: {time()-start}')

# 986262
