import random
import time
import string


def binary(decimal):
    deci = decimal
    i = 0
    q = 0
    result = 0
    while deci >= 2 or decimal == 1:
        result += 10**i * (deci % 2)
        q = deci // 2
        deci //= 2
        i += 1
        decimal = 0
    result += q*10**i
    return result


def calculate_magic_numbers(start, end):
    result = [random.randint(start, end) for i in range(10)]
    return result
# print(calculate_magic_numbers(1, 100))


def exam_numbers():
    corrects = 0
    mistakes = 0
    start = time.time()
    while time.time() - start < 20:
        decimal = random.randint(0, 15)
        result = binary(decimal)
        userInput = ""
        try:
            userInput = int(input(f"{decimal} in binary is : "))
        except:
            pass
        if result == userInput:
            corrects += 1
        else:
            mistakes += 1
    return f"{corrects} corrects \n{mistakes} wrongs"


# print(exam_numbers())

def check_pass(users_list):
    result = []
    for i in users_list:
        if (
            list(filter(lambda x: x.isupper(), i[1])) and
            list(filter(lambda x: x.islower(), i[1])) and
            list(filter(lambda x: x in string.punctuation, i[1])) and 
            len(i[1])>8 
            ):
            result.append(i[0])
    return result

# lst = [("a" , "Ali12*2333") , ('b', 'Aswer&&&') , ('c', "hassan#2@"), ('re',"HAAAAA!@#"), ('e' , "Asgh@")]
# check = check_pass(lst)
# print(check)
            