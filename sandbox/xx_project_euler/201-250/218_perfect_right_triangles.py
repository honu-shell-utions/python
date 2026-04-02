#-------------------------------------------------------------------------------
## Perfect right-angled triangles
## Problem 218
## Consider the right angled triangle with sides a=7, b=24 and c=25.
## The area of this triangle is 84, which is divisible by the perfect
## numbers 6 and 28.
## 
## Moreover it is a primitive right angled triangle as gcd(a,b)=1 and gcd(b,c)=1.
## Also c is a perfect square.
## 
## We will call a right angled triangle perfect if
## -it is a primitive right angled triangle
## -its hypotenuse is a perfect square
## 
## We will call a right angled triangle super-perfect if
## -it is a perfect right angled triangle and
## -its area is a multiple of the perfect numbers 6 and 28.
## 
## How many perfect right-angled triangles with c≤10^16 exist that
## are not super-perfect?
#-------------------------------------------------------------------------------
from math import gcd, sqrt, isqrt
from operator import itemgetter
#-------------------------------------------------------------------------------
def is_super_perfect(a,b):
    area =  a*b/2
    if area % 6 == 0 and area % 28 == 0:
        return True
    return False
#-------------------------------------------------------------------------------
def get_perfect_right_triangles(limit):
    a=0
    b=0
    c=0
    m=2
    prim_list = []
    while len(prim_list) < limit:
        for n in range(1,m):
            a=m*m-n*n
            b=2*m*n
            c=m*m+n*n
            if gcd(a,b,c) == 1 and sqrt(c) == isqrt(c):
                prim_list.append([a,b,c])
        m += 1
    return prim_list
#-------------------------------------------------------------------------------
list_size = 10**6
prims = get_perfect_right_triangles(list_size)
prims.sort(key=itemgetter(2))
for a,b,c in prims:
    if not is_super_perfect(a,b):
        print(a,b,c)
#-------------------------------------------------------------------------------
# solution: 0
#-------------------------------------------------------------------------------
