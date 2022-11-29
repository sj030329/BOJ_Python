import sys

n = int(sys.stdin.readline())
L = list(map(int, input().split()))

dp_i = [1]
dp_d = [1]

for i in range(1, n):
    max = 0
    for j in range(i):
        if L[i] > L[j]:
            if max < dp_i[j]:
                max = dp_i[j]
    dp_i.append(max+1)

L.reverse()

for i in range(1, n):
    max = 0
    for j in range(i):
        if L[i] > L[j]:
            if max < dp_d[j]:
                max = dp_d[j]
    dp_d.append(max+1)

dp_d.reverse()
    
dp_max = 0
for i in range(n):
    if dp_max < dp_i[i] + dp_d[i]:
        dp_max = dp_i[i] + dp_d[i]

print(dp_max-1)
