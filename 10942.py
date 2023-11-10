import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
dp = [[0 for i in range(n+1)] for i in range(n+1)]

for i in range(1, n+1):
    dp[i][i] = 1

for i in range(1, n):
    if a[i-1] == a[i]:
        dp[i][i+1] = 1

for j in range(2, n):
    for i in range(1, n-j+1):
        if a[i-1] == a[i+j-1]:
            if dp[i+1][i+j-1] == 1:
                dp[i][i+j] = 1
m = int(sys.stdin.readline())
for i in range(m):
    s, e = map(int, sys.stdin.readline().split())

    print(dp[s][e])