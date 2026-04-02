################################################################################
##Digit power sum
##Problem 119
##The number 512 is interesting because it is equal to
##the sum of its digits raised to some power: 5 + 1 + 2 = 8,
##and 8^3 = 512. Another example of a number with this property
##is 614656 = 28^4.
##
##We shall define a(subn) to be the nth term of this sequence
##and insist that a number must contain at least two digits to
##have a sum.
##
##You are given that a(sub2) = 512 and a(sub10) = 614656.
##
##Find a(sub30).
################################################################################
from operator import itemgetter
from time import time
################################################################################
def sum_of_digits(num):
    total = 0
    str_num = str(num)
    for d in str_num:
        total += int(d)
    return total
################################################################################
def pe_119():
    solutions = []
    for base in range(2,100):
        for exponent in range(2,11):
            result = base**exponent
            if result > 9 and sum_of_digits(result) == base:
                solutions.append([base,exponent,result])
    return solutions
################################################################################
start = time()
solutions = pe_119()
solutions = sorted(solutions, key=itemgetter(2))
print('The solution for n = 30:',solutions[29],'Run Time:',time()-start)

k = 1
for s in solutions:
    print(k,'\t',s)
    k += 1
################################################################################
#solution: 248155780267521
################################################################################
