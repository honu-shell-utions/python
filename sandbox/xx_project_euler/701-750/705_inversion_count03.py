#  -----------------------------------------------------------------------------
#  Total Inversion Count of Divided Sequences
#  Problem 705
#  https://projecteuler.net/problem=705
#  -----------------------------------------------------------------------------
#  -----------------------------------------------------------------------------
#  Divided Sequences
#  If each digit of a sequence is replaced by one of its divisors a divided sequence is obtained. 
#  For example, the sequence 332 has 8 divided sequences: 
#  {332,331,312,311,132,131,112,111}
#  -----------------------------------------------------------------------------
import numpy as np
from sympy import sieve
#  -----------------------------------------------------------------------------
def get_inversion_count(arr):
    n = len(arr)
    inv_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (arr[i] > arr[j]):
                inv_count += 1
    return inv_count
#  -----------------------------------------------------------------------------
def make_seq(N):
    seq = ''
    count = 0
    for p in sieve:
        if '0' not in str(p):
            seq += str(p)
            count += 1
            if count == N:
                return int(seq)
#  -----------------------------------------------------------------------------
def make_repeats():
    #figure out how often a divisor repeats in a given row
    REPEATS = [1]
    for ndx in range(1,len(BUCKET_LIST)):
        REPEATS.append(REPEATS[-1]*len(BUCKET_LIST[ndx-1]))
    return REPEATS
#  -----------------------------------------------------------------------------
def make_sols(grid):
    #from the loaded grid make the solutions
    solutions = []
    for col in range(NUM_COLS):
        #grab each column
        temp = list(grid[:,col])
        temp = map(str,temp)
        solutions.append(int(''.join(temp)))
    return solutions
#  -----------------------------------------------------------------------------    
def make_divided_sequences():
    #make the empty gird and populate with zeros
    grid = np.zeros((NUM_ROWS,NUM_COLS),dtype=int)

    #build list of lists with the row values
    res = []
    for row in range(NUM_ROWS):
        temp = []
        for j in range(NUM_COLS//REPEATS[row]):
            for k in range(REPEATS[row]):
                temp.append(BUCKET_LIST[row][j%len(BUCKET_LIST[row])])
        res.extend([temp])

    #from the list of lists populate the grid
    for row,r in enumerate(res):
        for col,val in enumerate(r):
            grid[row,col] = val

    return grid
#  -----------------------------------------------------------------------------
DIVS = [[0],[1], [1, 2], [1, 3], [1, 2, 4], [1, 5], [1, 2, 3, 6],
        [1, 7], [1, 2, 4, 8], [1, 3, 9]]

while True:
    k = input('\nEnter how many primes to use: ')
    try:
        n = make_seq(int(k))
        SEQ = abs(int(n))
        BUCKET_LIST = []
        NUM_COLS = 1
        for ndx in list(map(int,list(str(SEQ)))):
            BUCKET_LIST.append(DIVS[ndx])
            NUM_COLS *= len(DIVS[ndx])
        NUM_ROWS = len(BUCKET_LIST)
        REPEATS = make_repeats()
        grid = make_divided_sequences()
        solutions = make_sols(grid)
        inversions = 0
        for s in solutions:
            temp = list(str(s))
            arr = list(map(int,temp))
            inversions += get_inversion_count(arr)
        print(inversions)
        print(f'Length of sequence is: {len(solutions)}, the seed is {SEQ}.')
    except:
        break
#  -----------------------------------------------------------------------------
#  solution: 480440153
#  -----------------------------------------------------------------------------
