s = []
c = mx = 1
while True:
    s.append(int(input()))
    if 0 in s: break
for i in range(len(s)-1):
    if s[i]==s[i+1]:
        c += 1
        mx = max(mx,c)
    else:
        c = 1

print(mx)