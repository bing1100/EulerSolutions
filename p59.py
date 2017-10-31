import functools
import copy

# Place data into list format
cipherFile = open("p059_cipher.txt", "r")
data = [int(x) for x in cipherFile.read().split(",")]

# Common strings to look for in the data, add to this list
commonStrings = [['t','h','e'], ['a','n','d']]

# The threshold of occ of common strings to print the decoded message
threshold = 10

# Data storage
allDecryptions = []
prunedDecryptions = []

# Function that decodes datum using a length 3 key
def decryptXOR(datum, len3Key):
    ind = 0
    returnVal = []
    for char in datum:
        returnVal.append( char ^ len3Key[ind % 3] )
        ind += 1
    return returnVal

# Function that generates all decryptions of data using all 3 len lowercase letter combinations
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

# Function that counts the total occurrence of common strings in some datum
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
            else:
                posTrack[idx] = 0
    val = sum(x for x in occTrack)
    if (val > 0):
        print("Found with " + str(val))
    return int(val)

print(countCommonOcc(['t','h','e']))

# Function that prunes all the decryptions and only prints those messages with common word occurences
#  higher than the threshold
def pruneDecryptions():
    global allDecryptions
    global prunedDecryptions
    global threshold

    print("Starting to prune")

    occMap = list(map(lambda datum: countCommonOcc(datum), prunedDecryptions))
    printMap = list(map(lambda num: num >= threshold, occMap))

    print("Done Prunning")

    idx = 0 
    for b in printMap:
        if b:
            print("".join(allDecryptions[idx]))
        idx += 1

# Call the functions
decrypt()
pruneDecryptions()

"""
FOUND THIS IN THE DATA

(The Gospel of John, chapter 1) 1 In the beginning the Word already existed. He was with God, and he was God. 2 He was in the beginning with God. 3 He created everything there is. Nothing exists that he didn't make. 4 Life itself was in him, and this life gives light to everyone. 5 The light shines through the darkness, and the darkness can never extinguish it. 6 God sent John the Baptist 7 to tell everyone about the light so that everyone might believe because of his testimony. 8 John himself was not the light; he was only a witness to the light. 9 The one who is the true light, who gives light to everyone, was going to come into the world. 10 But although the world was made through him, the world didn't recognize him when he came. 11 Even in his own land and among his own people, he was not accepted. 12 But to all who believed him and accepted him, he gave the right to become children of God. 13 They are reborn! This is not a physical birth resulting from human passion or plan, this rebirth comes from God.14 So the Word became human and lived here on earth among us. He was full of unfailing love and faithfulness. And we have seen his glory, the glory of the only Son of the Father.

"""