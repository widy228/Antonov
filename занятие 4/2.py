a = int(input())
b = int(input())
if a < b:
    print(*[i for i in range(a, b+1)])
else:
    print(*[i for i in range(a, b-1, -1)])