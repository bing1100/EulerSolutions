import math

primes = [2]
primesHash = {"2":False}

def findPrimes(highest):
    for candidate in range(3, highest):

        for div in primes:

            if div <= math.sqrt(candidate):
                if (candidate % div) ==  0:
                    break
            else:
                primes.append(candidate)
                primesHash[str(candidate)] = False
                break

def genRotations(prime):

    digitList = [str(d) for d in str(prime)]
    rotationList = [str(prime)]

    for startPos in range(1, len(digitList)):

        rotatedNumber = []

        for ind in range(0, len(digitList)):
             rotatedNumber.append(digitList[(startPos+ind) % (len(digitList))])

        rotationList.append("".join(rotatedNumber))

    return sorted(set(rotationList))

print(genRotations(1234))

def checkListPrimes(listNums):

    listNotAllPrime = False

    for num in listNums:

        if num not in primesHash:
            listNotAllPrime = True
            break
        
    for num in listNums:

        if num in primesHash:
            primesHash[num] = True
    

    return 0 if listNotAllPrime else len(listNums)

def checkPrimes():

    count = 0

    for k, checked in primesHash.items():

        if not checked:

            listToCheck = genRotations(k)

            count += checkListPrimes(listToCheck)

    return count

findPrimes(1000000)
print(len(primes))
print(checkPrimes())
