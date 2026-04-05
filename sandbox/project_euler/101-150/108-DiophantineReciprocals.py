################################################################################
##Diophantine reciprocals I
##Problem 108
##In the following equation x, y, and z are positive integers.
## 
## 1/x + 1/y = 1/z
##
##For z = 4 there are exactly three distinct solutions:
## 
## 1/5 + 1/20 = 1/4
## 1/6 + 1/12 = 1/4
## 1/8 + 1/8  = 1/4
## 
##What is the least value of z for which the number of
##distinct solutions exceeds one-thousand?
##
##NOTE: This problem is an easier version of Problem 110;
##it is strongly advised that you solve this one first.
################################################################################
from sympy import divisors
from time import time
# https://keyzero.wordpress.com/2010/06/05/project-euler-problem-108/
################################################################################
def test_n(n):
    solutions = 0
    divisors_of_n = divisors(n**2)
    for d in divisors_of_n:
        if d+n <= 2*n:
            solutions += 1
            #print(d,d+n,n+n**2//d)
    return solutions
################################################################################
start = time()
n = 4
while True:
    solutions = test_n(n)
    if solutions >= 1_000:
        print('Solution:',n,'Run Time:',time()-start)
        break
    else:
        n += 1
################################################################################
#solution: 
################################################################################
