n = int(input())
a = 10 ** 1000
print(min(i for i in range(2, n+1) if n % i == 0))