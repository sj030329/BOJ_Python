## 재귀

import sys
n = int(sys.stdin.readline())
print(2**n-1)
def hanoi(n, s, m, e):
    if n == 1:
        print(s, e)
        return
    hanoi(n-1, s, e, m)
    print(s, e)
    hanoi(n-1, m, s, e)
hanoi(n, 1, 2, 3)

