##------------------------------------------------------------------------------
##Number Rotations
##Problem 168
##
##Consider the number 142857. We can right-rotate this
##number by moving the last digit (7) to the front of
##it, giving us 714285.
##
##It can be verified that 714285=5×142857.
##This demonstrates an unusual property of 142857: it
##is a divisor of its right-rotation.
##
##Find the last 5 digits of the sum of all
##integers n, 10 < n < 10^100, that have this property.
##------------------------------------------------------------------------------
def euler_168():
    total = 0
    for k in range(1, 100):
        for d in range(1, 10):
            for y in range(1, 10):
                x, r = divmod((10**k - d)*y, 10*d - 1)
                if r != 0 or x < 10**(k-1):
                    continue
                total += 10*x + y
    print(total % 10**5)
##------------------------------------------------------------------------------
euler_168()
##------------------------------------------------------------------------------
##solution: 59206
##------------------------------------------------------------------------------
