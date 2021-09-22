def height(i, dict_tree):
    if i not in dict_tree:
        return 0
    else:
        return 1 + height(dict_tree[i], dict_tree)

dict_tree = dict()
for i in range(int(input('Введите количество человек: ')) - 1):
    s = input('{0} пара: '.format(i+1)).split()
    dict_tree[s[0]] = s[1]

dict_answer = dict()
for i in set(dict_tree.keys()).union(set(dict_tree.values())):
    dict_answer[i] = height(i, dict_tree)

for key, value in sorted(dict_answer.items()):
    print(key, value)
