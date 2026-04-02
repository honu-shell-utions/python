################################################################################
##Coded triangle numbers 
##Problem 42
##The nth term of the sequence of triangle numbers is
##given by, tn = ½n(n+1); so the first ten triangle numbers are:
##
##1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
##
##By converting each letter in a word to a number
##corresponding to its alphabetical position and
##adding these values we form a word value.
##For example, the word value for SKY is 19 + 11 + 25 = 55 = t10.
##If the word value is a triangle number then we shall call
##the word a triangle word.
##
##Using words.txt (right click and 'Save Link/Target As...'),
##a 16K text file containing nearly two-thousand common
##English words, how many are triangle words?
################################################################################
def loadSetOfTriangleNumbers(size):
    triSet = set()
    for i in range(1,size+1):
        triSet.add(int(.5*i*(i+1)))
    return(triSet)
################################################################################
def init_data():
    f_in = open('42-words.txt', 'r')
    all_em = f_in.read()
    s = all_em.replace('"','').strip()
    lst = s.split(',')
    return lst
################################################################################
def isTriangleNumber(testMe,setOfTris):
    if testMe in setOfTris:
        return True
    else:
        return False
################################################################################
count = 0
setOfTris = loadSetOfTriangleNumbers(1000)
wordList = init_data()
for i in range(len(wordList)):
    currentWord = wordList[i]
    wordValue = 0
    for j in range(len(currentWord)):
        currentLetter = currentWord[j]
        wordValue += ord(currentLetter)-64
    if isTriangleNumber(wordValue,setOfTris):
        count += 1
        print(wordList[i],wordValue)
print(count)
################################################################################
#solution: 162
################################################################################
