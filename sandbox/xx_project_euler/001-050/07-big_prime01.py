##################################################################################
##By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
##we can see that the 6th prime is 13.
##What is the 10,001st prime number?
##################################################################################
##jim.mccleery, November, 2021, revised March, 2023
from sympy import isprime
##################################################################################
count = 0
i = 1
max = 10001
while count != max:
    i += 1
    if(isprime(i)):
        count += 1
print('Prime number '+str(max)+' is '+str(i)+'.')
##################################################################################
#solution: 104743 
