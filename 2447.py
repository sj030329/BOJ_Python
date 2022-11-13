## recursion

import sys
x = int(sys.stdin.readline())
for i in range(8):
    if 3**i == x:
        a = i
def pattern(n):
    if n == 1:
        return ["*"]
    p = pattern(n//3)
    L = []
    for s in p:
        L.append(s*3)
    for s in p:
        L.append(s+" "*(n//3)+s)
    for s in p:
        L.append(s*3)
    return L
print('\n'.join(pattern(x)))