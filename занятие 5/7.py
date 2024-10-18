s = []
while True:
    s.append(int(input()))
    if 0 in s: break
print(sum(1 for i in range(len(s)-1) if s[i]<s[i+1]))