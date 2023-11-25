# BFS

import sys, math
from collections import deque
n, m = map(int, sys.stdin.readline().split())
g = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

p = list(map(int, sys.stdin.readline().split()))
r = list(map(int, sys.stdin.readline().split()))
k = r[0]
q = deque([])
cnt = 0
d = [[0 for i in range(n+1)] for j in range(n+1)]
v = [0 for i in range(n+1)]
for i in range(1, n+1):
    for j in range(1, n+1):
        d[i][j] = math.floor(math.sqrt((g[i-1][0]-g[j-1][0])**2+(g[i-1][1]-g[j-1][1])**2))

for i in range(1, m+1):
    for j in range(1, n+1):
        if d[p[i-1]][j] <= r[i]:
            v[j] = 1
for i in range(1, n+1):
    if v[i] == 0:
        q.append(i)

while q:
    t = q.popleft()
    cnt += 1
    for i in range(1, n+1):
        if d[t][i] <= k:
            if v[i] == 1:
                v[i] = 0
                q.append(i)

print(cnt)