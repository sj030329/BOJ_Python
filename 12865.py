## dynamic programming

import sys
n, k = map(int, sys.stdin.readline().split())
data = []
for i in range(n):
    w, v = map(int, sys.stdin.readline().split())
    data.append([w, v])

def knapsack(k, data, n):
    list = [[0 for i in range(k+1)] for i in range(n+1)]
    for i in range(n+1):
        for j in range(k+1):
            if i == 0 or j == 0:
                list[i][j] = 0
            elif data[i-1][0] <= j:
                list[i][j] = max(data[i-1][1]+list[i-1][j-data[i-1][0]], list[i-1][j])
            else: list[i][j] = list[i-1][j]
    return list[n][k]
print(knapsack(k, data, n))