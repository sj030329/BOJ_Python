# bfs

import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())
g = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
v = [[0 for i in range(m)] for j in range(n)]
x = [1, -1, 0, 0]
y = [0, 0, 1, -1]
res = ""
for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            if v[i][j] == 0:
                q = deque([])
                q.append((i, j))
                v[i][j] = 1
                t = 1
                d = {}
                while q:
                    a, b = q.popleft()
                    for k in range(4):
                        dx = a + x[k]
                        dy = b + y[k]
                        if 0 <= dx < n and 0 <= dy < m:
                            if g[dx][dy] == 0:
                                if v[dx][dy] == 0:
                                    v[dx][dy] = 1
                                    t += 1
                                    q.append((dx, dy))
                            else:
                                d[(dx, dy)] = 1
                    t %= 10
                for l in d.keys():
                    v[l[0]][l[1]] += t
                    v[l[0]][l[1]] %= 10
for i in range(n):
    for j in range(m):
        if g[i][j] == 0:
            v[i][j] -= 1
        else:
            v[i][j] += 1
            v[i][j] %= 10
for i in range(n):
    res += ''.join(map(str, v[i]))
    if i != (n-1):
        res += "\n"
print(res)