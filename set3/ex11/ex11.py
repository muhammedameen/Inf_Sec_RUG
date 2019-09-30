import sys

def largePower(base, power ,modulus):
    if (power == 1):
        return base
    
    returned = largePower(base, power >> 1, modulus)
    returned = returned * returned % modulus
    if (power % 2 == 1):
        return returned * base % modulus
    else:
        return returned
    

def main(): 
    base, power, modulus = input("Enter: base power modulus").split()
    #print(largePower(43210,23456,99987))
    print(largePower(base,power,modulus))




if __name__ == "__main__":
    main()