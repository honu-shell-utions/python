#  -----------------------------------------------------------------------------
#  Counting primitive Pythagorean triples
#  Problem 540
#  https://projecteuler.net/problem=540
#  https://www.sciencedirect.com/science/article/pii/S0022314X1730344X
#  -----------------------------------------------------------------------------
import numpy as np
from time import time
#  -----------------------------------------------------------------------------
def gen_prim_pyth_trips(limit=None):
    A = [[1,2,2],[-2,-1,-2],[2,2,3]]
    B = [[1,2,2],[2,1,2],[2,2,3]]
    C = [[-1,-2,-2],[2,1,2],[2,2,3]]
    ABC = np.array([A, B, C])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, ABC)
#  -----------------------------------------------------------------------------
for limit in [20,10**6,10**8]:
    start = time()
    pt_gen = gen_prim_pyth_trips(limit)
    solution = sum(1 for trip in gen_prim_pyth_trips(limit) if all(trip))
    print(f'Solution for n = {limit}: {solution}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 500000000002845
#  -----------------------------------------------------------------------------
