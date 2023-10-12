ALPHABET_ENG:str = "abcdefghijklmnopqrstuvwxyz"
ALPHABET_RU:str = "абвгдеёжзийклмнопрстуфхцчшщъыьэюя" 


def language(text:str) -> str:
    if text[0].lower() in ALPHABET_ENG:
        return ALPHABET_ENG
    else:
        return ALPHABET_RU 


def register(literal:str, alphabet:str):
    if literal.islower():
        return alphabet
    elif literal.isupper():
        return alphabet.upper()
    else:
        return ''


def ceaser_cipher(text:str, literal_key:str):
    result = []
    dictionary:str = ""
    alphabet:str = language(text)
    key:int = 0

    if literal_key.isdigit():
        key = int(literal_key)
    else:
        key = alphabet.index(literal_key.lower()) + 1

    for i in range(len(text)):
      
        dictionary = register(text[i], alphabet)

        if dictionary == "":
            result.append(text[i])

        if text[i] in dictionary:
            for j in range(len(dictionary)):
             
                if 0 <= j + key < len(dictionary) and text[i] == dictionary[j]:
                    result.append(dictionary[j + key])
                elif j + key >= len(dictionary) and text[i] == dictionary[j]:
                    residue = len(dictionary) - j
                    result.append(dictionary[key - residue])

    return ''.join(result)


def ceaser_decrypt(text:str):
    dictionary:str = ""
    alphabet:str = language(text)
    
    result:str = ""
    for i in range(len(alphabet)):
        string:str = ""
        for j in range(len(text)):

            dictionary = register(text[j], alphabet)

            if dictionary == "":
                string += text[j]

            index = dictionary.index(text[j])
            string += dictionary[index - i]
        result += string + '\n'

    return result