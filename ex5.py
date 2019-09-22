import hashlib
def main() :

    #ciphertext
    ciphertext = " "
    # 1) read input ( password)
    password = input("enter the password: ")

    # 2) pass password to sha256
    hash1 = hashlib.sha256(password.encode()).hexdigest()

    # 3) pass the resulting value again to sha256
    hash2 = hashlib.sha256(hash1.encode()).hexdigest()

    #make hexadecimal keys
    global wholekey
    wholekey = hash1 + hash2

    plaintext = input("give me input nom, nom: ")
    #test if input is right size or use padding

    # repeat as many times as there is blocks
    for i in range (0, len(plaintext), 8):
        #split input into blocks of 8bytes
        block = plaintext[i:(i+8)]
        #split block into LH & RH
        LH = block[0 : len(block)//2]
        RH = block[len(block)//2 : ]

        #make 16 rounds with rh and lh
        for i in range (0, 16):
            LH, RH = feistel(LH,RH,i)
        #append the ciphertext of the last block
        ciphertext = ciphertext + feistel(LH,RH,i)
    return ciphertext

#returns the 4byte key of a certain round
def key(round) :
    return wholekey[round*8 : (round*8)+4 ]

<<<<<<< HEAD
# def keyz() :

# def feistel() :
=======
def feistel(LH,RH,round) :

    oldLH = LH
    # the old right half becomes the new left half
    LH = RH

    # LH1 ^ F(RH, key)
    # old left half XORed with
    RH = int(oldLH, base = 16) ^ int(key(round), base = 16)
    return(LH, RH)

>>>>>>> d1ab48686720602b22c5a42e4730f5b0d3d72ba1

if __name__ == "__main__":
    main()

    # 4)keys =  interpret characters of the sha256sum as hexadecimal values. (at the end: 64 bytes)
    # feistel function works on blocks of 8 bytes
    # 5) l2 = r1, r2 = manipulate l1
