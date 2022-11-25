"""
Задание 4.

Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""

WORD_LIST = ['разработка', 'администрирование', 'protocol', 'standard']

encode_list = []
for word in WORD_LIST:
    encode_word = word.encode('utf-8')
    encode_list.append(encode_word)

print(encode_list)
print('*' * 50)

decode_list = []
for word in encode_list:
    decode_word = word.decode('utf-8')
    decode_list.append(decode_word)

print(decode_list)
