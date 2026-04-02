#-------------------------------------------------------------------------------
## Sums of Digit Factorials
## Problem 254
## Define f(n) as the sum of the factorials of the digits of n.
## For example, f(342) = 3! + 4! + 2! = 32.
## 
## Define sf(n) as the sum of the digits of f(n).
## So sf(342) = 3 + 2 = 5.
## 
## Define g(i) to be the smallest positive integer n such
## that sf(n) = i. Though sf(342) is 5, sf(25) is also 5,
## and it can be verified that g(5) is 25.
## 
## Define sg(i) as the sum of the digits of g(i).
## So sg(5) = 2 + 5 = 7.
## 
## Further, it can be verified that g(20) is 267
## and ∑ sg(i) for 1 ≤ i ≤ 20 is 156.
## 
## What is ∑ sg(i) for 1 ≤ i ≤ 150?
#-------------------------------------------------------------------------------
from time import time
start = time()

#N = 20  # Answer: 156
#N = 63  # Answer: 3398
N = 150  # Answer: 8184523820510

facts = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]

def sum_of_digits(n):
    s = 0
    while n > 0:
        s += n % 10
        n//= 10
    return s

def all_nums(numDigits = 1, firstDigit = 1):
    """ Generates the sum of digits and the sum of the factorials of digits for
        numbers such that the number:
           * has numDigits digits
           * the first digit >= firstDigit > 0
           * the sequence of digits is non-descreasing
           * each digit 1 <= d <= 8 appears at most d times
    """
    for d in range(firstDigit, 9):
        if d >= numDigits:
            yield numDigits * d, numDigits * facts[d]
            maxRepeat = numDigits - 1
        else:
            maxRepeat = d
        for r in range(maxRepeat, 0, -1):
             for sg, f in all_nums(numDigits - r, d+1):
                 yield r * d + sg, r*facts[d] + f
    yield numDigits* 9, numDigits * facts[9]

def add(v1, v2):
    """ v1, v2, represent numbers with increasing sequence of digits;
        digit d appears at most d times;
        v1[d], v2[d] is the number of times the digit d appears in the
        respective addend """
    carry = 0
    res = [0]
    for d in range(1, 10):
        x = v1[d] + v2[d] + carry
        if d < 9:
            carry = x // (d+1)
            x -= carry * (d+1)
        res.append(x)
    return res

def fill_gs_1(g):
    cnt = 0
    numDigits = 1
    while cnt < N:
        for sg, f in all_nums(numDigits):
            sf = sum_of_digits(f)
            if sf <= N and g[sf] == 0:
                g[sf] = sg
                cnt += 1
                #print("***", cnt, f, sf, sg)        
                if f == 9999999:
                    return cnt
        numDigits += 1

def fill_gs_2(cnt, g):
    v = 10*[0]
    f = 9999999
    for d in range(9, 0, -1):
        v[d] = f//facts[d]
        f -= v[d] * facts[d]
    first = 9
    while cnt < N:
        if first == 9:
            incr = add(v, [0, 1, 0, 0, 0, 0, 0, 0, 0, 0]) # incr = v + 1
            first = 0
        v = add(v, incr)
        first += 1
        sg = sum(d * v[d] for d in range(1, 10))
        cnt += 1
        g[cnt] = sg
    
g = (N+1)*[0]
cnt = fill_gs_1(g)
fill_gs_2(cnt, g)

print(f'Solution: {sum(g)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 8184523820510
#-------------------------------------------------------------------------------
