import hashlib
def main() :
    # 1) read input ( password)
    password = input("enter the password: ")

    # 2) pass password to sha256
    hash1 = hashlib.sha256(password.encode()).hexdigest()

    # 3) pass the resulting value again to sha256
    hash2 = hashlib.sha256(hash1.encode()).hexdigest()

    print(password)
    print(hash1)
    print(hash2)

# def keyz() :

# def feistel() :

if __name__ == "__main__":
    main()


    # 3) pass the resulting value again to sha256
    # 4)keys =  interpret characters of the sha256sum as hexadecimal values. (at the end: 64 bytes)
    # feistel function works on blocks of 8 bytes
    # 5) l2 = r1, r2 = manipulate l1
