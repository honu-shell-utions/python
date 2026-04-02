################################################################################
##Arranged probability
##Problem 100
##If a box contains twenty-one coloured discs, composed of
##fifteen blue discs and six red discs, and two discs were
##taken at random, it can be seen that the probability of
##taking two blue discs, P(BB) = (15/21)×(14/20) = 1/2.
##
##The next such arrangement, for which there is exactly 50%
##chance of taking two blue discs at random, is a box containing
##eighty-five blue discs and thirty-five red discs.
##
##By finding the first arrangement to contain over
##10^12 = 1,000,000,000,000 discs in total, determine
##the number of blue discs that the box would contain.
################################################################################
# https://www.alpertron.com.ar/QUAD.HTM
################################################################################
def nextB(b,n):
    return 3*b + 2*n - 2
################################################################################
def nextN(b,n):
    return 4*b + 3*n - 3
################################################################################
import time
start = time.time()
limit = 10**12
n = 1
b = 1

while True:
    print('Total =',n,'blue =',b)
    if n > limit:
        break
    #get the next values of b and n   
    b,n = nextB(b,n), nextN(b,n)
  
print('Solution: ',b,'Run Time: ',time.time()-start)
################################################################################
#solution: 756872327473
################################################################################
