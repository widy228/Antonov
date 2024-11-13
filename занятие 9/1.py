#вариант 1
n = int(input("Введите число строк и столбцов N: "))
print('Введите элементы матрицы')
a = [[int(input()) for j in range(n)] for k in range(n)]
sm = cnt = 0

print('Матрица: ')
for k in a:
    for j in k:
        print(j, end = " ")
    print()

for i in range(n):
    for j in range(i+1,n):
        if i<j and a[i][j] > 0:
            sm += a[i][j]
            cnt += 1
print('Сумма положительных элементов над главной диагональю:', sm,
      'Кол-во положительных элементов над главной диагональю:',cnt)