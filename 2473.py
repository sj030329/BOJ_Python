# two pointer

import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
a.sort()
ans = [0] * 3
min = 10 ** 10
for i in range(n-2):
    x = a[i]
    t = n-1
    for j in range(i+1, n-1):
        l = j
        r = max(t, j+1)
        while l < r-1:
            if abs(x+a[l]+a[r]) > abs(x+a[l]+a[r-1]):
                r -= 1
            else:
                break
        if min > abs(x+a[l]+a[r]):
            min = abs(x+a[l]+a[r])
            ans = [x, a[l], a[r]]
        t = r
for i in ans:
    print(i, end=" ")