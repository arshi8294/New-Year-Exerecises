import threading
import random
import time
import string


def calculate_magic_numbers(start, end):
    result = [random.randint(start, end) for i in range(random.randint(1, 10))]
    return result


# ----------------------------------------------------------------------------------------------

def timer(secs: int = 20):
    for i in range(secs):
        time.sleep(1)
    return "\nnumber of correct answers: {} \nnumber of wrong answers: {}".format(corrects, mistakes)


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


def exam_numbers():

    # corrects and mistakes are globalized to be used in timer function to show result of exam numbers
    # because this function's thread will be terminated after executing main function
    global corrects
    corrects = 0
    global mistakes
    mistakes = 0

    while True:
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


# ----------------------------------------------------------------------

def check_pass(users_list):
    result = []
    for i in users_list:
        if (
            list(filter(lambda x: x.isupper(), i[1])) and
            list(filter(lambda x: x.islower(), i[1])) and
            list(filter(lambda x: x in string.punctuation, i[1])) and
            len(i[1]) > 8
        ):
            result.append(i[0])
    return result

# -----------------------------------------------------------------------------------------------


print(calculate_magic_numbers(1, 100))


threading.Thread(target=exam_numbers, daemon=True).start()
print(timer())

lst = [("ali", "Ali12*2333"), ('babak', 'Aswer&&&'), ('cyrus', "hassan#2@"),
       ('reza', "HAAAAA!@#"), ('dariush', "Asgh@"), ("farsad", "Hsn23@far")]
check = check_pass(lst)
print(check)
