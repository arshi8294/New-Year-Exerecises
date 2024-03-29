import random


def calculate_magic_numbers(start, end):
    result = [random.randint(start, end) for i in range(10)]
    return result


print(calculate_magic_numbers(1, 100))