#вариант 1
import random

n = int(input('Введите кол-во строк '))
m = int(input('Введите кол-во столбцов '))
a = [[random.randrange(20) for i in range(m)] for j in range(n)]

print('Матрица до: ')
for k in a:
    for j in k:
        print(j, end = " ")
    print()

for i in range(n):
    mx = -1000000000000
    mn = 1000000000000000
    imx = imn = 0
    for k in range(m):
        if a[i][k] > mx:
          mx = a[i][k]
          imx = k
    a[i][imx], a[i][0] = a[i][0], a[i][imx]
    for k in range(m):
        if a[i][k] < mn:
          mn = a[i][k]
          imn = k
    a[i][imn], a[i][-1] = a[i][-1], a[i][imn]

print()

print('Матрица после: ')
for k in a:
    for j in k:
        print(j, end = " ")
    print()


