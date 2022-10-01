import math
from frequencyAnalysis import*

def isPermutation(monoPercentage):
    engFreq = englishFrequencies()

    score = 0
    for i in range(26):
        engLetter = engFreq[i][0].capitalize()
        sortedMonoPercent = sortedMonoPercentage(monoPercentage)
        nextEngLetter = ''
        preEngLetter = ''
        if (i < 25):
            nextEngLetter = engFreq[i+1][0].capitalize()
        if (i > 0):
            preEngLetter = engFreq[i-1][0].capitalize()
        cipherLetter = sortedMonoPercent[i][0]
        if ((engLetter == cipherLetter)
                #& (sortedMonoPercent[i][1]/engFreq[i][1] < 1.15)):
                | (nextEngLetter == cipherLetter)
                | (preEngLetter == cipherLetter)):
            score += 1
    if (score >= 10):
        return True
    else:
        return False

def compareToEngDigFreq(digrams):
    engDig = mostFrequentDigrams()
    score = 0
    for i in range(10):
        #print(digrams[i][0])
        for j in range(10):
            if (digrams[i][0] == engDig[j]):
                score += 1
    return score

def decryptedPermutation(cipher):
    cipherLen = cipherLength(cipher)
    #print(cipherLen)
    divisors = []
    n = math.ceil(cipherLen/2)
    for i in range(n):
        if (cipherLen % (i+2) == 0):
            divisors.append(i+2)
    print("All The Possibilities For Key Length Are:")
    print(divisors)

    digramList = []
    for i in range(len(divisors)):
        numOfCols = divisors[i]
        numOfRows = math.floor(cipherLen/numOfCols)
        diFreq = [[0]*26 for i in range (26)]
        for j in range(cipherLen-numOfRows):
            #if ((j%numOfRows)!= 0):
            x = ord(cipher[j]) - 65
            y = ord(cipher[j+numOfRows]) - 65
            diFreq[x][y] += 1
        diFreq = sortedDigramFrequencies(diFreq)
        digramList.append(diFreq)

    max = -1
    keyLen = 0
    for i in range(len(digramList)):
        score = compareToEngDigFreq(digramList[i])
        #print(divisors[i],score)
        if (score > max):
            max = score
            keyLen = divisors[i]
    print("The Key Length Is Likely To Be",keyLen,'.')

    numOfRows = math.floor(cipherLen/keyLen)
    decryptedList = ['']*numOfRows
    for i in range(cipherLen):
        decryptedList[i%numOfRows] += cipher[i]
    #print(decryptedMess)
    #for i in range(keyLen):
        #print(decryptedList[i])
    return decryptedList