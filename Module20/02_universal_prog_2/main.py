def is_prime(n):
    for i in range(2, n):
        if n % i == 0 and n != 0:
            return False
    else: return True

def listPrimeN(obj):
    return [value for ind, value in enumerate(obj) if is_prime(ind)]


tpl = ('q', 'w', 'e', 'y', 'i', 'j', 'h')
str = 'qweyijh'
lst = ['q', 'w', 'e', 'y', 'i', 'j', 'h']
print(listPrimeN(tpl))
print(listPrimeN(str))
print(listPrimeN(lst))