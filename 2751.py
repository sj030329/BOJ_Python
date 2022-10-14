## sort

import sys
a = int(sys.stdin.readline())
L = []
for i in range(a):
    L.append(int(sys.stdin.readline()))
L.sort()
for i in range(a):
    print(L[i])