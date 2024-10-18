x = int(input())
y = int(input())
d = 1
while x < y:
    x += 0.1 * x
    d +=1
print(d)

