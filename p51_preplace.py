import math
import itertools
import copy

primes = [2,3]
primeHash = {2:0, 3:0}

def genPrimeList(target):
    global primes
    for i in range(4, target):
        for prime in primes:
            if (i % prime) == 0:
                break
            if prime >= math.sqrt(i):
                primes.append(i)
                primeHash[i] = True
                break

genPrimeList(100)
print(primes)

def findSameDigit(num_same, digit):
    track_Digit = [True] * len(digit)
    returnList = list()

    for i_initDigit in range(0,len(digit)):
        sameDigitIndices = list()
        if track_Digit[i_initDigit]:

            for i_currDigit in range(i_initDigit, len(digit)):
                if digit[i_initDigit] == digit[i_currDigit]:
                    sameDigitIndices.append(i_currDigit)
                    track_Digit[i_currDigit] = False

            if len(sameDigitIndices) == num_same:
                returnList.append(sameDigitIndices)

    return returnList

print(findSameDigit(3, [1,1,1]))
print(findSameDigit(3, [1,1,1,1]))
print(findSameDigit(2, [1, 2, 1, 2, 3, 3, 4]))

def genAllPrimeMutations(prime):
    digits = [int(d) for d in str(prime)]
    returnList = {prime:0}
    toMutate = list()
    indList = list()

    for num_match in range(0, len(digits)+1):
        indList += findSameDigit(num_match, digits)

    for n in indList:
        for i in range(1,len(n)+1):
            toMutate += list(itertools.combinations(n,i))

    for pMutation in toMutate:
        cDigits = copy.deepcopy(digits)
        for val in range(0,10):
            for ind in pMutation:
                cDigits[ind] = val
            key = int(''.join(str(e) for e in cDigits))
            if len([int(d) for d in str(key)]) == len(digits):
                if key in primeHash:
                    returnList[key] = 0

    return returnList

print(genAllPrimeMutations(11))

def primeDigitReplacement(target):
    for prime in primes:
        mutatedPrimes = copy.deepcopy(genAllPrimeMutations(prime))
        if len(mutatedPrimes) == target:
            return prime
    print("No Such Prime")
    return -1

genPrimeList(1000000)
test1 = genAllPrimeMutations(333337)
print(test1)
print(len(test1))

print(primeDigitReplacement(11))
print(primeDigitReplacement(8))
print(primeDigitReplacement(16))

#print(primeDigitReplacement(60))
