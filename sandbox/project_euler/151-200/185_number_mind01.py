#-------------------------------------------------------------------------------
## Number Mind
## Submit 
## Problem 185
## The game Number Mind is a variant of the well known game Master Mind.
## 
## Instead of coloured pegs, you have to guess a secret sequence of digits.
## After each guess you're only told in how many places you've guessed the
## correct digit. So, if the sequence was 1234 and you guessed 2036,
## you'd be told that you have one correct digit; however, you would NOT
## be told that you also have another digit in the wrong place.
## 
## For instance, given the following guesses for a 5-digit secret sequence,
## 
## 90342 ;2 correct
## 70794 ;0 correct
## 39458 ;2 correct
## 34109 ;1 correct
## 51545 ;2 correct
## 12531 ;1 correct
## 
## The correct sequence 39542 is unique.
## 
## Based on the following guesses,
## 
## 5616185650518293 ;2 correct
## 3847439647293047 ;1 correct
## 5855462940810587 ;3 correct
## 9742855507068353 ;3 correct
## 4296849643607543 ;3 correct
## 3174248439465858 ;1 correct
## 4513559094146117 ;2 correct
## 7890971548908067 ;3 correct
## 8157356344118483 ;1 correct
## 2615250744386899 ;2 correct
## 8690095851526254 ;3 correct
## 6375711915077050 ;1 correct
## 6913859173121360 ;1 correct
## 6442889055042768 ;2 correct
## 2321386104303845 ;0 correct
## 2326509471271448 ;2 correct
## 5251583379644322 ;2 correct
## 1748270476758276 ;3 correct
## 4895722652190306 ;1 correct
## 3041631117224635 ;3 correct
## 1841236454324589 ;3 correct
## 2659862637316867 ;2 correct
## 
## Find the unique 16-digit secret sequence.
#-------------------------------------------------------------------------------
from random import randint
import numpy as np
from time import time
#-------------------------------------------------------------------------------
def make_candidate(length):
    arr = np.zeros((10,length))
    row = randint(1,9)
    arr[row,0] = 1
    for col in range(1,length):
        row = randint(0,9)
        arr[row,col] = 1
    return arr
#-------------------------------------------------------------------------------
def make_guess_arr(guess):
    temp = np.zeros((10,len(guess)))
    col = 0
    for d in guess:
        row = int(d)
        temp[row,col] = 1
        col += 1
    return temp
#-------------------------------------------------------------------------------
def squish(arr,length):
    answer = ''
    for col in range(length):
        for row in range(10):
            if arr[row][col] == 1:
                answer += str(row)
                break
    return answer
#-------------------------------------------------------------------------------
def make_guess_list():
    temp = [['90342',2],\
            ['70794',0],\
            ['39458',2],\
            ['34109',1],\
            ['51545',2],\
            ['12531',1]]   
    return temp
#-------------------------------------------------------------------------------
def test_candidate(candidate):
    for guess, hits in guess_list:
        guess_arr = make_guess_arr(guess)
        if np.count_nonzero((guess_arr+candidate) == 2) != hits:
            return False
    return True
#-------------------------------------------------------------------------------
start = time()
guess_list = make_guess_list()
length = len(guess_list[0][0])
while True:
    candidate = make_candidate(length)
    if test_candidate(candidate):
        break
print(f'Solution: {squish(candidate,length)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#solution: 4640261571849533
#-------------------------------------------------------------------------------
