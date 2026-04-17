"""
https://projecteuler.net/problem=955
"""

import time

def T(n):
    return n * (n + 1) // 2

def next_hit_from_triangle_index(t):
    N = t * (t + 1)
    best_g = None
    best_m = None

    a = 1
    while a * a <= N:
        if N % a == 0:
            b = N // a

            # need g to be a positive integer
            if (b - a - 1) % 2 == 0:
                g = (b - a - 1) // 2
                m = (a + b - 1) // 2

                if g > 0 and (best_g is None or g < best_g):
                    best_g = g
                    best_m = m
        a += 1

    return best_g, best_m

def find_nth_index_fast(n):
    # first hit is 3 = T_2 at sequence index 0
    hit_count = 1
    seq_index = 0
    t = 2   # current hit value is T_t

    if n == 1:
        return seq_index, T(t)

    while hit_count < n:
        g, next_t = next_hit_from_triangle_index(t)
        seq_index += g
        t = next_t
        hit_count += 1

    return seq_index, T(t)


for count in range(10,71,10):
    start_time = time.perf_counter()
    print(find_nth_index_fast(count),end=' ')
    end_time = time.perf_counter()
    print(f"n = {count}, Execution time: {end_time - start_time:.4f} seconds")
