# 17-number_letter_counts.py
'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example,
342 (three hundred and forty-two) contains 23 letters and
115 (one hundred and fifteen) contains 20 letters.

The use of "and" when writing out numbers is in compliance with British usage.

ans:  21124
'''
import numpy as np

# list with key:value pairs 1:len(one), 2: len(two), ...
# 20:len(twenty)... 90:len(ninety)
lst2d = np.loadtxt('17-nums_as_words.txt', dtype=str)
ltr_tally = 0

def load_dictionary():
    d = {n:0 for n in range(0,1001)}  # initialize all dictionary keys to 0
    
    # update key:value (len(english spelling of numbers) from file
    for row in range(len(lst2d)):  
        d[int(lst2d[row][0])] = len(lst2d[row][1])
    return d

d_num_words = load_dictionary()

# generate the values (word lengths) for 21-99
for i in range(21, 100):
    tens = int(i/10)*10
    ones = i - tens
    d_num_words[i]  = d_num_words[tens] + d_num_words[ones]

# generate the values (word lengths) for 100-999
for i in range(100, 1000):
    hundreds = int(i / 100)
    tens_ones = i - hundreds * 100

    # if the value of tens and ones place is 0 use 'hundred'
    # instead of 'and hundred'
    if tens_ones == 0:
        d_num_words[i] = d_num_words[hundreds] + len('hundred')
    else:
        d_num_words[i] = d_num_words[hundreds] + len('andhundred') + d_num_words[tens_ones]

print(sum(d_num_words.values()))
#print(d_num_words)
#solution: 21124
