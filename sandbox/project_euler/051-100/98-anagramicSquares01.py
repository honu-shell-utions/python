################################################################################
##Anagramic squares
##Problem 98
##By replacing each of the letters in the word
##CARE with 1, 2, 9, and 6 respectively, we form
##a square number: 1296 = 36^2. What is remarkable
##is that, by using the same digital substitutions,
##the anagram, RACE, also forms a square number: 9216 = 96^2.
##We shall call CARE (and RACE) a square anagram word pair
##and specify further that leading zeroes are not permitted,
##neither may a different letter have the same digital value
##as another letter.
##
##Using words.txt (right click and 'Save Link/Target As...'),
##a 16K text file containing nearly two-thousand common English
##words, find all the square anagram word pairs (a palindromic
##word is NOT considered to be an anagram of itself).
##
##What is the largest square number formed by any member of such a pair?
##
##NOTE: All anagrams formed must be contained in the given text file.
################################################################################
def analyzePair(pair):
    pair1NumList = []
    pair2NumList = []

    for sq in squaresNoRepeats:
        #make sure we have a square of the same length as the word
        if len(str(sq)) != len(pair[0]):
            continue

        #empty the list
        pair1NumList.clear()

        #create the first num list (these are strings)
        sqStr = str(sq)
        for nStr in sqStr:
            pair1NumList.append(nStr)

        #make a copy
        pair2NumList = pair1NumList.copy()
        
        #update the nums in the second list 
        for i in range(len(pair[0])):
            ch = pair[0][i]
            strNum = pair1NumList[i]
            location = pair[1].index(ch)
            pair2NumList[location] = strNum

        #make a couple of strings from the two number lists
        t1 = ''
        t2 = ''
        
        for i in range(len(pair[0])):
            t1 += pair1NumList[i]
            t2 += pair2NumList[i]

        #see if the second number is in the squares list and doesn't begin with 0
        if int(t2) in squaresNoRepeats and t2[0] != '0':
            return True,int(t1),int(t2)

    return False,1,1
        
################################################################################
def noNumRepeats(num):
    word = str(num)
    for ch in word:
        if word.count(ch) > 1:
            return False
    return True
################################################################################
def makeSquareList():
    #create a list of squares from 1 digit long to 9 digits long
    for i in range(1,32000):
        temp = i**2
        if noNumRepeats(temp):
            squaresNoRepeats.append(temp)
################################################################################
def loadWordList():
    import csv
    wList = []
    with open('98-Words.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for word in row:
                wList.append(word)
    return wList
################################################################################
import time
start = time.time()

#load the word list from the file
words = loadWordList()

#to hold each word and the sorted version of that word
wordsAndSorted = []

#to hold the pairs of anagrams
anagramPairs = []

#to hold a list of square numbers
squaresNoRepeats = []
makeSquareList()

#to hold the solution
MAX = 0

#make a tuple from the word and the sorted word and append to new list
for w in words:
    wordsAndSorted.append([w,''.join(sorted(w))])

#sort on the second value in each tuple, these are the sorted words
wordsAndSorted.sort(key=lambda x:x[1])    

#make the anagram pair list
for i in range(1,len(wordsAndSorted)):
    if wordsAndSorted[i][1] in wordsAndSorted[i-1]:
        anagramPairs.append([wordsAndSorted[i-1][0],wordsAndSorted[i][0]])

#process each pair
for ap in anagramPairs:
    (success,result1,result2) = analyzePair(ap)
    if success:
        temp = max(result1,result2)
        print(ap,result1,result2)
        if temp > MAX:
            MAX = temp

print('The solution: ',MAX,'Run Time: ',time.time()-start)
################################################################################
#solution: 18769
################################################################################
