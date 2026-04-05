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
import time
################################################################################
def findMinPath(theData):
    # M × N matrix
    (M, N) = theData.shape

    # T[i][j] maintains the minimum value to reach cell (i, j) from cell (0, 0)
    T = np.zeros((M,N),int)

    # fill the matrix
    for i in range(M):
        for j in range(N):
            T[i][j] = theData[i][j]

            # fill the first row (there is only one way to reach any cell in the
            # first row from its adjacent left cell)
            if i == 0 and j > 0:
                T[0][j] += T[0][j - 1]

            # fill the first column (there is only one way to reach any cell in
            # the first column from its adjacent top cell)
            elif j == 0 and i > 0:
                T[i][0] += T[i - 1][0]

            # fill the rest with the matrix (there are two ways to reach any
            # cell in the rest of the matrix, from its adjacent
            # left cell or adjacent top cell)
            elif i > 0 and j > 0:
                T[i][j] += min(T[i - 1][j], T[i][j - 1])

            print('---------------------------------')
            print(theData)
            print()
            print(T)
            print('---------------------------------')

    # last cell of T[][] stores the minimum value to reach destination cell
    # (M-1, N-1) from source cell (0, 0)
    return T[M - 1][N - 1]

################################################################################
start = time.time()
dataArray = np.loadtxt('81-baby-matrix.csv',dtype=int,delimiter=',')
print('The minimum theData is', findMinPath(dataArray),'Run Time:',time.time()-start)
################################################################################
#solution: 427337
################################################################################
