################################################################################
##  Counting Digits
##  Problem 156
##  Starting from zero the natural numbers are written down in base 10 like this: 
##  0 1 2 3 4 5 6 7 8 9 10 11 12....
##  
##  Consider the digit d=1. After we write down each number n, we will update the
##  number of ones that have occurred and call this number f(n,1). The first values
##  for f(n,1), then, are as follows:
##  
##      n	f(n,1)
##      0	0
##      1	1
##      2	1
##      3	1
##      4	1
##      5	1
##      6	1
##      7	1
##      8	1
##      9	1
##      10	2
##      11	4
##      12	5
##      
##  Note that f(n,1) never equals 3. 
##  So the first two solutions of the equation f(n,1)=n are n=0 and n=1.
##  The next solution is n = 199981.
##  
##  In the same manner the function f(n,d) gives the total number of digits
##  d that have been written down after the number n has been written. 
##  In fact, for every digit d ≠ 0, 0 is the first solution of the equation
##  f(n,d)=n.
##  
##  Let s(d) be the sum of all the solutions for which f(n,d)=n. 
##  You are given that s(1)=22786974071.
##  
##  Find ∑ s(d) for 1 ≤ d ≤ 9.
##  
##  Note: if, for some n, f(n,d)=n for more than one value of d this value of
##  n is counted again for every value of d for which f(n,d)=n.
################################################################################
def f(n, d):
    tot, j, m, = 0, 0, n
    while m > 0:
        r = m % 10
        tot += r * j * 10**(j-1)
        if r > d:
            tot += 10**j
        elif r == d:
            tot += 1 + n % 10**j
        j += 1
        m //= 10
    return int(tot)

def p156(L):
    xsum = 0
    for d in range(1, 10):
        x = 0
        while x < L:
            t = f(x, d) - x
            if t == 0:
                print(d, x)
                xsum += x
            x += max(1, abs(t) // 10)
    return xsum

print(p156(10**11))
################################################################################
#solution: 21295121502550
################################################################################
