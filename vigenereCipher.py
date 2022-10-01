from indexOfCoincidence import*
from shiftCipher import*

def isVigenere(indexOfCoincid):
    if ((indexOfCoincid < 0.055)&(indexOfCoincid > 0.038)):
        return True
    else:
        return False

def findKeyLen(cipher):
    engIC = 0.06506
    m = 1
    isFound = False
    while (m < 26) & (isFound == False):
        m += 1
        mIndex = indexOfCoincidence(cipher,m)
        diff = abs(mIndex-engIC)
        if (diff < 0.005): 
            isFound = True
    return m

def multiKeysShift(cipher,keys):
    keyLen = len(keys)
    decryptedList = list(cipher)
    for i in range(len(decryptedList)):
        x = (ord(cipher[i])-65-keys[i%keyLen])%26
        decryptedList[i] = chr(x+97)
    decryptedMess = ""
    for i in range(len(decryptedList)):
        decryptedMess += decryptedList[i]
    return decryptedMess

def decryptedVigenere(cipher):
    cipherLen = cipherLength(cipher)
    keyLen = findKeyLen(cipher)
    print("The Key Length Of This Cipher Is",keyLen,'.')
    subStr = ['']*keyLen
    for i in range(cipherLen):
        subStr[i%keyLen] = subStr[i%keyLen]+cipher[i]

    keys = [-1]*keyLen
    for i in range(keyLen):
        #print("m =",i)
        keys[i] = findShiftKey(subStr[i])
    key = ""
    for i in range(keyLen):
        key += chr(keys[i]+97)
    print("The Key is",key,'.')
    decryptedMess = multiKeysShift(cipher,keys)
    #print(decryptedMess)
    return decryptedMess