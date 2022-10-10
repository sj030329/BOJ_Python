## dynamic programming

import sys
n = int(sys.stdin.readline())
L = [1, 2]
for i in range(2, n):
    L.append((L[i-2] + L[i-1])%15746)
print(L[n-1])