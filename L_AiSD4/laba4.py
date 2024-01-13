""" С клавиатуры вводятся два числа K и N. Квадратная матрица А(N,N), состоящая из 4-х равных по размерам подматриц,
B, C, D, E заполняется случайным образом целыми числами в интервале [-10,10]. Для тестирования использовать не случайное
заполнение, а целенаправленное.
Вид матрицы А:
D	Е
С	В
Для простоты все индексы в подматрицах относительные.
По сформированной матрице F (или ее частям) необходимо вывести не менее 3-х разных графиков.
Программа должна использовать функции библиотек numpy  и mathplotlib
Вариант 8:
Формируется матрица "F" следующим образом: скопировать в нее "А" и если в "С" количество простых чисел в
нечетных столбцах больше, чем количество нулевых элементов в четных строках, то поменять местами "Е" и "С" симметрично,
иначе "С" и "В" поменять местами несимметрично. При этом матрица "А" не меняется. После чего если определитель
матрицы "А" больше суммы диагональных элементов матрицы "F", то вычисляется выражение: A^-1 * A^T – K * F,
иначе вычисляется выражение (A^Т + G^-1 - F^-1) * K, где "G" - нижняя треугольная матрица, полученная из "А".
Выводятся по мере формирования "А", F и все матричные операции последовательно. """

import numpy as np
from matplotlib import pyplot as plt


