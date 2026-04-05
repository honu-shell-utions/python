#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
def cube_sum(cubes):
    s = 0
    for x in cubes:
        s += x[3] * x[4] * x[5]
    return s
#-------------------------------------------------------------------------------
def get_intersections(cubes, inters):
    ret = []
    for i in range(len(inters)):
        a = inters[i]
        for j in range(a[9] + 1, len(cubes)):
            b = cubes[j]
            if cube_intersect(a, b):
                inter = get_intersection(a, b)
                inter[9] = j
                ret.append(inter)
            else:
                if a[6] < b[0]:
                    break
    return ret
#-------------------------------------------------------------------------------
def get_intersection(a, b):
    x = max(a[0], b[0])
    rx = min(a[6], b[6])
    y = max(a[1], b[1])
    ry = min(a[7], b[7])
    z = max(a[2], b[2])
    rz = min(a[8], b[8])
    return [x, y, z, rx - x, ry - y, rz - z, rx, ry, rz, 0]
#-------------------------------------------------------------------------------
def cube_intersect(a, b):
    if a[6] < b[0] or b[6] < a[0]:
        return False  # x doesn't overlap
    if a[7] < b[1] or b[7] < a[1]:
        return False  # y doesn't overlap
    if a[8] < b[2] or b[8] < a[2]:
        return False  # z doesn't overlap
    # x, y, z overlap
    return True
#-------------------------------------------------------------------------------
def p212():
    fg = [0] * (target * 6 + 1)
    for k in range(6 * target + 1):
        if k <= 55:
            fg[k] = (100003 - 200003 * k + 300007 * k ** 3) % 1000000
        else:
            fg[k] = (fg[k - 24] + fg[k - 55]) % 1000000
            
    cubes = []
    for i in range(target):
        n = 6 * (i + 1)
        x, y, z, dx, dy, dz = fg[n - 5] % 10000, fg[n - 4] % 10000, fg[n - 3] % 10000, 1 + fg[n - 2] % 399, 1 + fg[
            n - 1] % 399, 1 + fg[n] % 399
        cubes.append([x, y, z, dx, dy, dz, x + dx, y + dy, z + dz, i])

    # sorting on x, y, z
    cubes = sorted(cubes, key=lambda t: (t[0], t[1], t[2]))
    for i in range(len(cubes)):
        cubes[i][9] = i
    s = cube_sum(cubes)
    inters = cubes[:]
    m = -1
    while len(inters) > 0:
        inters = get_intersections(cubes, inters)
        print(f'Found {len(inters)} intersections')
        s = s + m * cube_sum(inters)
        m *= -1
    return s
#-------------------------------------------------------------------------------
start = time()
target = 50000
ans = p212()
print(f'Solution: {ans}, Run-Time: {time() - start}')
#-------------------------------------------------------------------------------
# solution: 328968937309
#-------------------------------------------------------------------------------
