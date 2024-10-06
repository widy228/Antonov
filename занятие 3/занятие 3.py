intr = [1, 2, 3]
y = []
for i in range(3):
    a = int(input())
    if a in intr:
        y.append(a)
print(*y)
