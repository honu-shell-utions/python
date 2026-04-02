################################################################################
## Paper sheets of standard sizes: an expected-value problem
## Problem 151
## A printing shop runs 16 batches (jobs) every week and each
## batch requires a sheet of special colour-proofing paper of size A5.
##
## Every Monday morning, the supervisor opens a new envelope,
## containing a large sheet of the special paper with size A1.
##
## The supervisor proceeds to cut it in half, thus getting two
## sheets of size A2. Then one of the sheets is cut in half to
## get two sheets of size A3 and so on until an A5-size sheet is
## obtained, which is needed for the first batch of the week.
##
## All the unused sheets are placed back in the envelope.
##
## At the beginning of each subsequent batch, the supervisor takes
## from the envelope one sheet of paper at random. If it is of size A5,
## then it is used. If it is larger, then the 'cut-in-half' procedure
## is repeated until an A5-size sheet is obtained, and any remaining sheets
## are always placed back in the envelope.
##
## Excluding the first and last batch of the week, find the expected number
## of times (during each week) that the supervisor finds a single sheet of
## paper in the envelope.
##
## Give your answer rounded to six decimal places using the format x.xxxxxx .
################################################################################
from time import time
################################################################################
def place(size):          # Python uses the ** operator for exponentiation,
    return 10**(5 - size) # because ^ is used for bitwise XOR, as in C.
################################################################################
def sheets_of_size(n, bag):
    p = place(n)        # Get the place of the number                    100
    bag = bag // p      # Divide the bag number by the place number       12.11
    return bag % 10     # Remove the preceding digits by taking % 10       2
################################################################################
def cut(size, bag):
    p = place(size) 
    return int(
          bag            # Take the original bag         eg.  1210
        - p              # Remove the sheet                 - 100
        + ((p - 1) / 9)  # Add one of each smaller sheet    + (99 / 9)
    ) 
################################################################################
def only_one(bag):
    return (bag == 1   or bag == 10   or 
            bag == 100 or bag == 1000 or bag == 10000)
################################################################################
def total_sheets(bag):
    return (
          sheets_of_size(1, bag)
        + sheets_of_size(2, bag)
        + sheets_of_size(3, bag)
        + sheets_of_size(4, bag)
        + sheets_of_size(5, bag)
    )
################################################################################
def possibilities(poss):
    bag = poss[0]  # We're using an array instead of two arguments so that
    prob = poss[1] # we can pass items in the list returned by this function
                   # as arguments to the function.
        
    p = [] # The possibilities will be stored in a list.
    for size in range(1, 6): # For each paper size
        num_of_size = sheets_of_size(size, bag)
        if num_of_size > 0:
            p.append([
                # The `cut` function that we wrote earlier returns the
                # resulting bag if we cut a sheet of `size`.
                cut(size, bag),
                
                # Multiplying the probabilities of two events gives the
                # probability that both will occur. Since a result can only
                # occur if the result that produced it also occurred, we need 
                # to multiply the probability of both events together.
                # its probability 
                (num_of_size / total_sheets(bag)) * prob
            ])

    return p
################################################################################
def expected(poss, n):
    bag = poss[0]
    prob = poss[1]

    # If this result contains only one sheet, augment the expected value 
    # by the probability of getting this result.
    p_sum = int(only_one(bag)) * prob

    # If we've reached the maximum number of recursions, don't explore
    # the possibilities which result from this one.
    if n == 0: return p_sum
    
    # For each resulting possibility, augment the expected value by 
    # the output of this function applies to it, reducing `n` to 
    # prevent infinite recursion.
    for e in possibilities(poss):
        p_sum += expected(e, n - 1)

    return p_sum
################################################################################
start_time = time()
start = [10000, 1]
solution = expected(start, 14)
sec = round(time()-start_time,2)
print(round(solution-1,6))
print(f"--- {sec} seconds ---")
################################################################################
#solution: 0.464399
################################################################################
