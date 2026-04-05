################################################################################
# 51-primeDigitReplacements.py
#
# By replacing the 1st digit of the 2-digit number *3, it turns out that six of
# the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
#
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit
# number is the first example having seven primes among the ten generated numbers
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993.
#
# Consequently 56003, being the first member of this family, is the smallest
# prime with this property.
#
# Find the smallest prime which, by replacing part of the number
# (not necessarily adjacent digits) with the same digit, is part of an
# eight prime value family.
#
################################################################################
import math
import sympy as sy
################################################################################
def makePrimeList(begin,end):
    primes = [p for p in sy.primerange(begin,end)]
    return(primes)
################################################################################
primeset = set()
primes = makePrimeList(10**5,10**6)
for i in range(len(primes)):
    primeset.add(primes[i])
    
primeIndex = 0

def permu(bag):
	if len(bag) > 0:
		b= replacable_check(bag)
		if b: return b
	check = None
	for i in bag:
		check = permu([j for j in bag if not j == i])
		if check: return check
		
def replacable_check(bag):
	global primes, primeIndex
	p = [c for c in str(primes[primeIndex])]
	for i in bag: p[i] = "*"
	count, replacement = 0, -1
	for i in range(10):
		if int(''.join(p).replace("*", str(i))) in primeset:
			count += 1
			if i==0 and p[0]=="*": count -= 1
			elif replacement==-1: replacement = str(i)
	if count >= 8:
		return (''.join(p), primes[primeIndex], ''.join(p).replace("*", replacement))

result = None
while primeIndex<len(primes):
	result  = permu( range( len(str(primes[primeIndex]))-1))
	if result: break
	primeIndex += 1
	
if not result:
    print("no solution found")
else:
    print("template: %s, prime: %s, smallest in family: %s" % result)
################################################################################
#solution: 121313
################################################################################
