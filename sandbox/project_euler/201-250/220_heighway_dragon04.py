from math import sin, cos, radians
def new_string(old_string):
    new_str = ''
    for c in old_string:
        if c == 'a':
            new_str += 'aRbFR'
        elif c == 'b':
            new_str += 'LFaLb'
        else:
            new_str += c
    return new_str

z = complex(0,0)
points = [z]
theta = 90
path = 'Fa'
for k in range(10):
    path = new_string(path)
        
for c in path:   
    if c == 'F':
        dx = round(cos(radians(theta)))
        dy = round(sin(radians(theta)))
        z += complex(dx,dy)
        points.append(z)
    elif c == 'R':
        theta -= 90
    elif c == 'L':
        theta += 90

print(points[500])
#-------------------------------------------------------------------------------
