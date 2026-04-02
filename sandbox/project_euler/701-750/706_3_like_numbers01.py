#  -----------------------------------------------------------------------------
#  3-Like Numbers
#  Problem 706
#  https://projecteuler.net/problem=706
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def make_subs(n):
    str_n = str(n)
    subs = [str_n[i: j] for i in range(len(str_n)) for j in range(i + 1, len(str_n) + 1)]
    return subs
#  -----------------------------------------------------------------------------
def f(n):
    counter = 0
    subs = make_subs(n)
    for s in subs:
        if int(s) % 3 == 0:
            counter += 1
    if counter % 3 == 0:
        return True
    else:
        return False
#  -----------------------------------------------------------------------------
def F(d):
    counter = 0
    for n in range(10**(d-1),10**d):
        if f(n):
            counter += 1
            counter = counter % (10**9 + 7)
    return counter
#  -----------------------------------------------------------------------------
for n in [2,6]:
    start = time()
    print(f'Solution for n = {n:2} is {F(n):6}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 884837055
#  -----------------------------------------------------------------------------
