import sys
with open(sys.argv[1], 'r') as cipherText:
    cipher = cipherText.read()

cipher = cipher.replace(" ", "")
cipher = cipher.upper()

key = ['c','k','p','s','m','n','t',
        'u','q','v','w','g','b','x',
        'y','h','o','i','j','e','r',
        'z','l','f','d','a']

decryptedMess = ''
for i in range(len(cipher)):
    x = ord(cipher[i])-65
    decryptedMess += key[x]

with open('plaintext2.txt', 'w') as f:
        f.write(decryptedMess)

print("The decrypted message is now in 'plaintext2.txt' .")
