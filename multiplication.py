a = int(input('Please, enter a number: '))
b = int(input('Please, enter a number: '))
c = a
list1 = []

for i in range(1, b):
    list1.append(i)
#print(list1)


for element in list1:
    if element <= b:
        a += c
#        print(a)
print(a)