##1000-digit Fibonacci number 
##Problem 25
##The Fibonacci sequence is defined by the recurrence relation:
##
##Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
##Hence the first 12 terms will be:
##
##F1 = 1
##F2 = 1
##F3 = 2
##F4 = 3
##F5 = 5
##F6 = 8
##F7 = 13
##F8 = 21
##F9 = 34
##F10 = 55
##F11 = 89
##F12 = 144
##The 12th term, F12, is the first term to contain three digits.
##
##What is the index of the first term in the Fibonacci sequence
##to contain 1000 digits?
## jim mccleery, november, 2021
########################################################################
def fibo(n):
    if n == 1:
        return [1]
    if n == 2:
        return [1, 1]
    a = 1
    b = 1
    series = []
    series.append(a)
    series.append(b)
    
    for i in range(n-2):
        c = a + b
        series.append(c)
        a = b
        b = c
    return series
########################################################################
fibList = fibo(4800)
for i in range(1,len(fibList)):
    if fibList[i] >= 10**999:
        print(fibList[i])
        break
print(i+1,'     ',fibList[i])
#Solution: 4782
########################################################################
