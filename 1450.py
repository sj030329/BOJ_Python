# meet in the middle
n, c = map(int, input().split())

o = list(map(int, input().split()))
o.sort()

ans = 0

s = []
b = []

for i in range(((n+1)//2)):
    s.append(o[i])
for i in range(((n+1)//2), n):
    b.append(o[i])

sc = [0] * (2 ** len(s))
bc = [0] * (2 ** len(b))

for i in range(len(s)):
    for j in range(len(sc)):
        if ((j // (2 ** (len(s)-i-1))) % 2 == 1):
            sc[j] += s[i]

for i in range(len(b)):
    for j in range(len(bc)):
        if ((j // (2 ** (len(b)-i-1))) % 2 == 1):
            bc[j] += b[i]

bc.remove(0)

sc.sort()
bc.sort()

for i in sc:
    if i <= c:
        ans += 1 

p = len(sc) - 1

for i in bc:
    while p >= 0:
        if i + sc[p] <= c:
            ans += (p+1)
            break
        else: p -= 1

print(ans)