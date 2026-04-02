#  -----------------------------------------------------------------------------
from bisect import bisect
from time import time
#  -----------------------------------------------------------------------------
def make_rands():
    s = 290797
    rand_nums = []
    for i in range(N):
        rand_nums.append(s)
        s = (s * s) % 50515093
    rand_nums.sort()
    return rand_nums
#  -----------------------------------------------------------------------------
def find_median():
    lo, hi = rand_nums[0] * rand_nums[1], rand_nums[-1] * rand_nums[-2]
    mid_index = (N * (N - 1) // 2) // 2  #N things taken 2 at a time//2 -> mid position
    while lo < hi:
        mid = (lo + hi + 1) // 2
        c = 0
        for i, x in enumerate(rand_nums):
            if x * x > mid: break
            j = bisect(rand_nums, mid // x)
            c += max(j - i - 1, 0)
        if c > mid_index:
            hi = mid - 1
        else:
            lo = mid
    return lo
#  -----------------------------------------------------------------------------
for N in [3,103,10**6+3]:
    start = time()
    rand_nums = make_rands()
    print(f'Solution: {find_median() + 1:16}, Run-Time: {time()-start}')
    
# 475808650131120
#  -----------------------------------------------------------------------------
