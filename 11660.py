## dynamic programming

import sys

n,m = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr2 = [[0] * (n+1) for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        arr2[i][j] = (arr2[i-1][j]+arr2[i][j-1]-arr2[i-1][j-1]+arr[i-1][j-1])
for i in range(m):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    s = 0
    s += (arr2[x2][y2] + arr2[x1-1][y1-1] - arr2[x1-1][y2] - arr2[x2][y1-1])
    print(s)