import sys

a = int(sys.stdin.readline())
L = list(map(int, input().split()))
L.sort()

sum = L[0]
ans = 0
onAns = 0

if L[0] != 1:
    ans = 1
    onAns = 1

for i in range(1, a):
    if sum + 1 < L[i]:
        if onAns == 0:
            ans = sum + 1
            onAns = 1
    sum += L[i]
if onAns == 0:
    ans = sum + 1

print (ans)