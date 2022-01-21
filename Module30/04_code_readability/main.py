
def sim(x: int) -> bool:
    if x in [0, 1]:
        return False
    for i in range(2, x):
        if x % i == 0 or x == 0:
            return False
    return True


if __name__ == "__main__":
    print(list(filter(lambda x: all(map(lambda i: x % i != 0, range(2, int(x ** 0.5) + 1))), range(2, 1001))))

    print(list(filter(lambda x: sim(x), range(0, 1001))))
