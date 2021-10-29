import zipfile

def sort_col0(i):
    return i[0]

def sort_col1(i):
    return i[1]

zpf = zipfile.ZipFile('voyna-i-mir.zip', 'r')
voyna_i_mir = zpf.extract('voyna-i-mir.txt')
voyna_i_mir_file = open('voyna-i-mir.txt', 'r', encoding='utf-8')
analysis_file = open('result.txt', 'a', encoding='utf-8')

dict_letter = dict()
s = ' .,:;\'/|\?![()]\n0123456789+-=`~@"#$%^&*%№«»…„“—–° '
count = 0
for i_line in voyna_i_mir_file:
    for i_letter in i_line:
        if not (i_letter in s):
            count += 1
            if i_letter in dict_letter.keys():
                dict_letter[i_letter] = dict_letter.get(i_letter) + 1
            else: dict_letter[i_letter] = 1

lst = list()
for i_key, i_value in dict_letter.items():
    lst.append([i_key, round(i_value / count, 3)])

lst.sort(key=sort_col1, reverse=-1)

for i_list in lst:
    analysis_file.write(i_list[0] + ' ')
    analysis_file.write(str(i_list[1]) + '\n')