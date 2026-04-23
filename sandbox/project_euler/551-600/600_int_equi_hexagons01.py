"""
Let H(n) be the number of distinct integer sided equiangular
convex hexagons with perimeter not exceeding (n).

Hexagons are distinct if and only if they are not congruent.

You are given

H(6)=1,H(12)=10,H(100)=31248.

Find H(55106).

Of course for this graphics version computing H(55106) would take longer
than the heat death of the universe.  Version 2 does the job but is
no fun.

"""

from math import pi,sin,cos
from matplotlib.pyplot import *

def plot_line(x1, y1, x2, y2):
    """
    Plot a line segment between two points using matplotlib.
    """
    plot([x1, x2], [y1, y2])


# -----------------------------------------------------------------------------

def canonical_form(sides):
    """
    Smallest tuple under the 12 symmetries of the hexagon:
    6 rotations + 6 reflections.
    """
    s = tuple(sides)
    rev = s[::-1]

    best = None
    for i in range(6):
        r1 = s[i:] + s[:i]
        r2 = rev[i:] + rev[:i]
        if best is None or r1 < best:
            best = r1
        if r2 < best:
            best = r2
    return best


def unique_hexagons_up_to(n):
    """
    Return the set of distinct equiangular hexagons
    with positive integer sides and perimeter <= n.
    """
    unique = set()

    for a in range(1, n - 4):
        for b in range(1, n - 3):
            for c in range(1, n - 2):

                # perimeter = a+b+c+(a+b-e)+e+(b+c-e) = 2*a + 3*b + 2*c - e
                # so to have perimeter <= n, we need:
                # e >= 2*a + 3*b + 2*c - n
                e_min = max(1, 2 * a + 3 * b + 2 * c - n)

                # d = a+b-e >= 1  ->  e <= a+b-1
                # f = b+c-e >= 1  ->  e <= b+c-1
                e_max = min(a + b - 1, b + c - 1)

                for e in range(e_min, e_max + 1):
                    d = a + b - e
                    f = b + c - e
                    unique.add(canonical_form((a, b, c, d, e, f)))

    return unique


def display_unique_hexagons(n):
    count = 0
    hex = unique_hexagons_up_to(n)
    for h in hex:
        count += 1
        cla()
        x,y = 0,0
        theta = 0
        for s in h:
            x1,y1 = x+s*cos(theta),y+s*sin(theta)
            plot_line(x,y,x1,y1)
            x,y = x1,y1
            theta += pi/3
        title('Number of unique equialgular hexagons for n = '+str(n)+ ' is '+str(count))
        pause(0.2)

for n in [6,12,24,48,100]:
    display_unique_hexagons(n)
    show()
