################################################################################
## Special isosceles triangles
## Problem 138
## Consider the isosceles triangle with base length, b = 16, and legs, L = 17.
##
## By using the Pythagorean theorem it can be seen that the height of the triangle, 
## is 15, which is one less than the base length. With b = 272 and L = 305, we get 
## h = 273, which is one more than the base length, and this is the second smallest
## isosceles triangle with the property that h = b ± 1.
##
## Find ∑ L for the twelve smallest isosceles triangles for which h = b ± 1 and 
## b, L are positive integers.
################################################################################
from math import sqrt
from operator import itemgetter
################################################################################
limit = 10**10
def gen_triples(n):
    triples = []
    for x in range(1,limit):
        L1 = sqrt(5*x**2 + 4*x + 1)
        L2 = sqrt(5*x**2 - 4*x + 1)
        if L1 % 1 == 0:
            triples.append([2*x,int(L1)])
        if L2 % 1 == 0:
            triples.append([2*x,int(L2)])
        if len(triples) == n:
            return triples
        
    return triples
################################################################################
total = 0
triples = gen_triples(12)
#triples.sort(key=itemgetter(1))
for t in triples:
    print(t)
    total += t[1]

print(total)
################################################################################
#this code doesn't work
#solution: 1118049290473932
################################################################################
