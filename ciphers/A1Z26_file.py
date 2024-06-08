alphabetRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetEN = "abcdefghijklmnopqrstuvwxyz"

def a1z26RU(value:list[str], x2:int) -> str:
    result: str = ""

    if x2:
        function_eval: str = 'alphabetRU[(int(splitted[j]) // 2) - 1]'
    else:
        function_eval: str = 'alphabetRU[int(splitted[j]) - 1]'

    for i in value:
        splitted = i.split("-")

        for j in range(len(splitted)):
            try:
                result += eval(function_eval)
            except ValueError:
                result += splitted[j]

        result += ' '

    return result

def a1z26EN(value:list[str], x2:int) -> str:
    result: str = ""

    if x2:
        function_eval: str = 'alphabetEN[(int(splitted[j]) // 2) - 1]'
    else:
        function_eval: str = 'alphabetEN[int(splitted[j]) - 1]'

    for i in value:
        splitted = i.split('-')
        print('split 2', splitted)

        for j in range(len(splitted)):
            try:
                result += eval(function_eval)
            except ValueError:
                result += splitted[j]

        result += ' '

    return result


def a1z26_dec(locale:dict, language:str, value:str, x2:int) -> str | list[str]:

    split_value: list[str] = value.rstrip().split(' ')

    print('split 1', split_value)

    if language == locale['language_dropdown']['all_languages']:
        try:
            return [f"{locale['language_dropdown']['english']} {a1z26EN(split_value, x2).rstrip()}", f"{locale['language_dropdown']['russian']} {a1z26RU(split_value, x2).rstrip()}"]
        except:
            return a1z26RU(split_value, x2).rstrip()

    elif language == locale['language_dropdown']['english']:
        return a1z26EN(split_value, x2).rstrip()
    
    elif language == locale['language_dropdown']['russian']:
        return a1z26RU(split_value, x2).rstrip()

    return 'JSON failure'