def simple(a):
    if a < 0:
        a *= -1
    k = 0
    for i in range(2, a // 2 + 1):
        if a % i == 0:
            k += 1
    if k <= 0:
        return True
    else:
        return False


try:
    n = int(input('Введите число N > 4, являющееся размерностью матрицы "A": '))
    k = int(input('Введите число K, являющееся коэффициентом умножения: '))
    while n < 5:
        n = int(input('Введите число N > 4: '))

    simple_cnt = zero_cnt = sum_det_F = 0
    middle_n = n // 2 + n % 2  # Середина матрицы
    A = np.random.randint(-10.0, 10.0, (n, n))
    AT = np.transpose(A)  # Транспонированная матрица А
    det_A = np.linalg.det(A)  # Определитель матрицы А
    F = A.copy()  # Задаём матрицу F
    G = np.tri(n) * A  # Матрица G

    print('\nМатрица А:')
    print(A)
    print('\nТранспонированная А:')
    print(AT)

    # Выделяем матрицы E C B
    if n % 2 == 1:
        E = [A[i][middle_n - 1:n] for i in range(middle_n)]
        C = [A[i][0:middle_n] for i in range(middle_n - 1, n)]
        B = [A[i][middle_n - 1:n] for i in range(middle_n - 1, n)]
    else:
        E = [A[i][middle_n:n] for i in range(0, middle_n)]
        C = [A[i][0:middle_n] for i in range(middle_n, n)]
        B = [A[i][middle_n:n] for i in range(middle_n, n)]

    for i in range(middle_n):
        for j in range(middle_n):
            if (j + 1) % 2 == 1:  # Считаем кол-во простых чисел в нечётных столбцах
                if simple(int(C[i][j])):
                    simple_cnt += 1
            if (i + 1) % 2 == 0:  # Считаем кол-во нулевых элементов в чётных строках
                if C[i][j] == 0:
                    zero_cnt += 1

    if simple_cnt > zero_cnt:
        print(f'\nВ матрице "С" кол-во простых чисел в нечётных столбцах({simple_cnt})')
        print(f'больше чем кол-во нулевых элементов в чётных строках({zero_cnt})')
        print('поэтому симметрично местами подматрицы "E" и "C":')
        E, C = C, E
        for i in range(middle_n):
            C[i] = C[i][::-1]  # Симметрично меняем значения в C
            E[i] = E[i][::-1]  # Симметрично меняем значения в E
        if n % 2 == 1:
            for i in range(middle_n - 1, n):  # Перезаписываем С
                for j in range(middle_n):
                    F[i][j] = C[i - (middle_n - 1)][j]
            for i in range(middle_n):  # Перезаписываем Е
                for j in range(middle_n - 1, n):
                    F[i][j] = E[i][j - (middle_n - 1)]
        else:
            for i in range(middle_n, n):
                for j in range(middle_n):
                    F[i][j] = C[i - middle_n][j]
            for i in range(0, middle_n):
                for j in range(middle_n, n):
                    F[i][j] = E[i][j - middle_n]
    else:
        print(f'\nВ матрице "C" кол-во простых чисел в нечётных столбцах({simple_cnt})')
        print(f'меньше кол-во нулевых элементов в чётных строках({zero_cnt}) или равно ей')
        print('поэтому несимметрично меняем местами подматрицы "C" и "B":')
        C, B = B, C
        if n % 2 == 1:
            for i in range(middle_n - 1, n):  # Перезаписываем B
                for j in range(middle_n - 1, n):
                    F[i][j] = B[i - (middle_n - 1)][j - (middle_n - 1)]
            for i in range(middle_n - 1, n):  # Перезаписываем С
                for j in range(middle_n):
                    F[i][j] = C[i - (middle_n - 1)][j]
        else:
            for i in range(middle_n, n):
                for j in range(middle_n, n):
                    F[i][j] = B[i - middle_n][j - middle_n]  # Перезаписываем B
            for i in range(middle_n, n):
                for j in range(middle_n):
                    F[i][j] = C[i - middle_n][j]  # Перезаписываем С

    print('\nМатрица "F":')
    print(F)
    # Сумма диагональных элементов матрицы F
    for i in range(n):
        for j in range(n):
            if i == j:
                sum_det_F += F[i][j]
            if (i + j + 1) == n and ((i == j) != ((i + j + 1) == n)):
                sum_det_F += F[i][j]
    # A^-1 * A^T – K * F
    if det_A > sum_det_F:
        print(f'\nОпределитель матрицы "А"({int(det_A)})')
        print(f'больше суммы диагональных элементов матрицы "F"({int(sum_det_F)})')
        print('поэтому вычисляем выражение: A^-1 * A^T – K * F:')

        try:
            A_obr = np.linalg.inv(A)  # Обратная матрица A
            A_obrAT = A_obr * AT  # A^-1 * A^T
            KF = k * F
            result = A_obrAT - KF  # A^-1 * A^T – K * F

            print('\nРезультат K * F:')
            print(KF)
            print('\nОбратная матрица A:')
            print(A_obr)
            print("\nРезультат A^-1 * A^T:")
            print(A_obrAT)
            print('\nРезультат A^-1 * A^T – K * F:')
            print(result)
        except np.linalg.LinAlgError:
            print("Одна из матриц является вырожденной (определитель равен 0),"
                  " поэтому обратную матрицу найти невозможно.")
    # (A^Т + G^-1 - F^-1) * K
    else:
        print(f'\nОпределитель матрицы А({int(det_A)})')
        print(f'меньше суммы диагональных элементов матрицы F({int(sum_det_F)}) или равен ей')
        print('поэтому вычисляем выражение (A^Т + G^-1 - F^-1) * K:')

        for i in range(n):
            for j in range(n):
                if i >= j and (i + j + 1) >= n:
                    G[i][j] = A[i][j]

        try:
            F_obr = np.linalg.inv(F)  # Обратная матрица F
            G_obr = np.linalg.inv(G)  # Обратная матрица G
        except np.linalg.LinAlgError:
            print("Одна из матриц является вырожденной (определитель равен 0),"
                  " поэтому обратную матрицу найти невозможно. Перезапустите программу.")
            quit()

        ATG_obr = AT + G_obr  # AТ + G^-1
        ATG_obrF_obr = ATG_obr - F_obr  # A^Т + G^-1 - F^-1
        result = ATG_obrF_obr * k  # (A^Т + G^-1 - F^-1) * K

        print('\nОбратная матрица F:')
        print(F_obr)
        print('\nМатрица G:')
        print(G)
        print('\nОбратная матрица G:')
        print(G_obr)
        print('\nРезультат AТ + G^-1:')
        print(ATG_obr)
        print('\nРезультат A^Т + G^-1 - F^-1:')
        print(ATG_obrF_obr)
        print('\nРезультат (A^Т + G^-1 - F^-1) * K:')
        print(result)

    av = [np.mean(abs(F[i, ::])) for i in range(n)]
    av = int(sum(av))  # сумма средних значений строк (используется при создании третьего графика)
    fig, axs = plt.subplots(2, 2, figsize=(16, 9))
    x = list(range(1, n + 1))
    for j in range(n):
        y = list(F[j, ::])
        # обычный график
        axs[0, 0].plot(x, y, ',-', label=f"{j + 1} строка.")
        axs[0, 0].set(title="График с использованием функции plot:", xlabel='Номер элемента в строке',
                      ylabel='Значение элемента')
        axs[0, 0].grid()
        # гистограмма
        axs[0, 1].bar(x, y, 0.4, label=f"{j + 1} строка.")
        axs[0, 1].set(title="График с использованием функции bar:", xlabel='Номер элемента в строке',
                      ylabel='Значение элемента')
        if n <= 10:
            axs[0, 1].legend(loc='lower right')
            axs[0, 1].legend(loc='lower right')
    # Круговой график
    sizes = [round(np.mean(abs(F[i, ::])) * 100 / av, 1) for i in range(n)]
    axs[1, 0].set_title("График с использованием функции pie:")
    axs[1, 0].pie(sizes, labels=list(range(1, n + 1)), autopct='%1.1f%%', shadow=True)

    # Тепловая карта
    def heatmap(data, ax, cbar_kw=None, **kwargs):  # аннотированная тепловая карта
        if cbar_kw is None:
            cbar_kw = {}
        im = ax.imshow(data, **kwargs)
        cbar = ax.figure.colorbar(im, ax=ax, **cbar_kw)
        ax.set_xticks(np.arange(data.shape[1]))
        ax.set_yticks(np.arange(data.shape[0]))
        return im, cbar


    def annotate_heatmap(im, data=None, textcolors=("black", "white"), threshold=0):
        if not isinstance(data, (list, np.ndarray)):
            data = im.get_array()
        kw = dict(horizontalalignment="center", verticalalignment="center")
        texts = []
        for i in range(data.shape[0]):
            for j in range(data.shape[1]):
                kw.update(color=textcolors[int(data[i, j] > threshold)])
                text = im.axes.text(j, i, data[i, j], **kw)
                texts.append(text)
        return texts


    im, cbar = heatmap(F, ax=axs[1, 1], cmap="magma_r")
    texts = annotate_heatmap(im)
    axs[1, 1].set(title="Создание аннотированных тепловых карт:", xlabel="Номер столбца", ylabel="Номер строки")
    plt.suptitle("Использование библиотеки matplotlib")
    plt.tight_layout()
    plt.show()

    print('\nРабота программы завершена.')
except ValueError:  # ошибка на случай введения не числа в качестве порядка или коэффициента
    print('\nВведенный символ не является числом. Перезапустите программу и введите число.')