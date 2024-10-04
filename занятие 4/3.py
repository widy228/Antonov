a = int(input())
b = int(input())
print(*[i for i in range(a, b-1, -1) if i % 2 != 0])
