#  -----------------------------------------------------------------------------
#  Fibonacci paths
#  Problem 662
#  https://projecteuler.net/problem=662
#  -----------------------------------------------------------------------------
from math import gcd,sqrt,isqrt
from time import time
#  -----------------------------------------------------------------------------
def euler_662(w,h):
    dp = [[0 for j in range(h+1)] for i in range(w+1)]
    dp[0][0] = 1 
 
    for i in range(w+1):
        for j in range(h+1):
            for a,b in valid_moves:
                if a > i:
                    break
                if b <= j:
                    dp[i][j] = (dp[i][j] + dp[i-a][j-b]) % M
            for a,b in valid_moves:
                if a > j:
                    break
                if b <= i:
                    dp[i][j] = (dp[i][j] + dp[i-b][j-a]) % M

    return dp[w][h]
#  -----------------------------------------------------------------------------
def fibonacci_gen(T1=1,T2=1):
    yield T1
    yield T2
    while True:
        yield T1+T2
        T1,T2 = T2,T1+T2
#  -----------------------------------------------------------------------------
def get_prim_list(limit):
    a=0
    b=0
    c=0
    m=2
    prim_list = []
    while max(a,b) <= limit:
        for n in range(1,m):
            a=m*m-n*n
            b=2*m*n
            c=m*m+n*n
            if gcd(a,b,c) == 1:
                prim_list.append((a,b,c))           
        m += 1
    return prim_list
#  -----------------------------------------------------------------------------
def get_trip_list(limit):
    prim_list = get_prim_list(limit)
    trip_list = []
    for a,b,c in prim_list:
        trip_list.append((a,b,c))
        k = 2
        while max(k*a,k*b) <= limit:
            trip_list.append((k*a,k*b,k*c))
            k += 1
    return trip_list
#  -----------------------------------------------------------------------------
def is_fib(n):
    if n % 144 not in [ 0, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 123, 136, 141, 143]:
        return False 
    a = 5*n**2 + 4
    b = 5*n**2 - 4
    return (sqrt(a) == isqrt(a) or sqrt(b) == isqrt(b))
#  -----------------------------------------------------------------------------
M = 10**9+7
limit = 10**4
valid_moves = []
tl = get_trip_list(limit)
fg = fibonacci_gen(1,2)
while True:
    f = next(fg)
    if f > limit:
        break
    valid_moves.append((f,0))
for x,y,c in tl:
    if is_fib(c):
        if y > x:
            x,y = y,x
        valid_moves.append((x,y))
valid_moves = sorted(valid_moves)

for (w,h) in [(3,4),(10,10),(10**4,10**4)]:
    start = time()
    print(f'Solution: {euler_662(w,h):10}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 860873428
#  -----------------------------------------------------------------------------
