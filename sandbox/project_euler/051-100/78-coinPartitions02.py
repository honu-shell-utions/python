################################################################################
##Coin partitions 
##Problem 78
##Let p(n) represent the number of different ways in
##which n coins can be separated into piles. For example,
##five coins can be separated into piles in exactly seven
##different ways, so p(5)=7.
##
##OOOOO
##OOOO   O
##OOO   OO
##OOO   O   O
##OO   OO   O
##OO   O   O   O
##O   O   O   O   O
##Find the least value of n for which p(n) is divisible by one million.
################################################################################
import time

start = time.time()
partitions = [1, 1, 2, 3, 5, 7, 11, 15, 22, 30, 42]
n = 11
partition = 42
pentagonals = []

for k in range(1, 2000):
    pentagonals.append(k*(3*k-1)//2)
    k *= -1
    pentagonals.append(k*(3*k-1)//2)

start = time.time()

while partition != 0:
    partition = 0
    pentagonal = 0
    index = 0
    temp = 0
    is_positive = False
    
    while pentagonal <= n:
       if is_positive:
           partition += temp
       else:
           partition -= temp
       pentagonal = pentagonals[index]
       temp = partitions[n - pentagonal]
       if index % 2 == 0:
           is_positive = not is_positive
       index += 1
    partition %= 1000000
    partitions.append(partition)
    n += 1

print ("Found %d as the answer in %d ms." % (n-1, time.time()-start))

################################################################################
#solution: 55374
################################################################################
