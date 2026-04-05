##  It turns out that the “odd triplet” is simply part
##  of the Sierpinski triangle with a formula to calculate
##  the number of triplets less than a given n.
##  
##  Another way to create the Sierpinski triangle is via
##  Pascal's triangle. If you color the odd numbers in Pascal’s
##  triangle and shade out all the other spaces, you will see
##  Sierpinski’s triangle.

from math import log

def f(n):
    if n == 0:
        return 0
    if n < 5:
        return 1
    k = int(log(n, 2))
    return 3**(k-2) + 2*f(n - 2**k)
    
print('Project Euler 242 Solution =', f(10**12))    
# 997104142249036713
