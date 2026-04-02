# 089_roman.py
# For a number written in Roman numerals to be considered valid there are
# basic rules which must be followed. Even though the rules allow some numbers
# to be expressed in more than one way there is always a "best" way of writing
# a particular number.
#
# For example, it would appear that there are at least six ways of writing the
# number sixteen:
# IIIIIIIIIIIIIIII
# VIIIIIIIIIII
# VVIIIIII
# XIIIIII
# VVVI
# XVI
#
# However, according to the rules only XIIIIII and XVI are valid, and the last
# example is considered to be the most efficient, as it uses the least number
# of numerals.
#
# The 11K text file, roman.txt contains one thousand numbers written in valid,
# but not necessarily minimal, Roman numerals; see About... Roman Numerals
# for the definitive rules for this problem.
#
# Find the number of characters saved by writing each of these in
# their minimal form.
#
# Note: You can assume that all the Roman numerals in the file contain no more
# than four consecutive identical units.
import numpy as np

lst_roman = np.loadtxt('89-roman.txt', dtype=object)


def from_roman(s):
    rom_val = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    int_val = 0
    for i in range(len(s)):
#        print(int_val)
        if i > 0 and rom_val[s[i]] > rom_val[s[i - 1]]:
            int_val += rom_val[s[i]] - 2 * rom_val[s[i - 1]]
        else:
            int_val += rom_val[s[i]]
    return int_val


def to_roman(num):
    lookup = [
        (1000, 'M'),
        (900, 'CM'),
        (500, 'D'),
        (400, 'CD'),
        (100, 'C'),
        (90, 'XC'),
        (50, 'L'),
        (40, 'XL'),
        (10, 'X'),
        (9, 'IX'),
        (5, 'V'),
        (4, 'IV'),
        (1, 'I'),
            ]
    result = ''
    for n, roman in lookup:
        d, num = divmod(num, n)
#        print(d, num, roman)
        result += roman * d
    return result


def tally_lengths(lst_str):
    tally = 0
    for s in lst_str:
        tally += len(s)
    return tally


lst = []
for s in lst_roman:
    lst.append(from_roman(s))

lst_min_roman = []
for s in lst:
    lst_min_roman.append(to_roman(s))

file = open('f1.txt', 'w')
for items in lst_min_roman:
    file.writelines(items + '\n')
file.close()

sum_orig = tally_lengths(lst_roman)
sum_min = tally_lengths(lst_min_roman)
print(f'sum_orig: {sum_orig} sum_min: {sum_min}')
print(f'diff: {sum_orig - sum_min}')  # ans: 743

#solution: 743
