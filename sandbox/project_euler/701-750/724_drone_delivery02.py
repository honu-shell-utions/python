"""
https://projecteuler.net/problem=724

A depot uses (n) drones to disperse packages containing
essential supplies along a long straight road. Initially
all drones are stationary, loaded with a supply package.

Every second, the depot selects a drone at random and
sends it this instruction:

* If you are stationary, start moving at one centimetre
per second along the road.
* If you are moving, increase your speed by one centimetre
per second along the road without changing direction.

The road is wide enough that drones can overtake one
another without risk of collision.

Eventually, there will only be one drone left at the
depot waiting to receive its first instruction.
As soon as that drone has flown one centimetre along
the road, all drones drop their packages and return
to the depot.

Let (E(n)) be the expected distance in centimetres from
the depot that the supply packages land.

For example,

E(2)=7/2, E(5)=12019/720, E(100)approx 1427.193470.

Find (E(10^8)). Give your answer rounded to the nearest
integer.

"""
from random import randint

trials = 10**3

for n in [2,5,100]:
    expected_value = 0

    for _ in range(trials):
        drones = [(0, 0)] * n   # each drone = (distance, speed)
        has_not_moved = n

        while has_not_moved > 0:
            ndx = randint(0, n - 1)

            # first: selected drone receives instruction
            distance, speed = drones[ndx]

            if speed == 0:
                drones[ndx] = (0,1)
                has_not_moved -= 1
            else:
                drones[ndx] = (distance, speed + 1)

            # then: one second passes, so every moving drone advances
            new_drones = []
            for ndx in range(len(drones)):
                distance,speed = drones[ndx]
                drones[ndx] = distance + speed, speed

        trial_total = sum(distance for distance, speed in drones)
        expected_value += trial_total / n

    print(f'For n = {n}, Expected Value = {round(expected_value/trials,5)}') 

#for n = 2, expected value = 3.5
#for n = 5, expected value = 16.693055555555556
#for n = 100, expected value = 1427.193470




