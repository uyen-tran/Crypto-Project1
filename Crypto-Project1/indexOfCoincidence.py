from frequencyAnalysis import *

def indexOfCoincidence(cipher,m):
    cipherLen = cipherLength(cipher)
    subStr = ['']*m
    for i in range(cipherLen):    
        subStr[i%m] = subStr[i%m]+cipher[i]

    avgIndexOfCoincid = 0
    for i in range(m):
        singleIndex = singleKeyIndex(subStr[i])
        avgIndexOfCoincid += singleIndex
    avgIndexOfCoincid /= m

    return avgIndexOfCoincid

def singleKeyIndex(cipher):
    cipherLen = cipherLength(cipher)
    monoFrequency = monogramsFrequency(cipher)
    indexOfCoincid = 0
    for i in range(26):
        fi = monoFrequency[i]
        indexOfCoincid += fi*(fi-1)
    indexOfCoincid /= cipherLen*(cipherLen-1)
    return indexOfCoincid

def shiftedIndexOfCoincidence(cipher,g):
    pi = englishFrequencies()
    pi.sort(key=lambda x:x[0])
    fi = monogramsFrequency(cipher)
    #print(fi)
    n = cipherLength(cipher)
    shiftedIndex = 0
    for i in range(26):
        #print(chr(i+65),chr(((i+g)%26)+65))
        shiftedIndex += pi[i][1]*fi[(i+g)%26]
    shiftedIndex /= n
    return shiftedIndex/100