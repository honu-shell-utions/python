#-------------------------------------------------------------------------------
##Investigating the behaviour of a recursively defined sequence
##Problem 197
##Given is the function f(x) = ⌊2^(30.403243784-x^2)⌋ × 10^(-9)
##( ⌊ ⌋ is the floor-function), the sequence un is defined by
##u_sub(0) = -1 and u_sub(n+1) = f(u_sub(n)).
##
##Find u_sub(n) + u_sub(n+1) for n = 10^12.
##Give your answer with 9 digits after the decimal point.
#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
def f(x):
    return int(2 ** (30.403243784 - x*x)) * 1e-9
#-------------------------------------------------------------------------------    
def u(n):
    if n == 0:
        return -1
    else:
        return f(u(n-1))
#-------------------------------------------------------------------------------
start = time()
i = 0
while abs(u(i) - u(i+2)) > 1e-10:
    i += 1

print(f'Solution: {u(i) + u(i+1)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 1.710637717
#-------------------------------------------------------------------------------
