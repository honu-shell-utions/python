##------------------------------------------------------------------------------
##Exploring the number of different ways a number can be
##expressed as a sum of powers of 2
##
##Problem 169
##Define f(0)=1 and f(n) to be the number of different ways
##n can be expressed as a sum of integer powers of 2 using
##each power no more than twice.
##
##For example, f(10)=5 since there are five different ways
##to express 10:
##
##1 + 1 + 8
##1 + 1 + 4 + 4
##1 + 1 + 2 + 2 + 4
##2 + 4 + 4
##2 + 8
##
##What is f(10^25)?
##------------------------------------------------------------------------------
F = {}
F[0] = F[1] = 1
def f(n):
    if n in F:
        return F[n]
    if (n % 2):
        val = f(n//2)
    else:
        val = f(n//2) + f(n//2-1)
    F[n] = val
    return val

print(f(10**25))
#print(f(10))
##------------------------------------------------------------------------------
##solution: 178653872807
##------------------------------------------------------------------------------
