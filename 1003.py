## dynamic programming

import sys
data = []
a = int(sys.stdin.readline())
for i in range(a):
    data.append(list(map(int,sys.stdin.readline().split())))

for i in range(a):
    n = data[i][0]
    if n == 0:
        print(1,0)
    if n == 1:
        print(0,1)
    b = [0, 1, 1]
    if n > 1:
        for j in range(n-1):
            b.append(b[j+1]+b[j+2])
        print(b[n-1], b[n])