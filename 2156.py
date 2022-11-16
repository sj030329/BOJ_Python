## dynamic programming

import sys
a = int(sys.stdin.readline())
L = []
for i in range(a):
    L.append(int(sys.stdin.readline()))
count = [0] * a
count[0] = L[0]
if a > 1:
    count[1] = L[0] + L[1]
if a > 2:
    count[2] = max(L[0] + L[1], L[0] + L[2], L[1] + L[2])
for i in range(3, a):
    count[i] = max(count[i-1], count[i-2]+L[i], count[i-3]+L[i]+L[i-1])
print(count[a-1])