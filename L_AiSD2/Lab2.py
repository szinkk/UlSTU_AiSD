# Нечетные восьмиричные числа, не превышающие 409610, у которых вторая справа цифра равна 7.
# Выводит на экран цифры числа, исключая семерки.
# Вычисляется среднее число между минимальным и максимальным и выводится прописью.
import re
numbers = []
answer = []


def w(n):
    numeros = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять',
               '6': 'шесть', '7': 'семь', '8': 'восемь', '9': 'девять'}
    return numeros.get(n)


with open('test.txt', 'r') as f:
    buff = f.read()
    lines = buff.split()
    if not buff:
        print('Файл пуст')
        quit()
    for i in lines:
        if re.fullmatch(r'[1234567]{0,1}[01234567]{0,1}7[1357]', i):
            numbers.append(int(i))
            answer.append(i.replace('7', ''))
    if not numbers:
        print('Нет подходящих цифр')
        quit()
    else:
        print('Цифры чисел без 7:', *answer)
        answer = ''
        for i in str((max(numbers) + min(numbers)) // 2):
            answer += w(i) + ' '
        print('Среднее:', (max(numbers) + min(numbers)) // 2, answer)