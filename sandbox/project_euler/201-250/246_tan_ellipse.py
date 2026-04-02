#-------------------------------------------------------------------------------
## Tangents to an ellipse
## Problem 246
#-------------------------------------------------------------------------------
from math import sqrt, radians, pi, tan, acos
from time import time
#-------------------------------------------------------------------------------
# Solution Approach
#   0. Given an ellipse (e) : (x/a)**2 + (y/b)**2 = 1
#       And a point P : (x0, y0) outside the ellipse (e)
#
#   1. The slope of the tangent at point (x1, y1) on the ellipse (e) is,
#           (dy/dx) @(x1,y1) = - ( x1 / a**2 )/( y1 / b**2 )
#
#   2. Two tangents can be drawn from point (P) to the ellipse (e)
#       These tangents intersect the ellipse at point (x, y) given by,
#
#                  (x0/a) ± (y0/b)* sqrt((x0/a)**2 + (y0/b)**2 -1)
#           x/a = ---------------------------------------------------
#                            (x0/a)**2 + (y0/b)**2
#
#                  1 -(x0/a)*(x/a)
#           y/b = -----------------
#                      y0/b
#
#   3. The tangent with slope (m) will intersect the ellipse (e) at points,
#           x/a = ( y/b )*( a*m/b )
#           y/b = ± 1/ sqrt( 1+ ( a*m/b )**2 )
#       The y-intercept of the tangents (0, y0) is given by,
#           y0 = b* ( y/b -( a*m/b )* x/a)
#              = ± b* sqrt( 1+ ( a*m/b )**2 )
#              = ± sqrt ( b**2 + (a*m)**2 )
#       And the x-intercept (x0, 0) is given by,
#           x0 = a* ( x/a - (y/b)/( a*m/b ))
#              = ± a* sqrt( 1+ ( b/(a*m) )**2 )
#              = ± sqrt ( a**2 + (b/m)**2 )
#---------------------------------------------------------------------------
def angle_between_tangents(from_point, to_ellipse):
    A, B, A2, B2 = to_ellipse
    x0, y0 = from_point
    x02, y02 = x0*x0, y0*y0                     # squares
    x0_A, y0_B = x0/A, y0/B                     # normalized

    tmp1 = x02/A2 + y02/B2
    if tmp1 < 1 :
        print('Error : Point should be in the exterior of ellipse.')
        return []
    tmp2 = A* y0_B * sqrt( tmp1 -1 )
        
    # Intersection co-ordinates of the ellipse and the tangents
    x1 = (x0 + tmp2 ) /tmp1
    x2 = (x0 - tmp2 ) /tmp1
    y1 = ( 1 - x0_A*x1/A) *B /y0_B
    y2 = ( 1 - x0_A*x2/A) *B /y0_B

    angle = angle_formed([x0, y0], [x1, y1], [x2, y2])
    return angle
#---------------------------------------------------------------------------
def angle_formed(pt0, pt1, pt2) :
    dx1, dy1 = pt1[0] -pt0[0], pt1[1] -pt0[1]
    dx2, dy2 = pt2[0] -pt0[0], pt2[1] -pt0[1]
    dot_prod = dx1*dx2 + dy1*dy2
    len1 = sqrt( dx1*dx1 + dy1*dy1 )
    len2 = sqrt( dx2*dx2 + dy2*dy2 )
    angle = acos( dot_prod /len1 /len2 )
    return angle
#---------------------------------------------------------------------------
start = time()
ptM = [-2000, 1500]         # co-ordinates for point M
ptG = [ 8000, 1500]         # co-ordinates for point G
r = 15000                   # radius of circle

ae = (ptG[0] -ptM[0])/2     # twice the distance between the foci
a = r/2                     # a = semi-major axis
b = sqrt(a*a -ae*ae)        # b = semi-minor axis
a2, b2 = a*a, b*b
aRPS = radians(45)          # minimum angle RPS in radians

# Count number of points along y-axis :
m = tan( 0.5*( pi + aRPS ) )  # minimum tangent slope
max_y_intercept = int( sqrt( b2 + a2*m*m ))
pts_along_y = 2* ( max_y_intercept - int(b) )  # 2 : ± direction
    
# Count number of points along x-axis :
# Not counting the point on ellipse (a,0) and (-a,0)
m = tan( pi - 0.5*aRPS )      # maximum tangent slope
max_x_intercept = int( sqrt( a2 + b2/(m*m) ))
pts_along_x = 2* ( max_x_intercept - int(a) )  # 2 : ± direction
    
# Count remaining off-axis points :
pts_off_axis = 0
max_y, min_y = max_y_intercept, int(b)
for x in range( 1, max_x_intercept +1 ) :
    x2_a2 = x*x/a2;
    while ( min_y > 0 ) and (( x2_a2 + min_y*min_y/b2 ) > 1 ) :
        # decrease min_y so that point (x, min_y) is inside the ellipse
        #   if x >= a, min_y = 0
        min_y -= 1
    while ( max_y > min_y ) and \
            ( angle_between_tangents([x, max_y],[a, b, a2, b2]) < aRPS ) :
        # decrease max_y so that the tangents from max_y contain an angle
        #   greater than aRPS
        max_y -= 1
    pts_off_axis += 4*( max_y - min_y )             # 4 : each quadrant

# Ouptut :
total_pts = pts_along_x + pts_along_y + pts_off_axis

print(f'Solution: {total_pts}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 810834388
#-------------------------------------------------------------------------------
