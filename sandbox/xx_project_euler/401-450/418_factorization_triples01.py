#  -----------------------------------------------------------------------------
#  Factorisation triples
#  Problem 418
#  Let n be a positive integer. An integer triple (a, b, c)
#  is called a factorisation triple of n if:
#  
#  1 ≤ a ≤ b ≤ c
#  a·b·c = n
#  
#  Define f(n) to be a + b + c for the factorisation triple
#  (a, b, c) of n which minimises c / a.
#  One can show that this triple is unique.
#  
#  For example, f(165) = 19, f(100100) = 142 and f(20!) = 4034872.
#  
#  Find f(43!).
#  
#  https://projecteuler.net/problem=418
#  -----------------------------------------------------------------------------
from sympy import divisors
#  -----------------------------------------------------------------------------
def get_trips(n):
    divs = divisors(n)
    a = []
    c = []
    abc = []
    for ac in divs:
        a.append((ac,0,0))
        c.append((0,0,ac))     
    for a1 in a:
        for c1 in c:
            if abs(a1[0] - c1[2]) < 2:
                continue
            b = n/(a1[0]*c1[2])
            if int(b) == b:
                temp = sorted([a1[0],int(b),c1[2]])
                if not temp in abc:
                    abc.append(temp)
    return abc
#  -----------------------------------------------------------------------------
for n in [165,100100]:                
    min_c_over_a = 10**3
    min_trip = [0,0,0]
    for t in get_trips(n):
        if t[2]/t[0] < min_c_over_a:
            min_c_over_a = t[2]/t[0]
            min_trip = t
    print(f'for n = {n:8}, triple = {min_trip}, sum = {sum(min_trip)}, c/a = {min_c_over_a}')
#  -----------------------------------------------------------------------------    
#  For example, f(165) = 19, f(100100) = 142 and f(20!) = 4034872.
#  -----------------------------------------------------------------------------
#  solution: 1177163565297340320
#  -----------------------------------------------------------------------------
