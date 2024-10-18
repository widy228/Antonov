#вариант 1
s = input()
print(sum(1 for i in s.split() if i[0] == 'е'))