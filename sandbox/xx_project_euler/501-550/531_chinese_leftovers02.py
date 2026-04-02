#  -----------------------------------------------------------------------------
#  Chinese leftovers
#  Problem 531
#  https://projecteuler.net/problem=531
#  
#  Let g(a,n,b,m) be the smallest non-negative solution x to the system:
#  x = a mod n
#  x = b mod m
#  if such a solution exists, otherwise 0.
#  
#  E.g. g(2,4,4,6)=10, but g(3,4,4,6)=0.
#  
#  Let φ(n) be Euler's totient function.
#  
#  Let f(n,m)=g(φ(n),n,φ(m),m)
#  
#  Find ∑ f(n,m) for 1000000 ≤ n < m < 1005000
#  -----------------------------------------------------------------------------
from sympy.ntheory.factor_ import totient
from sympy.ntheory.modular import solve_congruence
from time import time
#  -----------------------------------------------------------------------------
class euler_531:
    def __init__(self,bot,top):
        self.bot = bot
        self.top = top
    #  ------------------------------------------------------------------------
    def get_sol(self,n,m):
        a = totient(n)
        b = totient(m)
        temp = solve_congruence((a,n),(b,m))
        if temp is not None:
            return temp[0]
        else:
            return 0
    #  ------------------------------------------------------------------------
    def get_answer(self):
        result = 0
        for m in range(self.bot+1,self.top):
            if m % 250 == 0:
                print(m, result)
            for n in range(bot,m):
                result += self.get_sol(n,m)
        return result
#  -----------------------------------------------------------------------------
bot = 10**6
top = bot + 5*10**3
instance = euler_531(bot,top)
print(instance.get_answer())
#  -----------------------------------------------------------------------------
#  solution: 4515432351156203105
#  -----------------------------------------------------------------------------
