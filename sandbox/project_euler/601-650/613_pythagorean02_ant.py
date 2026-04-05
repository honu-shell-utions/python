from math import *

sol = (9*log(3) + 32*log(2) - 25*log(5))/(24*pi) + 1/2
print(round(sol,10))

x, y = 30, 40
z = (x*x + y*y)**0.5
p = 0.5 - (x/y*log(z/x) + y/x*log(z/y)) / (2*pi)
print(round(p,10))

from scipy.integrate import dblquad as integrate
w,h = 40.0,30.0
f = lambda x,y: atan2(y,x)-atan2(y-h,x-w)
z = integrate(f,0,h,lambda x:w/h*x,w)
print(round(z[0]/(w*h*pi),10))
