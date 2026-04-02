from sympy import isprime
from itertools import combinations, permutations, chain
from time import time
    
def make_partitions(n):
    # base case of recursion: zero is the sum of the empty list
    if n == 0:
        yield []
        return		
    # modify partitions of n-1 to form partitions of n
    for p in make_partitions(n-1):
        yield [1] + p
        if p and (len(p) < 2 or p[1] > p[0]):
            yield [p[0] + 1] + p[1:]

def make_primes_pool():
    lst_primes = []
    temp = list(chain(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9' ], r) for r in range(1, 9)))
    for tmp in temp:
        for n in tmp:
            n = int(''.join(n))
            if isprime(n):
                lst_primes.append(n)
    return lst_primes

def get_prime_count(part):
    how_many = [0]*9
    for k in range(1,9):
        how_many[k] = part.count(k)
    return how_many

def process_prime_count(count):
    combo_list = []
    for k in range(1,9):
        if count[k] != 0:
            combos = list(combinations(all_primes[k],count[k]))
            combo_list.append(combos)                          
    return combo_list

def get_hits1(count):
    hits = 0
    combo_list = process_prime_count(count)
    for c1 in combo_list[0]:
        temp = list(c1)
        temp = [str(x) for x in temp]
        temp = ''.join(temp)
        temp = sorted(temp)
        temp = ''.join(temp)
        if temp == '123456789':
            hits += 1           
    return hits

def get_hits2(count):
    hits = 0
    combo_list = process_prime_count(count)
    for c1 in combo_list[0]:
        for c2 in combo_list[1]:
            temp = list(c1)+list(c2)
            temp = [str(x) for x in temp]
            temp = ''.join(temp)
            temp = sorted(temp)
            temp = ''.join(temp)
            if temp == '123456789':
                hits += 1           
    return hits

def get_hits3(count):
    hits = 0
    combo_list = process_prime_count(count)
    for c1 in combo_list[0]:
        for c2 in combo_list[1]:
            for c3 in combo_list[2]:
                temp = list(c1)+list(c2)+list(c3)
                temp = [str(x) for x in temp]
                temp = ''.join(temp)
                temp = sorted(temp)
                temp = ''.join(temp)
                if temp == '123456789':
                    hits += 1           
    return hits

def how_many_different_primes(count):
    total = 0
    for k in range(1,9):
        if count[k] != 0:
            total += 1
    return total

start = time()    
prime_list = make_primes_pool()
pan_primes1 = []
pan_primes2 = []
pan_primes3 = []
pan_primes4 = []
pan_primes5 = []
pan_primes6 = []
pan_primes7 = []
pan_primes8 = []

for current_prime in prime_list:
    if len(str(current_prime)) == 1:
        pan_primes1.append(current_prime)
    elif len(str(current_prime)) == 2:
        pan_primes2.append(current_prime)
    elif len(str(current_prime)) == 3:
        pan_primes3.append(current_prime)
    elif len(str(current_prime)) == 4:
        pan_primes4.append(current_prime)
    elif len(str(current_prime)) == 5:
        pan_primes5.append(current_prime)
    elif len(str(current_prime)) == 6:
        pan_primes6.append(current_prime)
    elif len(str(current_prime)) == 7:
        pan_primes7.append(current_prime)
    else:
        pan_primes8.append(current_prime)

all_primes = [0]*9
all_primes[1] = pan_primes1
all_primes[2] = pan_primes2
all_primes[3] = pan_primes3
all_primes[4] = pan_primes4
all_primes[5] = pan_primes5
all_primes[6] = pan_primes6
all_primes[7] = pan_primes7
all_primes[8] = pan_primes8

prime_length_count = []
for p in make_partitions(9):
    if p.count(1) < 5 and len(p) > 1:
        prime_length_count.append(get_prime_count(p))

solutions = 0
for count in prime_length_count:
    num_primes = how_many_different_primes(count)
    if num_primes == 1:
        solutions += get_hits1(count)
    elif num_primes == 2:
        solutions += get_hits2(count)
    else:
        solutions += get_hits3(count)
    
print('\nSolution:',solutions,'Run Time:',time()-start,'\n')
#solution: 44680
