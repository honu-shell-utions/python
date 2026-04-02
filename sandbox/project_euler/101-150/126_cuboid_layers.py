################################################################################
# 126_cuboid_layers.py
#
# The minimum number of cubes to cover every visible face on a
# cuboid measuring 3 x 2 x 1 is twenty-two.
#
# If we then add a second layer to this solid it would require forty-six cubes
# to cover every visible face, the third layer would require seventy-eight
# cubes, and the fourth layer would require one-hundred and eighteen cubes to
# cover every visible face.
# 
# However, the first layer on a cuboid measuring 5 x 1 x 1 also requires
# twenty-two cubes; similarly the first layer on cuboids measuring
# 5 x 3 x 1, 7 x 2 x 1, and 11 x 1 x 1 all contain forty-six cubes.
# 
# We shall define C(n) to represent the number of cuboids that contain n cubes
# in one of its layers. So C(22) = 2, C(46) = 4, C(78) = 5, and C(118) = 8.
# 
# It turns out that 154 is the least value of n for which C(n) = 10.
# 
# Find the least value of n for which C(n) = 1000.
################################################################################
def cubes(x,y,z,n):
    return 2*(x*y + y*z + x*z) + 4*(x+y+z +n -2)*(n-1)
################################################################################
from time import time
start = time()
limit = 20000
keepers = []
tally = [0]*(limit+1)

for x in range(1,limit):
    if cubes(x,x,x,1) > limit:
        break
    for y in range(x, limit):
        if cubes(x,y,y,1) > limit:
            break
        for z in range(y,limit):
            if cubes(x,y,z,1) > limit:
                break
            for n in range(1,limit):
                temp = cubes(x,y,z,n)
                if temp > limit:
                    break
                else:
                    tally[temp] += 1

for i in range(len(tally)):
    if tally[i] == 1000:
        keepers.append(i)

print('The solution:',min(keepers),'Run Time:',time()-start)
################################################################################
#solution: 18522
################################################################################
