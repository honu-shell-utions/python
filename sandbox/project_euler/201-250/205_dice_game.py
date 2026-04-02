#-------------------------------------------------------------------------------
## Dice Game
## Problem 205
## Peter has nine four-sided (pyramidal) dice, each with faces numbered 1, 2, 3, 4.
## Colin has six six-sided (cubic) dice, each with faces numbered 1, 2, 3, 4, 5, 6.
## 
## Peter and Colin roll their dice and compare totals: the highest total wins.
## The result is a draw if the totals are equal.
## 
## What is the probability that Pyramidal Pete beats Cubic Colin?
## Give your answer rounded to seven decimal places in the form 0.abcdefg
#-------------------------------------------------------------------------------
import itertools
from time import time
#-------------------------------------------------------------------------------
start = time()
pyramidal_counts = {}
cubic_counts = {}

# pyramidal
for i in itertools.product(range(1, 5), repeat=9):
    s = sum(i)
    pyramidal_counts[s] = pyramidal_counts.get(s, 0) + 1

# cubic
for i in itertools.product(range(1, 7), repeat=6):
    s = sum(i)
    cubic_counts[s] = cubic_counts.get(s, 0) + 1

pyramid_wins = 0
cubic_wins = 0
tie = 0
for i in pyramidal_counts:
    for j in cubic_counts:
        c = pyramidal_counts[i] * cubic_counts[j]
        if i > j:
            pyramid_wins += c
        elif i < j:
            cubic_wins +=c
        else:
            tie +=c

solution = float(pyramid_wins) / (pyramid_wins + cubic_wins + tie)
print(f'Solution: {round(solution,7)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 0.5731441
#-------------------------------------------------------------------------------
