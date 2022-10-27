## math

import sys
a = int(sys.stdin.readline())
for i in range(a):
    b, c = map(int, sys.stdin.readline().split())
    x = int(c - b)
    y = int(x**0.5)
    if x == y**2:
        print(2*y-1)
    elif y*(y+1) >= x:
        print(2*y)
    else : print(2*y+1)