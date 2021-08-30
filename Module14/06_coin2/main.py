import math
print('Введите координаты монетки:')
x = float(input('X = '))
y = float(input('Y = '))
r = float(input('Введите радиус: '))
oxy = math.sqrt(x*x + y*y)
if oxy <= r:
    print('Монетка где-то рядом')
else: print('Монетки в области нет')