import functools
import copy

cipherFile = open("p059_cipher.txt", "r")

data = [int(x) for x in cipherFile.read().split(",")]

commonStrings = [['t','h','e'], ['a','n','d']]

threshold = 8

allDecryptions = []
prunedDecryptions = []

def decryptXOR(datum, len3Key):
    ind = 0
    returnVal = []
    for char in datum:
        returnVal.append( char ^ len3Key[ind % 3] )
        ind += 1
    return returnVal

def decrypt():
    global allDecryptions
    global data
    for k0 in range(97,123):
        for k1 in range (97, 123):
            for k2 in range(97, 123):
                print("decrypting " + chr(k0) + " " + chr(k1) + " " + chr(k2))

                len3Key = [k0,k1,k2]
                allDecryptions.append([chr(c) for c in decryptXOR(data, len3Key)])
                prunedDecryptions.append([chr(c) for c in decryptXOR(data, len3Key)])
    print("Done Decrypting")

def countCommonOcc(datum):
    global commonStrings
    lenCommonString = [len(common) for common in commonStrings]
    posTrack = [0] * len(commonStrings)
    occTrack = [0] * len(commonStrings)
    for char in datum:
        for idx in range(0,len(commonStrings)):
            compareChar = commonStrings[idx][posTrack[idx]]
            if compareChar == char:
                posTrack[idx] += 1
            if posTrack[idx] == lenCommonString[idx]:
                posTrack[idx] = 0
                occTrack[idx] += 1
    val = reduce(lambda sum,y: sum + y, occTrack)
    print("Found with " + str(val))
    return val

def pruneDecryptions():
    global allDecryptions
    global prunedDecryptions
    global threshold

    print("Starting to prune")

    map(lambda datum: countCommonOcc(datum), prunedDecryptions)

    print("Done Prunning")

    map(lambda num: num >= threshold, prunedDecryptions)

    idx = 0
    for b in prunedDecryptions:
        if b:
            print("".join(allDecryptions[idx]))
        idx += 1

decrypt()
pruneDecryptions()
