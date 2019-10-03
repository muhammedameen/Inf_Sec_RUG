import sys

#Function to compute base^power % modulus
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
    base, power, modulus = [int(x) for x in input("Enter base power modulus: \n").split()]
    print(base, "^", power, "%", modulus, "=", largePower(base,power,modulus) )

if __name__ == "__main__":
    main()