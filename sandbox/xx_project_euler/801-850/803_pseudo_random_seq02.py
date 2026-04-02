## -----------------------------------------------------------------------------
## Pseudorandom sequence
## Problem 803
## https://projecteuler.net/problem=803
## -----------------------------------------------------------------------------
def direct2(dist,start=0):
    a=25214903917
    master=pow(a,dist+1,((a-1)*2**48))
    return 11+((a*11*(master-1))//(a-1))%2**48
## -----------------------------------------------------------------------------
def find_offset(goal):
    found=False
    exponent=1
    distance=0
    seed=0
    while not found:
        while seed%2**exponent == goal%2**exponent and exponent<50:
            exponent+=1
        distance+=2**(exponent-1)
        seed=direct2(distance)
        
        if seed==goal:
            found=True
    return distance
## -----------------------------------------------------------------------------
P = 144933752257087
L = 160163661474491
print('\n Calculating offset between Puzzle and Lucky (forwards)')
print('PuzzleOne offset from start is...')
p1_offset=find_offset(P)
print(p1_offset)
print('LuckyText offset from start is...')
lucky_offset=find_offset(L)
print(lucky_offset)
print('PuzzleOne to  LuckyText is :')
print(lucky_offset-p1_offset)
## -----------------------------------------------------------------------------
## solution: 9300900470636
## -----------------------------------------------------------------------------
