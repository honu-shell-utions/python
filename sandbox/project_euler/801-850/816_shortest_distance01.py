#  -----------------------------------------------------------------------------
#  Shortest distance among points
#  Problem 816
#  https://projecteuler.net/problem=816
#  -----------------------------------------------------------------------------
from itertools import combinations
from math import sqrt
#  -----------------------------------------------------------------------------
def rand_gen():
    s_current = 290797
    while True:
        yield s_current
        s_current = s_current**2 % 50515093
#  -----------------------------------------------------------------------------
def make_points(k):
    rg = rand_gen()
    points = []
    while len(points) < k:
        points.append((next(rg),next(rg)))
    return points
#  -----------------------------------------------------------------------------
def dist(p1,p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    return sqrt( (x2-x1)**2 + (y2-y1)**2 )
#  -----------------------------------------------------------------------------
def d(k):
    min_dist = 10**10
    points = make_points(k)
    combos = combinations(points,2)
    min_distance = 10**8
    for p1,p2 in combos:
        d = dist(p1,p2)
        if d < min_dist:
            min_dist = d
            print(f'current min distance: {min_dist:20.9f}')
    return min_dist
#  -----------------------------------------------------------------------------
for n in [14,2*10**3,2*10**4,2*10**5,2*10**6]:
    print(f'Solution for n = {n:10,}, minimum diatance: {d(n):20.9f}')
#  -----------------------------------------------------------------------------
#  solution: 20.880613018
#  -----------------------------------------------------------------------------
