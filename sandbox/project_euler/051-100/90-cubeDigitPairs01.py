################################################################################
# 90-cubeDigitPairs.py
# 
# Each of the six faces on a cube has a different digit (0 to 9) written on
# it; the same is done to a second cube. By placing the two cubes side-by-side
# in different positions we can form a variety of 2-digit numbers.
#
# For example, the square number 64 could be formed:  6 4  picture: a box with
#  a six, another box with a four.
#
# In fact, by carefully choosing the digits on both cubes it is possible to
# display all of the square numbers below one-hundred:
# 01, 04, 09, 16, 25, 36, 49, 64, and 81.
#
# For example, one way this can be achieved is by placing {0, 5, 6, 7, 8, 9}
# on one cube and {1, 2, 3, 4, 8, 9} on the other cube.
#
# However, for this problem we shall allow the 6 or 9 to be turned upside-down
# so that an arrangement like {0, 5, 6, 7, 8, 9} and {1, 2, 3, 4, 6, 7} allows
# for all nine square numbers to be displayed; otherwise it would be
# impossible to obtain 09.
#
# In determining a distinct arrangement we are interested in the digits on
# each cube, not the order.
# {1, 2, 3, 4, 5, 6} is equivalent to {3, 6, 4, 1, 2, 5}
# {1, 2, 3, 4, 5, 6} is distinct from {1, 2, 3, 4, 5, 9}
#
# But because we are allowing 6 and 9 to be reversed, the two distinct sets
# in the last example both represent the extended set {1, 2, 3, 4, 5, 6, 9}
# for the purpose of forming 2-digit numbers.
#
# How many distinct arrangements of the two cubes allow for all of the square
# numbers to be displayed?
################################################################################
from itertools import combinations
import time
################################################################################
def makeCombos():
    combos = combinations([0,1,2,3,4,5,6,7,8,6],6)
    return list(combos)
################################################################################
def getDie01Combo(idx):
        return die01Combos[idx]   
################################################################################
def getDie02Combo(idx):
        return die02Combos[idx]   
################################################################################
def testThisRoll(d1, d2):
    size = len(theSquares)
    gottaHit = [False]*size   
    for pip1 in d1:
        for pip2 in d2:
            target = str(pip1) + str(pip2)
            if target in theSquares:
                idx = theSquares.index(target)
                gottaHit[idx] = True
            target = str(pip2) + str(pip1)
            if target in theSquares:
                idx = theSquares.index(target)
                gottaHit[idx] = True
        
    if False in gottaHit:
        return False
    else:
        return True
                
################################################################################
start = time.time()
die01Combos = list(makeCombos())
die02Combos = list(makeCombos())
theSquares = ['01','04','06','16','25','36','46','81']
count = 0
for i in range(len(die01Combos)):
    for j in range(len(die01Combos)):
        die01 = getDie01Combo(i)
        die02 = getDie02Combo(j)
        if testThisRoll(die01,die02):
            count += 1

print('Solution:',count//2,'Run Time:',time.time()-start)

################################################################################
#solution: 1217
################################################################################
