# greedy

import sys

n = int(sys.stdin.readline())
ans = 0
num = []
for _ in range(n):
    num.append(int(sys.stdin.readline()))

a = []
b = []
c = 0
d = 0

for i in num:
    if i > 1:
        a.append(i)
    elif i < 0:
        b.append(i)
    elif i == 1:
        c += 1
    else:
        d += 1

a.sort(reverse=True)
b.sort()
for i in range(0, len(a)-1, 2):
    ans += a[i] * a[i+1]
if len(a)%2 == 1:
    ans += a[-1]
for i in range(0, len(b)-1, 2):
    ans += b[i] * b[i+1]
if len(b)%2 == 1:
    if d == 0:
        ans += b[-1]
ans += c
print(ans)