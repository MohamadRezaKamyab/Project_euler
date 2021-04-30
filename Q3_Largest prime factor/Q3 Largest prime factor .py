#The prime factors of 13195 are 5, 7, 13 and 29.
#What is the largest prime factor of the number 600851475143 ?

a = 2;
number = 600851475143;
reverse = 0;

for a in range(a , number):

    while (number % a == 0):
        if reverse != a:
            reverse = a
            print(reverse)    
        number = number / a
    