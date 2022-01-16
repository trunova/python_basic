from collections import Counter


def can_be_poly(line: str) -> bool:
    return len(list(filter(lambda x: x % 2, list(Counter(line).values())))) <= 2


if __name__ == "__main__":
    print(can_be_poly('ababc'))
    print(can_be_poly('abbbc'))