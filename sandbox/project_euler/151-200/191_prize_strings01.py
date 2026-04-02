#-------------------------------------------------------------------------------
## Prize Strings
## Problem 191
## A particular school offers cash rewards to children with good
## attendance and punctuality. If they are absent for three consecutive
## days or late on more than one occasion then they forfeit their prize.
## 
## During an n-day period a trinary string is formed for each child
## consisting of L's (late), O's (on time), and A's (absent).
## 
## Although there are eighty-one trinary strings for a 4-day period
## that can be formed, exactly forty-three strings would lead to a prize:
## 
## OOOO OOOA OOOL OOAO OOAA OOAL OOLO OOLA OAOO OAOA
## OAOL OAAO OAAL OALO OALA OLOO OLOA OLAO OLAA AOOO
## AOOA AOOL AOAO AOAA AOAL AOLO AOLA AAOO AAOA AAOL
## AALO AALA ALOO ALOA ALAO ALAA LOOO LOOA LOAO LOAA
## LAOO LAOA LAAO
## 
## How many "prize" strings exist over a 30-day period?
#-------------------------------------------------------------------------------
from itertools import product
from time import time
#-------------------------------------------------------------------------------
def get_cases():
    return product(['A','O','L'], repeat=4)
#-------------------------------------------------------------------------------
def good(case):
    if 'AAA' in ''.join(case):
        return False
    if c.count('L') > 1:
        return False
    return True
#-------------------------------------------------------------------------------
start = time()
cases = get_cases()
total = 0

for c in cases:
    if good(c):
        total += 1

print(f'Solution: {total}, Run-Time: {time()-start}')

#-------------------------------------------------------------------------------
#solution: 1918080160
#-------------------------------------------------------------------------------
