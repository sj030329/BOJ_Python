# stack

import sys

n = int(sys.stdin.readline())

k = int(sys.stdin.readline())
s = [[k, 1]]
cnt = 0

for i in range(n-1):
    k = int(sys.stdin.readline())
    while s and k > s[-1][0]:
        a = s.pop(-1)
        cnt += a[1]
        if not s:
            cnt -= 1
    if s and k == s[-1][0]:
        cnt += s[-1][1]
        s[-1][1] += 1
        if len(s) > 1:
            cnt += 1
    else:
        s.append([k, 1])
        cnt += 1

print(cnt)