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
from math import log, pi

gamma = 0.5772156649015328606

def E(n):
    H = log(n) + gamma + 1/(2*n) - 1/(12*n*n)
    H2 = pi*pi/6 - 1/n + 1/(2*n*n)
    return n/2 * (H*H + H2)

for n in [2,5,100]:
    print(f'for n = {n}, Expected package distance is: {round(E(n),5)}')
print(f'for n = {10**8}, Expected package distance is: {round(E(10**8))}')
