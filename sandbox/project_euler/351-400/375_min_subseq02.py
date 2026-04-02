#  -----------------------------------------------------------------------------
#  Minimum of subsequences
#  Problem 375
#  https://projecteuler.net/problem=375
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def solve(N):
    M  = 0 
    ai  = [0] 
    sai  = 0 
    li  = [0] 
    S  = 290797
    bar  = 50515093
    for j in range(N):
        S  = (S*S) % bar
        jj  = 0 
        jjs  = 0 
        js  = len(ai)-1
        while(jjs <= js and S < ai[js-jjs]):
            sai -= ai[js-jjs]*li[js-jjs] 
            del ai[len(ai)-1]
            jj += li[js-jjs] 
            jjs += 1 
            del li[len(li)-1]
        sai += (jj+1)*S 
        ai.append(S) 
        li.append(jj+1)
        M += sai
        if(j % (N/10) == 0 or j  == N-1):
            solution = M
    return solution
#  -----------------------------------------------------------------------------
for n in [2,3,5,10,20,10**2,10**3,10**4,2*10**9]:
    start = time()
    print(f'n = {n:6}: {solve(n):20}, Run-Time: {time()-start:6.3f}')
#  -----------------------------------------------------------------------------
# 14598198  for solve(2)
# 44119381  for solve(3)
# 104348007 for solve(5)
# 432256955 for solve(10)
# 1264201746 for solve(20)
# 27022904418 for solve(10**2)
# 322833621931 for solve(10**3)
# 3264567774119 for solve(10**4)
# 7435327983715286168 solve(2*10**9)
#  -----------------------------------------------------------------------------
