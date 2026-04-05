#  -----------------------------------------------------------------------------
#  Almost Pi
#  Problem 461
#  Let fn(k) = e^(k/n)-1, for all non-negative integers k.
#  
#  Remarkably:
#  fsub(200)(6)+fsub(200)(75)+fsub(200)(89)+fsub(200)(226) = 3.141592644529… ≈ π.
#  
#  In fact, it is the best approximation of π of the form
#  fn(a) + fn(b) + fn(c) + fn(d) for n = 200.
#  
#  Let g(n) = a^2 + b^2 + c^2 + d^2 for a, b, c, d that minimize
#  the error: | fn(a) + fn(b) + fn(c) + fn(d) - π|
#  (where |x| denotes the absolute value of x).
#  
#  You are given g(200) = 6^2 + 75^2 + 89^2 + 226^2 = 64658.
#  
#  Find g(10_000).
#  -----------------------------------------------------------------------------
from math import pi, expm1
from time import time
start = time()

N = 10**4
g = []

x = 0
ex = expm1(x/N)
while ex < pi:
    y = 0
    ey = expm1(y/N)
    while y <= x and ex+ey < pi:
        g += [ex+ey]
        y += 1
        ey = expm1(y/N)
    x += 1
    ex = expm1(x/N)

g.sort()

x, y = 0, len(g)-1
p1 = q1 = 0

while x <= y:
    p = g[x+1]+g[y]
    q = g[x]+g[y-1]
    if abs(p-pi) < abs(q-pi):
        x += 1
    else:
        y -= 1
    p, q = g[x], g[y]
    if abs(p+q-pi) < abs(p1+q1-pi):
        p1, q1 = p, q

answer = 0

x = 0
ex = expm1(x/N)
while ex < pi:
    y = 0
    ey = expm1(y/N)
    while y <= x and ex+ey < pi:
        if ex+ey == p1 or ex+ey == q1:
            answer += x**2+y**2
        y += 1
        ey = expm1(y/N)
    x += 1
    ex = expm1(x/N)

print(f'Solution: {answer}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 159_820_276
#  -----------------------------------------------------------------------------
