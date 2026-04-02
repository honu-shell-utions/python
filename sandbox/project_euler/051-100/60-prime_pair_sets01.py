################################################################################
# 60-prime_pair_sets.py
#
# The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes
# and concatenating them in any order the result will always be prime. For
# example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these
# four primes, 792, represents the lowest sum for a set of four primes with
# this property.
#
# Find the lowest sum for a set of five primes for which any two primes
# concatenate to produce another prime.
#
################################################################################
from sympy import sieve, isprime, prime
import itertools
################################################################################
def makePrimeList(size):
    primeList = list(sieve.primerange(size))
    return(primeList)
################################################################################
def makeCombinations(primeList,r):
    combinations_object = itertools.combinations(primeList,r)
    comboList = list(combinations_object)
    return(comboList)
################################################################################
def makePermuts(primeCombo,r):
    permutations_object = itertools.permutations(primeCombo,r)
    permutList = list(permutations_object)
    return(permutList)
################################################################################
def checkPair(first,second):
    first = str(first)
    second = str(second)
    if not isprime(int(first+second)) or not isprime(int(second+first)):
        return False
    else:
        return True
################################################################################
print('--------------------------making prime list---------------------------')
primeList = makePrimeList(700)
print('--------------------------making combo list---------------------------')
comboList = makeCombinations(primeList,4)
winnerList = []
print('--------------------------starting nested loop------------------------')

for i in range(len(comboList)):
    allGood = True
    permutList = makePermuts(comboList[i],2)
    for j in range(len(permutList)):
        if not checkPair(permutList[j][0],permutList[j][1]):
            allGood = False
            break
    if allGood:
        winnerList.append(comboList[i])
        
print('--------------------------printing solution list----------------------')
print(winnerList,sum(winnerList[0]))
################################################################################
################################################################################
