#-------------------------------------------------------------------------------
##Fractions involving the number of different ways a number can
##be expressed as a sum of powers of 2
##
##Problem 175
##Define f(0)=1 and f(n) to be the number of ways to write n as
##a sum of powers of 2 where no power occurs more than twice. 
##
##For example, f(10)=5 since there are five different ways to express 10:
##10 = 8+2 = 8+1+1 = 4+4+2 = 4+2+2+1+1 = 4+4+1+1
##
##It can be shown that for every fraction p/q (p>0, q>0) there exists
##at least one integer n such that f(n)/f(n-1)=p/q.
##
##For instance, the smallest n for which f(n)/f(n-1)=13/17 is 241.
##The binary expansion of 241 is 11110001.
##
##Reading this binary number from the most significant bit to the
##least significant bit there are 4 one's, 3 zeroes and 1 one. We
##shall call the string 4,3,1 the Shortened Binary Expansion of 241.
##
##Find the Shortened Binary Expansion of the smallest n for which
##f(n)/f(n-1)=123,456,789/987,654,321.
##
##Give your answer as comma separated integers, without any whitespaces.
#-------------------------------------------------------------------------------
from time import time
from math import gcd
from fractions import Fraction
#-------------------------------------------------------------------------------
def cont_fraction(frac):
    c_list = [int(frac)]
    frac -= int(frac)
    while frac:
        frac = 1 / frac
        c_list.append(int(frac))
        frac -= int(frac)
    return c_list[1:]
#-------------------------------------------------------------------------------
def sbe(c_list):
    if len(c_list) % 2 == 0:
        c_list[-1] -= 1
        c_list += [1]
    c_list.reverse()
    return c_list
#-------------------------------------------------------------------------------
start = time()
top = 123456789
bottom = 987654321
g = gcd(top,bottom)
top //= g
bottom //= g
cf = cont_fraction(Fraction(top,bottom))

print(f'The solution: {sbe(cf)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#solution: 1,13717420,8
#-------------------------------------------------------------------------------
