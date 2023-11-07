import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
max = 10 ** 5
d = [-1] * (max + 1)
c = 0
queue = deque([])
if k == 0:
    print(n)
else:
    d[n] = 0
    if n != 0:
        queue.append(n)
    else:
        queue.append(1)
        d[1] = 1
    while queue:
        x = queue.popleft()
        if x == k:
            print(d[x])
            break
        if x == 1:
            d[2] = d[1]
            queue.append(2)
        else:   
            t = x
            while t <= max:
                if d[t] == -1:
                    d[t] = d[x]
                else:
                    if t != x:
                        break
                if t == k:
                    print(d[x])
                    c = 1
                    break
                for i in (t-1, t+1):
                    if 0 < i <= max:
                        if d[i] == -1:
                            queue.append(i)
                            d[i] = d[x] + 1
                t *= 2
            if c == 1:
                break