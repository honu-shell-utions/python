#-------------------------------------------------------------------------------
# 223_almost_right-angled_triangles_I.py
#
# almost right-angled triangles I
# Let us call an integer sided triangle with sides a ≤ b ≤ c barely acute if
# the sides satisfy a^2 + b^2 = c^2 + 1
#
# How many barely acute triangles are there with perimeter ≤ 25_000_000?
# ans== 61614848
#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
def is_triangle(a,b,c):
    if a+b > c and a+c > b and b+c > a:
        return True
    return False
#-------------------------------------------------------------------------------
def is_almost(a,b,c):
    return a**2 + b**2 == c**2 + 1
#-------------------------------------------------------------------------------
def find_em(limit):
    count = 0
    for a in range(1,limit):
        for b in range(a,limit):
            for c in range(b,limit):
                if not is_triangle(a,b,c) or a + b + c > limit:
                    break
                if is_almost(a,b,c):
                    count += 1
    return count
#-------------------------------------------------------------------------------
start = time()
limit = 25*10**6
count = find_em(limit)
print(f'Solution: {count}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 61614848
#-------------------------------------------------------------------------------
