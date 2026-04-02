##We start with a set of 90 two-digit numbers, accepting all of them,
##and then try to add a trailing digit, checking for the last 3 digit
##sum and rejecting all the numbers with sums exceeding 9. The trick
##is that we don't need the actual numbers, we only need to keep the
##last two digits of all accepted numbers and the total of all numbers
##with these two last digits.
##
##A natural way of doing this is to create a 100-long list, assign 0s to
##indices 0 though 9, corresponding to not allowing lead 0s, and then 1 to
##all the rest. Then in each try we go through values of a new digit, break
##each list index into digits and try the sum for total. If the sum is
##acceptable, we collect the totals corresponding to acceptable indices in
##a new 100-long list, the new index is determined by the last digit of the
##old index now becoming the lead digit, and the new digit as the new last
##digit. It is actually easier to write
##this as a code than explain it in words :) The code runs for about 5ms.

N = 20
d = 9

candidates = [1]*100
for _ in range(10):
    candidates[_] = 0

for _ in range(N-2):
    candidates_old = candidates.copy()
    candidates = [0]*100
    for i in range(10):
        for j in range(100):
            if (j//10 + j%10 + i) <= d:               
                candidates[(j%10)*10+i] += candidates_old[j]  
              
print(sum(candidates))
