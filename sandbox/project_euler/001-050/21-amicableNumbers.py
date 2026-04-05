##Let d(n) be defined as the sum of proper divisors of n
##(numbers less than n which divide evenly into n).
##If d(a) = b and d(b) = a, where a ≠ b, then a and b are
##an amicable pair and each of a and b are called amicable numbers.
##
##For example, the proper divisors of 220 are
##1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284.
##The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.
##
##Evaluate the sum of all the amicable numbers under 10000.
##################################################################################
##jim mccleery, november, 2021
##################################################################################
def properFactors(num):
    factorList = []
    for i in range(1,num):
        if num % i == 0:
            factorList.append(i)
    return factorList
##################################################################################
def d(num):
    return(sum(properFactors(num)))
##################################################################################
def isAmicable(num):
    if d(d(num)) == num and d(num) != num:
        return True
    else:
        return False    
##################################################################################
max = 10000
total = 0
for i in range(1,max):
    if isAmicable(i):
        total += i
        print(i)
print('Sum of amicable numbers less than 10000 is:',total)
##################################################################################
#solution: 31626
