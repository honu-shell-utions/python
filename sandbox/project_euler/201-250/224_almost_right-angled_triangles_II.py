#-------------------------------------------------------------------------------
# 224_almost_right-angled_triangles_II.py
#
# almost right-angled triangles II
# Let us call an integer sided triangle with sides a ≤ b ≤ c barely obtuse if
# the sides satisfy a^2 + b^2 = c^2 - 1
#
# How many barely obtuse triangles are there with perimeter ≤ 75_000_000?
# ans==4137330
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
import queue
from time import time
#-------------------------------------------------------------------------------
def euler_224(n):
    f = lambda a,b,c: (a-2*b+2*c,2*a-b+2*c,2*a-2*b+3*c)
    g = lambda a,b,c: (-2*a+b+2*c,-a+2*b+2*c,-2*a+2*b+3*c)
    h = lambda a,b,c: (2*a+b+2*c,a+2*b+2*c,2*a+2*b+3*c)

    q = queue.Queue()
    q.put((2,2,3))
    answer = 1
    while not q.empty():
        a,b,c = q.get()
        if a != b:
            y = f(a,b,c)
            if sum(y) <= n:
                q.put(y)
                answer += 1
        y = g(a,b,c)
        if sum(y) <= n:
            q.put(y)
            answer += 1
        y = h(a,b,c)
        if sum(y) <= n:
            q.put(y)
            answer += 1
    return answer
#-------------------------------------------------------------------------------
start = time()
print(f'Solution: {euler_224(75*10**6)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# solution: 4137330
#-------------------------------------------------------------------------------

