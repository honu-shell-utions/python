################################################################################
##Modified Fibonacci golden nuggets
##Problem 140
################################################################################
from time import time
# a(n + 4) = -a(n) + 7 a(n + 2) + 7 (for all n>=1), from WolfRam Alpha vai Calvin
def make_list():
    seq_list = [2,5,21,42]
    for k in range(4,100):
        seq_list.append(-seq_list[k-4]+7*seq_list[k-2]+7)
    return seq_list
################################################################################
start = time()
seq_list = make_list()
print('The solution:',sum(seq_list[:30]),'Run Time:',time()-start)
################################################################################
#solution: 5673835352990
################################################################################
