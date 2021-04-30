#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?


def multiples(n):
    i = 0;
    multipleprime = 0;
    for counter in range(2 , n):
        if n % counter == 0:
            if isprime(counter) == True:              
                i += 1
                if counter != multipleprime :
                    multipleprime = counter
        if i > 1:
            multipleprime = 0
        else:
            continue
    else:
        return multipleprime


def isprime (n):
    if n == 1:
        return False
    for counter in range (2 , n):
        if n % counter == 0 :
            break
    else:
        return True
    return False

def smallmultiple (n):
    smallmulty = 1;
    for counter in range (2 , n + 1):
        if isprime(counter) == True:
            smallmulty *= counter
        else:
            if multiples(counter) != 0:
                smallmulty *= multiples(counter)
    return smallmulty
                
number = 20;
print(smallmultiple(number))
                
               