def main():
    num = int(input('Введите число: '))
    if num == 0:
        return 0
    else:
        maximum = main()
        return max(num, maximum)

print(f'Наибольшее значение: {main()}')