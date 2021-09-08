listClass1 = []
listClass2 = []
listClass = []
for i in range(160, 177, 2):
    listClass1.append(i)
for i in range(162, 181, 3):
    listClass1.append(i)
n = 160
m = 162
for i in range(16):
    if n > m:
        listClass.append(m)
        m += 3
    else:
        listClass.append(n)
        n += 2
print(listClass)