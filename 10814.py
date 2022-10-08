import sys

a = int(sys.stdin.readline())
L = []
for i in range(a):
    b, c = map(str, sys.stdin.readline().split())
    L.append([b, c])
L.sort(key = lambda x : int(x[0]))
for i in range(a):
    print(L[i][0], L[i][1])