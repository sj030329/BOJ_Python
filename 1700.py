import sys

n, k = map(int, sys.stdin.readline().split())
d = list(map(int, sys.stdin.readline().split()))

a = [0] * n
cnt = 0
for i in range(k):
    if not d[i] in a:
        if 0 in a:
            for j in range(n):
                if a[j] == 0:
                    a[j] = d[i]
                    break
        else:
            m = 0
            c = 0
            for j in range(n):
                t = k-i+1
                for l in range(i+1, k):
                    if a[j] == d[l]:
                        t = l-i
                        break
                if t > m:
                    m = t
                    c = j
            a[c] = d[i]
            cnt += 1
print(cnt)

