##The sum of the squares of the first ten natural numbers is, 385
##The square of the sum of the first ten natural numbers is, 3025
##Hence the difference between the sum of the squares of the first
##ten natural numbers and the square of the sum is 2640.
##Find the difference between the sum of the squares of the first
##one hundred natural numbers and the square of the sum.

totalOfSquares = 0
total = 0
for i in range(1,101):
    totalOfSquares += i**2
    total += i

print(totalOfSquares)
print(total**2)
print(total**2 - totalOfSquares)
#solution: 25164150 
