#  -----------------------------------------------------------------------------
#  Range flips
#  Problem 430
#  https://projecteuler.net/problem=430
#  -----------------------------------------------------------------------------
from random import randint
#  -----------------------------------------------------------------------------
def E(num_squares,num_turns):
    status = [True]*num_squares
    for _ in range(num_turns):
        start = randint(0,num_squares-1)
        end = randint(start,num_squares-1)
        for j in range(start,end+1):
            status[j] = not status[j]
    return sum(status)
#  -----------------------------------------------------------------------------
def euler_430(num_squares,num_turns,num_trials):
    total = 0
    for _ in range(num_trials):
        total += E(num_squares,num_turns)
    return total/num_trials
#  -----------------------------------------------------------------------------
num_trials = 10**7
print(euler_430(3,1,num_trials),10/9)
print(euler_430(3,2,num_trials),5/3)
print(euler_430(10,4,num_trials),5.157)
print(euler_430(100,10,num_trials),51.893)
#  -----------------------------------------------------------------------------
#  solution: 5000624921.38
#  -----------------------------------------------------------------------------
