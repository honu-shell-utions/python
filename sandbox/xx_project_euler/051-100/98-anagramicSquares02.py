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
class Word:
  def __init__(self,currentWord):
    self.word = currentWord
    self.sorted = sorted(currentWord)
    self.sortedJoin = ''.join(sorted(currentWord))
    self.length = len(currentWord)
    temp = set()
    for c in self.word:
      temp.add(c)
    if len(temp) == len(self.word):
      self.duplicates = False
    else:
      self.duplicates = True   

  def printMe(self):
    print(self.word,self.sorted,self.sortedJoin,self.length)
################################################################################
class Square:
  def __init__(self,sq):
    self.num = sq
    self.str = str(sq)
    self.length = len(self.str)
    temp = set()
    for c in self.str:
      temp.add(c)
    if len(temp) == len(self.str):
      self.duplicates = False
    else:
      self.duplicates = True   

  def printMe(self):
    print(self.num)
################################################################################
def makeSquareList():
  from math import isqrt
  sqList = []
  #create a list of squares from 1 digit long to 9 digits long
  for i in range(1,isqrt(999999999)+1):
      temp = i**2
      temp = Square(temp)
      if temp.duplicates == False:
        sqList.append(temp)
  return sqList
################################################################################
def loadWordList():
    import csv
    wList = []
    with open('98-Words.txt', 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            for word in row:
              temp = Word(word)
              if temp.duplicates == False:
                wList.append(temp)
    return wList
################################################################################
def isInList(test):
  for sq in squares:
    if test.num == sq.num:
      return True
  return False
################################################################################
def analyzePair(pair):
    pair1NumList = []
    pair2NumList = []

    for sq in squares:
        #make sure we have a square of the same length as the word
        if sq.length != pair[0].length:
            continue

        #empty the list
        pair1NumList.clear()

        #create the first num list (these are strings)
        for c in sq.str:
          pair1NumList.append(c)

        #make a copy
        pair2NumList = pair1NumList.copy()
        
        #update the nums in the second list 
        for i in range(pair[0].length):
            ch = pair[0].word[i]
            strNum = pair1NumList[i]
            location = pair[1].word.index(ch)
            pair2NumList[location] = strNum

        #make a couple of strings from the two number lists
        t1 = ''
        t2 = ''
        
        for i in range(pair[0].length):
            t1 += pair1NumList[i]
            t2 += pair2NumList[i]

        temp = Square(int(t2))

        #see if the second number is in the squares list and doesn't begin with 0
        if isInList(temp) and t2[0] != '0':
            return True,int(t1),int(t2)

    return False,1,1
        
################################################################################
import time
start = time.time()

#make the square list and istantiate each as Square
squares = makeSquareList()

#load the word list from the file
words = loadWordList()

#make list of anagram pairs
pairs = []

words.sort(key=lambda x: x.sortedJoin)

previous = words[0]
for i in range(1,len(words)):
  if previous.sortedJoin == words[i].sortedJoin:
    pairs.append((previous,words[i]))
  previous = words[i]

MAX = 0    
#process each pair
for ap in pairs:
    (success,result1,result2) = analyzePair(ap)
    if success:
        temp = max(result1,result2)
        ap[0].printMe()
        ap[1].printMe()
        print(result1,result2)
        if temp > MAX:
            MAX = temp

print('The solution: ',MAX,'Run Time: ',time.time()-start)
################################################################################
#solution: 18769
################################################################################
