a = int(input('Please, enter a number: '))
b = int(input('Please, enter a number: '))

def mult(a, b):
    c = a
    if a == 0 or b == 0:
        return('0')

    if b < 0:
        b = -b

    for i in range(1, b):
        if i <= b:
            a += c
    return(a)

print(mult(a, b))
