# Problem 19
# 
# You are given the following information.
# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
#
# A leap year occurs on any year evenly divisible by 4, but not on a century
# unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century
# (1 Jan 1901 to 31 Dec 2000)?  ans: 171

import datetime

x = datetime.datetime(1900, 1, 1)
print(x.year, x.strftime('%B'), x.strftime('%A'))

tally = 0
for y in range(1901, 2001):
    for m in range(1, 13):
        x = datetime.datetime(y, m, 1)
        if x.strftime('%A') == 'Sunday':
            tally += 1

print(tally)
#solution: 171
