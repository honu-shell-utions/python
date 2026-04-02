#  -----------------------------------------------------------------------------
#  Eulercoin
#  Problem 700
#  https://projecteuler.net/problem=700
#  -----------------------------------------------------------------------------
from itertools import count
from time import time
#  -----------------------------------------------------------------------------
def find_nth_coin(n=16):
    euler_coines =[(1,1,FIRST_COIN)]
    current_eulercoin = FIRST_COIN
    last_coin = FIRST_COIN
    num_coins = 1
    factor = 2
    while num_coins < n:
        current_eulercoin = FIRST_COIN*factor % MOD
        if current_eulercoin < last_coin:
            num_coins += 1
            last_coin = current_eulercoin
            euler_coines.append((num_coins,factor,last_coin))
        factor += 1
    return euler_coines
#  -----------------------------------------------------------------------------
def euler_700(split_value=16):
    euler_coins = find_nth_coin(split_value)
    STOP = euler_coins[-1][-1]
    new_curr_eulercoin = 1
    num_coins = split_value
    curr_max = MOD
    inv = pow(FIRST_COIN,-1,MOD)
    while new_curr_eulercoin != STOP:
        factor = inv*new_curr_eulercoin
        number = factor % MOD
        if number < curr_max:
            curr_max = number
            num_coins += 1
            euler_coins.append((num_coins,factor,new_curr_eulercoin))
        new_curr_eulercoin += 1
    return euler_coins
#  -----------------------------------------------------------------------------
FIRST_COIN = 1504170715041707
MOD = 4503599627370517
for split in range(15,18):
    start = time()
    total = 0
    coins = euler_700(split)
    for num,factor,c in coins:
        print(f'{num:4} {factor:24} {c:16}')
        total += c
    print(f'Solution: {total}, Split: {split}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 1517926517777556
#  -----------------------------------------------------------------------------
