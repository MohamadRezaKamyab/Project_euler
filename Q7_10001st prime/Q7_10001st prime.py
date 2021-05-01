#! /usr/bin/python3

def main ():
    counter = 0;
    Primenumbers = 0;
    while (Primenumbers != 10001):
        counter +=1
        if isprime(counter) == True:
            Primenumbers += 1
    print(counter)   
def isprime(n):
    if n == 1:
        return False
    for divider in range (2 , n):
        if n % divider == 0:
            return False
    else:
        return True

if __name__ == "__main__" :
    main()  