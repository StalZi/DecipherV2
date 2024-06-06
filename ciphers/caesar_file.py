alphabetRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetEN = "abcdefghijklmnopqrstuvwxyz"

def caesarALL(value:str, rot:int) -> str:

    result = ""

    for i in range(len(value)):
            
            if value[i] in alphabetRU:
                try:
                    result += alphabetRU[alphabetRU.find(value[i]) + rot]
                except IndexError:
                    result += alphabetRU[alphabetRU.find(value[i]) + rot - len(alphabetRU)]

            elif value[i] in alphabetRU.upper():
                try:
                    result += alphabetRU.upper()[alphabetRU.upper().find(value[i]) + rot]
                except IndexError:
                    result += alphabetRU.upper()[alphabetRU.upper().find(value[i]) + rot - len(alphabetRU)]

            elif value[i] in alphabetEN:
                try:
                    result += alphabetEN[alphabetEN.find(value[i]) + rot]
                except IndexError:
                    try:
                        result += alphabetEN[alphabetEN.find(value[i]) + rot - len(alphabetEN)]
                    except IndexError:
                            break

            elif value[i] in alphabetEN.upper():
                while True:
                    try:
                        result += alphabetEN.upper()[alphabetEN.upper().find(value[i]) + rot]
                    except IndexError:
                        try:
                            result += alphabetEN.upper()[alphabetEN.upper().find(value[i]) + rot - len(alphabetEN)]
                        except IndexError:
                            break

            else:
                result += value[i]

    return result


def caesarRU(value:str, rot:int) -> str:

    result = ""

    for i in range(len(value)):

        if value[i] in alphabetRU:
            try:
                result += alphabetRU[alphabetRU.find(value[i]) + rot]
            except IndexError:
                result += alphabetRU[alphabetRU.find(value[i]) + rot - len(alphabetRU)]

        elif value[i] in alphabetRU.upper():
            try:
                result += alphabetRU.upper()[alphabetRU.upper().find(value[i]) + rot]
            except IndexError:
                result += alphabetRU.upper()[alphabetRU.upper().find(value[i]) + rot - len(alphabetRU)]

        else:
            result += value[i]

    return result


def caesarEN(value:str, rot:int) -> str:

    result = ""

    for i in range(len(value)):

        if value[i] in alphabetEN:
            try:
                result += alphabetEN[alphabetEN.find(value[i]) + rot]
            except IndexError:
                result += alphabetEN[alphabetEN.find(value[i]) + rot - len(alphabetEN)]

        elif value[i] in alphabetEN.upper():
            try:
                result += alphabetEN.upper()[alphabetEN.upper().find(value[i]) + rot]
            except IndexError:
                result += alphabetEN.upper()[alphabetEN.upper().find(value[i]) + rot - len(alphabetEN)]

        else:
            result += value[i]

    return result


def caesar_dec(locale, language:str, value:str, rot:str) -> str | list[str]:

    if language == locale['language_dropdown']['all_languages']:

        if rot == locale['rot_dropdown']['rot_all']:
            resultall = []
            for i in range(1, 33):

                resultall.append(caesarALL(value, i))
            print(resultall)
            return resultall

        else:

            return caesarALL(value, int(rot))

    elif language == locale['language_dropdown']['russian']:

        if rot == locale['rot_dropdown']['rot_all']:
            resultall = []
            for i in range(1, len(alphabetRU)):

                resultall.append(caesarRU(value, i))

            return resultall

        else:

            return caesarRU(value, int(rot))


    elif language == locale['language_dropdown']['english']:

        if rot == locale['rot_dropdown']['rot_all']:
            resultall = []
            for i in range(1, len(alphabetEN)):

                resultall.append(caesarEN(value, i))

            return resultall

        else:

            return caesarEN(value, int(rot))
        
    return 'JSON failure'