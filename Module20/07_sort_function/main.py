def tpl_sort(tpl):
    for i in tpl:
        if not isinstance(i, int):
            return tpl
    return tuple(sorted(tpl))

tpl = (1, 3, 7, 6, 5, 44, 2, 6, 1)
tpl1 = (1 , 3, 7, 6.2, 5, 44.4, 2, 6, 1)

print (tpl_sort(tpl))
print (tpl_sort(tpl1))
