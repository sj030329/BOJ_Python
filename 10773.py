## stack

import sys
n = int(sys.stdin.readline())
L = []
count = 0
for i in range(n):
    a = int(sys.stdin.readline())
    if a != 0:
        L.append(a)
        count += a
    else:
        count -= L[-1]
        L[-1] = 0
        L.remove(0)
print(count)