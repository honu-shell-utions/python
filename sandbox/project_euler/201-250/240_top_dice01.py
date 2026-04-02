# p240_top_dice_monteCarlo.py
#
# Top Dice
# There are 1_111 ways in which five 6-sided dice (sides numbered 1 to 6)
# can be rolled so that the top three sum to 15. Some examples are: 
# 
# D1, D2, D3, D4, D5 = 4, 3, 6, 3, 5 
# D1, D2, D3, D4, D5 = 4, 3, 3, 5, 6 
# D1, D2, D3, D4, D5 = 3, 3, 3, 6, 6 
# D1, D2, D3, D4, D5 = 6, 6, 3, 3, 3 
# 
# In how many ways can twenty 12-sided dice (sides numbered 1 to 12)
# be rolled so that the top ten sum to 70?
# {ans == 7448717393364181966}
# -----------------------------------------------------------------------------
import numpy as np
from time import time

t0 = time()
arr = np.arange(1, 7, dtype=np.uint8)
target_sum = 15
st = set()
for i in range(10**6):
    die = np.random.choice(arr, replace=True, size=5)
    b = np.sort(die)
    t = tuple(die)
    tmp = sum(b[-3:])
    if tmp == target_sum:
        st.add(t)
        
ans = len(st)
print(f'{ans:,} {ans==1111} rt: {time()-t0}')
# -----------------------------------------------------------------------------
