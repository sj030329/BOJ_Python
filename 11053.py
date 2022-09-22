## dynamic programming

import sys
n = int(sys.stdin.readline())
series = list(map(int, sys.stdin.readline().split()))
L = [0]
for i in range(n):
    start = 0
    end = len(L) - 1
    while start <= end:
        mid = (start+end)//2
        if L[mid] < series[i]:
            start = mid + 1
        else:
            end = mid - 1
    if start >= len(L):
        L.append(series[i])
    else:
        L[start] = series[i]
print(len(L) - 1)