# Topological Sorting
import sys
from collections import deque
n, m = map(int, sys.stdin.readline().split())

g = [[] for i in range(n+1)]
cnt = [0] * (n+1)
q = deque([])

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())

    cnt[b] += 1
    g[a].append(b)

for i in range(1, n+1):
    if cnt[i] == 0:
        q.append(i)

while q:
    t = q.popleft()
    for i in g[t]:
        cnt[i] -= 1
        if cnt[i] == 0:
            q.append(i)
    print(t, end=" ")