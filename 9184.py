## recursion
## dynamic programming

import sys
def w(a,b,c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1
    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)
    if L[a][b][c] != 0:
        return L[a][b][c]
    if a < b < c:
        L[a][b][c] = w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
    else:
        L[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
        return w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
L = [[[0]*(21) for _ in range(21)] for _ in range(21)]
while 1:
    a, b, c = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1 and c == -1 :
        break
    print ("w(", a,", ", b,", ", c, ") = ", w(a,b,c), sep="")