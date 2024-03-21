import keyword


def decrypt_clue(text):
    refrence = keyword.kwlist
    result = [i for i in refrence if i in text]
    return result

file = open("mysterious.txt", "r")
text = file.read()
print(decrypt_clue(text))