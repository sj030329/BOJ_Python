## dynamic programming

import sys
n = int(sys.stdin.readline())
L = []
for i in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    L.append([a,b,c])
for i in range(1, n):
    L[i][0] += min(L[i-1][1], L[i-1][2])
    L[i][1] += min(L[i - 1][0], L[i - 1][2])
    L[i][2] += min(L[i - 1][1], L[i - 1][0])
print(min(L[-1]))