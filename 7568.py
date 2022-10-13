## brute force

import sys
a = int(sys.stdin.readline())
s = []
for i in range(a):
    b,c = map(int, sys.stdin.readline().split())
    s.append((b, c))
for i in s:
    rank = 1
    for j in s:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end = " ")