def fuctorial(a):
    res = 1
    for i in range(1, a + 1):
        res *= i
    return(res)

print(fuctorial(5))