# bit masking
import sys

def bitcount(n):
    if n == 0:
        return 0
    else:
        return n % 2 + bitcount(n//2)

n, m = map(int, sys.stdin.readline().split())
cnt = 0
g  = [sys.stdin.readline().rstrip() for i in range(n)]
d = {}
for i in g:
    c = 0b0000000000
    for j in i:
        c |= (1 << int(j))
    if c in d:
        d[c] += 1
    else:
        d[c] = 1

for i in d.keys():
    for j in d.keys():
        if i != j:
            t = i | j
            if bitcount(t) == m:
                cnt += (d[i] * d[j])
        else:
            if bitcount(i) == m:
                cnt += (d[i] * (d[i]-1))
print(cnt//2)