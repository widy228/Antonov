# вариант 9
def count_steps_to_zero(n):
    steps = 0
    while n > 0:
        n -= sum(int(i) for i in str(n))
        steps += 1
    return steps
num = int(input('Введите число: '))
print("Нуль получится через", count_steps_to_zero(num), "шага(ов)")