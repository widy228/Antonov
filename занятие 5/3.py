n = int(input())
a = 1
for i in range(0, n+1):
    if a <= n:
        a *= 2
    else:
        print(i-1, a//2)
        break