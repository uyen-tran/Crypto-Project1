import sys
from frequencyAnalysis import *
from indexOfCoincidence import *
from permutationCipher import decryptedPermutation, isPermutation
from shiftCipher import *
from vigenereCipher import*

with open(sys.argv[1], 'r') as cipherText:
    cipher = cipherText.read()

cipher = cipher.replace(" ", "")
cipher = cipher.upper()

cipherLen = cipherLength(cipher)

    ### Frequency Analysis ###

# monogram frequencies #
monoFrequency = monogramsFrequency(cipher) 
monoPercentage = monogramsPercentage(monoFrequency,cipherLen)
printSortedMonogramsPercentage(monoPercentage) 

# digram frequencies #
diFreq = digramFrequencies(cipher)
sortedDiFreq = sortedDigramFrequencies(diFreq)
# print the first 10 digrams with highest frequencies #
print("The Most Common Digrams In The Cipher Are:")
for i in range(15):
    print(sortedDiFreq[i][0],':',sortedDiFreq[i][1],'times')


    ### Index Of Coincidence ###

singleIndex = singleKeyIndex(cipher)
print("Index of Coincidence:",round(singleIndex,3),'.')


    ### Cipher Type Analysis ###

if (isVigenere(singleIndex)):
    print("The given cipher is likely a Vigenere Cipher .")
    message = decryptedVigenere(cipher)
    print("The decrypted message will be outputted to a file '.txt'.")
    name = input("How do you want to name your file? ")
    with open(name, 'w') as f:
        f.write(message)
    print("The message is now in",name,'.')
else:
    #if the ciphertext frequencies look very similar to English frequencies,
    #then it is likely a Permutation cipher.
   
    if (isPermutation(monoPercentage)):
        print("The given cipher is likely a Permutation Cipher .")
        message = decryptedPermutation(cipher)
        print("The Possible Matrix Is:")
        for i in range(len(message)):
            print(message[i])
        print("We haven't been able to find the permutation .")
    else:
        key = findShiftKey(cipher)
        if (key != -1):
            print("The given cipher is likely a Caesar Cipher with key =",key,'.')
            message = decryptedCaesar(cipher,key)
            print("The decrypted message will be outputted to a file '.txt'.")
            name = input("How do you want to name your file? ")
            with open(name, 'w') as f:
                f.write(message)
            print("The message is now in",name,'.')
        else:
            engIC = 0.06506
            if (abs(engIC-singleIndex) < 0.006):
                print("The given cipher is likely a Substitution Cipher.")
                print("User should try to decrypt mannually using the frequencies analysis.")
            else:
                print("The given cipher is likely a One-Time Pad Cipher which cannot be solve.")
