#Животные делятся на спокойных и буйных. Буйные могут стоять только через одну клетку или больше.
#У животных есть рейтинг впечатлений. Найти такое расположение клеток, чтобы животные с максимальным рейтингом 
#стояли ближе к началу.
#Требуется для свого варианта второй части л.р. №6 написать объектно-ориентированную реализацию


from itertools import permutations
import random as r


class Zoopark:

    def __init__(self):
        self.cells = []
        self.output = ''
        self.personality = ['Буйный', 'Спокойный']
        self.permutation = []

        self.cells_permutations()

    def differences(self, x):
        flag = True

        for j in range(len(x) - 2):
            if (x[j][1] == x[j + 1][1] == 'Буйный') or (x[j + 1][1] == x[j + 2][1] == 'Буйный'):
                flag = False
                break

        if flag:
            self.permutation += [[*x]]

    def cells_permutations(self):
        try:
            k = int(input('\nВведите натуральное число K - кол-во животных в зоопарке: '))
            while k < 1:
                k = int(input('Введите число K > 0: '))

            print('\nЖивотные делятся на спокойных и буйных.\nБуйные могут стоять только через одну клетку или '
                  'больше.\nУ животных есть рейтинг впечатлений. Найти такое расположение клеток,\nчтобы животные стояли в '
                  'порядке убывания рейтинга впечатлений.')

            for i in range(1, k + 1):
                if [x[1] for x in self.cells].count('Буйный') < (k // 2):
                    self.cells.append([r.randint(10, 100), r.choice(self.personality), i])
                else:
                    self.cells.append([r.randint(10, 100), 'Спокойный', i])

            print('\nЖивотные в зоопарке | Рейтинг , Характер , Клетка |:')
            for i in self.cells:
                self.output = '{} | {}, {}, {}'.format(self.output, *i)
            print(f'{self.output[1::]} |')

            for i in permutations(self.cells, len(self.cells)):
                self.differences(i)

            if self.permutation:
                self.output = ''
                for h in max(self.permutation):
                    self.output = '{} | {}, {}, {}'.format(self.output, *h)
                print('\nСамое выгодное расположение клеток | Рейтинг | Характер | Клетка |:')
                print(f'{self.output[1::]} |')
            else:
                print('\nНет подходящих вариантов.')

            print('\nРабота программы завершена.')
        except ValueError:
            print('\nВы ввели символ, а не число, перезапустите программу и введите нужное число.')

Zoopark()
