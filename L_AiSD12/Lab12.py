import random
import numpy as np
from decimal import Decimal, getcontext


# Функция вычисляющая сумму знакопеременного ряда
def calculations(matrix, accuracy):
    # Задаем переменные для вычислений
    n = 1
    sum_series = 0
    fact = 1
    sign = random.choice([1, -1])
    curr_matrix = matrix

    while True:
        # Вычисление текущего члена ряда и сложение с предыдущими членами
        curr_term = Decimal(np.linalg.det(curr_matrix) / fact)
        sum_series += sign * curr_term

        # Проверка точности вычислений
        if abs(curr_term) < 1 / (10 ** accuracy):
            break

        # Считаем переменные для следующей итерации цикла
        n += 1
        sign = -sign
        fact *= n
        curr_matrix *= curr_matrix

    return sum_series  # возвращаем сумму ряда


try:
    # Считываем значение точности вычислений
    t = int(input("Введите число t > 0\nt - количество знаков после запятой\n"))
    while t > 323 and t < 1:
        t = int(input("Вы ввели некорректное значение t\n"))

    # Создаем матрицу со значениями от -1 до 1 и случайно созданным рангом k
    k = random.randint(2, 10)
    x = np.round(np.random.uniform(-1, 1, (k, k)), 3)

    # Выводим матрицу
    print(f"\nМатрица:\n{x}")

    # Считываем значение точности t для Decimal
    getcontext().prec = t + 100

    # Вызываем функцию вычисления ряда
    output = calculations(x, t)

    # Выводим сумму ряда с заданной точностью
    print(f"Сумма ряда с точностью до {t} знаков после запятой: {output:.{t}f}")

except ValueError:
    print("\nВы ввели символ, а не число, перезапустите программу и введите корректное значение")

