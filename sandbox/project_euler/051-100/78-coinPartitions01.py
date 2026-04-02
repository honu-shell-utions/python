################################################################################
##Coin partitions 
##Problem 78
##Let p(n) represent the number of different ways in
##which n coins can be separated into piles. For example,
##five coins can be separated into piles in exactly seven
##different ways, so p(5)=7.
##
##OOOOO
##OOOO   O
##OOO   OO
##OOO   O   O
##OO   OO   O
##OO   O   O   O
##O   O   O   O   O
##Find the least value of n for which p(n) is divisible by one million.
################################################################################
def getWays(n):
    n -= 1
    if n % 2 == 0:
        m = n // 2
        return(m*(3*m + 1)//2)
    else:
        m = (n+1)//2
        return(m*(3*m-1)//2)
################################################################################
num = 0
while True:
    test = getWays(num)
    print(num,test)
    if num == 20: break
##    if test // 1_000_000 == test / 1_000_000:
##        break
    num += 1

print(num)
################################################################################
#solution:
################################################################################
