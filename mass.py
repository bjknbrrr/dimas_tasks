a = [5, 1, 17, 6, 8, 34, 19, 9]
a.sort()
b = []

def sort_even(a):
    for i in a:
        if i % 2 == 0:
            b.append(i)
    return b

def sort_odd(a):
    for j in a:
        if j % 2 == 1:
            b.append(j)
    return b

print(sort_odd(a))
print(sort_even(a))
