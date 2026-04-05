#-------------------------------------------------------------------------------
## The Chase
## Problem 227
##
## The Chase is a game played with two dice and an even number of players.
## 
## The players sit around a table and the game begins with two opposite players
## having one die each. On each turn, the two players with a die roll it.
## 
## If the player rolls 1, then the die passes to the neighbour on the left.
## If the player rolls 6, then the die passes to the neighbour on the right.
## Otherwise, the player keeps the die for the next turn.
## 
## The game ends when one player has both dice after they have been rolled and
## passed; that player has then lost.
## 
## In a game with 100 players, what is the expected number of turns the game lasts?
## 
## Give your answer rounded to ten significant digits.
#-------------------------------------------------------------------------------
from random import choice
from time import time
#-------------------------------------------------------------------------------
def make_players(n):
    if n % 2 != 0:
        print('Must have an even number of players.')
        return
    players = [0]*n
    players[0] = 1
    players[n//2] = 1
    return players
#-------------------------------------------------------------------------------
def make_play():
    global die_01
    global die_02
    
    p1 = choice([1,2,3,4,5,6])
    p2 = choice([1,2,3,4,5,6])
    if p1 == 1:
        players[die_01] = 0
        die_01 = (die_01-1+num_players) % num_players
        players[die_01] += 1
    if p1 == 6:
        players[die_01] = 0
        die_01 = (die_01+1+num_players) % num_players
        players[die_01] += 1
    if p2 == 1:
        players[die_02] = 0
        die_02 = (die_02-1+num_players) % num_players
        players[die_02] += 1
    if p2 == 6:
        players[die_02] = 0
        die_02 = (die_02+1+num_players) % num_players
        players[die_02] += 1

#-------------------------------------------------------------------------------
start = time()
num_players = 100
limit = 10**6
num_plays = 0
for _ in range(limit):
    players = make_players(num_players)
    die_01 = 0
    die_02 = num_players//2
    while True:
        make_play()
        num_plays += 1
        if max(players) == 2:
            break
print(f'Solution: {round(num_plays/limit,6)}, Run-Time: {time()-start}')
#-------------------------------------------------------------------------------
# solution: 3780.618622
#-------------------------------------------------------------------------------
