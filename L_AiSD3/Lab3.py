import random


def printm(mat):
    for row in mat:
        for elem in row:
            print('{:5}'.format(elem), end=' ')
        print()


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


def paste(matF, matrix, column_index, row_index):
    a = column_index
    for row in matrix:
        for element in row:
            matF[row_index][column_index] = element
            column_index += 1
        row_index += 1
        column_index = a


def zero(size):
    return [[0 for _ in range(size)] for _ in range(size)]


def inputm(mat, i1, i2, j1, j2):
    zero_mat = zero(len(mat) // 2)
    for i in range(i1, i2):
        for j in range(j1, j2):
            zero_mat[i - i1][j - j1] = mat[i][j]
    return zero_mat


K = int(input('Введите число K: '))
n = int(input('Введите число число N, больше или равное 5: '))

if n > 5:
    pass
else:
    print('Введен неправильное N, попробуйте еще')
    while n < 5:
        n = int(input('Введите число число N, больше или равное 5: '))

answer = input(
    'Для использование единичной матрицы напишите 1, для использования случайно сгенерированной напишите 2: ')
if answer not in ['1', '2']:
    print('Попробуйте ещё')
    while answer not in ['1', '2']:
        n = int(input(
            'Для использование единичной матрицы напишите 1, для использования случайно сгенерированной напишите 2: '))
if answer == '1':
    A = [[(1) for i in range(n)] for j in range(n)]
elif answer == '2':
    A = [[random.randint(-10, 10) for i in range(n)] for j in range(n)]

print('Матрица А:')
printm(A)

half_n = n // 2
fix_n = half_n
if n % 2 != 0:
    fix_n += 1

E = inputm(A, 0, half_n, fix_n, n)
B = inputm(A, fix_n, n, fix_n, n)
C = inputm(A, fix_n, n, 0, half_n)
D = inputm(A, 0, half_n, 0, half_n)

print('Подматрицы матрицы A:')
print('Подматрица D')
printm(D)
print('Подматрица E')
printm(E)
print('Подматрица С')
printm(C)
print('Подматрица B')
printm(B)

simp, null = 0, 0

# область 2
for i in range(n // 4, half_n):
    for j in range(half_n - i - 1, i + 1):
        if (j + 1) % 2 != 0:
            if simple(C[i][j]):
                simp += 1

# область 3
for i in range((n // 4) + 1):
    for j in range(i, half_n - i):
        if (i + 1) % 2 == 0:
            if C[j][i] == 0:
                null += 1

print('количество простых чисел в нечетных столбцах в области 2: ', simp)

print('количество нулевых  элементов в четных строках в области 3:', null)

if simp > null:
    print('поменяем в С симметрично области 1 и 3 местами')
    print('Начальная подматрица C:')
    printm(C)
    for i in range((n // 4) + 1):
        for j in range(i, half_n - i):
            C[j][i], C[j][((n // 4) + 1) - i] = C[j][((n // 4) + 1) - i], C[j][i]
    print('Получившаяся подматрица С:')
    printm(C)
else:
    print('С и В поменяем местами несимметрично')
    C, B = B, C

F = A.copy()
paste(F, D, 0, 0)
paste(F, E, fix_n, 0)
paste(F, B, fix_n, fix_n)
paste(F, C, 0, fix_n)

print('Матрица F:')
printm(F)


print('Вычисляем ((К*A)*F – (K * AT):')


At = zero(n)
print("Матрица А транспонированая:")
for i in range(n):
    for j in range(n):
        At[i][j] = A[j][i]
printm(At)


KA = A.copy()
for i in range(n):
    for j in range(n):
        KA[i][j] *= K
print('Результат K * A:')
printm(KA)


KAF = zero(n)
for i in range(n):
    for j in range(n):
        KAF[i][j] = (KA[i][j] * F[i][j]) // 2
print('Результат (К*A) * F:')
printm(KAF)


KAt = At.copy()
for i in range(n):
    for j in range(n):
        KAt[i][j] *= K
print('Результат K * AT:')
printm(KAt)


result = zero(n)
for i in range(n):
    for j in range(n):
        result[i][j] = KAF[i][j] - KAt[i][j]
print('Результат:')
printm(result)
