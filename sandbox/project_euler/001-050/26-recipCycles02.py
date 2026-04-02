##---------------------------------------------------------------------------
##--Reciprocal cycles
##--
##--Problem 26
##--A unit fraction contains 1 in the numerator.
##--The decimal representation of the unit fractions with
##--denominators 2 to 10 are given:
##--
##--1/2	= 	0.5
##--1/3	= 	0.(3)
##--1/4	= 	0.25
##--1/5	= 	0.2
##--1/6	= 	0.1(6)
##--1/7	= 	0.(142857)
##--1/8	= 	0.125
##--1/9	= 	0.(1)
##--1/10	= 	0.1
##--Where 0.1(6) means 0.166666..., and has a 1-digit
##--recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.
##--
##--Find the value of d < 1000 for which 1/d contains
##--the longest recurring cycle in its decimal fraction part.
##-- jim mccleery, november, 2012, rewritten February, 2023
##---------------------------------------------------------------------------
from fractions import Fraction
from sympy import sieve
##---------------------------------------------------------------------------
def find_rat_pat_len(den,base=10):
    fractional = Fraction(1,den)
    fractional_digits = []
    seen = {}
    while fractional not in seen:
        seen[fractional] = len(fractional_digits)
        digit, fractional = divmod(fractional * base, 1)
        fractional_digits.append(digit)
    s = seen[fractional]
    return fractional_digits,len(fractional_digits[s:] if fractional else [])
##---------------------------------------------------------------------------
limit = 10**3
longest = 0
for p in sieve:
    pattern,length = find_rat_pat_len(p)
    if p >= limit:
        break
    if length > longest:
        longest = length
        keep = p
        long_pat = pattern
print(f'1/{keep} produces a repeating pattern {longest} digits in length.')
print('Press Enter to see the string of digits that repeats.')
input()
long_pat_chr = map(str,long_pat)
print(''.join(long_pat_chr))
##---------------------------------------------------------------------------
## solution: 983
##---------------------------------------------------------------------------
