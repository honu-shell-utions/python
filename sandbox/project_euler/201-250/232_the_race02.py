from time import time
start = time()

f_dict = {}

def f(turn, one_score, two_score):
    if one_score >= 100:
        return 0.0

    if two_score >= 100:
        return 1.0
    
    if turn == 1:
        return f(2,one_score, two_score)/2 + f(2,one_score+1,two_score)/2

    if (one_score, two_score) in f_dict:
        return f_dict[(one_score, two_score)]

    max_prob = 0

    for t in range(1,8+1):
        prob_two_next = (1/2**t)/(1 - (2**t-1)/(2**(t+1)))

        prob_win = prob_two_next * f(1, one_score, two_score + 2**(t-1))
        prob_win += (1-prob_two_next) * f(2, one_score +1, two_score)

        max_prob = max(max_prob, prob_win)


    f_dict[(one_score, two_score)] = max_prob
    return max_prob

print("Answer: %.8f" % f(1,0,0))
print("Time: ", time() - start)
# 0.83648556
