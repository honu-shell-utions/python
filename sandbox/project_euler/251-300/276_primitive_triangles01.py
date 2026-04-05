#  -----------------------------------------------------------------------------
#  Primitive Triangles
#  Problem 276
#  Consider the triangles with integer sides a, b and c with a ≤ b ≤ c.
#  An integer sided triangle (a,b,c) is called primitive if gcd(a,b,c)=1. 
#  How many primitive integer sided triangles exist with a perimeter not
#  exceeding 10 000 000?
#  https://projecteuler.net/problem=276
#  -----------------------------------------------------------------------------
from math import ceil, floor
from time import time
#  -----------------------------------------------------------------------------
# Alcuin's sequence
def Alcuin(n):
    ans = 0
    ans = (round((n * n) / 12) - floor(n / 4) * floor((n + 2) / 4))
    return ans
#  -----------------------------------------------------------------------------
start = time()
BOUND = 10**7
nonprimitive_triangle_count = [0] * (BOUND+1)
primitive_triangle_count = [0] * (BOUND+1)

for i in range(2, BOUND+1):
    curcount = Alcuin(i) - nonprimitive_triangle_count[i]
    primitive_triangle_count[i] = curcount
    for j in range(2 * i, BOUND+1, i):
        nonprimitive_triangle_count[j] += curcount

print(f'Solution: {sum(primitive_triangle_count)}, Run-Time: {time()-start:.3f}')
#  -----------------------------------------------------------------------------
#  solution: 5777137137739632912
#  -----------------------------------------------------------------------------
