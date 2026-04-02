def points(dart):
    left = dart[:1]
    if left == 'S':
        mult = 1
    elif left == 'D':
        mult = 2
    else:
        mult = 3      
    return mult*int(dart[1:])

def score(game):
    total = 0
    for dart in game.split():
        total += points(dart)
    return total

from time import time
start = time()
darts = [m+str(n) for m in 'SDT' for n in range(1, 21)] + ['S25', 'D25']
doubles = [d for d in darts if d[0]=='D']


chkouts = set(doubles)

for d in doubles:
    for a in darts:
        chkouts.add(a+' '+d)
        for b in darts:
            if a<b: chkouts.add(a+' '+b+' '+d)
            else:   chkouts.add(b+' '+a+' '+d)

total = 0
for game in chkouts:
    temp = score(game)
    if temp < 100:
        total += 1

print(total, time()-start)
#solution: 38182

