def is_prime(n):
    if n != 0 and n != 1:
        for i in range(2, n):
            if n % i == 0 :
                return False
        else: return True
    else: return False

def listPrimeN(obj):
    return [value for ind, value in enumerate(obj) if is_prime(ind)]


tpl = ('q', 'w', 'e', 'y', 'i', 'j', 'h')
str = 'qweyijh'
lst = ['q', 'w', 'e', 'y', 'i', 'j', 'h']
print(listPrimeN(tpl))
print(listPrimeN(str))
print(listPrimeN(lst))
