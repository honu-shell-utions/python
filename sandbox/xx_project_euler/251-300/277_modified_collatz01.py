#  -----------------------------------------------------------------------------
#  A Modified Collatz sequence
#  Problem 277
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def find_seq(target):
    for start in range(begin_at,10**20):
        coll_seq_nums = []
        coll_seq_letters = []
        n, d = next_coll(start)
        coll_seq_nums.append(n)
        coll_seq_letters.append(d)
        while coll_seq_nums[-1] != 1:
            n, d = next_coll(coll_seq_nums[-1])
            coll_seq_nums.append(n)
            coll_seq_letters.append(d)
            if ''.join(coll_seq_letters[:len(target)]) == target:
                return(start,target)
#  -----------------------------------------------------------------------------
def next_coll(coll):
    if coll % 3 == 0:
        return coll//3, 'D'
    if coll % 3 == 1:
        return (4*coll+2)//3, 'U'
    return (2*coll-1)//3, 'd' 
#  -----------------------------------------------------------------------------
start = time()
begin_at = 10**6
target = 'DdDddUUdDD'

print(f'Solution: {find_seq(target)}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 1004064
#  -----------------------------------------------------------------------------
