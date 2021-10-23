nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]

def listComprehensions(lst, newLst):
    for i in lst:
        if isinstance(i, list):
            listComprehensions(i, newLst)
        else:  newLst.append(i)

newLst = list()
listComprehensions(nice_list, newLst)
print(newLst)