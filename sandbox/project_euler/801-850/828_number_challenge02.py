#  -----------------------------------------------------------------------------
#  Numbers Challenge
#  Problem 828
#  https://projecteuler.net/problem=828
#  -----------------------------------------------------------------------------
from time import time
#  -----------------------------------------------------------------------------
def read_file():
    tot_and_six = []
    n = 0
    in_file = open("828_number_challenge.txt","r")
    try:
        for line in in_file.readlines():
            line = line.strip()
            target = line[:3]
            n1,n2,n3,n4,n5,n6 = line[4:].split(',')
            tot_and_six.append((int(target),int(n1),int(n2),int(n3),int(n4),int(n5),int(n6)))
            n += 1                  
    except IOError:
        print ("File Access Error")
    finally:
        in_file.close()
        print ("total number of records:\t",n)
    return tot_and_six
#  -----------------------------------------------------------------------------
def solve(xs, target):
  if xs == [target]:
    return True
  for i, x in enumerate(xs):
    for j, y in enumerate(xs[:i]):
      zs = set(z for z in [x+y, x-y, y-x, x*y] if z > 0)
      if x%y == 0:
        zs.add(x//y)
      if y%x == 0:
        zs.add(y//x)
      if any(solve(xs[:j] + xs[j+1:i] + xs[i+1:] + [z], target) for z in zs):
        return True
  return False

#  -----------------------------------------------------------------------------
start = time()
total = 0
records = read_file()
for k,r in enumerate(records):
    target = r[0]
    xs = r[1:]
    res = 10**9
    for mask in range(1 << len(xs)):
        ys = [x for i, x in enumerate(xs) if mask & (1 << i)]
        if sum(ys) < res and solve(ys, target):
              res = sum(ys)
    if res == 10**9:
        res = 0
    total += 3**(k+1) * res
    
print(f'Solution: {total % 1005075251}, Run-Time: {time()-start}')
#  -----------------------------------------------------------------------------
#  solution: 148693670
#  -----------------------------------------------------------------------------
