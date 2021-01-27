a = [5, 1, 17, 6, 8, 34, 19, 9]
a.sort()
def sort_f(a):
    for i in a:
        if i % 2 == 1:
            print(i)
    for j in a:
        if j % 2 == 0:
            print(j)
sort_f(a)



