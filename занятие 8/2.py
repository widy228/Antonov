# вариант 9
import random
import math

def f(x):
    mul = math.prod(x)
    sr = round(sum(x)/len(x), 3)
    print('Произведение элементов:', mul, 'Среднеарифметическое:', sr)

n_a = int(input('Введите длину массива A '))
a = [random.randrange(-20, 20) for i in range(n_a)]
n_b = int(input('Введите длину массива B '))
b = [random.randrange(-20, 20) for k in range(n_b)]
n_c = int(input('Введите длину массива C '))
c = [random.randrange(-20, 20) for l in range(n_c)]
print("Массив А:", a)
print("Массив B:", b)
print("Массив C:", c)
f(a)
f(b)
f(c)