import sys
sys.setrecursionlimit(10**5)
t = int(sys.stdin.readline())
v = []
a = []

def dfs(n, s):
    t = a[n-1]
    if v[t] == 0:
        v[t] = v[n] + 1
        dfs(t, s)
    else:
        if v[t] > 0:
            if t != s:
                k = s
                while k != t:
                    v[k] = -1
                    k = a[k-1]
        else:
            k = s
            while k != t:
                v[k] = -1
                k = a[k-1]

for _ in range(t):
    n = int(sys.stdin.readline())

    a = list(map(int, sys.stdin.readline().split()))
    v = [0] * (n+1)

    for i in range(1, n+1):
        if v[i] == 0:
            v[i] = 1
            dfs(i, i)
    cnt = 0
    for i in range(1, n+1):
        if v[i] < 0:
            cnt += 1
    print(cnt)

