def summ(*args, lst=None):
    s = 0
    if lst == None:
        for i in args:
            s += i
    else:
        for i in lst:
            if isinstance(i, list):
                s += summ(lst=i)
            else: s += i
    return s

print(summ(lst=[[1, 2, [3]], [1], 3]))
print(summ(1, 2, 3, 4, 5))
