import sys
n = int(sys.stdin.readline())
S = set()
for i in range(n):
    data = list(map(str, sys.stdin.readline().split()))
    a = data[0]
    if len(data) == 2:
        b = int(data[1])
    if a == "all":
        S = set([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20])
    if a == "empty":
        S = set()
    if a == "add":
        S.add(b)
    if a == "remove":
        S.discard(b)
    if a == "check":
        if b in S:
            print(1)
        else: print(0)
    if a == "toggle":
        if b in S:
            S.discard(b)
        else:
            S.add(b)