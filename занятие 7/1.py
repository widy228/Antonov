# вариант 1
n = int(input('Введите кол-во элементов массива: '))
print('Введите элементы массива')
s = [int(input()) for i in range(n)]
s.reverse()
print(max(s), s)