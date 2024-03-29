import random
import datetime


def binary(decimal):
    i = 0
    q = 0
    result = 0
    while decimal>=2:
        result += 10**i * (decimal%2)
        q = decimal // 2
        decimal //= 2
        i += 1
    result += q*10**i
    return result

def calculate_magic_numbers(start, end):
    result = [random.randint(start, end) for i in range(10)]
    return result
# print(calculate_magic_numbers(1, 100))


def exam_numbers():
    decimal = random.randint(0, 15)
    print(decimal)
    result = binary(decimal) 
    return result

print(exam_numbers())