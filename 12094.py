# 구현
# c++로 바꿔서 성공

import sys

n = int(sys.stdin.readline())
temp = 0
g = [[[0 for i in range(n)] for j in range(n)] for k in range(11)]
g[0] = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

for i in g[0]:
    for j in i:
        temp = max(temp, j)

ans = [0] * 11
for i in range(10, -1, -1):
    ans[i] = temp
    temp //= 2

def recursion(t, lans):
    global g
    global ans
    if lans > ans[10]:
        temp = lans
        for i in range(10, -1, -1):
            ans[i] = temp
            temp //= 2
    if t == 10:
        return
    else:
        for i in range(4):
            lmax = move(i, t, lans)
            f = 0
            for j in range(n):
                for k in range(n):
                    if g[t][j][k] != g[t+1][j][k]:
                        f = 1
                        if lmax >= ans[t+1]:
                            recursion(t+1, lmax)
                        break
                if f == 1:
                    break

def move(m, t, lmax):
    global g
    if m == 0:
        for i in range(n):
            cnt = -1
            c = 0
            for j in range(n):
                if g[t][i][j] != 0:
                    if cnt != -1 and g[t][i][j] == g[t+1][i][cnt] and c == 0:
                        g[t+1][i][cnt] *= 2 
                        lmax = max(lmax, g[t+1][i][cnt])
                        g[t+1][i][n-j+cnt] = 0
                        c = 1
                    else:
                        cnt += 1
                        g[t+1][i][cnt] = g[t][i][j]
                        c = 0
                else:
                    g[t+1][i][n-j+cnt] = 0
    elif m == 1:
        for i in range(n):
            cnt = 0
            c = 0
            for j in range(n):
                if g[t][i][n-j-1] != 0:
                    if cnt != 0 and g[t][i][n-j-1] == g[t+1][i][n-cnt] and c == 0:
                        g[t+1][i][n-cnt] *= 2
                        lmax = max(lmax, g[t+1][i][n-cnt])
                        g[t+1][i][j-cnt] = 0
                        c = 1
                    else:
                        g[t+1][i][n-cnt-1] = g[t][i][n-j-1]
                        cnt += 1
                        c = 0
                else:
                    g[t+1][i][j-cnt] = 0
    elif m == 2:
        for j in range(n):
            cnt = -1
            c = 0
            for i in range(n):
                if g[t][i][j] != 0:
                    if cnt != -1 and g[t][i][j] == g[t+1][cnt][j] and c == 0:
                        g[t+1][cnt][j] *= 2
                        lmax = max(lmax, g[t+1][cnt][j])
                        g[t+1][n-i+cnt][j] = 0
                        c = 1
                    else:
                        cnt += 1
                        g[t+1][cnt][j] = g[t][i][j]
                        c = 0
                else:
                    g[t+1][n-i+cnt][j] = 0
    elif m == 3:
        for j in range(n):
            cnt = 0
            c = 0
            for i in range(n):
                if g[t][n-i-1][j] != 0:
                    if cnt != 0 and g[t][n-i-1][j] == g[t+1][n-cnt][j] and c == 0:
                        g[t+1][n-cnt][j] *= 2
                        lmax = max(lmax, g[t+1][n-cnt][j])
                        g[t+1][i-cnt][j] = 0
                        c = 1
                    else:
                        g[t+1][n-cnt-1][j] = g[t][n-i-1][j]
                        cnt += 1
                        c = 0
                else:
                    g[t+1][i-cnt][j] = 0
    return lmax

recursion(0, ans[10])

print(ans[-1])