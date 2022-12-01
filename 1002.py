## math

import sys
a = int(sys.stdin.readline())
for i in range(a):
    b, c, d, e, f, g = map(int, sys.stdin.readline().split())
    distance = (e-b)**2+(f-c)**2
    if distance == 0 and d == g:
        print(-1)
    elif (d+g)**2 > distance > abs(g-d)**2:
        print(2)
    elif abs(g-d)**2 == distance:
        print(1)
    elif (d+g)**2 == distance:
        print(1)
    else : print(0)