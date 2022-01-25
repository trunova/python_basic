import itertools

if __name__ == "__main__":
    numbers = '0123456789'
    for pin in itertools.combinations_with_replacement(numbers, 4):
        print(pin)
