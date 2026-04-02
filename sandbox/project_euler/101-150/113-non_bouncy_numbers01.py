################################################################################
##Non-bouncy numbers 
##Problem 113
##Working from left-to-right if no digit is exceeded by the digit
##to its left it is called an increasing number; for example, 134468.
##
##Similarly if no digit is exceeded by the digit to its right it
##is called a decreasing number; for example, 66420.
##
##We shall call a positive integer that is neither increasing
##nor decreasing a "bouncy" number; for example, 155349.
##
##As n increases, the proportion of bouncy numbers below n
##increases such that there are only 12951 numbers below
##one-million that are not bouncy and only 277032 non-bouncy
##numbers below 10^10.
##
##How many numbers below a googol (10^100) are not bouncy?
################################################################################
from time import time
from math import factorial
################################################################################ 
def nCr(n,r):
    top = factorial(n)
    bottom = factorial(n-r)*factorial(r)
    return int(top/bottom)
################################################################################  
def pe_113(n):
    increasing = nCr(n+9,9)-1
    decreasing = nCr(n+10,10)-1
    return increasing+decreasing-10*n
################################################################################  
start = time()
print('The Solution:',pe_113(100),'Run Time:',time()-start)
################################################################################
#solution: 51161058134250
################################################################################
