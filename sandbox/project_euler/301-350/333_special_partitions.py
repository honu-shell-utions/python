#  -----------------------------------------------------------------------------
#  Special partitions
#  Problem 333
#  All positive integers can be partitioned in such a way that each
#  and every term of the partition can be expressed as 2ix3j, where i,j ≥ 0.
#  
#  Let's consider only such partitions where none of the terms can
#  divide any of the other terms. 
#  For example, the partition of 17 = 2 + 6 + 9 = (2^1x3^0 + 2^1x3^1 + 2^0x3^2)
#  would not be valid since 2 can divide 6. Neither would the partition
#  17 = 16 + 1 = (2^4x3^0 + 2^0x3^0) since 1 can divide 16. The only valid
#  partition of 17 would be 8 + 9 = (2^3x3^0 + 2^0x3^2).
#  
#  Many integers have more than one valid partition, the first being 11
#  having the following two partitions. 
#  11 = 2 + 9 = (2^1x3^0 + 2^0x3^2) 
#  11 = 8 + 3 = (2^3x3^0 + 2^0x3^1)
#  
#  Let's define P(n) as the number of valid partitions of n.
#  For example, P(11) = 2.
#  
#  Let's consider only the prime integers q which would have a single
#  valid partition such as P(17).
#  
#  The sum of the primes q <100 such that P(q)=1 equals 233.
#  
#  Find the sum of the primes q < 10^6 such that P(q)=1.
#  
#  https://projecteuler.net/problem=333
#
#  First calculate the list of all the numbers below the max of the form: 
#  n = 2^i*3^j
#  This one is called m_group
#  Then calculate dynamically all the combinations of those numbers that does
#  not include divisors in the list. This is called "combos".
#  Then sum the "combos" sequences and store in  "solutions"
#  And finally sum the elements of solutions that are prime and not repeated.
#  -----------------------------------------------------------------------------
from time import time
from math import log
from collections import Counter
from sympy import isprime
#  -----------------------------------------------------------------------------
class euler_333:
    def __init__(self,limit):
        self.limit = limit
        self.max2 = int(log(limit,2))
        self.max3 = int(log(limit,3))
        self.m_group = self.make_m_group()
        self.combos = [self.m_group]
        self.sols_list = self.make_sols_list()
    #  ------------------------------------------------------------------------
    def make_m_group(self):
        m_group = []
        for j in range(self.max2+1):
            for i in range(self.max3+1):
                if 2**j*3**i < self.limit:
                    m_group.append([2**j*3**i])
        m_group.sort()
        return m_group
    #  ------------------------------------------------------------------------
    def make_sols_list(self):
        sols_list = []
        while len(self.combos[-1]) > 0:
            self.combos.append([])
            for p1 in range(len(self.combos[-2])):
                nn = self.combos[-2][p1]
                pi = self.m_group.index([self.combos[-2][p1][-1]]) 
                for p2 in range(pi+1,len(self.m_group)):
                    n2 = self.m_group[p2][0]
                    oki = True
                    for n in nn:
                        if n2 % n == 0 or n % n2 == 0:
                            oki = False
                    if oki != 0 and sum(nn+[n2]) < self.limit:
                        self.combos[-1].append(nn+[n2])
                        sols_list.append(sum(nn+[n2]))
        return sols_list
    #  ------------------------------------------------------------------------
    def get_solution(self):
        result = 0
        solution = dict(Counter(self.sols_list))  
        for val, rep in solution.items():
            if rep == 1 and isprime(val):
                result += val
        return result + 5
    #  ------------------------------------------------------------------------
#  -----------------------------------------------------------------------------
for exp in range(2,7):
    start = time()
    limit = 10**exp
    instance = euler_333(limit)
    sol = instance.get_solution()
    print(f'Solution for n = 10^{exp}: {sol:10}, Run-Time: {time()-start}')
    if exp == 6 and sol == 3053105:
        print('bingo, bingo, bingo......')
#  -----------------------------------------------------------------------------
#  solution: 3053105
#  -----------------------------------------------------------------------------
