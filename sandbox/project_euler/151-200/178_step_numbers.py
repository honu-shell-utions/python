#-------------------------------------------------------------------------------
# 178_step_numbers.py
# 
# 
# Problem 178 - Step Numbers
# Consider the number 45656.
# 
# It can be seen that each pair of consecutive digits of 45656 has a difference
# of one.
# 
# A number for which every pair of consecutive digits has a difference of one is
# called a step number.
# 
# A pandigital number contains every decimal digit from 0 to 9 at least once.
# 
# How many pandigital step numbers less than 10**40 are there?
#-------------------------------------------------------------------------------
def is_pandigital(n):
    n_str = str(n)
    if '0' in n_str and '9' in n_str:
        return True
    return False
#-------------------------------------------------------------------------------
def is_step(n):
    n_list = list(str(n))
    for k in range(len(n_list)-1):
        if abs(int(n_list[k])-int(n_list[k+1])) != 1:
            return False
    return True
#-------------------------------------------------------------------------------
first_pan_step = 9876543210
pan_steps = 0
for n in range(first_pan_step,10**40):
    if str(n)[:1] != '9': continue
    if is_step(n) and is_pandigital(n):
        print(n)
        pan_steps += 1     
print(pan_steps)
#-------------------------------------------------------------------------------
#solution: 126461847755
#-------------------------------------------------------------------------------
