################################################################################
##Square root convergents
##Problem 57
##It is possible to show that the square root of two can
##be expressed as an infinite continued fraction.
##
##By expanding this for the first four iterations, we get:
##1.5
##1.4
##1.41666
##1.41379
##
##The next three expansions are 
## 
##99/70
##239/169
##577/408
##
##but the eighth expansion, 1393/985
##is the first example where the number of digits
##in the numerator exceeds the number of digits in the denominator.
##
##In the first one-thousand expansions, how many
##fractions contain a numerator with more digits than the denominator?
################################################################################
import math
################################################################################
limit = 1000
result = 0
den = 2
num = 3
for i in range(1,limit):
    num += 2*den
    den = num - den
    if int(math.log10(num)) > int(math.log10(den)):
        result += 1
print(result)
################################################################################
#solution: 153
################################################################################
