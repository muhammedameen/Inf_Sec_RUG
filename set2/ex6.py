import sys 
import binascii

########## ENCRYPTION #########

def getPublicKey(privateKey,n,m):
    publicKey = []
    for a in privateKey:
        publicKey.append((m * a) % n)
    
    return publicKey

def getEncryptedValue(weightValue, publicKey):
    value = 0
    for idx in range(0,len(publicKey)):
        if (weightValue & 1): #there is a 1 on the first bit
            value += publicKey[idx]
            #print(publicKey[idx])
        weightValue >>= 1 #shift one step to the right
    
    return value

def encrypt(text,publicKey):
    encryption = []
    if (len(text) % 2 == 0): #we need uneven number of char
        text += '0'
    for idx in range(0,len(text)-1):
        if (idx % 2 != 0): #we only want to handle the even idx,because 2 char/block
            continue
        weightValue =  (ord(text[idx]) << 8 ) + ord(text[idx+1])
        encryption.append(getEncryptedValue(weightValue,publicKey))
    return encryption

######### DECRYPTION ##############

def getWeights(number, privateKey):
    weights = ""
    idx = len(privateKey) - 1 #we want to start at the highest value
    while (idx >= 0):
        if (number >= privateKey[idx]): 
            number -= privateKey[idx]
            weights += '1'
        else:
            weights += '0'
        idx -= 1 
    if (number != 0):
        print("ERROR in getWeights()")
    return int(weights,2)
    

def decrypt(encryptedMessage, n, privateKey):
    originalText = ""
    modularInverse = 11929
    for num in encryptedMessage:
        num = num * modularInverse % n
        weight = getWeights(num,privateKey)
        originalText += chr(weight >> 8) + chr(weight & 255)
    return originalText


def main():
    privateKey = [1,3,7,12,25,48,96,194,388,775,1550,3101,6200,12413,24843,49726]
    n = 149112
    m = 25
    text = "Hello World!"
    publicKey = getPublicKey(privateKey,n,m)
    encryptedMessage = encrypt(text,publicKey)
    print("encryption", encryptedMessage)
    originalText = decrypt(encryptedMessage,n,privateKey)
    print("original text: ",originalText)
    

if __name__ == "__main__":
    main()