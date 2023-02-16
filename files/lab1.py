
ALPHABET2 = []

with open('files/cod1.txt', 'r', encoding='utf-8') as f:
    data = f.read()
    len_data = len(data)
    for el in data:
        ALPHABET2.append(el)
ALPHABET2 = list(set(ALPHABET2))
print(''.join(ALPHABET2))

