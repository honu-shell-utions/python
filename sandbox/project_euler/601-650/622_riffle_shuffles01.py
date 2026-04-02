#  -----------------------------------------------------------------------------
#  Riffle Shuffles
#  Problem 622
# s https://projecteuler.net/problem=622
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def shuffle(deck):
    left = deck[:len_deck//2]
    right = deck[len_deck//2:]
    for k in range(len_deck):
        if k % 2 == 0:
            deck[k] = left[k//2]
        else:
            deck[k] = right[k//2]
    return deck
#  -----------------------------------------------------------------------------
def s(len_deck):
    deck = [card for card in range(1,len_deck+1)]
    num_shuffles = 1
    temp = deck.copy()
    temp = shuffle(temp)
    while temp != deck:
        num_shuffles += 1
        temp = shuffle(temp)
    return num_shuffles
#  -----------------------------------------------------------------------------
total = 0
num_shuffles = 60
for len_deck in range(2,10**20+1,2):
    if s(len_deck) == num_shuffles:
        total += len_deck
        print(f'Num shuffles: {num_shuffles}, deck length: {len_deck:20}, total: {total}')
        if total == 3010983666182123972:
            break
#  -----------------------------------------------------------------------------
#  solution: 3010983666182123972
#  -----------------------------------------------------------------------------
