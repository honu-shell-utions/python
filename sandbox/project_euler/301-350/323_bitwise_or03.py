#  -----------------------------------------------------------------------------
#  Bitwise-OR operations on random integers 
#  Problem 323
#  https://projecteuler.net/problem=323
#  -----------------------------------------------------------------------------
from random import choice
from time import time
#  -----------------------------------------------------------------------------
def find_expected_value():
    diff = 10**(-12)
    n = 0
    ev = 0
    previous_ev = 0
    while True:
        ev +=(1-(1-(1/2)**n)**32)
        if abs(ev - previous_ev) < diff:
            break
        else:
            previous_ev = ev
        n += 1
    return ev
#  -----------------------------------------------------------------------------
solution = find_expected_value()
print(f'Solution: {round(solution,10)}')
#  -----------------------------------------------------------------------------
#  solution: 6.3551758451
#  -----------------------------------------------------------------------------
