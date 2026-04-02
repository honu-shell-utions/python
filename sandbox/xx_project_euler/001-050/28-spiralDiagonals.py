## Spiral Diagonals
## Problem 28
## Starting with the number 1 and moving to the right in a clockwise
## direction a 5 by 5 spiral is formed as follows:
##
##  21 22 23 24 25
##  20  7  8  9 10
##  19  6  1  2 11
##  18  5  4  3 12
##  17 16 15 14 13
##
##  diagonals: 21, 7, 1, 3, 13
##             17, 5, 1, 9, 25
##             -----------------
##             38, 12, 2, 12, 38
##
## 43 44 45 46 47 48 49
## 42 21 22 23 24 25 26
## 41 20  7  8  9 10 27
## 40 19  6  1  2 11 28
## 39 18  5  4  3 12 29
## 38 17 16 15 14 13 30
## 37 36 35 34 33 32 31
##
##  diagonals: 43, 21, 7, 1, 3, 13, 31
##             37, 17, 5, 1, 9, 25, 49
##             -------------------------
##             80, 38, 12, 2, 12, 38, 80

##
## It can be verified that the sum of the numbers on the diagonals is 101.
##
## What is the sum of the numbers on the diagonals in a 1001 by 1001
## spiral formed in the same way?
###########################################################################
## jim mccleery, november, 2021
###########################################################################
totalDiagsUR = 0
totalDiagsLR = 0
upperRightCorner = 1001**2
n = 0
while (2*n+1)**2 <= upperRightCorner:
    totalDiagsUR += (2*n+1)**2
    n+=1

nAtEndOfFirstLoop = n+1

for n in range(1,nAtEndOfFirstLoop):
    totalDiagsLR += 4*n**2-10*n+7
    
totalDiags = 2*(totalDiagsUR+totalDiagsLR) - 3
print(totalDiags)
#solution: 669171001
###########################################################################
