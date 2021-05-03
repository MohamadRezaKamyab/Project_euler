#! /usr/bin/python3

#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?
from math import sqrt, ceil

def main():
    print(Largest_Prime(60))

def Largest_Prime(n):
    # since 2 is the only even prime
    if n == 1: return print('there is no prime numbers')
    if n < 1: return print('the number you have given is not a Natural Number')
    
    counter = 2
    while (n % counter) == 0:
        n = n / counter
        prime = counter
    
    counter = 3
    while counter <= n:
        while (n % counter) == 0:
            n = n / counter
            prime = counter
        counter += 2
    
    return prime
if __name__ == "__main__" : main()
    