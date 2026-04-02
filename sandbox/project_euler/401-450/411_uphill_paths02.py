#  -----------------------------------------------------------------------------
#  Uphill paths
#  Problem 411
#  https://projecteuler.net/problem=411
#  -----------------------------------------------------------------------------
import bisect
#  -----------------------------------------------------------------------------
def generate_points(n):
  if n == 1:
    return [[0]]
  points = [None for x in range(n)]
  x = 1
  y = 1
  points[x] = y
  while True:
    x = (3 * x) % n
    y = (2 * y) % n
    ys = points[x]
    if ys is None:
      points[x] = y
    elif type(ys) is int:
      if y == ys:
        break
      points[x] = {y, ys}
    else:
      if y in ys:
        break
      ys.add(y)
  return points
#  -----------------------------------------------------------------------------
def find_path(points):
  s = []
  for ys in points:
    if type(ys) is int:
      ix = bisect.bisect_right(s, ys)
      if ix >= len(s):
        s.append(ys)
      else:
        s[ix] = ys
    elif ys is not None:
      ix = 0
      for y in sorted(ys):
        ix = bisect.bisect_right(s, y, lo=ix)
        if ix >= len(s):
          s.append(y)
        else:
          s[ix] = y
  return len(s)
#  -----------------------------------------------------------------------------
def t411(n):
  sigma = 0
  for k in range(1, n + 1):
    points = generate_points(k**5)
    s = find_path(points)
    sigma += s
    print("%2d %8d %8d" % (k, sigma, s))
  return sigma
#  -----------------------------------------------------------------------------
print(f'Solution: {t411(30)}')
#  -----------------------------------------------------------------------------
#  solution: 9936352
#  -----------------------------------------------------------------------------
