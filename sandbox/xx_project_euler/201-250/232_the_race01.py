#-------------------------------------------------------------------------------
## The Race
## Problem 232
## Two players share an unbiased coin and
## take it in turns to play The Race.
## 
## On Player 1's turn, the coin is tossed
## once. If it comes up Heads, then Player
## 1 scores one point; if it comes up Tails,
## then no points are scored.
## 
## On Player 2's turn, a positive integer, 
## T, is chosen by Player 2 and the coin is tossed 
## T times. If it comes up all Heads, then Player 2 scores 
## 2T−1 points; otherwise, no points are scored.
## 
## Player 1 goes first and the winner is the
## first to 100 or more points.
## 
## Player 2 always selects the number, T,
## of coin tosses that maximises the probability of winning.
## 
## What is the probability that Player 2 wins?
## 
## Give your answer rounded to eight decimal places
## in the form 0.abcdefgh.
#-------------------------------------------------------------------------------
from random import choice
#-------------------------------------------------------------------------------
def player2():
    num_rolls = 1
    while 2**(num_rolls-1) + player2_score < player1_score + 1:
        num_rolls += 1
            
    for _ in range(num_rolls):
        play = choice(['H','T'])
        if play == 'T':
            return 0
        
    return 2**(num_rolls-1)
#-------------------------------------------------------------------------------
def play_game():
    global player1_score
    global player2_score
    while True:
        player2_score += player2()
        if player2_score >= winning_total:
            return 1

        player1_score += choice([0,1])
        if player1_score == winning_total:
            return 0
#-------------------------------------------------------------------------------
games = 10**6
for n in [2,4,10,50,100.500]:
    winning_total = n
    player2_wins = 0
    for _ in range(games):
        player1_score = choice([0,1])
        player2_score = 0
        player2_wins += play_game()
    print('for winning total =',n,'\t--->',round(player2_wins/games,8))
#-------------------------------------------------------------------------------
#if winning_total = 2 solution is: 0.52592593
#if winning_total = 4 solution is: 0.60375309
#if winning_total = 10 solution is: 0.67006457
#if winning_total = 50 solution is: 0.79438583
#if winning_total = 100 solution is: 0.83648556
# solution: 0.83648556
#-------------------------------------------------------------------------------
