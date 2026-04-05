################################################################################
##Path sum: three ways
##Problem 82
##A more challenging version of Problem 81.
##
##Find the minimal path sum in the 5 by 5 matrix below, by starting in any
##cell in the left column and finishing in any cell in the right column,
##and only moving up, down, and right, is indicated in red and bold; the
##sum is equal to 994.
##
##(131 673  234* 103* 18*
## 201* 96* 342* 965 150
## 630 803  746  422 111
## 537 699  497  121 956
## 805 732  524   37 331)
##
##Find the minimal path sum from the left column to the right column in
##matrix.txt (right click and "Save Link/costMatrixarget As..."), a 31K text file
##containing an 80 by 80 matrix.
################################################################################
import numpy as np
import time
################################################################################
def buildCostMatrix(matrix):

    #determine the shape of the matrix being processed
    (numRows,numCols) = matrix.shape
    #creat a list that initially contains the first colume of matrix
    best = [matrix[row][0] for row in range(numRows)]

    #loop through the columns   
    for col in range(1,numCols):
        #create a new list from the next column
        column = [matrix[row][col] for row in range(numRows)]
        #make a copy of it
        tmp = column.copy()

        for i in range(numRows):
            column[i] += best[i] #right, add value on the left

            for j in range(0, i): #up
                if sum([best[j]]+tmp[j:i+1]) < column[i]:
                    column[i] = sum([best[j]]+tmp[j:i+1])

            for k in range(i, numRows): #bottom
                if sum([best[k]]+tmp[i:k+1]) < column[i]:
                    column[i] = sum([best[k]]+tmp[i:k+1])

        #point to the best so far
        best = column

    return min(best)

################################################################################
start = time.time()
dataArray = np.loadtxt('82-baby-matrix.csv',dtype=int,delimiter=',')
print('The solutioin:',buildCostMatrix(dataArray),'Run Time:',time.time()-start)
################################################################################
#solution: 260324
################################################################################
