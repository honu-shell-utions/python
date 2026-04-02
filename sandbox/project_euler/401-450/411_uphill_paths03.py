#  -----------------------------------------------------------------------------
#  Uphill paths
#  Problem 411
#  https://projecteuler.net/problem=411
#  -----------------------------------------------------------------------------
from operator import itemgetter
#  -----------------------------------------------------------------------------
def gen_points(n):
    points = set()
    for i in range(2*n+1):
        pt = (2**i % n,3**i % n)
        points.add(pt)
    return sorted(list(points))
#  -----------------------------------------------------------------------------
def longest_increasing_subsequence(points):
    l = []
    for i in range(len(points)):
        l.append(max([l[j] for j in range(i) if l[j][-1] < points[i]] or [[]], key=len) 
                  + [points[i]])
    return max(l, key=len)
#  -----------------------------------------------------------------------------
total = 0
for k in range(1,31):
    points = gen_points(k**5)
    points = sorted(points,key=itemgetter(1))
    longest = longest_increasing_subsequence(points)
    path_length = len(longest)
    total += path_length
    print(f'{k:2}, {k**5:10}, {path_length:10}, {total:10}')
#  -----------------------------------------------------------------------------
#  solution: 9936352
#  -----------------------------------------------------------------------------
