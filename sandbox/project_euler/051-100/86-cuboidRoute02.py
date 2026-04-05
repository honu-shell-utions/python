################################################################################
##Cuboid route
##Problem 86
##A spider, S, sits in one corner of a cuboid room,
##measuring 6 by 5 by 3, and a fly, F, sits in the
##opposite corner. By travelling on the surfaces of
##the room the shortest "straight line" distance
##from S to F is 10 and the path is shown on the diagram.
##
##However, there are up to three "shortest" path candidates
##for any given cuboid and the shortest route doesn't
##always have integer length.
##
##It can be shown that there are exactly 2060 distinct cuboids,
##ignoring rotations, with integer dimensions, up to a maximum
##size of M by M by M, for which the shortest route has integer
##length when M = 100. This is the least value of M for which
##the number of solutions first exceeds two thousand; the number
##of solutions when M = 99 is 1975.
##
##Find the least value of M such that the number of solutions
##first exceeds one million.
################################################################################
import math
import time
################################################################################
def run():
    limit = 1_000_000
    count = 0
    M = 0
    while count < limit:
        M += 1
        for a in range(1,M+1):
            for b in range(a,M+1):
                tmp = math.sqrt((a+b)**2 + M**2)
                if tmp % 1 == 0:
                    count +=1      
    return M
################################################################################    
start = time.time()
print('Solution is:',run(),'Run time is:',time.time()-start)
################################################################################
#solution: 1818
################################################################################
