def fib(a):
    if a <= 1:
        return a
    else:
        return fib(a-1) + fib(a-2)

n = int(input())
print(sum(fib(i) for i in range(n+1)))