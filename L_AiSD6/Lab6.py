from itertools import permutations
import random as r


def differences(x):
    global permutation
    flag = True
    if len(permutation) == 500_000:
        d = int(input(f'\nКолличество возможных расположений достигло {len(permutation)}. '
                      f'Хотите дождаться вывода? ( Да = 1 | Нет = 0 ): '))
        while d != 0 and d != 1:
            d = int(input('Принимаются только значения "0" и "1": '))
        if d == 0:
            flag = False
    if len(x) < 3:
        flag = False
    for j in range(len(x) - 2):
        if (x[j][1] == x[j+1][1] == 'Буйный') or (x[j+1][1] == x[j+2][1] == 'Буйный'):
            flag = False
            break
    if flag:
        permutation += [[*x]]


y = ''
personality = ['Буйный', 'Спокойный']
permutation = []

try:
    a = int(input('Запустить обычную версию программы или усложнённую? ( Обычную = 0 | Усложнённую = 1 ): '))
    while a != 0 and a != 1:
        a = int(input('Принимаются только значения "0" и "1": '))

    k = int(input('\nВведите натуральное число K - кол-во животных в зоопарке: '))
    while k < 1:
        k = int(input('Введите число K > 0: '))

    cells = []

    # Первая часть задания
    if a == 0:
        h = 0
        cells = [x for x in range(1, k+1)]

        for i in permutations(cells, len(cells)):
            h += 1
            permutation += [[*i]]
            if h == 500_000:
                d = int(input(f'\nКолличество возможных расположений достигло {len(permutation)}. '
                              f'Хотите дождаться вывода? ( Да = 1 | Нет = 0 ): '))
                while d != 0 and d != 1:
                    d = int(input('Принимаются только значения "0" и "1": '))
                if d == 0:
                    print('\nРабота программы завершена.')
                    quit()

        if permutation:
            y = ''
            if len(permutation) <= 25:
                print('\nРасположения клеток:')
                for k in permutation:
                    print(*k)
            else:
                d = int(input(f'\nКолличество возможных расположений равно {len(permutation)}. '
                              f'Вывести их на экран? ( Да = 1 | Нет = 0 ): '))
                while d != 0 and d != 1:
                    a = int(input('Принимаются только значения "0" и "1": '))
                if d == 1:
                    print('\nРасположения клеток:')
                    for k in permutation:
                        print(*k)
        else:
            print('\nНет подходящих вариантов.')

    # Вторая часть задания
    else:
        print('\nЖивотные делятся на спокойных и буйных.\nБуйные могут стоять только через одну клетку или '
              'больше.\nУ животных есть рейтинг впечатлений. Найти такое расположение клеток,\nчтобы животные стояли в '
              'порядке убывания рейтинга впечатлений.')

        for i in range(1, k + 1):
            if [x[1] for x in cells].count('Буйный') < (k // 2):
                cells.append([r.randint(10, 100), r.choice(personality), i])
            else:
                cells.append([r.randint(10, 100), 'Спокойный', i])

        print('\nЖивотные в зоопарке | Рейтинг | Характер | Клетка |:')
        for i in cells:
            y = '{} | {}, {}, {}'.format(y, *i)
        print(f'{y[1::]} |')

        for i in permutations(cells, len(cells)):
            differences(i)

        if permutation:
            y = ''
            for h in max(permutation):
                y = '{} | {}, {}, {}'.format(y, *h)
            print('\nСамое выгодное расположение клеток | Рейтинг | Характер | Клетка |:')
            print(f'{y[1::]} |')
        else:
            print('\nНет подходящих вариантов.')

    print('\nРабота программы завершена.')
except ValueError:
    print('\nВы ввели символ, а не число, перезапустите программу и введите нужное число.')
