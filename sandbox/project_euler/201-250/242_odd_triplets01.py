#-------------------------------------------------------------------------------
## Odd Triplets
## Problem 242
## 
## Given the set {1,2,...,n}, we define f(n,k) as the number
## of its k-element subsets with an odd sum of elements. For
## example, f(5,3) = 4, since the set {1,2,3,4,5} has four
## 3-element subsets having an odd sum of elements,
## i.e.: {1,2,4}, {1,3,5}, {2,3,4} and {2,4,5}.
## 
## When all three values n, k and f(n,k) are odd, we say that they make 
## an odd-triplet [n,k,f(n,k)].
## 
## There are exactly five odd-triplets with n ≤ 10, namely:
## [1,1,f(1,1) = 1], [5,1,f(5,1) = 3], [5,5,f(5,5) = 1], [9,1,f(9,1) = 5]
## and [9,9,f(9,9) = 1].
## 
## How many odd-triplets are there with n ≤ 10^12 ?
#-------------------------------------------------------------------------------
from itertools import combinations
from time import time
#-------------------------------------------------------------------------------
def f(n, k):
    counter = 0
    t_lst = [x for x in range(1,n + 1)]
    for ss in combinations(t_lst, k):
        if sum(ss) % 2 != 0:
            counter += 1
    if counter % 2 != 0:
        return counter
    return 0
#-------------------------------------------------------------------------------
start = time()
limit = 10**2 #139
solution = 0
for n in range(1,limit+1,2):
    for k in range(1,limit+1,2):
        if k > n:
            break
        temp = f(n,k)
        if temp: 
            print(n,k,temp)
            solution += 1

print(f'Solution: {solution}, Run-Time: {time()-start}')           
#-------------------------------------------------------------------------------
# solution: 997104142249036713 
#-------------------------------------------------------------------------------
