#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
def rnge(a, b):
  return [b * (2 * a - b - 1), b * (2 * a - b + 1)]
#-------------------------------------------------------------------------------
def ceildiv(a, b):
  return -(-a // b)
#-------------------------------------------------------------------------------
def rec(init, rang, dept):
  res = 0
  strt = (init + ceildiv(rang[0], init)) // 2
  ed = (init + ceildiv(rang[1], init)) // 2
  for k in range(strt, 1 + ed):
    nrang = rnge(k, init)
    nrang[0] += 1
    nrang[0] = max(nrang[0], rang[0])
    nrang[1] = min(nrang[1], rang[1])
    if k == init:
      res += dept * (nrang[1] - nrang[0] + 1)
    else:
      res += rec(k, nrang, dept + 1)
  return res
#-------------------------------------------------------------------------------
for D in [5,6,10,12,14]:
    start = time()
    begin = 10 ** (D - 1)
    end = 10 ** D - 1
    init = 7 * 10 ** ((D - 2) // 2) if D % 2 == 0 else 2 * 10 ** ((D - 1) // 2)
    res = rec(init, [begin, end], 1)
    res /= (end - begin + 1)
    print(f'Solution for D = {D}: {round(res,10)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
#D = 5  # Answer: 3.2102888889
#D = 6  # Answer: 3.3431844444
#D = 10  # Answer: 3.9456584348
#D = 12  # Answer: 4.2038288238
#D = 14  # Answer: 4.4474011180
#-------------------------------------------------------------------------------
