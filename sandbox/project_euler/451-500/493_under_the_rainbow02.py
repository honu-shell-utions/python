#  -----------------------------------------------------------------------------
#  Under The Rainbow
#  Problem 493
#  70 coloured balls are placed in an urn, 10 for each of the seven rainbow colours.
#  What is the expected number of distinct colours in 20 randomly picked balls?
#  Give your answer with nine digits after the decimal point (a.bcdefghij).
#  Red, Orange, Yellow, Green, Blue, Indigo and Violet.
#  -----------------------------------------------------------------------------
from math import comb
#  -----------------------------------------------------------------------------
ans = round(7*(1-(comb(60, 20) / comb(70, 20))), 9)
print(ans, ans == 6.818741802)
#  -----------------------------------------------------------------------------
#  solution: 6.818741802
#  -----------------------------------------------------------------------------

