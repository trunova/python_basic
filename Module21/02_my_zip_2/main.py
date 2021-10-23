def my_zip(s1, s2):
    l = list()
    if min(len(s1), len(s2)) > 0:
        l.append((s1[0], s2[0]))
        l.extend(my_zip(s1[1:], s2[1:]))
    return l

print(my_zip(['a', 'b', 'c'], ['p', 'r', 't', 'y']))
print(my_zip('uabc', 'rty'))
print(my_zip(('a', 'b', 'c'), ('r', 't', 'y')))



