################################################################################
##Monopoly odds
##Problem 84
##In the game, Monopoly, the standard board is set up in the following way:
##
##A player starts on the GO square and adds the scores on two 6-sided dice
##to determine the number of squares they advance in a clockwise direction.
##Without any further rules we would expect to visit each square with equal
##probability: 2.5%. However, landing on G2J (Go To Jail), CC (community chest),
##and CH (chance) changes this distribution.
##
##In addition to G2J, and one card from each of CC and CH, that orders the
##player to go directly to jail, if a player topOfStacks three consecutive doubles,
##they do not advance the result of their 3rd topOfStack. Instead they proceed directly
##to jail.
##
##At the beginning of the game, the CC and CH cards are shuffled. When a player
##lands on CC or CH they take a card from the top of the respective pile and,
##after following the instructions, it is returned to the bottom of the pile.
##There are sixteen cards in each pile, but for the purpose of this problem we
##are only concerned with cards that order a movement; any instruction not concerned
##with movement will be ignored and the player will remain on the CC/CH square.
##
##Community Chest (2/16 cards):
##Advance to GO
##Go to JAIL
##
##Chance (10/16 cards):
##Advance to GO
##Go to JAIL
##Go to C1
##Go to E3
##Go to H2
##Go to R1
##Go to next R (railway company)
##Go to next R
##Go to next U (utility company)
##Go back 3 squares.
##
##The heart of this problem concerns the likelihood of visiting a particular square.
##That is, the probability of finishing at that square after a topOfStack. For this reason
##it should be clear that, with the exception of G2J for which the probability of
##finishing on it is zero, the CH squares will have the lowest probabilities,
##as 5/8 request a movement to another square, and it is the final square that the
##player finishes at on each topOfStack that we are interested in. We shall make no
##distinction between "Just Visiting" and being sent to JAIL, and we shall also
##ignore the rule about requiring a double to "get out of jail", assuming that
##they pay to get out on their next turn.
##
##By starting at GO and numbering the squares sequentially from 00 to 39 we can
##concatenate these two-digit numbers to produce strings that correspond with
##sets of squares.
##
##Statistically it can be shown that the three most popular squares, in order,
##are JAIL (6.24%) = Square 10, E3 (3.18%) = Square 24, and GO (3.09%) = Square 00.
##So these three most popular squares can be listed with the six-digit modal string:
##102400.
##
##If, instead of using two 6-sided dice, two 4-sided dice are used, find the
##six-digit modal string.
################################################################################
import random
from operator import itemgetter
from collections import deque
################################################################################
theSquares = ['GO','A1','CC1','A2','T1','R1','B1','CH1','B2','B3','JAIL',\
              'C1','U1','C2','C3','R2','D1','CC2','D2','D3','FP',\
              'E1','CH2','E2','E3','R3','F1','F2','U2','F3','G2J',\
              'G1','G2','CC3','G3','R4','CH3','H1','T2','H2']

theIndices = ['00','01','02','03','04','05','06','07','08','09','10',\
              '11','12','13','14','15','16','17','18','19','20',\
              '21','22','23','24','25','26','27','28','29','30',\
              '31','32','33','34','35','36','37','38','39']

CC = [2,17,33]
CCList = deque([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
CH = [7,22,36]
CHList = deque([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16])
UT = [12,28]
RR = [5,15,25]
countDoubles = 0

squareHits = [0]*len(theSquares)
squarePercents = [0]*len(theSquares)
################################################################################
def newLocation(currentLocation):
    global countDoubles
    die01 = random.randint(1,4)
    die02 = random.randint(1,4)
    toss = die01 + die02
    if die01 == die02:
        countDoubles += 1
    else:
        countDoubles = 0
        
    if countDoubles == 3:
        countDoubles = 0
        return 10
    else:
        return (currentLocation + toss) % len(theSquares)
################################################################################
def nextCC(currentLocation):
    topOfStack = CCList[0]
    CCList.rotate(1)
    #advance to GO
    if topOfStack == 1:
        return 0
    #goto JAIL
    if topOfStack == 2:
        return 10
    else:
        return currentLocation
################################################################################
def nextCH(currentLocation):
    topOfStack = CHList[0]
    CHList.rotate(1)
    #goto GO
    if topOfStack == 1:
        return 0
    #goto JAIL
    if topOfStack == 2:
        return 10
    #goto C1
    if topOfStack == 3:
        return 11
    #goto E3
    if topOfStack == 4:
        return 24    
    #goto H2
    if topOfStack == 5:
        return 39
    #goto R1
    if topOfStack == 6:
        return 5
    #goto next R
    if topOfStack == 7 or topOfStack == 8:
        return nextR(currentLocation)
    #goto next U
    if topOfStack == 9:
        return nextU(currentLocation)
    #go back 3 positions
    if topOfStack == 10:
        if currentLocation >= 3:
            return currentLocation - 3
        else:
            return len(theSquares) - 3
        
    return currentLocation
################################################################################
def nextU(position):
    for ut in UT:
        if position < ut:
            return ut
    return 2
################################################################################
def nextR(position):
    for rr in RR:
        if position < rr:
            return rr
    return 5
################################################################################
random.shuffle(CHList)
random.shuffle(CCList)

numRolls = 3_000_000
location = 0

for i in range(numRolls):
    #toss the dice
    location = newLocation(location)
    if location in CC:
        location = nextCC(location)
    if location in CH:
        location = nextCH(location)
    if location == 30:
        location = 10
    squareHits[location] += 1

total = sum(squareHits)
for i in range(len(squareHits)):
    squarePercents[i] = round(100*squareHits[i]/total,2)
    
targets = []
for i in range(len(squareHits)):
    targets.append([theIndices[i],theSquares[i],squarePercents[i]])

temp = sorted(targets,key=itemgetter(2),reverse=True)
print(temp[0][0]+temp[1][0]+temp[2][0])

################################################################################
#solution: 101524
################################################################################
