################################################################################
from time import time
from matplotlib import pyplot as plt
from math import sqrt, pi, cos, sin
from numpy import linspace
################################################################################
def draw_graph(x, y, hit_list):
    plt.figure(figsize=(7,9))
    plt.plot(x, y,color='blue')
    for i in range(len(hit_list)-1):
        plt.plot([hit_list[i][0],hit_list[i+1][0]],[hit_list[i][1],hit_list[i+1][1]])
    plt.show()
################################################################################    
def create_plot(hit_list):
    deltaXs = linspace(-5,5,1000)
    deltaYs = [[sqrt(100 - 4*x**2),-sqrt(100 - 4*x**2)] for x in deltaXs]
    draw_graph(deltaXs,deltaYs,hit_list)
################################################################################
start = time()
hit_list = [(0.0,10.1),(1.4,-9.6)]
xA = hit_list[0][0]
yA = hit_list[0][1]
xO = hit_list[1][0]
yO = hit_list[1][1]

while xO > 0.01 or xO < -0.01 or yO < 0:
    mA = (yO - yA) / (xO - xA)  # slope
    mO = -4*xO / yO             # slope ellipse tangent

    # slope of B
    tanA = (mA - mO) / (1 + mA*mO)
    mB = (mO - tanA)/ (1 + tanA*mO)

    interceptB = yO - mB * xO

    # solve the quadratic equation for finding the intersection of B and the
    # ellipse a*x^2 + b*x + c = 0
    a = 4 + mB**2
    b = 2 * mB * interceptB
    c = interceptB**2 - 100
    
    ans1 = (-b + sqrt(b**2 - 4 * a * c)) / (2 * a)
    ans2 = (-b - sqrt(b**2 - 4 * a * c)) / (2 * a)
    
    xA = xO
    yA = yO

    # take the solution which is furtherst from x0
    if abs(ans1 - xO) > abs(ans2 - xO):
        xO = ans1
    else:
        xO = ans2
    yO = mB * xO + interceptB
    hit_list.append((xO,yO))

create_plot(hit_list)
print(f'The number of bounces is: {len(hit_list)-2:}, runtime: {time()-start}')
################################################################################
#solution: 354
################################################################################
