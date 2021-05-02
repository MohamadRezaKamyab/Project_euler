#! /usr/bin/python3

def main():
    print(Sum(4000000))

def Sum(n):
    counter = 1;
    summation = 0
    while Even_Fibonacci(counter) < n:
        summation += Even_Fibonacci(counter)
        counter += 1
    return summation

def Even_Fibonacci(n):
    if n == 1: return 2
    if n < 0 : return 0  
    return 4 * (Even_Fibonacci(n - 1)) + Even_Fibonacci(n - 2)


if __name__ == '__main__': main() 