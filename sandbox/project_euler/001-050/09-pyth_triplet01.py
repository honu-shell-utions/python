##A Pythagorean triplet is a set of three natural numbers, a < b < c,
##for which, a^2 + b^2 = c^2
##For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
##There exists exactly one Pythagorean triplet for which a + b + c = 1000.
##Find the product abc.
#-------------------------------------------------------------------------------
from math import gcd
from operator import itemgetter
#-------------------------------------------------------------------------------
def get_prim_list(limit):
    a=0
    b=0
    c=0
    m=2
    prim_list = []
    while c < limit//2:
        for n in range(1,m):
            a=m*m-n*n
            b=2*m*n
            c=m*m+n*n
            if a+b+c > limit:
                break
            if gcd(a,b,c) == 1:
                prim_list.append(sorted([a,b,c]))           
        m += 1
    return prim_list
#-------------------------------------------------------------------------------
def get_trip_list(prim_list,limit):
    trip_list = []
    for a,b,c in prim_list:
        trip_list.append([a,b,c])
        k = 2
        while k*a + k*b + k*c <= limit:
            trip_list.append([k*a,k*b,k*c])
            k += 1
    return trip_list
#-------------------------------------------------------------------------------
max_p = 10**2
p_list = get_prim_list(max_p)
p_list.sort(key=itemgetter(2))
t_list = get_trip_list(p_list,max_p)
for a,b,c in t_list:
        print(a,b,c)
#-------------------------------------------------------------------------------    
#solution: 31875000
#-------------------------------------------------------------------------------
