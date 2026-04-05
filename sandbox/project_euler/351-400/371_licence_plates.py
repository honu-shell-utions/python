#  -----------------------------------------------------------------------------
#  Licence plates
#  Problem 371
#  https://projecteuler.net/problem=371
#  -----------------------------------------------------------------------------
from random import randint
#  -----------------------------------------------------------------------------
def get_plate():
    return randint(0,999)
#  -----------------------------------------------------------------------------
limit = 10**8
total = 0
for _ in range(limit):
    plates_for_match = []
    while True:
        plate = get_plate()
        if 1000 - plate not in plates_for_match:
            plates_for_match.append(plate)
        else:
            total += len(plates_for_match) + 1
            break

print(round(total/limit,8))   
#  -----------------------------------------------------------------------------
#  solution: 40.66368097
#  -----------------------------------------------------------------------------
