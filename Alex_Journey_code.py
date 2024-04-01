import first_mission as first
import second_mission as second
# this module will execute exam_numbers function because we need its result that is based on user input
import third_mission as third


def list_catalyst(*args):
    result = []
    for lst in args:
        if not (isinstance(lst, list) or isinstance(lst, tuple)):
            lst = lst.split()

        for i in lst:
            if isinstance(i, tuple) or isinstance(i, list):
                result.extend(list_catalyst(i))
            else:
                result.append(str(i))
    return result


def unlock_vault(clues):
    result = ""
    vault = list_catalyst(*clues)
    for i in vault:
        result += i[0]
    return result


res1 = first.return_mission_1
res2 = second.return_second_mission
res3_1 = third.return_third_mission_1
res3_2 = third.return_third_mission_2
res3_3 = third.return_third_mission_3
results_list = [res1, res2, res3_1, res3_2, res3_3]

print("\n")  # to end line of input third_mission
code_of_alex_journey = unlock_vault(results_list)
print(code_of_alex_journey)
