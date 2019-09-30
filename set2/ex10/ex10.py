import sys
import hashlib

def keyScheduling(key):
    keyLength = len(key) #keylength in bits
    permutations = []
    
    #initialize permutations with 0 to 255
    for idx in range(0,255): 
        permutations.append(idx)
    
    idx2 = 0
    for idx1 in range(0,255):
        idx2 = (idx2 + permutations[idx1] + int(key[idx1 % keyLength])) % 256
        permutations[idx1], permutations[idx2] = permutations[idx2], permutations[idx1] 

    print(permutations)
    return permutations

def pseudoRandomGeneration(permutations):
    idx1 = 0
    idx2 = 0
    


def main():
    keyChar = input("Supply the key you want to use: ")
    print (sys.stdin.buffer.read())

    #put the key in binary 
    key = ''.join(format(ord(i), 'b') for i in keyChar)
    print(key) 
    #permutations = keyScheduling(key)
    #pseudoRandomGeneration(permutations)

if __name__ == "__main__":
    main()