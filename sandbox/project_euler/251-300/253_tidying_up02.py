from random import shuffle
from time import time
#-------------------------------------------------------------------------------
start = time()
N = 40
total = 0
kMax = 10**8
k = 1
r = [x for x in range(N)]

for k in range(1,kMax+1):
    ones_zeros = N*[1]
    shuffle(r)
    segments = 1
    seg_max = 1
    for i in range(N - 2):
        if r[i] != 0 and r[i] != N - 1 and ones_zeros[r[i] + 1] == ones_zeros[r[i] - 1] == 1:
            segments += 1
        elif r[i] != 0 and r[i] != N - 1 and ones_zeros[r[i] + 1] == ones_zeros[r[i] - 1] == 0:
            segments -= 1
        elif (r[i] == 0 and ones_zeros[r[i] + 1] == 0) or (r[i] == N - 1 and ones_zeros[r[i] - 1] == 0):
            segments -= 1
        if segments > seg_max:
            seg_max = segments
        ones_zeros[r[i]] = 0
    total += seg_max
    average = 1.0*total/k
    if k % 10**5 == 0:
        print(f'k: {k}, current average: {round(average,6)}')

print(f'Solution: {round(average,6)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 11.492847
#-------------------------------------------------------------------------------
