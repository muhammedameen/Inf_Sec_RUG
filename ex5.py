import hashlib
# dafuq? hexadecimals, binary, string. when do i need which data type?



def main() :

    #ciphertext
    ciphertext = " "
    # 1) read input ( password)
    password = input("enter the password: ")

    # 2) pass password to sha256
    hash1 = hashlib.sha256(password.encode()).hexdigest()
    print(type(hash1))

    # 3) pass the resulting value again to sha256
    hash2 = hashlib.sha256(hash1.encode('UTF-8')).hexdigest()

    #make hexadecimal keys
    global wholekey
    wholekey = hash1 + hash2

    plaintext = input("input: ")
    #test if input is right size or use padding

    #split plaintext into blocks of 8 bytes
    # repeat as many times as there is blocks
    for i in range (0, len(plaintext), 8):
        #split input into blocks of 8bytes
        block = plaintext[i:(i+8)]

        #split block into LH & RH
        LH = block[0 : ((len(block)//2))]

        RH = block[(len(block)//2) : ]


        #encrytion
        # 16 rounds
        for r in range (0, 16):
            LH, RH = feistel(LH,RH,r)

        #append the ciphertext of the last block
        ciphertext += (LH + RH)

    return ciphertext

#returns the 4byte key of a certain round
def key(round) :
    currentkey = wholekey[round*8 : (round*8)+4 ]
    return currentkey

def feistel(LH,RH,round) :

    oldLH = LH
    # the old right half becomes the new left half
    LH = RH
    print(oldLH, key(round))
    RH = xor(oldLH, key(round))
    return(LH, RH)

#hex(ord('a') ^ 0x4b)

# xor two strings
def xor(s1, s2):
    return ''.join(chr(ord(a) ^ ord(b)) for a, b in zip(s1, s2))

if __name__ == "__main__":
    print(main())

    # 4)keys =  interpret characters of the sha256sum as hexadecimal values. (at the end: 64 bytes)
    # feistel function works on blocks of 8 bytes
    # 5) l2 = r1, r2 = manipulate l1
