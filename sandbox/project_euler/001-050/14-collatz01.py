##The following iterative sequence is defined for the set of positive integers:
##
##n → n/2 (n is even)
##n → 3n + 1 (n is odd)
##
##Using the rule above and starting with 13, we generate the following sequence:
##13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
##It can be seen that this sequence (starting at 13 and finishing at 1)
##contains 10 terms. Although it has not been proved yet (Collatz Problem),
##it is thought that all starting numbers finish at 1.
##Which starting number, under one million, produces the longest chain?
##NOTE: Once the chain starts the terms are allowed to go above one million.
###################################################################################
def num_terms(num):
    num_t = 1
    while num > 1:
        num_t += 1
        if num % 2 == 0:
            num = num // 2
        else:
            num = 3*num + 1       
    return(num_t)
###################################################################################
from time import time
start = time()
limit = 10**6
max_terms = 0
for i in range(1,limit,2):
    temp = num_terms(i)
    if temp > max_terms:
        max_terms = temp
        start_value = i
        
print(f'Starting Value: {start_value} produces: {max_terms} terms in {time()-start:5.3f} seconds.')
###################################################################################
#solution: 837799
###################################################################################
