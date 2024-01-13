# Нечетные восьмиричные числа, не превышающие 409610, у которых вторая справа цифра равна 7.
# Выводит на экран цифры числа, исключая семерки.
# Вычисляется среднее число между минимальным и максимальным и выводится прописью.

buff_len = 1
work_buff = ''
numbers = []


# перевод цифр пропись
def w(n):
    numeros = {0: 'ноль', 1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
         6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'}
    return numeros.get(n)


with open('test.txt', 'r') as f:
    buff = f.read(buff_len)
    if not buff:
        print('Файл пуст')
    while buff: # чтение файла поблочно
        while '0' <= buff <= '9':
            if '0' <= buff <= '9':
                work_buff += buff
            buff = f.read(buff_len) # читаем блок
        if len(work_buff) > 0:  # проверска подходит ли число под условие
            try:
                if int(work_buff) % 2 != 0:
                    if int(work_buff, 8) < 4096:
                        answer = ''
                        try:
                            if work_buff[-2] == '7':
                                numbers.append(int(work_buff))
                        except IndexError:
                            work_buff = ''
                            buff = f.read(buff_len)
            except ValueError:
                work_buff = ''
                buff = f.read(buff_len) # читаем следующий блок
        work_buff = ''
        buff = f.read(buff_len) # читаем следующий блок
    if not numbers:
        print('Нет подходящих цифр')
    else:
        print(numbers) # вывод подходящих чисел
        answers = []
        for i in numbers:
            answer = ''
            for j in str(i):
                if j != '7':
                    answer += j
            answers.append(answer)
        print('Цифры чисел без 7:', *answers)
        answer = ''
        for i in str((max(numbers) + min(numbers)) // 2):
            answer += w(int(i)) + ' '
        print('Среднее:', (max(numbers) + min(numbers)) // 2, answer)
