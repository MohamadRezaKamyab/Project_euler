#! /usr/bin/python3
from math import sqrt, floor

def main():
    for a in range(1 , 1000 // 3):
        for b in range(1000):
            c = sqrt((a ** 2) + (b ** 2))
            if a + b + c == 1000:
                print(a * b * c)
if __name__ == '__main__' : main()