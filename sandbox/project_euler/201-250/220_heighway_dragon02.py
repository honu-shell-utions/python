#-------------------------------------------------------------------------------
## Heighway Dragon
## Problem 220
## Let D0 be the two-letter string "Fa". For n≥1, derive
## Dn from Dn-1 by the string-rewriting rules:
## 
## "a" → "aRbFR"
## "b" → "LFaLb"
## 
## Thus, D0 = "Fa", D1 = "FaRbFR", D2 = "FaRbFRRLFaLbFR", and so on.
## 
## These strings can be interpreted as instructions to a computer
## graphics program, with "F" meaning "draw forward one unit", "L"
## meaning "turn left 90 degrees", "R" meaning "turn right 90 degrees",
## and "a" and "b" being ignored. The initial position of the computer
## cursor is (0,0), pointing up towards (0,1).
## 
## Then Dn is an exotic drawing known as the Heighway Dragon of order n.
## For example, D10 is shown below; counting each "F" as one step, the
## highlighted spot at (18,16) is the position reached after 500 steps.
## 
## What is the position of the cursor after 1012 steps in D50 ?
## Give your answer in the form x,y with no spaces.
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from math import sin, cos, radians
#-------------------------------------------------------------------------------
def draw_axes():
    size = 30
    plt.plot([-size,size],[0,0])
    plt.plot([0,0],[-size,size])
#-------------------------------------------------------------------------------
def plot_point(x,y):
    plt.plot(x,y,'o')
#-------------------------------------------------------------------------------
def get_pairs(moves):
    x = 0
    y = 0
    theta = 90
    points = [(x,y)]
    for c in moves:
        if c == 'F':
            dx = round(cos(radians(theta)))
            dy = round(sin(radians(theta)))
            x += dx
            y += dy
            points.append((x,y))
        if c == 'R':
            theta -= 90
        if c == 'L':
            theta += 90
    return points
#-------------------------------------------------------------------------------
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
#-------------------------------------------------------------------------------
current_string = 'Fa'
for k in range(10):
    current_string = new_string(current_string)

points = get_pairs(current_string)
print(points[500])
for x,y in points:
    plot_point(x,y)
draw_axes()
plt.show()    
#-------------------------------------------------------------------------------
# solution: 139776,963904
#-------------------------------------------------------------------------------
