# 54-poker_hands.py
#
# In the card game poker, a hand consists of five cards and are ranked, from
# lowest to highest, in the following way:
# 20-High Card: Highest value card.
# 25-One Pair: Two cards of the same value.
# 30-Two Pairs: Two different pairs.
# 35-Three of a Kind: Three cards of the same value.
# 40-Straight: All cards are consecutive values.
# 45-Flush: All cards of the same suit.
# 50-Full House: Three of a kind and a pair.
# 55-Four of a Kind: Four cards of the same value.
# 60-Straight Flush: All cards are consecutive values of same suit.
# 65-Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# 
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.
# 
# If two players have the same ranked hands then the rank made up of the highest
# value wins; for example, a pair of eights beats a pair of fives (see example 1
# below). But if two ranks tie, for example, both players have a pair of queens,
# then highest cards in each hand are compared (see example 4 below); if the
# highest cards tie then the next highest cards are compared, and so on.
# 
# Consider the following five hands dealt to two players:
# Hand		Player 1		        Player 2		        Winner
# 		5H 5C 6S 7S KD        	2C 3S 8S 8D TD
#  1	    	pair of fives        	pair of eights    	player 2
# 
#             	5D 8C 9S JS AC       	2C 5C 7D 8S QH
#  2		highest card ace	        highest card queen	player 1
# 
# 		2D 9C AS AH AC		3D 6D 7D TD QD
#  3		three aces		flush diamonds		player 2
# 
# 		4D 6S 9H QH QC		3D 6D 7H QD QS
#  4		pair of queens		pair of queens		player 1
# 		highest card nine	highest card seven
# 
# 		2H 2D 4C 4D 4S		3C 3D 3S 9S 9D
#  5		full house with		full house with		player 1
# 		three fours		three threes
# 
# The file, poker.txt, contains one-thousand random hands dealt to two players.
# Each line of the file contains ten cards (separated by a single space): the
# first five are Player 1's cards and the last five are Player 2's cards. You
# can assume that all hands are valid (no invalid characters or repeated cards),
# each player's hand is in no specific order, and in each hand there is a clear
# winner.
# 
# How many hands does Player 1 win?
################################################################################
hands01 = []
hands02 = []
################################################################################
def readTheFile():
    with open("54-poker.txt",'r') as poker_file:
        for twoHands in poker_file:
            twoHands = twoHands.split()
            hand01 = (''.join(twoHands[:5]))    #split off the first hand
            hand02 = (''.join(twoHands[5:]))    #split off the second hand
            hands01.append(processHand(hand01))
            hands02.append(processHand(hand02))
################################################################################
def processHand(fullHand):
    tempList = []

    ns = noSuites(fullHand)             #remove the suits from the hand string
    vs = valueSet(ns)                   #make the set of card values in the hand
    ss = suiteSet(fullHand)             #make the set of card suites in the hand
    mbu = makebinFlags(vs)              #make the binary string w/card 'markers'
    mbc = makebinCount(ns)              #make the binary string w/value counts
    hv = computeHandValue(mbc,mbu,ss)   #compute the hand value using mod 15

    tempList.append(fullHand)
    tempList.append(ns)
    tempList.append(vs)
    tempList.append(ss)
    tempList.append(mbu)
    tempList.append(mbc)
    tempList.append(hv)

    return(tempList)
################################################################################
def noSuites(fh):
    temp = ''
    for i in range(0,9,2):
        temp += fh[i]
    return(temp)
################################################################################
def valueSet(ns):
    temp = set()
    for i in range(len(ns)):
        temp.add(ns[i])
    temp = (''.join(list(temp)))
    return(temp)
################################################################################
def suiteSet(fh):
    temp = set()
    for i in range(1,10,2):
        temp.add(fh[i])
    temp = (''.join(list(temp)))
    return(temp)
################################################################################    
def makebinFlags(vs):
    choices = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    bin = ['0','0','0','0','0','0','0','0','0','0','0','0','0','0','0']
    for ch in vs:
        position = choices.index(ch)
        if position != -1:
            bin[position] = '1'
    return(''.join(bin))   
################################################################################
def makebinCount(ns):
    binString = ''
    values = 'AKQJT98765432'
    for ch in values:
        num = ns.count(ch)
        if num == 4:
            binString += '1111'
        elif num == 3:
            binString += '0111'
        elif num == 2:
            binString += '0011'
        elif num == 1:
            binString += '0001'
        else:
            binString += '0000'
    binString += '00000000'
    return(binString)   
################################################################################
def isStraight(mbu):
    if mbu.find('11111') != -1 or mbu == '100000000111100':
        return(True)
    else:
        return(False)
################################################################################
def isFlush(ss):
    return(len(ss) == 1)   
################################################################################
def isRoyalFlush(mbu):
    return(mbu == '111110000000000')
################################################################################
def computeHandValue(mbc,mbu,ss):
    decimalValue = from_binary(mbc)
    temp = decimalValue % 15
    if temp == 1:
        #return('Four Of A Kind')
        return(55)
    elif temp == 10:
        #return('Full House')
        return(50)
    elif temp == 9:
        #return('Three Of A Kind')
        return(35)
    elif temp == 7:
        #return('Two Pairs')
        return(30)
    elif temp == 6:
        #return('One Pair')
        return(25)
    elif temp == 5:
        if isStraight(mbu) and isFlush(ss) and isRoyalFlush(mbu):
            #return('Royal Flush')
            return(65)
        elif isStraight(mbu) and isFlush(ss):
            #return('Straight Flush')
            return(60)
        elif isStraight(mbu):
            #return('Straight')
            return(40)
        elif isFlush(ss):
            #return('Flush')
            return(45)
        else:
            #return('High Card')
            return(20)
    else:
        return(0)
    
################################################################################
def processTie(first,second):
    if first[6] == 20:
        if first[4] > second[4]:
            return(1)
        elif first[4] < second[4]:
            return(2)
        else:
            return(0)

    elif first[6] == 25:
        pos1 = first[5].find('11')
        pos2 = second[5].find('11')
        if pos1 < pos2:
            return(1)
        else:
            return(2)
    else:
        return(0)   
################################################################################
def to_binary(d):
    b = ''
    while True:
        if d == 0:
            break
        elif (d % 2) == 0:
            d = d // 2
            b = '0' + b
        else:
            d = d // 2
            b = '1' + b
    return b
################################################################################
def from_binary(binary):
    binary = binary[::-1]
    d = 0
    power = 0 
    for i in binary:
        d += int(i) * (2 ** power)
        power +=1 
    return d 

################################################################################
readTheFile()
firstWins = 0
secondWins = 0
ties = 0
tieHands01 = []
tieHands02 = []

for i in range(len(hands01)):
    if hands01[i][6] > hands02[i][6]:
        firstWins += 1
    elif hands01[i][6] < hands02[i][6]:
        secondWins += 1
    else:
        tieHands01.append(hands01[i])
        tieHands02.append(hands02[i])

for i in range(len(tieHands01)):
    result = processTie(tieHands01[i],tieHands02[i])
    if result == 1:
        firstWins += 1
    elif result == 2:
        secondWins += 1
    else:
        ties += 1

print(firstWins,secondWins,ties)
################################################################################
#solution: 376
################################################################################


