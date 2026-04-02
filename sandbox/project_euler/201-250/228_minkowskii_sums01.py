#-------------------------------------------------------------------------------
## Minkowski Sums
## Problem 228
## Let Sn be the regular n-sided polygon – or shape – whose
## vertices vk (k = 1,2,…,n) have coordinates:
## 
## xsub(k)   =   cos( 2k-1/n ×180° )
## ysub(k)   =   sin( 2k-1/n ×180° )
## 
## Each Ssub(n) is to be interpreted as a filled shape consisting
## of all points on the perimeter and in the interior.
## 
## The Minkowski sum, S+T, of two shapes S and T is the result
## of adding every point in S to every point in T, where point
## addition is performed coordinate-wise: (u, v) + (x, y) = (u+x, v+y).
## 
## For example, the sum of S3 and S4 is the six-sided shape
## shown in pink below:
## 
## picture showing Ssub(3) + Ssub(4)
## 
## How many sides does S(1864) + S(1865) + … + S(1909) have?
#-------------------------------------------------------------------------------
import matplotlib.pyplot as plt
from math import sin, cos, radians
#-------------------------------------------------------------------------------
def draw_figure(points):
    for x,y in points:
        plt.plot(x,y,'o')
#-------------------------------------------------------------------------------
def get_pairs(n):
    points = []
    for k in range(1,n+1):
        x = cos((2*k-1)/n * radians(180))
        y = sin((2*k-1)/n * radians(180))
        points.append((x,y))
    return points
#-------------------------------------------------------------------------------
S3 = get_pairs(3)
S4 = get_pairs(4)
S3_plus_S4 = []

for x1,y1 in S3:
    for x2,y2 in S4:
        S3_plus_S4.append((x1+x2,y1+y2))
 
draw_figure(S3)
plt.show()
draw_figure(S4)
plt.show()    
draw_figure(S3_plus_S4)
plt.show()    

#-------------------------------------------------------------------------------
# solution: 86226
#-------------------------------------------------------------------------------
