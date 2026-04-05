from math import log
GAMMA = 0.577215664901532
# https://en.wikipedia.org/wiki/Euler%27s_constant

def L(n):
    return int(log(n,2))

def B(n):
    return 1+((n+1)*L(n)-2*(2**L(n)-1))/n 

def R(n):
    h = log(n)+GAMMA
    return (-3*n+2*(n+1)*h)/n

n = 10**10
print(round(R(n)-B(n),8))
#  solution: 11.92412011
