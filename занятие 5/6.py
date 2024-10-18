a = []
while True:
    a.append(int(input()))
    if 0 in a:
        print(sum(a)/(len(a)-1))
        break