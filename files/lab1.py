sorted_alphabet = []
sorted_frequencies = []
key = {'8': '', 'И': '', '2': ' ', 'Х': '', '>': '', 'Ф': '', '0': '', '1': 'О', 'c': 'Ъ', '.': '', ' ': '', 't': 'Э',
       'Ы': '', 'О': '', 'А': '', ',': '', 'К': 'О', 'Е': '', 'Б': '', '<': '', 'a': '', 'М': '', '?': '', '9': '',
       'b': '', 'Л': '', 'Д': '', 'r': '', '3': '', 'Я': ' ', '-': '', 'Ч': '', 'Ь': ''}


def find_alphabet():
    ALPHABET2 = set()
    with open('files/cod1.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        for el in data:
            ALPHABET2.add(el)
    ALPHABET2 = list(ALPHABET2)
    return ''.join(ALPHABET2)


def encrypt():
    ALPHABET2 = '8И2Х>Ф01c. tЫОА,КЕБ<aМ?9bЛДr3Я-ЧЬ'
    ALPHABET_MAP2 = set(ALPHABET2)
    FREQUENCIES2 = {ch: 0 for j, ch in enumerate(ALPHABET2)}

    with open('files/cod1.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        len_data = len(data)
        for el in data:
            if el in ALPHABET_MAP2:
                FREQUENCIES2[f'{el}'] += 1

        # for i in range(len(ALPHABET2)):
        #     FREQUENCIES2[f'{ALPHABET2[i]}'] = round(FREQUENCIES2[f'{ALPHABET2[i]}'] / len_data, 6)

        pairs = [[k, v] for (k, v) in FREQUENCIES2.items()]
        for i in range(len(pairs)):
            print(pairs[i][0], pairs[i][1])


encrypt()
