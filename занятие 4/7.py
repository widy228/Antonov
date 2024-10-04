def fctrl(a):
    if a == 1: return a
    else: return a * fctrl(a - 1)

n = int(input())
print(sum(fctrl(i) for i in range(1,n+1)))
