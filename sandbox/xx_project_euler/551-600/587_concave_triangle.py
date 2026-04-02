#  -----------------------------------------------------------------------------
#  Concave triangle
#  Problem 587
#  https://projecteuler.net/problem=587
#  -----------------------------------------------------------------------------
import matplotlib.pyplot as plt
from math import pi
from scipy.integrate import quad
from math import sqrt
#  -----------------------------------------------------------------------------
def make_circle(x,y,r):
    return plt.Circle((x,y),r,fill=False)
#  -----------------------------------------------------------------------------
def get_intercept():
    A = 1+1/NC**2
    B = 2/NC-2/NC**2+4*(NC-1)
    C = 4*(NC-1)**2-2/NC+1/NC**2
    x = (-B-sqrt(B**2-4*A*C))/(2*A)
    return x
#  -----------------------------------------------------------------------------
def f1(x):
    m = 1/NC
    return m*(x-1)+2
#  -----------------------------------------------------------------------------
def f2(x):
  return 1-sqrt(1-(x+2*(NC-1))**2)
#  -----------------------------------------------------------------------------
def plot_circles(ratio):
    x = 0
    fig, ax = plt.subplots()
    plt.axis('off')
    ax.set_aspect('equal', adjustable='datalim')
    for _ in range(NC):
        ax.add_patch(make_circle(x,0,1))
        x -= 2
    #plot left side of rectangle
    plt.plot([-2*NC+1,-2*NC+1],[-1,1])
    #plot top of rectange
    plt.plot([-2*NC+1,1],[1,1])
    #plot right side of rectangle
    plt.plot([1,1],[-1,1])
    #plot bottom of rectangle
    plt.plot([-2*NC+1,1],[-1,-1])
    #plot diagonal
    plt.plot([-2*NC+1,1],[-1,1])
    #add title
    if NC > 1:
        plt.title(f'For {NC} circles the ratio is {ratio}%.')
    else:
        plt.title(f'For {NC} circle the ratio is {ratio}%.')
    ax.plot()
    plt.show()
#  -----------------------------------------------------------------------------
def get_ratio():
    a = -(2*NC - 1)
    b = get_intercept()
    A1, err = quad(f1,a,b)  
    A2, err = quad(f2,b,a+1)
    return 100*(A1+A2)/CORNER
#  -----------------------------------------------------------------------------
GRAPHICS = True
CORNER = (4-pi)/4
NC = 1
while True:
    ratio = get_ratio()
    if GRAPHICS and NC <= 15:
        plot_circles(ratio)
    print(f'For N = {NC:6}: {ratio}%')
    if ratio < 0.1:
        break
    NC += 1
#  -----------------------------------------------------------------------------
#  solution: 2240
#  -----------------------------------------------------------------------------
