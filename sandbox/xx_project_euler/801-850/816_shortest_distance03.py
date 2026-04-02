#  -----------------------------------------------------------------------------
#  Shortest distance among points
#  Problem 816
#  https://projecteuler.net/problem=816
#  -----------------------------------------------------------------------------
from itertools import combinations
from math import sqrt
from pylab import plot, show, axis, title, gca
#  -----------------------------------------------------------------------------
def plot_points(points):
    for x,y in points:
        plot(x,y,'o')
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
    combos = combinations(points,2)
    min_distance = 10**8
    print(k,'-'*60)
    for p1,p2 in combos:
        d = dist(p1,p2)
        if d < min_dist:
            min_dist = d
            min_pair = (p1,p2)
        print(p1,p2,'current min:',min_dist)
    print('-'*62)
    return min_pair,min_dist
#  -----------------------------------------------------------------------------
for num_pts in range(3,21):
    points = make_points(num_pts)
    plot_points(points)
    min_pair,min_dist = d(num_pts)
    plot([min_pair[0][0],min_pair[1][0]],[min_pair[0][1],min_pair[1][1]])
    title(f'{min_dist:.9f} for {num_pts} points.')
    ax = gca()
    ax.axes.set_aspect(1)
    show()
#  -----------------------------------------------------------------------------
#  solution: 20.880613018
#  -----------------------------------------------------------------------------
