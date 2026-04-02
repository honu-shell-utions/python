##Primes with runs
##Problem 111
##Considering 4-digit primes containing repeated digits it is
##clear that they cannot all be the same: 1111 is divisible by
##11, 2222 is divisible by 22, and so on. But there are nine
##4-digit primes containing three ones:
##
##1117, 1151, 1171, 1181, 1511, 1811, 2111, 4111, 8111
##
################################################################################
##We shall say that M(n, d) represents the maximum number of
##repeated digits for an n-digit prime where d is the repeated
##digit, N(n, d) represents the number of such primes,
##and S(n, d) represents the sum of these primes.
##
##So M(4, 1) = 3 is the maximum number of repeated digits
##for a 4-digit prime where one is the repeated digit, there
##are N(4, 1) = 9 such primes, and the sum of these primes
##is S(4, 1) = 22275. It turns out that for d = 0, it
##is only possible to have M(4, 0) = 2 repeated digits,
##but there are N(4, 0) = 13 such cases.
##
##In the same way we obtain the following results for 4-digit primes.
##---------------------------------
##Digit,d   M(4,d) N(4,d)   S(4,d)
##---------------------------------
##  0	    2	    13	    67061
##  1	    3	     9	    22275
##  2	    3	     1	     2221
##  3	    3	    12	    46214
##  4	    3	     2	     8888
##  5	    3	     1	     5557
##  6	    3	     1	     6661
##  7	    3	     9	    57863
##  8	    3	     1	     8887
##  9	    3	     7	    48073
##---------------------------------
##For d = 0 to 9, the sum of all S(4, d) is 273700.
##
##Find the sum of all S(10, d).
##
################################################################################
from sympy import nextprime
from time import time
################################################################################
def M(prime):
    temp = [0]*10
    strPrime = str(prime)
    for d in '0123456789':
        temp[int(d)] = strPrime.count(d)
    return temp.index(max(temp)),max(temp)
################################################################################
bottom = 10**9
M_list = [0]*10
N_list = [0]*10
S_list = [0]*10
big_sum = 0

prime = nextprime(bottom)
while True:
    digit,count = M(prime)
    if M_list[digit] < count:
        M_list[digit] = count
    prime = nextprime(prime)
    if prime >= bottom*10:
        break

prime = nextprime(bottom)
while True:
    digit,count = M(prime)
    if count == M_list[digit]:
        N_list[digit] += 1
        S_list[digit] += prime
        big_sum += prime
    prime = nextprime(prime)
    if prime >= bottom*10:
        break

print('Digit,d  M(4,d) N(4,d)   S(4,d)')
print('-------------------------------')
for i in range(len(M_list)):
    print(i,'\t',M_list[i],'\t',N_list[i],'\t',S_list[i])
print('-------------------------------')
print('Sum of the sums:',big_sum)
################################################################################
#solution: 612407567715
################################################################################
