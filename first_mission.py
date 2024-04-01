import keyword


def decrypt_clue(file):

    text = file.read()
    refrence = keyword.kwlist
    result = [(i, text.count(i)) for i in refrence if i in text]
    return result


return_mission_1 = decrypt_clue(open("mysterious.txt", "r"))

if __name__ == "__main__":
    print(return_mission_1)
