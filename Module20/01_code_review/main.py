students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(dict):
    lst = []
    l = 0
    for i_num, i_information in students.items():
        if 'interests' in i_information:
            lst += i_information['interests']
        if 'surname' in i_information:
            l += len(i_information['surname'])
    return lst, l

pairs = []
for i_num, i_information in students.items():
    if 'age' in i_information:
        pairs += (i_num, i_information['age'])
print(pairs)
my_lst, l = f(students)
print(my_lst, l)
