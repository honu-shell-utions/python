#-------------------------------------------------------------------------------
##Investigating numbers with few repeated digits
##Problem 172
##How many 18-digit numbers n (without leading zeros)
##are there such that no digit occurs more than three times in n?
#-------------------------------------------------------------------------------
from itertools import product
from time import time
#-------------------------------------------------------------------------------
def make_choices(num_digits):
    temp = [str(x) for x in range(num_digits)]
    temp = list(product(temp,repeat=num_digits))
    n_list = []
    for t in temp:
        if t[0] != '0':
            n_list.append(t)
    return(n_list)
#-------------------------------------------------------------------------------
def count_repeating_digits(n,max_repeats):
    res = 0
    cnt = [0] * 10
    while (n > 0):
        rem = n % 10
        cnt[rem] += 1
        n = n // 10
    if max(cnt) <= max_repeats:
        return True
    else:
        return False
#-------------------------------------------------------------------------------
def euler_172(num_list,max_repeats):
    count = 0
    for current in num_list:
        test_me = int(''.join(current))
        if count_repeating_digits(test_me,max_repeats):
            count += 1
    return(count)
#-------------------------------------------------------------------------------
start = time()
num_digits = 8
max_repeats = 3
num_list = make_choices(num_digits)
count = euler_172(num_list,max_repeats)

print(f'The solution: {count}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#solution: 227485267000992000
#-------------------------------------------------------------------------------
