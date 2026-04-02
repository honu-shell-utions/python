################################################################################
## Searching a triangular array for a sub-triangle having minimum-sum
## Problem 150
## In a triangular array of positive and negative integers, we wish to
## find a sub-triangle such that the sum of the numbers it contains is
## the smallest possible.
##
## In the example below, it can be easily verified that the marked
## triangle satisfies this condition having a sum of −42.
##
## We wish to make such a triangular array with one thousand rows,
## so we generate 500500 pseudo-random numbers sk in the range ±2^19,
## using a type of random number generator
## (known as a Linear Congruential Generator) as follows:
##
## t := 0 
## for k = 1 up to k = 500500: 
##    t := (615949*t + 797807) modulo 2^20
##    sk := t−2^19
##
## Thus: s1 = 273519, s2 = −153582, s3 = 450905 etc
##
## Our triangular array is then formed using the pseudo-random numbers thus:
##
##      s1
##    s2  s3
##  s4  s5  s6  
## s7  s8  s9  s10
##etc....
##
##Sub-triangles can start at any element of the array and extend down
##as far as we like (taking-in the two elements directly below it from
##the next row, the three elements directly below
##from the row after that, and so on).
##
##The "sum of a sub-triangle" is defined as the sum of all the elements it contains. 
##Find the smallest possible sub-triangle sum.
################################################################################
import numpy as np
################################################################################
def make_pseudo_list():
    temp = 0
    temp_lst = []
    for k in range(ROWS*(ROWS+1)//2):
        temp = (615949*temp + 797807) % 2**20
        temp_lst.append(temp - 2**19)
    return temp_lst
################################################################################
def load_2d_array():
    index = 0
    for x,y in cor_list:
        arr[x,y] = pseudo_list[index]
        index += 1
################################################################################
def make_cor_list():
    temp = []
    col_stop = [n for n in range(COLS // 2, COLS +1)]
    i = COLS // 2
    for row in range(0, (COLS // 2)+1):
        for col in range(i, col_stop[row]+1, 2):
            temp.append((row, col))
        i -= 1
    return temp
################################################################################
ROWS = 4
COLS = ROWS*2 - 1
arr = np.zeros([ROWS,COLS],int)
pseudo_list = make_pseudo_list()
cor_list = make_cor_list()
load_2d_array()
print(arr)
################################################################################
#solution: -271248680
################################################################################


