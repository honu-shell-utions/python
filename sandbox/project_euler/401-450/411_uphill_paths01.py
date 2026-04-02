#  -----------------------------------------------------------------------------
#  Uphill paths
#  Problem 411
#  https://projecteuler.net/problem=411
#  -----------------------------------------------------------------------------
import matplotlib.pyplot as plt
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
for n in [22,123,10**4]:
    points = gen_points(n)
    points = sorted(points,key=itemgetter(1))
    longest = longest_increasing_subsequence(points)
    x_path = [0]
    y_path = [0]
    for p in longest:
        x,y = p
        x_path.append(x)
        y_path.append(y)
    lis_size = len(longest)
    x_path.append(n)
    y_path.append(n)
    x_vals = []
    y_vals = []
    for p in points:
        x,y = p
        x_vals.append(x)
        y_vals.append(y)   
    plt.plot(x_vals,y_vals,'o',color='red')
    plt.plot(x_path,y_path)
    plt.plot([0,n],[0,n],'o',color='black')
    plt.title(f'LIS for n = {n} is {lis_size}')
    ax = plt.gca()
    ax.axes.set_aspect(1) 
    plt.show()
#  -----------------------------------------------------------------------------
#  solution: 9936352
#  -----------------------------------------------------------------------------
