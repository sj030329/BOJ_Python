## dynamic programming

import sys

n, k = map(int,sys.stdin.readline().split())
L = []
for i in range(n):
    L.append(int(sys.stdin.readline()))
L.sort()

DP = [1]
for i in range(1, k+1):
    DP.append(0)
for i in range(n):
    for j in range(1, k+1):
        if (j >= L[i]):
            DP[j] += DP[j-L[i]]
    
print(DP[-1])