## binary search

import sys
a, b = map(int, sys.stdin.readline().split())
max = 0
min = 0
L = list(map(int, sys.stdin.readline().split()))
for i in range(a):
    if L[i] > max:
        max = L[i]
n = 0
while min <= max:
    n = (max+min)//2
    total = 0
    for i in L:
        if i > n:
            total += (i-n)
    if total >= b:
        min = n + 1
    else : max = n - 1
print(max)