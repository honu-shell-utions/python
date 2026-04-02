# p-161_triominoes.py
# 
# A triomino is a shape consisting of three squares joined via the edges. There
# are two basic forms:
# XX XXX
# X
# If all possible orientations are taken into account there are six:
# XX  XX  X     X  X  XXX
# X    X  XX   XX  X
#                  X
#
# 
# Any n by m grid for which n by m is divisible by 3 can be tiled with
# triominoes.
# If we consider tilings that can be obtained by reflection or rotation from
# another tiling as different there are 41 ways a 2 by 9 grid can be tiled with
# triominoes:
#
# In how many ways can a 9 by 12 grid be tiled in this way by triominoes?
#
# 20574308184277971  <--- two different sources one c, one java solution
# 20574308184277971  but I haven't checked it yet...
# -----------------------------------------------------------------------------
b = [[False for j in range(12)] for i in range(9)]

figures = [((1,0),(0,1)),((0,1),(1,1)),((1,0),(1,1)),
     ((0,1),(-1,1)),((1,0),(2,0)),((0,1),(0,2))]

s = [{} for i in range(len(b[0]))]

def p(i, j, f):
    if b[i][j]:
        return False
    for x in f:
        if not(0 <= i + x[0] < len(b) and 0 <= j + x[1] < len(b[0])) or \
           b[i+x[0]][j+x[1]]:
            return False
    b[i][j] = True
    for x in f:
        b[i+x[0]][j+x[1]] = True
    return True

def q(i, j, f):
    b[i][j] = False
    for x in f:
        b[i+x[0]][j+x[1]] = False

def step(i, j, m):
    if i == len(b):
        t = tuple(tuple(x) for x in b)
        if t in s[j]:
            s[j][t] += m
        else:
            s[j][t] = m
    elif b[i][j]:
        step(i + 1, j, m)
    else:
        for f in figures:
            if p(i, j, f):
                step(i + 1, j, m)
                q(i, j, f)

step(0, 0, 1)
for j in range(1, len(b[0])):
    for bb in s[j-1]:
        b = [list(x) for x in bb]
        step(0, j, s[j-1][bb])

print(sum(x for x in s[-1].values()))


# -----------------------------------------------------------------------------
# solution: 20574308184277971
# -----------------------------------------------------------------------------
