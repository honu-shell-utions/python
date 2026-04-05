from functools import lru_cache
from time import time

@lru_cache()
def lucas(n):
    if n == 1:
        return n
    if n == 0:
        return 2
    return lucas(n - 1) + lucas(n - 2)

def f(i):
    return ((i<<1)&62)|((i>>5)^(((i>>4)&1)&((i>>3)&1)))


start = time()
av = [i for i in range(64)]
cycles = []

for i in range(64):
    if i in av:
        av.remove(i)
        cycles.append([i])
        j = f(i)
        while j not in cycles[-1]:
            if j in av:
                av.remove(j)
            cycles[-1].append(j)
            j = f(j)

solution = 1            
for c in cycles:
    print(c,'---> ',len(c),'cycles')
    solution *= lucas(len(c))

print(f'\nSolution: {solution}, Run-Time: {time()-start}')
# 15964587728784
