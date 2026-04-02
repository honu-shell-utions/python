#-------------------------------------------------------------------------------
##Investigating in how many ways objects of two different colours can be grouped
##Problem 181
##Having three black objects B and one white object W they
##can be grouped in 7 ways like this:
##
##(BBBW)(B,BBW)(B,B,BW)(B,B,B,W)(B,BB,W)(BBB,W)(BB,BW)
##
##In how many ways can sixty black objects B and forty
##white objects W be thus grouped?
#-------------------------------------------------------------------------------
from random import randint
#-------------------------------------------------------------------------------
def get_sol(black,white):
    sol = []
    front_tot = 0
    back_tot = 0
    while front_tot + back_tot < black + white:
        first,second = pairs[randint(0,len(pairs)-1)]
        if first == 0 and second == 0:
            continue
        if front_tot + first <= black and back_tot + second <= white:
            front_tot += first  
            back_tot += second
            sol.append([first,second])
    return sorted(sol,reverse=True)

limit = 10**3
black = 3
white = 1
pairs = []
for b in range(black+1):
    for w in range(white+1):
        pairs.append((b,w))
        
solutions = []
for _ in range(limit):
    sol = get_sol(black,white)
    if not sol in solutions:
        solutions.append(sol)

for s in solutions:
    print(s)
#-------------------------------------------------------------------------------
#solution: 83735848679360680
#-------------------------------------------------------------------------------
