## DP

import sys
a = int(sys.stdin.readline())
L = [0] * (a+3)
for i in range(1, a+1):
    L[i] = int(sys.stdin.readline())
count = [0] * (a+3)
count[1] = L[1]
count[2] = L[1] + L[2]
count[3] = max(L[1] + L[3], L[2] + L[3])
for i in range(4, a+1):
    count[i] = max(L[i-1]+count[i-3]+L[i], count[i-2]+L[i])
print(count[a])