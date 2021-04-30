sum = 0
a , b , c = 1 , 1 , 2
while c <= 4000000:
    sum += c
    print(sum)
    a = c + b
    b = c + a
    c = b + a
