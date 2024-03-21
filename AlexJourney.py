import keyword


def decrypt_clue(text: str):
    refrence = keyword.kwlist
    result = [(i, text.count(i)) for i in refrence if i in text]
    return result

file = open("mysterious.txt", "r")
text = file.read()
print(decrypt_clue(text))