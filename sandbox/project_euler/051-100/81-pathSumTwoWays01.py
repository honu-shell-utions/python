################################################################################
##Path sum: two ways
##Problem 81
##In the 5 by 5 matrix below, the minimal path sum from the top
##left to the bottom right, by only moving to the right and down,
##is indicated in bold red and is equal to 2427.
##
##
##    (131* 673  234  103   18
##     201*  96* 342* 965  150
##     630  803  746* 422* 111
##     537  699  497  121* 956
##     805  732  524   37* 331*)
##
##Find the minimal path sum from the top left to the bottom right
##by only moving right and down in matrix.txt
##(right click and "Save Link/Target As..."), a 31K text file
##containing an 80 by 80 matrix.
################################################################################
import numpy as np
import random
################################################################################
dataArray = np.loadtxt('81-matrix.csv',dtype=int,delimiter=',')
minPathList = []
minPathSum = 10**20
arrayDim = dataArray.shape
rows = arrayDim[0]
cols = arrayDim[1]
numMoves = (rows-1)+(cols-1)

while True:
    currentRow = 0
    currentCol = 0
    minPathList.clear()
    minPathList.append(dataArray[0][0])
    rightMoves = 0
    downMoves = 0

    while len(minPathList) < numMoves+1:
        hit = False
        if random.random() < .5 and downMoves < rows - 1:
            #move down
            downMoves += 1
            currentRow += 1
            hit = True
        elif rightMoves < cols - 1:
            #move right
            rightMoves += 1
            currentCol += 1
            hit = True
        if hit:
            minPathList.append(dataArray[currentRow][currentCol])

    if sum(minPathList) < minPathSum:
        minPathSum = sum(minPathList)
        print(minPathList)
        print(minPathSum)
################################################################################
#solution: 427337
################################################################################
