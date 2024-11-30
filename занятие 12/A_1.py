def factorial(m):
    if m == 0:
        return 1
    return factorial(m-1) * m

x = int(input('Введите число Х: '))
n = int(input('Введите число N: '))

print((x ** n)/factorial(n))