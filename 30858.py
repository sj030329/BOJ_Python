# hashing

import sys

n, k, m, f = map(int, sys.stdin.readline().split())

b = [0] * (n+1)
d = {}
t = 1

for i in range(k):
    a = list(map(int, sys.stdin.readline().split()))
    d2 = {}
    for i in a:
        d2[i] = 1
    for i in d2.keys():
        b[i] += t
    t *= 2
print(b)
for i in range(1, n+1):
    if b[i] not in d:
        d[b[i]] = i
    else:
        d[b[i]] = 0

for i in range(f):
    a = sys.stdin.readline().strip()
    x = 0
    t = 1
    for j in a:
        if j == "Y":
            x += t
        t *= 2
    if x in d:
        print(d[x])
    else:
        print(0)
    