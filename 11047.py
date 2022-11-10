## greedy

import sys

a,b = map(int, sys.stdin.readline().split())
L = []
for i in range(a):
    L.append(int(sys.stdin.readline()))
L.reverse()
count = 0
for i in range(a):
    if b >= L[i]:
        n = b//L[i]
        count += n
        b -= L[i] * n
print(count)