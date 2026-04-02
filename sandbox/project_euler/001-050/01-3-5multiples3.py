#  -----------------------------------------------------------------------------
#  If we list all the natural numbers below 10 that are multiples of 3 or 5,
#  we get 3, 5, 6 and 9. The sum of these multiples is 23.
#  Find the sum of all the multiples of 3 or 5 below 1000.
#  -----------------------------------------------------------------------------
##multiple = 3
##bigN = 999
##littleN = bigN // multiple
##total = multiple*littleN*(littleN+1)/2
##print(int(total))
##
##multiple = 5
##bigN = 999
##littleN = bigN // multiple
##total = total + multiple*littleN*(littleN+1)/2
##print(int(total))
##
##multiple = 15
##bigN = 999
##littleN = bigN // multiple
##total = total - multiple*littleN*(littleN+1)/2
##print(int(total))

class euler_01:
    def __init__(self,m1,m2,limit):
        self.limit = limit
        self.m1 = m1
        self.m2 = m2
        self.total = self.compute_sum()
    #  ------------------------------------------------------------------------
    def compute_sum(self):
        little_n = self.limit // self.m1
        total = self.m1*little_n*(little_n+1)//2
        
        little_n = self.limit // self.m2
        total += self.m2*little_n*(little_n+1)//2
        
        little_n = self.limit // (self.m1 * self.m2)
        total -= self.m1*self.m2*little_n*(little_n+1)//2

        if self.limit % self.m1 == 0 or self.limit % self.m2 == 0:
            total -= self.limit

        return total  
    #  ------------------------------------------------------------------------
    def get_sum(self):
        return self.total
    #  ------------------------------------------------------------------------
for exp in range(3,11):
    instance = euler_01(3,5,10**exp)
    print(instance.get_sum())
#  -----------------------------------------------------------------------------
#  solution: 233168
#  -----------------------------------------------------------------------------
