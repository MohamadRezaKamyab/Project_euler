#! /usr/bin/python3

def main ():
    sum = sumsquaredifference(100)
    print(sum)

def sumofsquare(n):
    # sum of square numbers =  [n(n+1)(2n+1)] / 6
    sumofsquare = (n * (n + 1) * (2 * n + 1)) / 6 
    return sumofsquare

def squaresum(n):
    squaresum = (n * (n + 1)) / 2
    squaresum *= squaresum 
    return squaresum

def sumsquaredifference(n):
    sumsquaredifference = squaresum(n) - sumofsquare(n)
    return sumsquaredifference
   
if __name__ == "__main__": 
    main()             