#-------------------------------------------------------------------------------
# Inscribed circles of triangles with one angle of 60 degrees
# Problem 195
# Let's call an integer sided triangle with exactly one angle of
# 60 degrees a 60-degree triangle.
# 
# Let r be the radius of the inscribed circle of such a 60-degree triangle.
# 
# There are 1234 60-degree triangles for which r ≤ 100. 
# Let T(n) be the number of 60-degree triangles for which r ≤ n, so
# T(100) = 1234,  T(1000) = 22767, and  T(10000) = 359912.
# 
# Find T(1053779).
#-------------------------------------------------------------------------------
# a=k(2mn+n^2) or k(m^2-n^2)
# b=k(2mn+m^2)
# c=k(m^2+mn+n^2)
# 
# (c^2 = a^2 + b^2 - ab for a 60 degree triangle is the case that must hold true)
# 
# Radius of circle inscribed in a triangle = A/k,  where k = (a+b+c)/2
# Area of triangle = ab*sinC/2
# 
# So given:
# r = 2A/(a+b+c)
# 2A = ab*sin60
# 
# This combines to:
# r = a*b*sqrt(3)/(2*(a+b+c))
# Which, when taking the parameters into account, simplifies to:
# 
# r = m*n*sqrt(3)/2
# or
# r = (m-n)*(m+2n)/(2*sqrt(3))
# 
# Just loop through all m and n where m>n>0 and (m-n)%3!=0, start
# ramping up the overall multiplier, and continue as long as you
# do not exceed N. By far, the hardest part of this problem was
# making sense of the parameterizations.  In the end, though, it
# was a lot less of a headache to just generate the two types of
# primitive triangles.
#-------------------------------------------------------------------------------
from math import gcd, sqrt
from time import time
#-------------------------------------------------------------------------------
start = time()
N = 1053779
sqrt3 = sqrt(3)
sqrt32 = sqrt3/2
#-------------------------------------------------------------------------------
def f1(m,n):
    return m*n*sqrt32
#-------------------------------------------------------------------------------
def f2(m,n):
    return (m-n)*(m+2*n)/(2*sqrt3)
#-------------------------------------------------------------------------------
def euler_195(f):
    count = 0
    n = 1
    while True:
        m = n+1
        if f(m,n) > N:
            break
        while True:
            if (m-n) % 3 != 0:
                if gcd(m,n) == 1:
                    r = f(m,n)
                    k = 1
                    if r > N:
                        break
                    while True:
                        if r > N:
                            break
                        count += 1
                        k += 1
                        r = k*f(m,n)
            m += 1
        n += 1
    return count
#-------------------------------------------------------------------------------
sols = euler_195(f1)
sols += euler_195(f2)
#-------------------------------------------------------------------------------
print(f'Soulition: {sols}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 75085391
#-------------------------------------------------------------------------------
