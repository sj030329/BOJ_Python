# DP
import sys

n = int(sys.stdin.readline())
w = int(sys.stdin.readline())

p1 = [1, 1]
p2 = [n, n]

a = [[0, 0] for _ in range(w)]
for i in range(w):
    t = list(map(int, sys.stdin.readline().split()))
    a[i] = t

def d(n1, n2):
    if n2 == 0:
        return abs(1 - a[n1-1][0]) + abs(1 - a[n1-1][1])
    elif n1 == 0:
        return abs(n - a[n2-1][0]) + abs(n - a[n2-1][1])
    else:
        return abs(a[n1-1][0] - a[n2-1][0]) + abs(a[n1-1][1] - a[n2-1][1])

dp = [[10 ** 8 for j in range(w+1)] for i in range(w+1)]

dp[0][1] = d(0, 1)
dp[1][0] = d(1, 0)

for i in range(1, w):
    for j in range(0, i):
        if j != 0:
            dp[j][i+1] = min(dp[j][i+1], dp[j][i] + abs(a[i-1][0] - a[i][0]) + abs(a[i-1][1] - a[i][1]))
            dp[i+1][i] = min(dp[i+1][i], dp[j][i] + abs(a[i][0] - a[j-1][0]) + abs(a[i][1] - a[j-1][1]))
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + abs(a[i][0] - a[i-1][0]) + abs(a[i][1] - a[i-1][1]))
            dp[i][i+1] = min(dp[i][i+1], dp[i][j] + abs(a[j-1][0] - a[i][0]) + abs(a[j-1][1] - a[i][1]))
        else:
            dp[j][i+1] = min(dp[j][i+1], dp[j][i] + d(i, i+1))
            dp[i+1][i] = min(dp[i+1][i], dp[j][i] + d(i+1, j))
            dp[i+1][j] = min(dp[i+1][j], dp[i][j] + d(i+1, i))
            dp[i][i+1] = min(dp[i][i+1], dp[i][j] + d(j, i+1))

min = dp[0][w]
idx1 = 0
idx2 = w
for i in range(w):
    if min > dp[i][w]:
        min = dp[i][w]
        idx1, idx2 = i, w
    if min > dp[w][i]:
        min = dp[w][i]
        idx1, idx2 = w, i
ans = []
while idx1 != 0 and idx2 != 0:
    if abs(idx1-idx2) > 1:
        if idx1 > idx2:
            idx1 -= 1
            ans.append(1)
        else:
            idx2 -= 1
            ans.append(2)
    else:
        if idx1 > idx2:
            for i in range(idx1-1):
                if dp[idx1][idx2] == dp[i][idx2] + d(idx1, i):
                    idx1 = i
                    ans.append(1)
                    break
        else:
            for i in range(idx2-1):
                if dp[idx1][idx2] == dp[idx1][i] + d(i, idx2):
                    idx2 = i
                    ans.append(2)
                    break
while idx1 != 0 or idx2 != 0:
    if idx1 != 0:
        idx1 -= 1
        ans.append(1)
    else:
        idx2 -= 1
        ans.append(2)

res = ""
res += str(min) + '\n'
for i in range(w-1, -1, -1):
    res += str(ans[i]) + '\n'
print(res)