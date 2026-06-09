# -----------------------------------------------------------------------------
# Jim McCleery
# June 8, 2026
# Kailua-Kona, HI
#
# https://projecteuler.net/problem=496
# -----------------------------------------------------------------------------

import time
from math import isqrt, gcd

def F(L):
    total_BC_sum = 0
    
    # Since m < 2n and primitive_a = m*n <= L,
    # The absolute maximum limit for n occurs when m is at its lowest (~n)
    # n * n <= L => max_n = isqrt(L)
    max_n = isqrt(L)
    
    for n in range(1, max_n + 1):
        # We need primitive_a = m * n <= L  =>  m <= L // n
        # Also bounded by the geometric rule: m < 2 * n
        max_m = min(2 * n - 1, L // n)
        
        for m in range(n + 1, max_m + 1):
            if gcd(m, n) == 1:
                primitive_a = m * n
                
                # Maximum multiplier k such that k * primitive_a <= L
                K = L // primitive_a
                
                # Direct arithmetic sum of: primitive_a * (1 + 2 + ... + K)
                total_BC_sum += primitive_a * (K * (K + 1)) // 2
                
    return total_BC_sum

# -----------------------------------------------------------------------------
# MAIN EXECUTION BLOCK WITH TIMING
# -----------------------------------------------------------------------------
n = 10**9
start_time = time.perf_counter()
result = F(n)
end_time = time.perf_counter()
execution_time = end_time - start_time
print(f"F({n}) = {result} (Took {execution_time:.6f} seconds)")
