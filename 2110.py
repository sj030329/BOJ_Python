## binary search

import sys
a, b = map(int, sys.stdin.readline().split())
L = []
for i in range(a):
    L.append(int(sys.stdin.readline()))
L.sort()
max = L[-1]
min = 1
n = 0
while min <= max:
    n = (max+min)//2
    cnt = 1
    start = L[0]
    for i in L:
        if i >= n + start:
            cnt += 1
            start = i
    if cnt >= b:
        min = n + 1
    else : max = n - 1
print(max)
