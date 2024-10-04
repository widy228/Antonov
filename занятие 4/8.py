n = int(input())
for i in range(1, n+1):
    print(*[k for k in range(1, i+1)], sep='')