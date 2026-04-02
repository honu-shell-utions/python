##The sum of the squares of the first ten natural numbers is, 385
##The square of the sum of the first ten natural numbers is, 3025
##Hence the difference between the sum of the squares of the first
##ten natural numbers and the square of the sum is 2640.
##Find the difference between the sum of the squares of the first
##one hundred natural numbers and the square of the sum.
## [n(n+1)(2n+1)] / 6

def sum_squares(n):
    return n*(n+1)*(2*n+1)//6

def square_sum(n):
    return (n*(n+1)//2)**2

res1 = sum_squares(100)
res2 = square_sum(100)
print(abs(res1-res2))
#solution: 25164150 
