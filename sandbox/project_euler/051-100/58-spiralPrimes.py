################################################################################
##Spiral primes
##
##Problem 58
##Starting with 1 and spiralling anticlockwise in the following way,
##a square spiral with side length 7 is formed.
##
##  37 36 35 34 33 32 31
##  38 17 16 15 14 13 30
##  39 18  5  4  3 12 29
##  40 19  6  1  2 11 28
##  41 20  7  8  9 10 27
##  42 21 22 23 24 25 26
##  43 44 45 46 47 48 49
##
##It is interesting to note that the odd squares lie along the
##bottom right diagonal, but what is more interesting is that 8
##out of the 13 numbers lying along both diagonals are prime;
##that is, a ratio of 8/13 ≈ 62%.
##
##If one complete new layer is wrapped around the spiral above,
##a square spiral with side length 9 will be formed. If this
##process is continued, what is the side length of the square
##spiral for which the ratio of primes along both diagonals
##first falls below 10%?
##
##
##  37(-3,+3) 36(-2,+3) 35(-1,+3) 34(-0,+3) 33(+1,+3) 32(+2,+3) 31(+3,+3)
##  38(-3,+2) 17(-2,+2) 16(-1,+2) 15(-0,+2) 14(+1,+2) 13(+2,+2) 30(+3,+2)
##  39(-3,+1) 18(-2,+1)  5(-1,+1)  4(-0,+1)  3(+1,+1) 12(+2,+1) 29(+3,+1)
##  40(-3,+0) 19(-2,+0)  6(-1,+0)  1(-0,+0)  2(+1,+0) 11(+2,+0) 28(+3,+0)
##  41(-3,-1) 20(-2,-1)  7(-1,-1)  8(-0,-1)  9(+1,-1) 10(+2,-1) 27(+3,-1)
##  42(-3,-2) 21(-2,-2) 22(-1,-2) 23(-0,-2) 24(+1,-2) 25(+2,-2) 26(+3,-2)
##  43(-3,-3) 44(-2,-3) 45(-1,-3) 46(-0,-3) 47(+1,-3) 48(+2,-3) 49(+3,-3)
################################################################################
import math
import sympy as sy
################################################################################
# prints all numbers on the diagonals of a sq*sq spiral
sq = 26_001
while True:
    primes = 0
    d = 1
    while 2*d - 1 < sq:
        temp = 4*d*d - 4*d +1
        if sy.isprime(temp): primes += 1
        #print(temp,sy.isprime(temp))
        temp = 4*d*d - 4*d +1 + 1*2*d
        if sy.isprime(temp): primes += 1
        #print(temp,sy.isprime(temp))
        temp = 4*d*d - 4*d +1 + 2*2*d
        if sy.isprime(temp): primes += 1
        #print(temp,sy.isprime(temp))
        temp = 4*d*d - 4*d +1 + 3*2*d
        if sy.isprime(temp): primes += 1
        #print(temp,sy.isprime(temp))
        d += 1
    if sy.isprime(sq*sq): primes += 1
    
    #print(sq*sq,sy.isprime(sq*sq))
    result = primes/(sq*2 - 1)
    print(sq,primes,result)
    if result < .10: break
    sq += 2
################################################################################
#solution: 26241
################################################################################
