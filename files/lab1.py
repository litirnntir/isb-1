def find_alphabet():
    ALPHABET2 = set()
    with open('files/cod1.txt', 'r', encoding='utf-8') as f:
        data = f.read()
        len_data = len(data)
        for el in data:
            ALPHABET2.add(el)
            # FREQUENCIES[f'{el.upper()}'] += 1
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
            if el.upper() in ALPHABET_MAP2:
                FREQUENCIES2[f'{el.upper()}'] += 1

        for i in range(len(ALPHABET2)):
            FREQUENCIES2[f'{ALPHABET2[i]}'] = round(FREQUENCIES2[f'{ALPHABET2[i]}'] / len_data, 4)

        sorted_freq_alph = dict(sorted(FREQUENCIES2.items(), key=lambda item: item[1]))
        sorted_alphabet = list(sorted_freq_alph)
        sorted_frequencies = list({v: k for k, v in sorted_freq_alph.items()})

        for i in range(0, len(list(sorted_frequencies))):
            print(sorted_frequencies[i], sorted_alphabet[i])


encrypt()
