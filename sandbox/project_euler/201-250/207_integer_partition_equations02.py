from fractions import Fraction
def euler_207():

    perfect = 0
    total = 0
    nextPowerOf2 = 2
    i = 1
    upper_bound = Fraction(1,12345)

    while True:
        num = i * (i + 1)
        total += 1
        if i + 1 == nextPowerOf2:
            perfect += 1
            nextPowerOf2 *= 2
        if Fraction(perfect,total) < upper_bound:
            print(Fraction(perfect,total))
            break
        i += 1

    print(num)

euler_207()
