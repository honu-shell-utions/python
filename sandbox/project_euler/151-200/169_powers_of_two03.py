# forum name: tzaman Pakistan
'''
First I get the binary representation of the number; then I go through it
keeping track of two variables, called 'split' and 'unsplit', which are the
number of representations possible with splitting the highest bit, and without.
Starting from the bottom bit, I count the zeros between 1-bits (I call 'em
'gaps' in the code) and use them to count the number of new split/unsplit
configurations there will be.

I get the answer in 0.1ms, and I can calculate 10^25000
(12...1957, 9983 digits) in about 1.5 seconds. 
'''
from math import log


def f(n):
    split, unsplit, gap = 0, 0, 0
    for i in range(1+int(log(n, 2))):
        if n>>i&1 == 0: gap+=1
        else:
            if unsplit:
                unsplit, split = (1+gap)*unsplit + split, gap*unsplit + split
            else:
                unsplit, split = gap+1, gap
            gap = 0
    return unsplit
ans = f(10**25)
print(f'{ans} {ans==178653872807}')

# forum name: arn.zarn Russia 
def f169(b):
    if b == '' or b == '0' or b == '1': return 1
    
    # f169(xxx11...11) = f169(xxx)
    b = b.rstrip('1') # strip trailing `1's
        
    # f169(xxx1000...0) = f169(xxx0)*n + f169(xxx)
    n = len(b) - len(b.rstrip('0')) # number of trailing zeros
    x = b[:-n-1] # 'xxx1000...0' -> 'xxx'
    return f169(x + '0') * n + f169(x)


ans = f169(bin(10**25)[2:])
print(f'{ans} {ans==178653872807}')

# forum name: hbf Norway 
def p169(n=10**25):
    # ways to write 10**25 as sum([0..2]*(2**x))
    p = [0, 1] # p[1-i] = number of ways to add i to next bit
    while n:
        p[n & 1] = sum(p) # set p for least significant bit
        n >>= 1
    return p[1]
ans = p169()
print(f'{ans} {ans==178653872807}')
