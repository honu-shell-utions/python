'''
18-max_path_sum.py

By starting at the top of the triangle below and moving to adjacent numbers
on the row below, the maximum total from top to bottom is 23.
   3             3
  7 4            7
 2 4 6           4
8 5 9 3          9
That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:
                75
              95 64
             17 47 82
            18 35 87 10
           20 04 82 47 65
          19 01 23 75 03 34
         88 02 77 73 07 63 67
        99 65 04 28 06 16 70 92
       41 41 26 56 83 40 80 70 33
      41 48 72 33 47 32 37 16 94 29
     53 71 44 65 25 43 91 52 97 51 14
   70 11 33 28 77 73 17 78 39 68 17 57
  91 71 52 38 17 14 91 43 58 50 27 29 48
 63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23

NOTE: As there are only 16384 routes, it is possible to solve this problem by
trying every route. However, Problem 67, is the same challenge with a triangle
containing one-hundred rows; it cannot be solved by brute force, and requires
a clever method.
'''
import numpy as np
import time

#create the list
numList = []

#open the the file
file1 = open("67-data-in.txt", "r")

#function to compute max of the 'triangle' elements
def maxTri(top,left,right):
    sum1 = top + left
    sum2 = top + right
    if sum1 > sum2:
        return(sum1)
    else:
        return(sum2)
    
#read the first line of the input file & build the list
numberOfRows = 0
line = file1.readline()
while line:
    numberOfRows += 1
    numList.append(line.split())
    line = file1.readline()
file1.close()

#convert the list to a 2d array with elements appropriately spaced
numberOfColumns = 2*len(max(numList, key=len)) - 1
numArray = np.zeros((numberOfRows,numberOfColumns), dtype=int)
middleColumn = int(numberOfColumns/2)
for r in range(len(numList)):
    pad = 0
    for c in range(len(numList[r])):
        numArray[r,middleColumn - r + pad] = numList[r][c]
        pad += 2

#make a copy of the numArray before altering it
originalArray = numArray.copy()

#compute max path
##print(numArray)
##time.sleep(3)
##print()
for r in range(numberOfRows-2, -1, -1):
    for c in range(1,numberOfColumns-1):
        numArray[r,c] = maxTri(numArray[r,c],numArray[r+1,c-1],numArray[r+1,c+1])
##    print(numArray)
##    time.sleep(3)
##    print()      
    

originalArray[0,middleColumn] = numArray[0,middleColumn]

#max path total in the middle of the top row
lengthOfTopRow = len(originalArray[0])
print('The solution:',originalArray[0][(lengthOfTopRow-1)//2])
#solution: 7273
