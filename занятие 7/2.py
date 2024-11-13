#вариант 1
n = int(input('Введите кол-во элементов массива: '))
print('Введите элементы массива')
s = [float(input()) for i in range(n)]
sr = (sum(s)/len(s))
s = [sr if i == 0 else i for i in s]
print(s)