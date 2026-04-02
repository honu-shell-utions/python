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
from random import choice
from collections import Counter
################################################################################
def pickpaper(paperlist, paperchoice):
    
    if paperchoice == "A2":
        paperlist.remove(paperchoice)
        paperlist.append("A3")
        paperlist.append("A4")
        paperlist.append("A5")

    elif paperchoice == "A3":
        paperlist.remove(paperchoice)
        paperlist.append("A4")
        paperlist.append("A5")
        
    elif paperchoice == "A4":
        paperlist.remove(paperchoice)
        paperlist.append("A5")
        
    elif paperchoice == "A5":
        paperlist.remove(paperchoice)

    return paperlist
################################################################################
def euler_151(): 
    temp = []
    overall = []
    big_counter = 0
    for x in range(LIMIT):   
        paper = ["A2","A3","A4","A5"]
        for y in range(1,15):
            paperchoice = choice(paper)
            paper = pickpaper(paper, paperchoice)
            if len(paper) == 1:
                big_counter += 1
                continue
    return big_counter
################################################################################
LIMIT = 10**6
start = time()        
print(round(euler_151()/LIMIT-1,6))
sec = round(time()-start,2)
print(f"--- {sec} seconds ---")
################################################################################
#solution: 0.464399
################################################################################
