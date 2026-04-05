# ----------------------------------------------------------------------------
# 260_stoneGame.py
#
# A game is played with three piles of stones and two players. On each
# player's turn, the player may remove one or more stones from the piles.
# However, if the player takes stones from more than one pile, then the same
# number of stones must be removed from each of the selected piles.
#
# In other words, the player chooses some N > 0 and removes:
#  • N stones from any single pile; or
#  • N stones from each of any two piles (2N total); or
#  • N stones from each of the three piles (3N total)
# The player taking the last stone(s) wins the game.
#
# A winning configuration is one where the first player can force a win. For
# example, (0, 0, 13), (0, 11, 11), and (5, 5, 5) are winning configurations
# because the first player can immediately remove all stones.
#
# A losing configuration is one where the second player can force a win, no
# matter what the first player does.  For example, (0, 1, 2) and (1, 3, 3) are
# losing configurations: any legal move leaves a winning configuration for the
# second player.
#
# Consider all losing configurations (x↓i, y↓i, z↓i)
# where x↓i ≤ y↓i ≤ z↓i ≤ 100.  We can verify that ∑(x↓i + y↓i + z↓i) = 173895
# for these.
#
# Find ∑(x↓i + y↓i + z↓i) where (x↓i, y↓i, z↓i) ranges over the losing
# configurations with x↓i ≤ y↓i ≤ z↓i ≤ 1000.
# ----------------------------------------------------------------------------
nmax = 1000

s = [[[0 for a in range(b + 1)]
      for b in range(c + 1)]
     for c in range(nmax + 1)]

def sort(a, b, c):
    if a <= b and a <= c:
        return a, min(b, c), max(b, c)
    if b <= c:
        return b, min(a, c), max(a, c)
    return c, min(a, b), max(a, b)

def rmoves(a, b, c):
    for aa in range(nmax - a):
        yield sort(a + aa + 1, b, c)
    for bb in range(nmax - b):
        yield sort(a, b + bb + 1, c)
    for cc in range(nmax - c):
        yield sort(a, b, c + cc + 1)
    for ab in range(nmax - max(a, b)):
        yield sort(a + ab + 1, b + ab + 1, c)
    for ac in range(nmax - max(a, c)):
        yield sort(a + ac + 1, b, c + ac + 1)
    for bc in range(nmax - max(b, c)):
        yield sort(a, b + bc + 1, c + bc + 1)
    for abc in range(nmax - max(a, b, c)):
        yield sort(a + abc + 1, b + abc + 1, c + abc + 1)
    
ss = 0

for n in range(3 * nmax + 1):
    for c in range(nmax + 1):
        for b in range(c + 1):
            a = n - c - b
            if 0 <= a <= b:
                if s[c][b][a] == 0:
                    ss += a + b + c
                    for aa, bb, cc in rmoves(a, b, c):
                        s[cc][bb][aa] = 1

print(ss)




# ----------------------------------------------------------------------------






# ----------------------------------------------------------------------------
# solution: 167542057
# ----------------------------------------------------------------------------
