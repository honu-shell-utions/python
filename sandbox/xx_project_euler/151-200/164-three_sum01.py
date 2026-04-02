#-------------------------------------------------------------------------------
##Numbers for which no three consecutive digits have a
##sum greater than a given value
##
##Problem 164
##How many 20 digit numbers n (without any leading zero)
##exist such that no three consecutive digits of n have
##a sum greater than 9?
#-------------------------------------------------------------------------------
def digit_sum(n):
    return sum(int(c) for c in str(n))
#-------------------------------------------------------------------------------
def test3(n):
    n_str = str(n)
    for k in range(len(n_str)-2):
        temp_str = n_str[k:k+3]
        temp_int = int(temp_str)
        if digit_sum(temp_int) > 9:
            return False
    return True
#-------------------------------------------------------------------------------
counter = 0
exp = 6
for k in range(10**exp,10**(exp+1)):
    if test3(k):
        counter += 1

print(counter)



#-------------------------------------------------------------------------------
#solution:
#-------------------------------------------------------------------------------
