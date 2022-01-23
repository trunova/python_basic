import re


def numberTemplate(number: str, index: int):
    print('{} номер:'.format(index), end=' ')
    if re.fullmatch(r'\b[89]\d{9}\b', number) is not None:
        print("всё в порядке")
    else:
        print("не подходит")


if __name__ == "__main__":
    lst = ['9999999999', '999999-999', '99999x9999']
    list(map(numberTemplate, lst, range(1, len(lst) + 1)))
