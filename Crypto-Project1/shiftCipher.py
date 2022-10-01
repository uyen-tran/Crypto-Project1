from indexOfCoincidence import *

def findShiftKey(cipher):
    shiftedIndex = [0]*26
    for i in range(26):
        shiftedIndex[i] = shiftedIndexOfCoincidence(cipher,i)
        #print(i,shiftedIndex[i])
    engIC = 0.06506
    min = 1
    key = -1
    for i in range(26):
        diff = abs(shiftedIndex[i]-engIC)
        #print(i,diff)
        if (diff < min):
            min = diff
            key = i
    #print(min)
    #the longer the cipher are, the smaller the difference can be.
    if (min < 0.008): 
        return key
    else:
        return -1

def decryptedCaesar(cipher,key):
    decryptedList = list(cipher)
    for i in range(len(decryptedList)):
        x = (ord(cipher[i])-65-key)%26
        decryptedList[i] = chr(x+97)
    decryptedMess = ""
    for i in range(len(decryptedList)):
        decryptedMess += decryptedList[i]
    return decryptedMess