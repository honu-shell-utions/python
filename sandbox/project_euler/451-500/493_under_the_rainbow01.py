#  -----------------------------------------------------------------------------
#  Under The Rainbow
#  Problem 493
#  70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.
#  What is the expected number of distinct colours in 20 randomly picked balls?
#  Give your answer with nine digits after the decimal point (a.bcdefghij).
#  Red, Orange, Yellow, Green, Blue, Indigo and Violet.
#  -----------------------------------------------------------------------------
from random import shuffle
#  -----------------------------------------------------------------------------
def make_list():
    temp = 'ROYGBIV'
    colors = ''
    for _ in range(10):
        colors += temp
    temp = sorted(colors)
    return temp
#  -----------------------------------------------------------------------------
limit = 10**10
total = 0
color_list = make_list()
for _ in range(limit):
    shuffle(color_list)
    unique = set(color_list[:20])
    total += len(unique)

print(round(total/limit,9))
#  -----------------------------------------------------------------------------
#  solution: 6.818741802
#  -----------------------------------------------------------------------------

