#-------------------------------------------------------------------------------
##Obtuse Angled Triangles
##Problem 210
##Consider the set S(r) of points (x,y) with integer
##coordinates satisfying |x| + |y| ≤ r.
##
##Let O be the point (0,0) and C the point (r/4,r/4). 
##Let N(r) be the number of points B in S(r), so that
##the triangle OBC has an obtuse angle, i.e. the largest
##angle α satisfies 90°<α<180°.
##
##So, for example, N(4)=24 and N(8)=100.
##
##What is N(1,000,000,000)?
#-------------------------------------------------------------------------------
from time import time
#-------------------------------------------------------------------------------
def is_valid(x,y):
    if abs(x) + abs(y) <= radius:
        return True
    else:
        return False
#-------------------------------------------------------------------------------
def is_obtuse(x,y):
    x1,y1 = fixed_point
    
    a_squared = x**2 + y**2
    b_squared = (x-x1)**2 + (y-y1)**2
    c_squared = x1**2 + y1**2

    if a_squared > b_squared + c_squared:
        return True
    if b_squared > a_squared + c_squared:
        return True
    if c_squared > a_squared + b_squared:
        return True
    return False
#-------------------------------------------------------------------------------
start = time()
radius = 10**9
fixed_point = (radius/4,radius/4)
hits = 0
for x in range(-radius,radius+1):
    for y in range(x+1,radius+1):
        if is_valid(x,y):
            if is_obtuse(x,y):
                hits += 1
print(f'Solution: {2*hits}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 1598174770174689458
#-------------------------------------------------------------------------------
