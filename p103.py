import math

listSpecialSets = [[1], [1,2]]

def genNewDiff(diff):
    firstDiff = diff[0]
    sumDiff = sum(diff[1:])

    if firstDiff < sumDiff:
        sortedDiff = sorted(diff[1:])
        newDiff = [sumDiff]
        newDiff.extend(sortedDiff)
        return newDiff

    return diff

print(genNewDiff([6,3,2,1,1]))

def genDiff(listNum):
    diff = [listNum[0]] * len(listNum)

    for idx in range(1, len(listNum)):
        diff[idx] = listNum[idx] - listNum[idx-1]

    return diff

print(genDiff([1,2,3,4,5,6]))

def makeNewSeq(oldSeq, diff):
    baseNum = oldSeq[math.floor(len(oldSeq)/2) - 1]
    newSeq = [baseNum]

    for idx in range(0, len(diff)):
        newSeq.append(newSeq[idx] + diff[idx])

    return newSeq

print(makeNewSeq([1,2,3,4], [1,2,3,4,5]))

def genSpecialSequence(n):

    for i in range(1, n):

        diff = genNewDiff(genDiff(listSpecialSets[i]))
        newSeq = makeNewSeq(listSpecialSets[i], diff)

        listSpecialSets.append(newSeq)

    return listSpecialSets[n]

print(genSpecialSequence(5))
    