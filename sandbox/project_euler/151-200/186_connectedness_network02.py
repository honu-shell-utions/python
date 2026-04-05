from time import time

start = time()
N = 10**6

def gen():
    s = []
    k = 1
    while True:
        if k <= 55:
            s.append((100003 - 200003*k + 300007*k*k*k) % N)
            k += 1
        else:
            s.append((s[-24] + s[-55]) % N)
        yield s[-1]
                 
friends = []
for n in range(N):
    friends.append([n])

PM = 524287
num = gen()
    
calls = 0
certain_percent = round(0.99 * N)

while len(friends[PM]) < certain_percent:
    i = next(num)
    j = next(num)
    if i == j:
        continue
    calls += 1
    add_book1, add_book2 = friends[i], friends[j]
    if add_book1 is add_book2:
        continue
    if len(add_book2) > len(add_book1):
        add_book1, add_book2 = add_book2, add_book1
    add_book1.extend(add_book2)
    for k in add_book2:
        friends[k] = add_book1

print(f'Solution: {calls}, Run-Time: {time()-start}')
#solution: 2325629
