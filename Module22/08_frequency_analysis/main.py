def sort_col0(i):
    return i[0]
def sort_col1(i):
    return i[1]
text_file = open('text.txt', 'r')
analysis_file = open('analysis.txt', 'a')
dict_letter = dict()
s = '.,!-\n '
count = 0
for i_line in text_file:
    for i_letter in i_line:
        i_letter = i_letter.lower()
        if not (i_letter in s):
            count += 1
            if i_letter in dict_letter.keys():
                dict_letter[i_letter] = dict_letter.get(i_letter) + 1
            else: dict_letter[i_letter] = 1

lst = list()
for i_key, i_value in dict_letter.items():
    lst.append([i_key, round(i_value / count, 3)])

lst.sort(key=sort_col0)
lst.sort(key=sort_col1, reverse=-1)

for i_list in lst:
    analysis_file.write(i_list[0] + ' ')
    analysis_file.write(str(i_list[1]) + '\n')