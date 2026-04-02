#  -----------------------------------------------------------------------------
#  Digital root clocks
#  Problem 315
#  https://projecteuler.net/problem=315
#  -----------------------------------------------------------------------------
#imports
from turtle import *
from random import choice
#  -----------------------------------------------------------------------------
#constants
BLOCK = 20
X_DIM, Y_DIM = 800,800

DIGIT0 = [
'XXXXXXX',
'X     X',
'X     X',
'X     X',
'X     X',
'X     X',
'X     X',
'XXXXXXX']

DIGIT1 = [
'   X   ',
'   X   ',
'   X   ',
'   X   ',
'   X   ',
'   X   ',
'   X   ',
'   X   ']

DIGIT2 = [
'XXXXXXX',
'      X',
'      X',
'XXXXXXX',
'X      ',
'X      ',
'X      ',
'XXXXXXX']

DIGIT3 = [
'XXXXXXX',
'      X',
'      X',
'XXXXXXX',
'      X',
'      X',
'      X',
'XXXXXXX']

DIGIT4 = [
'X     X',
'X     X',
'X     X',
'XXXXXXX',
'      X',
'      X',
'      X',
'      X']

DIGIT5 = [
'XXXXXXX',
'X      ',
'X      ',
'XXXXXXX',
'      X',
'      X',
'      X',
'XXXXXXX']

DIGIT6 = [
'XXXXXXX',
'X      ',
'X      ',
'XXXXXXX',
'X     X',
'X     X',
'X     X',
'XXXXXXX']

DIGIT7 = [
'XXXXXXX',
'X     X',
'      X',
'      X',
'      X',
'      X',
'      X',
'      X']

DIGIT8 = [
'XXXXXXX',
'X     X',
'X     X',
'XXXXXXX',
'X     X',
'X     X',
'X     X',
'XXXXXXX']

DIGIT9 = [
'XXXXXXX',
'X     X',
'X     X',
'XXXXXXX',
'      X',
'      X',
'      X',
'  XXXXX']

DIGITS = [DIGIT0,DIGIT1,DIGIT2,DIGIT3,DIGIT4,DIGIT5,\
          DIGIT6,DIGIT7,DIGIT8,DIGIT9]
#  -----------------------------------------------------------------------------
#methods
def set_up():
  drawing_area = Screen()
  drawing_area.setup(X_DIM,Y_DIM)
  color('blue')
  shape("square")
  speed(0)
  title('Project Euler 315 - Digital Roots')
  penup()
  hideturtle()
#  -----------------------------------------------------------------------------
def make_digit(DIG,x,y):
  for row in range(8):
    for col in range(7):
      character = DIG[7-row][col]
      screen_x = x+col*BLOCK
      screen_y = y+row*BLOCK
      goto(screen_x,screen_y)
      if character == 'X':
        stamp()
      goto(-X_DIM,-Y_DIM)
#  -----------------------------------------------------------------------------
#driver
set_up()
while True:
  D0 = choice(DIGITS)
  D1 = choice(DIGITS)
  D2 = choice(DIGITS)
  make_digit(D0,-230,-70)
  make_digit(D1,-70,-70)
  make_digit(D2,90,-70)
  for _ in range(10**8):
    pass
  clear()
#  -----------------------------------------------------------------------------
#  solution: 13625242
#  -----------------------------------------------------------------------------

