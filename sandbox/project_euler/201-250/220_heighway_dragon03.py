
"""
    This was indeed a fun and rewarding problem: after a little
    analysis, I was able to create a remarkably simple
    algorithm.

    The first important realization is that D(n) is a prefix of
    D(n+1), so the number 50 in D(50) is not really important -
    we might as well think of D as an infinite sequence.

    Define the function dragon(n) to be the position reached
    after n steps, so dragon(0) = (0,0), dragon(1) = (0,1), and
    dragon(500) = (18,16).

    The next important realization is related to the fractal
    nature of the dragon curve: If we take only the
    even-numbered points, we get the same curve scaled and
    rotated by 45 degrees. Thus if dragon(n) = (x, y), then
    dragon(2n) = (x+y, y-x).

    We also know that the dragon curve alternates vertical and
    horizontal moves. Thus for even n, dragon(n) has the same
    x-coordinate as dragon(n+1), and for odd n, they have the
    same y-coordinate.

    So if we have
      dragon(n) = (x,y)
      dragon(n+1) = (u,v)

    Then we can calculate
      dragon(2n) = (x+y, y-x)
      dragon(2n+1) = (x+y, v-u)
      dragon(2n+2) = (u+v, v-u)

    The algorithm recursively calculates dragon(n) and dragon(n+1)
    at the same time. At each step there is a single recursive call
    with n = n/2.

    It calculates dragon(10^12) instantly, and dragon(10^10000)
    takes about 2 seconds.

"""

def dragon(n):
    if n == 0:
        return ((0, 0), (0, 1))

    (x, y), (u, v) = dragon(n//2)

    if n % 2 == 0:
        return ((x+y, y-x), (x+y, v-u))
    else:
        return ((x+y, v-u), (u+v, v-u))

x,y = dragon(500)[0]
print(f'Dragon(500) = ({x},{y})')
x,y = dragon(10**12)[0]
print(f'Dragon(10**12) = ({x},{y})')

# 139776,963904
