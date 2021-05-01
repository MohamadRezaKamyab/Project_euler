#! /usr/bin/python3

def main ():
    print(multiplesof_3_and_5(999))

def sumdividedby3 (n):
    sum = 3 * (n // 3 * (n // 3 + 1) / 2)
    return sum

def sumdividedby5 (n):
    sum = 5 * (n // 5 * (n // 5 + 1) / 2)
    return sum

def sumdividedby15 (n):
    sum = 15 * (n // 15 * (n // 15 + 1) / 2)
    return sum

def multiplesof_3_and_5 (n):
    sum = sumdividedby3(n) + sumdividedby5(n) - sumdividedby15(n)
    return sum

if __name__ == '__main__': main()