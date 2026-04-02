#  -----------------------------------------------------------------------------
#  McCarthy 91 function
#  Problem 555
#  https://projecteuler.net/problem=555
#  https://oeis.org/search?q=McCarthy+91+function&language=english&go=Search
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def euler_555(p, m):
    ans = 0 

    # Iterate over the possible values of d
    for d in range(1, p // 2 + 1):

        # For this value of d, the possible values of s are exactly the
        # multiples of d between d and p - d
        min_s = d
        max_s = (p - d) - (p % d)
            
        # Find the count and sum of the possible values of s
        count_s = (max_s - min_s) // d + 1
        sum_s = (min_s + max_s) * count_s // 2

        # Add on the contribution to the sum
        ans += count_s * d * (d + 2 * m + 1) // 2 - d * sum_s

    return ans
#  -----------------------------------------------------------------------------
for p,m in [(10,10),(10**3,10**3),(10**6,10**6)]:
    start = time()
    print(f'Solution for (p,m) = ({p:7},{m:7}): {euler_555(p,m):18}, Run-Time: {time()-start:6.3f}')
#  -----------------------------------------------------------------------------
#  solution: 208517717451208352
#  -----------------------------------------------------------------------------
