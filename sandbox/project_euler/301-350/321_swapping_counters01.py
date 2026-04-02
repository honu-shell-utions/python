#  -----------------------------------------------------------------------------
#  Swapping Counters
#  Problem 321
#  https://projecteuler.net/problem=321
#  https://www.ivl-projecteuler.com/overview-of-problems/30-difficulty/problem-321
#  https://oeis.org/A005563     
#  -----------------------------------------------------------------------------
import time, math
#  -----------------------------------------------------------------------------
def equationsolver(x, startx, starty, a, b, c, d, e, f):
    x1 = startx
    y1 = starty
    solutions = []
    while len(solutions) != x:
        xn = a*x1 + b*y1 + c
        yn = d*x1 + e*y1 + f
        if xn > 0:
            solutions.append(xn)
        x1 = xn
        y1 = yn
    return solutions
#  -----------------------------------------------------------------------------
def euler_321(limit):
    solutions = equationsolver(limit, 0, 0, 3, 2, 3, 4, 3, 5) + equationsolver(limit, 0, -1, 3, 2, 3, 4, 3, 5)
    return sum(sorted(list(set(solutions)))[:limit])
#  -----------------------------------------------------------------------------
while True:
    n = input("Input an integer: ")
    try:
        n = int(n)
    except:
        break
    print(f'Solution: {euler_321(n)}')

#  -----------------------------------------------------------------------------
#  solution for n = 40: 2470433131948040
#  -----------------------------------------------------------------------------
