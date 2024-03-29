def list_identifier(item: str):
    if item[0] == "[" and item[-1] == "]":
        return True


def dict_identifier(item: str):
    if item[0] == "{" and item[-1] == "}":
        return True


def string_identifier(item: str):
    if item[0] == "'" and item[-1] == "'":
        return True


def float_identifier(item: str):
    if (item[0] in [str(i) for i in range(10)] or item[0] == '-') and "." in item:
        return True


def integer_identifier(item: str):
    if item[0] in [str(i) for i in range(10)] or item[0] == '-' and not (float_identifier(item)):
        return True


def bool_identifier(item: str):
    if item in ["True", "False"]:
        return True
    

functions_lst = [bool_identifier, string_identifier, float_identifier,
                 integer_identifier, list_identifier, dict_identifier]


def item_type(item: str):
    for i in functions_lst:
        t = i(item)
        if t:
            t = str(i)
            return t[10: t.index("_"): ]



def result_item(item: str):
    t = item_type(item)
    if t == "bool":
        if item == "True":
            return True
        else:
            return False

    if t == "string":
        return item[1:-1:]   # returns None if item is a empty string
    
    if t == "float":
        return float(item)
    
    if t == "integer":
        return int(item)
    
    if t == "list":
        item = item.replace(" ", "")
        if len(item[1:-1]):
            result = item[1:-1].split(",")
            return [result_item(i) for i in result]
        return []
    
    if t == "dict":
        d = {}
        item = item[1:-1].replace(" ", "")
        if not(len(item)):
            return d
    
        item = item.split(",")
        for i in range(len(item)):
            item[i] = item[i].split(":")
            
            key , value = item[i]
            key , value = result_item(key) , result_item(value)

            d[key] = value

        return d

        
def solve_puzzles(puzzles):

    text = puzzles.read()
    items = text.split("\n")
    truthiness_lst = []
    for item in items:
        item = result_item(item)
        truthiness_lst.append(bool(item))
    return truthiness_lst


print(solve_puzzles(puzzles = open("puzzles.txt", "r")))





