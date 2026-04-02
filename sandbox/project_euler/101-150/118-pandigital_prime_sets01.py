from sympy import isprime
from itertools import combinations, permutations, chain
from time import time
    
def make_primes_pool():
    lst_primes = []
    temp = list(chain(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9' ], r) for r in range(1, 9)))
    for tmp in temp:
        for n in tmp:
            n = int(''.join(n))
            if isprime(n):
                lst_primes.append(n)
    return lst_primes

def test8_1():
    count = 0
    for p8 in pan_primes8:
        for p1 in pan_primes1:
            temp = ''.join(sorted(str(p1)+str(p8)))
            if temp == '123456789':
                count += 1
    return count

def test7_2():
    count = 0
    for p7 in pan_primes7:
        for p2 in pan_primes2:
            temp = ''.join(sorted(str(p2)+str(p7)))
            if temp == '123456789':
                count += 1
    return count

def test7_1_1():
    count = 0
    combos = list(combinations(pan_primes1,2))
    for p7 in pan_primes7:
        for c in combos:
            temp = ''.join(sorted(str(p7)+str(c[0])+str(c[1])))
            if temp == '123456789':
                count += 1
    return count
           
def test6_3():
    count = 0
    for p6 in pan_primes6:
        for p3 in pan_primes3:
            temp = ''.join(sorted(str(p6)+str(p3)))
            if temp == '123456789':
                count += 1
    return count

def test6_2_1():
    count = 0
    for p6 in pan_primes6:
        for p2 in pan_primes2:
            for p1 in pan_primes1:
                temp = ''.join(sorted(str(p6)+str(p2)+str(p1)))
                if temp == '123456789':
                    count += 1
    return count

def test6_1_1_1():
    count = 0
    combos = list(combinations(pan_primes1,3))
    for p6 in pan_primes6:
        for c in combos:
            temp = ''.join(sorted(str(p6)+str(c[0])+str(c[1])+str(c[2])))
            if temp == '123456789':
                count += 1
    return count

def test5_4():
    count = 0
    for p5 in pan_primes5:
        for p4 in pan_primes4:
            temp = ''.join(sorted(str(p5)+str(p4)))
            if temp == '123456789':
                count += 1
    return count

def test5_3_1():
    count = 0
    for p5 in pan_primes5:
        for p3 in pan_primes3:
            for p1 in pan_primes1:
                temp = ''.join(sorted(str(p5)+str(p3)+str(p1)))
                if temp == '123456789':
                    count += 1
    return count

def test5_2_2():
    count = 0
    combos = list(combinations(pan_primes2,2))
    for c in combos:
        for p5 in pan_primes5:
            temp = ''.join(sorted(str(c[0])+str(c[1])+str(p5)))
            if temp == '123456789':
                count += 1
    return count

def test5_2_1_1():
    count = 0
    combos = list(combinations(pan_primes1,2))
    for p5 in pan_primes5:
        for p2 in pan_primes2:
            for c in combos:
                temp = ''.join(sorted(str(p5)+str(p2)+str(c[0])+str(c[1])))
                if temp == '123456789':
                    count += 1
    return count

def test5_1_1_1_1():
    count = 0
    combos = list(combinations(pan_primes1,4))
    for p5 in pan_primes5:
        for c in combos:
            temp = ''.join(sorted(str(p5)+str(c[0])+str(c[1])+\
                                  str(c[2])+str(c[3])))
            if temp == '123456789':
                count += 1
    return count

def test4_4_1():
    count = 0
    combos = list(combinations(pan_primes4,2))
    for c in combos:
        for p1 in pan_primes1:
            temp = ''.join(sorted(str(c[0])+str(c[1])+str(p1)))
            if temp == '123456789':
                count += 1
    return count

def test4_3_2():
    count = 0
    for p4 in pan_primes4:
        for p3 in pan_primes3:
            for p2 in pan_primes2:
                temp = ''.join(sorted(str(p4)+str(p3)+str(p2)))
                if temp == '123456789':
                    count += 1
    return count

def test4_3_1_1():
    count = 0
    combos = list(combinations(pan_primes1,2))
    for p4 in pan_primes4:
        for c in combos:
            for p3 in pan_primes3:
                temp = ''.join(sorted(str(p4)+str(p3)+str(c[0])+str(c[1])))
                if temp == '123456789':
                    count += 1
    return count

def test4_2_2_1():
    count = 0
    combos = list(combinations(pan_primes2,2))
    for p4 in pan_primes4:
        for c in combos:
            for p1 in pan_primes1:
                temp = ''.join(sorted(str(p4)+str(p1)+str(c[0])+str(c[1])))
                if temp == '123456789':
                    count += 1
    return count

def test4_2_1_1_1():
    count = 0
    combos = list(combinations(pan_primes1,3))
    for p4 in pan_primes4:
        for p2 in pan_primes2:
            for c in combos:
                temp = ''.join(sorted(str(p4)+str(p2)+str(c[0])+str(c[1])+str(c[2])))
                if temp == '123456789':
                    count += 1
    return count

def test3_3_3():
    count = 0
    combos = list(combinations(pan_primes3,3))
    for c in combos:
        temp = ''.join(sorted(str(c[0])+str(c[1])+str(c[2])))
        if temp == '123456789':
            count += 1
    return count

def test3_3_2_1():
    count = 0
    combos = list(combinations(pan_primes3,2))
    for c in combos:
        for p2 in pan_primes2:
            for p1 in pan_primes1:
                temp = ''.join(sorted(str(c[0])+str(c[1])+str(p2)+str(p1)))
                if temp == '123456789':
                    count += 1
    return count

def test3_3_1_1_1():
    count = 0
    combos1 = list(combinations(pan_primes1,3))
    combos3 = list(combinations(pan_primes3,2))
    for c1 in combos1:
        for c3 in combos3:
            temp = ''.join(sorted(str(c1[0])+str(c1[1])+str(c1[2])+str(c3[0])+str(c3[1])))
            if temp == '123456789':
                count += 1
    return count

def test3_2_2_2():
    count = 0
    combos = list(combinations(pan_primes2,3))
    for c in combos:
        for p3 in pan_primes3:
            temp = ''.join(sorted(str(c[0])+str(c[1])+str(c[2])+str(p3)))
            if temp == '123456789':
                count += 1
    return count

def test3_2_2_1_1():
    count = 0
    combos2 = list(combinations(pan_primes2,2))
    combos3 = list(combinations(pan_primes1,2))
    for c2 in combos2:
        for c3 in combos3:
            for p3 in pan_primes3:
                temp = ''.join(sorted(str(p3)+str(c2[0])+str(c2[1])+str(c3[0])+str(c3[1])))
                if temp == '123456789':
                    count += 1
    return count

def test3_2_1_1_1_1():
    count = 0
    combos = list(combinations(pan_primes1,4))
    for p3 in pan_primes3:
        for p2 in pan_primes2:
            for c in combos:
                temp = ''.join(sorted(str(p3)+str(p2)+str(c[0])+str(c[1])+\
                            str(c[2])+str(c[3])))
                if temp == '123456789':
                    count += 1
    return count

def test2_2_2_1_1_1():
    count = 0
    combos1 = list(combinations(pan_primes1,3))
    combos2 = list(combinations(pan_primes2,3))
    for c1 in combos1:
        for c2 in combos2:
            temp = ''.join(sorted(str(c1[0])+str(c1[1])+str(c1[2])+\
                        str(c2[0])+str(c2[1])+str(c2[2])))
            if temp == '123456789':
                count += 1
    return count

def test2_2_2_2_1():
    count = 0
    combos = list(combinations(pan_primes2,4))
    for p1 in pan_primes1:
        for c in combos:
            temp = ''.join(sorted(str(p1)+str(c[0])+str(c[1])+str(c[2])+str(c[3])))
            if temp == '123456789':
                count += 1
    return count

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

totals = []
totals.append(test8_1())
totals.append(test7_2())
totals.append(test7_1_1())
totals.append(test6_3())
totals.append(test6_2_1())
totals.append(test6_1_1_1())
totals.append(test5_4())
totals.append(test5_3_1())
totals.append(test5_2_2())
totals.append(test5_2_1_1())
totals.append(test5_1_1_1_1())
totals.append(test4_4_1())
totals.append(test4_3_2())
totals.append(test4_3_1_1())
totals.append(test4_2_2_1())
totals.append(test4_2_1_1_1())
totals.append(test3_3_3())
totals.append(test3_3_2_1())
totals.append(test3_3_1_1_1())
totals.append(test3_2_2_2())
totals.append(test3_2_2_1_1())
totals.append(test3_2_1_1_1_1())
totals.append(test2_2_2_2_1())
totals.append(test2_2_2_1_1_1())

print('\nSolution:',sum(totals),'Run Time:',time()-start,'\n')
#solution: 44680
