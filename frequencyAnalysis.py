from audioop import reverse


def cipherLength(cipher):
    return len(cipher)

def monogramsFrequency(cipher):
    monoFrequency = [0]*26
    for i in range(26):
        monoFrequency[i] = cipher.count(chr(i+65))
    return monoFrequency

def monogramsPercentage(monoFrequency,cipherLen):
    monoPercentage = [0]*26
    for i in range(26):
        monoPercentage[i] = monoFrequency[i]/cipherLen*100
    return monoPercentage

def englishFrequencies():
    ## cited from https://cryptoclub.org/#vAllTools ##
    engFreq = [['e',12.7],['t',9.1],['a',8.2],
               ['o',7.5],['i',7.0],['n',6.8],
               ['s',6.3],['h',6.1],['r',6.0],
               ['d',4.3],['l',4.0],['u',2.8],
               ['c',2.8],['w',2.4],['m',2.4],
               ['f',2.2],['y',2.0],['g',2.0],
               ['p',1.9],['b',1.5],['v',1.0],
               ['k',0.8],['x',0.2],['j',0.2],
               ['z',0.1],['q',0.1]]
    return engFreq

def sortedMonoPercentage(monoPercentage):
    sortedMonoPercent = [['A',0] for i in range(26)]
    for i in range(26):
        sortedMonoPercent[i][1] = monoPercentage[i]
        sortedMonoPercent[i][0] = chr(i+65)
    sortedMonoPercent.sort(key=lambda x:x[1], reverse=True)
    return sortedMonoPercent

def printSortedMonogramsPercentage(monoPercentage):
    sortedMonoPercent = sortedMonoPercentage(monoPercentage)
    #print(sortedMonoPercent)
    
    engFreq = englishFrequencies()
    print("Letter Frequencies")
    print(" Cipher    VS   English")
    for i in range(26):
        print(sortedMonoPercent[i][0],':',round(sortedMonoPercent[i][1],1),
                '%     ',engFreq[i][0],':',engFreq[i][1],'%')

def digramFrequencies(cipher):
    cipherLen = cipherLength(cipher)
    digramFrequency = [[0]*26 for i in range (26)]
    for i in range(cipherLen-1):
        x = ord(cipher[i]) - 65
        y = ord(cipher[i+1]) - 65
        digramFrequency[x][y] += 1

    return digramFrequency

def sortedDigramFrequencies(diFreq):
    sortedDiFreq = [['A',0] for i in range(26*26)]
    index = 0
    for i in range(26):
        for j in range(26):
            sortedDiFreq[index][0] = chr(i+65)+chr(j+65)
            sortedDiFreq[index][1] = diFreq[i][j]
            index += 1
    sortedDiFreq.sort(key=lambda x:x[1], reverse=True)
    return sortedDiFreq

def mostFrequentDigrams():
    mostFreqDigr = ['TH','HE','IN','ER','AN','RE',
                    'ON','AT','EN','ND','TI','ES']
    return mostFreqDigr