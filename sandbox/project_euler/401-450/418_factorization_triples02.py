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
#  For example, f(165) = 19, f(100100) = 142 and f(20!) = 4034872.
#  Find f(43!).
#  https://projecteuler.net/problem=418
#  -----------------------------------------------------------------------------
from math import factorial
from time import time
#  -----------------------------------------------------------------------------
def get_divs(N,left,right):
    divs = set()
    for i in range(left,right+1):
        if N % i == 0:
            divs.add(i)
            divs.add(N//i)
    return sorted(list(divs))
#  -----------------------------------------------------------------------------
def get_trips(N,left,right):
    divs = get_divs(N,left,right)
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
            b = N/(a1[0]*c1[2])
            if int(b) == b:
                temp = sorted([a1[0],int(b),c1[2]])
                if not temp in abc:
                    abc.append(temp)
    return abc
#  -----------------------------------------------------------------------------
def euler_418(n,epsilon):
    start = time()
    N = factorial(n)
    cr_N = int(N**(1/3))
    left = int(cr_N*epsilon)
    right = int(cr_N/epsilon)
    min_q = 10**3
    min_trip = [0,0,0]
    min_sum = 10**10
    for t in get_trips(N,left,right):
        if t[2]/t[0] < min_q:
            min_q = t[2]/t[0]
            min_sum = sum(t)
            min_trip = t
    print('\n\nProject Euler 418')
    print(f'For n = factorial({n}), Smallest triple: {min_trip}')
    print(f'Smallest c/a: {min_q}, Sum: {min_sum}')
    print(f'Run-Time: {time()-start}')
#  ----------------------------------------------------------------------------- 
euler_418(20,.999)
euler_418(43,.9999)
#  -----------------------------------------------------------------------------    
#  for n = factorial(20), smallest triple = [1343680, 1344000, 1347192], sum = 4034872
#  for n = factorial(43), (392386762388275200, 392388272221065120, 392388530688000000)
#  -----------------------------------------------------------------------------
#  solution: 1177163565297340320
#  -----------------------------------------------------------------------------
