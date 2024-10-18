s = []
while True:
    s.append(int(input()))
    if 0 in s:
        print(len(s)-1)
        break