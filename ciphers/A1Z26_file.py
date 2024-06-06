alphabetRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetEN = "abcdefghijklmnopqrstuvwxyz"

def a1z26RU(value:list[str], x2) -> str:
    result:str = ""

    for i in range(len(value)):
        
        splitted = value[i].split("-")

        if x2 is False:
            for j in range(len(splitted)):
            
                result += alphabetRU[int(splitted[j]) - 1]
        else:
            for j in range(len(splitted)):
            
               result += alphabetRU[(int(splitted[j]) // 2) - 1]

    return result

def a1z26EN(value:list[str], x2) -> str:
    result:str = ""

    for i in range(len(value)):

        splitted = value[i].split("-")

        if x2 is False:
            for j in range(len(splitted)):
            
                result += alphabetEN[int(splitted[j]) - 1]
        else:
            for j in range(len(splitted)):
            
               result += alphabetEN[(int(splitted[j]) // 2) - 1]

    return result


def a1z26_dec(language:str, value:str, x2:bool = False) -> str | list[str] | None:

    split_value: list[str] = value.split(" ")

    if language == "Все, что ниже":
        try:
            return [a1z26EN(split_value, x2), a1z26RU(split_value, x2)]
        except:
            return a1z26RU(split_value, x2)

    elif language == "Русский":

        return a1z26RU(split_value, x2)


    elif language == "English":

        return a1z26EN(split_value, x2)