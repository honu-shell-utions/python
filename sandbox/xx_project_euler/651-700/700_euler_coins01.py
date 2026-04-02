#  -----------------------------------------------------------------------------
#  Eulercoin
#  Problem 700
#  https://projecteuler.net/problem=700
#  finding the 16th eulercoin
#  -----------------------------------------------------------------------------
from itertools import count
#  -----------------------------------------------------------------------------
def seq_gen():
    seed = 1504170715041707
    for factor in count(1):
        yield (factor,seed*factor % 4503599627370517)
#  -----------------------------------------------------------------------------
def test_seq(n):
    seq = seq_gen()
    for _ in range(n):
        print(next(seq))
#  -----------------------------------------------------------------------------
def find_euler_coins():
    seq = seq_gen()
    factor,c = next(seq)
    num_coins = 1
    nums = [factor]
    coins = [c]
    print(f'Number of coins: {num_coins:3}, factor:{factor:10}, new_coin:{c:17}')
    while True:
        factor,new_coin = next(seq)
        if new_coin < min(coins):
            nums.append(factor)
            coins.append(new_coin)
            num_coins += 1
            print(f'Number of coins: {num_coins:3}, factor:{factor:10}, new_coin:{new_coin:17}')
        if len(coins) == 16:
            return nums,coins
#  -----------------------------------------------------------------------------
nums,coins = find_euler_coins()
print(coins[-1])
#  NOTE: this version just finds the 16th Euler Coin, see version 2 for
#  the full solution
#  -----------------------------------------------------------------------------
#  solution: 1517926517777556
#  -----------------------------------------------------------------------------

