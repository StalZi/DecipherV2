alphabetRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetEN = "abcdefghijklmnopqrstuvwxyz"

def atbashALL(value:str) -> str:
    result: str = ""

    for i in range(len(value)):

            if value[i] in alphabetRU:
                result += alphabetRU[len(alphabetRU) - alphabetRU.find(value[i]) - 1]

            elif value[i] in alphabetRU.upper():
                result += alphabetRU.upper()[len(alphabetRU) - alphabetRU.upper().find(value[i]) - 1]

            elif value[i] in alphabetEN:
                result += alphabetEN[len(alphabetEN) - alphabetEN.find(value[i]) - 1]

            elif value[i] in alphabetEN.upper():
                result += alphabetEN.upper()[len(alphabetEN) - alphabetEN.upper().find(value[i]) - 1]

            else:
                result += value[i]

    return result

def atbashRU(value:str) -> str:
    result: str = ""

    for i in range(len(value)):

            if value[i] in alphabetRU:
                result += alphabetRU[len(alphabetRU) - alphabetRU.find(value[i]) - 1]

            elif value[i] in alphabetRU.upper():
                result += alphabetRU.upper()[len(alphabetRU) - alphabetRU.upper().find(value[i]) - 1]

            else:
                result += value[i]

    return result

def atbashEN(value:str) -> str:
    result: str = ""

    for i in range(len(value)):

            if value[i] in alphabetEN:
                result += alphabetEN[len(alphabetEN) - alphabetEN.find(value[i]) - 1]

            elif value[i] in alphabetEN.upper():
                result += alphabetEN.upper()[len(alphabetEN) - alphabetEN.upper().find(value[i]) - 1]

            else:
                result += value[i]

    return result

def atbash_dec(locale:dict, language:str, value:str) -> str:

    if language == locale['language_dropdown']['all_languages']:

        return atbashALL(value)

    elif language == locale['language_dropdown']['english']:

        return atbashEN(value)
    
    elif language == locale['language_dropdown']['russian']:

        return atbashRU(value)


    return 'JSON failure'