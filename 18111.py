## brute force

import sys
a, b, c = map(int, sys.stdin.readline().split())
L = []
for i in range(a):
    data = list(map(int, sys.stdin.readline().split()))
    for j in range(b):
        L.append(data[j])
L.sort()
maxh = L[-1]
minh = L[0]
mintime = -1
height = -1
for i in range(minh, maxh+1):
    count = 0
    inven = c
    for j in range(len(L)):
        if L[j] < i :
            count += (i-L[j])
            inven -= (i-L[j])
        elif L[j] > i:
            count += 2*(L[j]-i)
            inven += (L[j]-i)
    if inven >= 0:
        if mintime == -1:
            mintime = count
            height = i
        elif count <= mintime:
            mintime = count
            height = i
print(mintime, height)