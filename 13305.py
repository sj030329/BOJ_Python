## greedy

import sys
a = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))
c = list(map(int, sys.stdin.readline().split()))
min = c[0]
cost = 0
for i in range(a-1):
    if min > c[i]:
        min = c[i]
    cost += min * b[i]
print(cost)