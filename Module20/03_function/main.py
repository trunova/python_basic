def f(x, n):
    firstInd = x.index(n)
    secondInd = len(x)
    for i in enumerate(x):
        if i[1] == n and x.index(n) != i[0]:
            secondInd = i[0] + 1
            break
    return x[firstInd: secondInd]
x = (1, 2, 3, 4, 4, 5, 6, 3)

print(f(x, int(input('Введите число: '))))
