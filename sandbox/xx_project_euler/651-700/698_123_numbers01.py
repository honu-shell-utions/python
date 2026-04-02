#  -----------------------------------------------------------------------------
#  123 Numbers
#  Problem 698
#  https://projecteuler.net/problem=698
#  -----------------------------------------------------------------------------
from time import time
from math import factorial
#  -----------------------------------------------------------------------------
def get_min(dic):
    res = 999999
    for d in dic:
        v = dic[d]
        if v < res:
            res = v
    return res
#  -----------------------------------------------------------------------------
def get_possible_sets(dic, m):
    res = []
    for d in dic:
        if dic[d] == m:
            res.append(list(d))
    return res
#  -----------------------------------------------------------------------------
def remove_from_dict(dic, delete):
    for d in delete:
        dic.pop(tuple(d))
    return dic
#  -----------------------------------------------------------------------------
def number_of_permutations(d):
    a, b, c = d[0], d[1], d[2]
    return factorial(a+b+c) // (factorial(a) * factorial(b) * factorial(c))
#  -----------------------------------------------------------------------------
def next_digit(dic, old_sum, N):
    # digit 1
    new_sum = 0
    for d in dic:
        v = d.copy()
        if v[0] == 0:
            continue
        v[0] -= 1
        new_sum += number_of_permutations(v)
    if old_sum + new_sum >= N:
        return 1, old_sum
    old_sum += new_sum
    # digit 2
    new_sum = 0
    for d in dic:
        v = d.copy()
        if v[1] == 0:
            continue
        v[1] -= 1
        new_sum += number_of_permutations(v)
    if old_sum + new_sum >= N:
        return 2, old_sum
    else:
        # print('3', new_sum)
        return 3, old_sum + new_sum
#  -----------------------------------------------------------------------------
def F(limit):
    # Up to 3 digits per 1, 2 or 3 with a total digit count up to 999.
    # This is way too much but on the safe side.
    counts = [0, 1, 2, 3, 11, 12, 13, 21, 22, 23, 31, 32, 33, 111,\
              112, 113, 121, 122, 123, 131, 132, 133, 211, 212, 213,\
              221, 222, 223, 231, 232, 233, 311, 312, 313, 321, 322,\
              323, 331, 332, 333]

    digit_numbers = {}
    for a in counts:
        for b in counts:
            for c in counts:
                digit_numbers[tuple([a, b, c])] = a + b + c

    m = get_min(digit_numbers)
    sum_old = -1    # (0,0,0) is counted in the loop.

    while not m >= 999:  # (999 over 333 alone is a number with 275 digits ...
                         # this is really enough!)
        sum_new = 0
        sets = get_possible_sets(digit_numbers, m)
        digit_numbers = remove_from_dict(digit_numbers, sets)

        for d in sets:
            p = number_of_permutations(d)
            sum_new += p

        if sum_old + sum_new > limit:
            break

        sum_old += sum_new
        m = get_min(digit_numbers)

    result = []
    while not sets == [[0, 0, 0]]:
        dig, sum_old = next_digit(sets, sum_old, limit)
        result.append(dig)
        new_sets = []
        for s in sets:
            if not s[dig-1] == 0:
                s[dig-1] -= 1
                new_sets.append(s)
        sets = new_sets.copy()

    number = 0
    while result:
        number *= 10
        number += result.pop(0)
    return number
#  -----------------------------------------------------------------------------
MOD = 123123123
for N in [4,10,40,10**3,6*10**3,111111111111222333]:
    start = time()
    if N != 6*10**3:
        res = F(N) % MOD
    else:
        res = F(N)
    print(f'Solution for N = {N:20}: {res:15}, Run-Time: {time()-start:0.2f}')
#  -----------------------------------------------------------------------------
#  solution: 57808202
#  -----------------------------------------------------------------------------
