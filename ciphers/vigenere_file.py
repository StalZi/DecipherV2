from string import whitespace

alphabetRU = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
alphabetEN = "abcdefghijklmnopqrstuvwxyz"

l2iRU: dict = dict(zip(alphabetRU, range(len(alphabetRU))))
l2iEN: dict = dict(zip(alphabetEN, range(len(alphabetEN))))

i2lRU: dict = dict(zip(range(len(alphabetRU)), alphabetRU))
i2lEN: dict = dict(zip(range(len(alphabetEN)), alphabetEN))


def vigenereRU(split_encrypted, key) -> str:
    decrypted: str = ""

    for each_split in split_encrypted:

            i = 0

            for letter in each_split:

                number = (l2iRU[letter] - l2iRU[key[i]]) % len(alphabetRU)
                decrypted += i2lRU[number]

                i += 1

    return decrypted

def vigenereEN(split_encrypted, key) -> str:
    decrypted: str = ""

    for each_split in split_encrypted:

            i = 0

            for letter in each_split:

                number = (l2iEN[letter] - l2iEN[key[i]]) % len(alphabetEN)
                decrypted += i2lEN[number]

                i += 1

    return decrypted

def vigenere_dec(locale:dict, language:str, value:str, key:str) -> str:

    value = value.lower()

    whitespace_indices: list = []
    i = 0
    for index, character in enumerate(value):
        if character in whitespace:
            whitespace_indices.append(index - i)
            i += 1

    value = ''.join(value.split())

    split_encrypted: list = [value[i : i + len(key)] for i in range(0, len(value), len(key))]

    if language == locale['language_dropdown']['english']:
        d = vigenereEN(split_encrypted, key)

    elif language == locale['language_dropdown']['russian']:
        d = vigenereRU(split_encrypted, key)
    
    else:
        return 'JSON failure'

    d = list(d)
    for index, i in enumerate(whitespace_indices):
        d.insert(index + i, " ")
    d = ''.join(d)

    return d