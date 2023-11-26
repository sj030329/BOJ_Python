# case work

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
d = {}

cnt = 0
s = sum(a)
m1 = max(a)
a.remove(m1)
m2 = max(a)
a.remove(m2)
m3 = max(a)

if s - m1 - m2 - m3 == m3:
    cnt += 1
cnt += a.count(s-m1-m2*2)

k = s-m1*2

for i in range(1, 1000001):
    d[i] = 0
for i in a:
    d[i] += 1

d[m2] += 1

if 1 < k <= 2000000:
    for i in range(max(1, k-1000000), (k+1) // 2):
        cnt += d[i] * d[k-i]

    if k % 2 == 0:
        if d[k//2] > 1:
            cnt += d[k//2] * (d[k//2]-1) // 2

print(cnt)