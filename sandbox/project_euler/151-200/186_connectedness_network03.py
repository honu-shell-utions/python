from time import time
from random import choice

def euler_186():
    calls = 0
    while True:
        call_from = choice(numbers)
        call_to = choice(numbers)
        if call_from == call_to:
            continue  
        calls += 1  
        friends[call_from] = friends[call_from].union(friends[call_to])
        for f in friends[call_from]:
            friends[f] = friends[f].union(friends[call_from])
            if len(friends[f]) >= limit:
                return calls

start = time()
limit = 10**6
friends = []
numbers = []
for n in range(limit):
    friends.append({n})
    numbers.append(n)
limit = int(0.99*limit)    
calls = euler_186()

print(f'Solution: {calls}, Run-Time: {time()-start}')
#solution: 2325629
