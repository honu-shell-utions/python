#  -----------------------------------------------------------------------------
#  Digital root clocks
#  Problem 315
#  https://projecteuler.net/problem=315
#  -----------------------------------------------------------------------------
#imports
from time import time
from sympy import primerange
import numpy as np
#  -----------------------------------------------------------------------------
#constants
TRANS = {0:0b1101111,1:0b0100010,2:0b1110101,3:0b1110011,4:0b0111010,\
         5:0b1011011,6:0b1011111,7:0b1101010,8:0b1111111,9:0b1111011}

GRID = np.zeros((11,10),dtype=int)
#  -----------------------------------------------------------------------------
def load_grid():
  for row in range(11):
    for col in range(10):
      if row == 10:
        GRID[row,col] = bin(TRANS[col]).count('1')
      else:
        GRID[row,col] = bin(TRANS[row] ^ TRANS[col]).count('1')
#  -----------------------------------------------------------------------------
#methods
def digit_sum(n):
  return sum(map(int,list(str(n))))
#  -----------------------------------------------------------------------------
def make_chain(n):
  num_list = [n]
  while True:
    n = digit_sum(n)
    num_list.append(n)
    if len(str(n)) == 1:
      return num_list
#  -----------------------------------------------------------------------------
def sam_count_trans(num_list):
  trans = 0
  for num in num_list:
    for d in map(int,list(str(num))):
      trans += GRID[10,d]
  return trans*2
#  -----------------------------------------------------------------------------
def max_count_trans(num_list):
  num_rows = len(num_list)+1
  num_cols = len(str(num_list[0]))
  arr = np.zeros((num_rows,num_cols),dtype=int)

  #load with -1 in each position
  for row in range(num_rows):
    for col in range(num_cols):
      arr[row,col] = -1
  
  #load nums into array
  for ndx1,num in enumerate(num_list):
    digits = list(map(int,list(str(num))))
    for ndx2,d in enumerate(digits,start = num_cols-len(str(num))):
      arr[ndx1,ndx2] = d

  #compute transactions
  trans = 0
  #take care of the first row
  for digit in arr[0]:
    trans += GRID[10,digit]

  #process the rest of the rows
  for row in range(1,num_rows):
    for col in range(num_cols):
      if arr[row,col] == -1 and arr[row-1,col] != -1:
        trans += GRID[10,arr[row-1,col]]
      elif arr[row,col] != -1:
        trans += GRID[arr[row,col],arr[row-1,col]]
      
  return trans
#  -----------------------------------------------------------------------------
#driver
start = time()
all_sam = 0
all_max = 0
load_grid()
primes = list(primerange(10**7,2*10**7))
for p in primes:
  num_list = make_chain(p)
  all_sam += sam_count_trans(num_list)
  all_max += max_count_trans(num_list)
print('Total Sam transitions:',all_sam)
print('Total Max transitions:',all_max)
print('Sam transitions - Max transitions:',all_sam-all_max)
print('Run-Time:',time()-start)
#  -----------------------------------------------------------------------------
#  solution: 13625242
#  -----------------------------------------------------------------------------

