# Billionaire
# https://projecteuler.net/problem=267
# https://www.ivl-projecteuler.com/overview-of-problems/50-difficulty/problem-267
import math

def winnings(x, f):
    return pow(1 + 2*f, x) * pow(1 - f, 1000 - x)
    
def find_f():
    #Finds the optimal f
    f = 0.001
    goal = 10**9
    step = 0.001 #Adjust this for greater accuracy
    best_f, corresponding_x = 0, 1000
    while f < 0.5:
        x = 1
        while winnings(x, f) < goal:
            x += 1 #Adjust this for greater accuracy
        if x < corresponding_x:
            best_f, corresponding_x = f, x
        f += step
    return best_f, corresponding_x

def n_choose_r(n, r):  # nCr function
    if r > n:
        return "n must be greter than r"
    else:
        return int(math.factorial(n) / (math.factorial(r) * math.factorial(n - r)))
    
def compute():
    total = 0
    for h in range(432, 1001):
        total += n_choose_r(1000, h)
    return round(total/pow(2, 1000), 12)

print(compute())
