#ЦИКЛ

def fuctorial(a):
    res = 1
    for i in range(1, a + 1):
        res *= i
    return(res)
print(fuctorial(5))

#РЕКУРСИЯ
def fuctorial(a, res):
    if a == 0 or a==1:
        return res
    else:
        return fuctorial(a-1, (res*(a)))
print(fuctorial(6, 1))
