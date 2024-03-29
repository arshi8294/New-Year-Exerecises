import keyword


def decrypt_clue(file):

    text = file.read()
    refrence = keyword.kwlist
    result = [(i, text.count(i)) for i in refrence if i in text]
    return result

print(decrypt_clue(file = open("mysterious.txt", "r")))