import sys

n = int(sys.stdin.readline())
g = [[[0 for i in range(n)] for j in range(n)] for k in range(6)]
g[0] = [list(map(int, sys.stdin.readline().split())) for i in range(n)]
maxn = [0] * 6

for i in g[0]:
    for j in i:
        maxn[0] = max(maxn[0], j)

def recursion(t):
    global g
    if t == 5:
        return
    else:
        for i in range(4):
            move(i, t)
            recursion(t+1)

def move(m, t):
    global g
    global ans
    if m == 0:
        for i in range(n):
            cnt = -1
            c = 0
            for j in range(n):
                if g[t][i][j] != 0:
                    if cnt != -1 and g[t][i][j] == g[t+1][i][cnt] and c == 0:
                        g[t+1][i][cnt] *= 2 
                        maxn[t+1] = max(maxn[t+1], g[t+1][i][cnt])
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
                        maxn[t+1] = max(maxn[t+1], g[t+1][i][n-cnt])
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
                            maxn[t+1] = max(maxn[t+1], g[t+1][cnt][j])
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
                            maxn[t+1] = max(maxn[t+1], g[t+1][n-cnt][j])
                            g[t+1][i-cnt][j] = 0
                            c = 1
                    else:
                        g[t+1][n-cnt-1][j] = g[t][n-i-1][j]
                        cnt += 1
                        c = 0
                else:
                    g[t+1][i-cnt][j] = 0

recursion(0)

print(maxn[5])