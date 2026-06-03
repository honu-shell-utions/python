"""
Jim McCleery
June 3, 2026
Kailua-Kona, HI

https://projecteuler.net/problem=826

"""
import numpy as np
from sympy import nextprime

def F(n, trials=10**2):
    total_painted_length = 0
    
    for _ in range(trials):
        # 1. Randomly place 'n' birds on the 1-unit wire and sort their positions
        birds = np.sort(np.random.random(n))
        
        # 2. Calculate the lengths of the (n-1) internal intervals
        # intervals[i] is the length between bird i and bird i+1
        intervals = np.diff(birds)
        
        # 3. Track which intervals get painted (initialized to False)
        painted = np.zeros(n - 1, dtype=bool)
        
        # 4. For each bird, find its closest neighbor and paint that interval
        for i in range(n):
            if i == 0:
                # Leftmost bird only has a neighbor to its right (interval 0)
                painted[0] = True
            elif i == n - 1:
                # Rightmost bird only has a neighbor to its left (the last interval)
                painted[-1] = True
            else:
                # Middle birds look left and right, picking the shorter distance
                left_dist = intervals[i - 1]
                right_dist = intervals[i]
                
                if left_dist < right_dist:
                    painted[i - 1] = True
                else:
                    painted[i] = True
                    
        # 5. Sum up the lengths of all intervals that were marked as painted
        trial_painted_length = np.sum(intervals[painted])
        total_painted_length += trial_painted_length
        
    # Return the expected (average) painted length across all trials
    return total_painted_length / trials

# Run the simulation
simulated = 0
prime = 3
count = 0
while prime < 10**6:
    count += 1
    simulated += F(prime)
    prime = nextprime(prime)
    if count % 10**2 == 0:
        print(f'{simulated/count:.10f}')

print(f'Monte Carlo simulation: {simulated/count:.10f}')



