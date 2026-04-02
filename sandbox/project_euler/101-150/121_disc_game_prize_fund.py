# 121_disc_game_prize_fund.py
#
# A bag contains one red disc and one blue disc. In a game of chance a player
# takes a disc at random and its colour is noted. After each turn the disc is
# returned to the bag, an extra red disc is added, and another disc is taken
# at random.
#
# The player pays £1 to play and wins if they have taken more blue discs than
# red discs at the end of the game.
#
# If the game is played for four turns, the probability of a player winning is
# exactly 11/120, and so the maximum prize fund the banker should allocate for
# winning in this game would be £10 before they would expect to incur a loss.
# Note that any payout will be a whole number of pounds and also includes the
# original £1 paid to play the game, so in the example given the player
# actually wins £9.
#
# Find the maximum prize fund that should be allocated to a single game in
# which fifteen turns are played.
from sympy.functions.combinatorial.numbers import stirling
from math import factorial, floor
from time import time

start = time()
s = [stirling(16,i,kind=1) for i in range(1,17)]
s = s[::-1]

total = sum(s[:8])
recip = factorial(16)/total
print('Solution:',floor(float(recip)),'Run Time',time()-start)


#solution: 2269
