import sys

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
b = list(map(int, sys.stdin.readline().split()))

s = []
t = -1
ti = -1

for k in range(100, 0, -1):
    idxi = ti + 1
    for i in range(idxi, n):
        if a[i] == k:
            idxj = t + 1
            for j in range(idxj, m):
                if a[i] == b[j]:
                    if j > t:
                        s.append(k)
                        t = j
                        ti = i
                        break
                        
print(len(s))
if len(s) != 0:
    for i in s:
        print(i, end=" ")
