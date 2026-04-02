#  -----------------------------------------------------------------------------
#  Shortest distance among points
#  Problem 816
#  https://projecteuler.net/problem=816
#  -----------------------------------------------------------------------------
from scipy.spatial import KDTree
#  -----------------------------------------------------------------------------
def gen_s():
        s = 290797
        while True:
                yield s
                s = s**2%50515093
#  -----------------------------------------------------------------------------
def gen_p():
	s_gen = gen_s()
	while True:
		yield next(s_gen), next(s_gen)
#  -----------------------------------------------------------------------------
def make_points(k):
    gp = gen_p()
    points = []
    while len(points) < k:
        points.append(next(gp))
    return points
#  -----------------------------------------------------------------------------
for num_pts in [14,20,10**2,10**3,10**4,10**5,2*10**6]:
    gp = gen_p()
    points = make_points(num_pts)
    tree = KDTree(points)
    min_dist = 10**10
    min_pair = (0, 1)
    for i, x in enumerate(points):
        (dist,), (j,) = tree.query(x, k=(2,), distance_upper_bound = min_dist)
        if dist < min_dist:
            min_dist = dist
            min_pair = (i, j)
    sol = round(min_dist,9)
    print(f'The shortest distance for {num_pts:,} points is {sol}.')
#  -----------------------------------------------------------------------------
#  solution: 20.880613018
#  -----------------------------------------------------------------------------
