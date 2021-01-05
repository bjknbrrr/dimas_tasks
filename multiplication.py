a = int(input('Please, enter a number: '))
b = int(input('Please, enter a number: '))
c = a
def mult(a, b, c):
    for i in range(1, b):
        if i <= b:
            a += c
    if a == 0 or b == 0:
        return('0')
    else:
        return(a)
print(mult(a, b, c))
