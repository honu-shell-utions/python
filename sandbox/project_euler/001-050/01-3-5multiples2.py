#If we list all the natural numbers below 10 that are multiples of 3 or 5,
#we get 3, 5, 6 and 9. The sum of these multiples is 23.
#Find the sum of all the multiples of 3 or 5 below 1000.


multiple = 3
bigN = 999
littleN = bigN // multiple
total = multiple*littleN*(littleN+1)/2
print(int(total))

multiple = 5
bigN = 999
littleN = bigN // multiple
total = total + multiple*littleN*(littleN+1)/2
print(int(total))

multiple = 15
bigN = 999
littleN = bigN // multiple
total = total - multiple*littleN*(littleN+1)/2
print(int(total))
