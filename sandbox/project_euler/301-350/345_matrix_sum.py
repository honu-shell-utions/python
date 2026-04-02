#  -----------------------------------------------------------------------------
#  Matrix Sum
#  Problem 345
#  https://projecteuler.net/problem=345
#  -----------------------------------------------------------------------------
import numpy as np
from scipy.optimize import linear_sum_assignment
from time import time
#  -----------------------------------------------------------------------------
def get_data(f_name):
    data = np.loadtxt(f_name,dtype=int)
    return data
#  -----------------------------------------------------------------------------
def process_array(data):
    r, c = linear_sum_assignment(data*-1)
    ans = data[r, c].sum()
    return ans
#  -----------------------------------------------------------------------------
for f_name in ['345_sample1.txt','345_sample2.txt','345_data.txt']:
    start = time()
    data = get_data(f_name) 
    ans = process_array(data)
    print(f'Solution: {ans}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 13938
#  -----------------------------------------------------------------------------
