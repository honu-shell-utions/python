#-------------------------------------------------------------------------------
import queue
from time import time
#-------------------------------------------------------------------------------
def euler_223(n):
    f = lambda a,b,c: (a-2*b+2*c,2*a-b+2*c,2*a-2*b+3*c)
    g = lambda a,b,c: (-2*a+b+2*c,-a+2*b+2*c,-2*a+2*b+3*c)
    h = lambda a,b,c: (2*a+b+2*c,a+2*b+2*c,2*a+2*b+3*c)

    q = queue.Queue()
    q.put((1,1,1))
    q.put((1,2,2))
    answer = 2
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
print(f'Solution: {euler_223(25*10**6)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
